"""
Paper Pipeline CLI - Batch operations for paper search, fetch, and management.

Usage:
    python cli.py search "urban microbiome" --max 50 --oa-only
    python cli.py fetch --collection metasub --email user@example.com
    python cli.py status
    python cli.py collection create metasub --dois "10.1038/xxx" "10.1016/yyy"
    python cli.py grobid-status
"""

import argparse
import json
import sys
from pathlib import Path

from paper_pipeline.discovery import PaperDiscovery
from paper_pipeline.fetcher import PaperFetcher, ContentResult
from paper_pipeline.extractor import PaperExtractor
from paper_pipeline.store import PaperStore


def cmd_search(args):
    """Search for papers on OpenAlex."""
    discovery = PaperDiscovery(email=args.email)

    filters = {}
    if args.oa_only:
        filters["is_oa"] = True
    if args.year_from:
        filters["publication_year"] = f">{args.year_from - 1}"

    papers = discovery.search(
        args.query,
        max_results=args.max,
        filters=filters if filters else None,
    )

    store = PaperStore(args.data_dir)

    saved = 0
    for paper in papers:
        if paper.get("doi"):
            store.save_layer(paper["doi"], "L0", paper)
            saved += 1

    print(f"\nFound {len(papers)} papers, saved {saved} with DOI as L0")
    print(f"Store: {store.get_stats()}")

    if args.collection:
        dois = [p["doi"] for p in papers if p.get("doi")]
        store.create_collection(args.collection, dois)
        print(f"Created collection '{args.collection}' with {len(dois)} papers")


def cmd_fetch(args):
    """Fetch full-text content for papers."""
    store = PaperStore(args.data_dir)
    fetcher = PaperFetcher(email=args.email, pdf_dir=args.data_dir)
    extractor = PaperExtractor()

    # Get DOIs to fetch
    if args.collection:
        dois = store.get_collection(args.collection)
        if not dois:
            print(f"Collection '{args.collection}' not found")
            return
    elif args.doi:
        dois = [args.doi]
    else:
        # Fetch all papers without content
        papers = store.list_papers({"has_layer": "L0"})
        dois = [
            doi for doi, entry in store.index.get("papers", {}).items()
            if not entry.get("content_available")
        ]

    print(f"Fetching content for {len(dois)} papers...")

    for i, doi in enumerate(dois, 1):
        print(f"[{i}/{len(dois)}] {doi}... ", end="", flush=True)

        # Load L0 for work_data
        l0 = store.load_layer(doi, "L0")

        result = fetcher.fetch_content(doi, work_data=l0)
        print(f"{result.source} ({result.content_type})")

        # Save raw content
        if result.content_type == "pmc_xml" and result.data:
            store.save_content(doi, "fulltext", result.data)
        elif result.content_type == "abstract_only" and result.data:
            store.save_content(doi, "abstract", result.data)

        # Extract text
        if result.content_type in ("pmc_xml", "pdf"):
            extraction = extractor.extract(result, pdf_path=result.pdf_path)
            if extraction.full_text:
                store.save_content(doi, "fulltext", extraction.full_text)
            if extraction.sections:
                store.save_layer(doi, "L2", {
                    "sections": extraction.sections,
                    "extraction_method": extraction.extraction_method,
                    "tables": extraction.tables,
                    "figure_captions": extraction.figure_captions,
                })
            # Save GROBID TEI if available
            if extraction.extraction_method == "grobid" and result.pdf_path:
                tei_path = Path(result.pdf_path).parent / "grobid.tei.xml"
                if tei_path.exists():
                    store.save_content(doi, "grobid_tei", tei_path.read_text())

            store.update_content_info(doi, result.source, extraction.extraction_method)

    print(f"\nFetch complete. Stats: {json.dumps(fetcher.get_stats(), indent=2)}")


def cmd_status(args):
    """Show store status."""
    store = PaperStore(args.data_dir)
    stats = store.get_stats()

    print(f"Paper Pipeline Store Status")
    print(f"{'='*40}")
    print(f"Total papers: {stats['total_papers']}")
    print(f"Content available: {stats['content_available']}")
    print(f"\nLayer counts:")
    for layer, count in stats["layer_counts"].items():
        print(f"  {layer}: {count}")
    print(f"\nCollections: {', '.join(stats['collections']) if stats['collections'] else '(none)'}")


def cmd_collection(args):
    """Manage collections."""
    store = PaperStore(args.data_dir)

    if args.action == "create":
        if not args.name or not args.dois:
            print("Usage: collection create <name> --dois <doi1> <doi2> ...")
            return
        path = store.create_collection(args.name, args.dois)
        print(f"Created collection '{args.name}' at {path}")

    elif args.action == "list":
        collections = store.list_collections()
        if collections:
            for name in collections:
                dois = store.get_collection(name)
                print(f"  {name}: {len(dois) if dois else 0} papers")
        else:
            print("No collections found")

    elif args.action == "show":
        if not args.name:
            print("Usage: collection show <name>")
            return
        dois = store.get_collection(args.name)
        if dois:
            print(f"Collection '{args.name}': {len(dois)} papers")
            for doi in dois:
                l0 = store.load_layer(doi, "L0")
                title = l0.get("title", "Unknown") if l0 else "No L0"
                print(f"  - {doi}: {title[:60]}")
        else:
            print(f"Collection '{args.name}' not found")


def cmd_grobid_status(args):
    """Check GROBID service status."""
    extractor = PaperExtractor()
    if extractor.grobid_available:
        print(f"GROBID is running at {extractor.grobid_url}")
    else:
        print(f"GROBID is NOT available at {extractor.grobid_url}")
        print("Start with: docker run --rm --init --ulimit core=0 -p 8070:8070 grobid/grobid:0.8.2-crf")


def main():
    parser = argparse.ArgumentParser(
        description="Paper Pipeline - Search, fetch, and manage academic papers"
    )
    parser.add_argument("--data-dir", default="data/papers", help="Data directory")
    subparsers = parser.add_subparsers(dest="command", help="Command to run")

    # search
    p_search = subparsers.add_parser("search", help="Search for papers")
    p_search.add_argument("query", help="Search query")
    p_search.add_argument("--max", type=int, default=50, help="Max results")
    p_search.add_argument("--oa-only", action="store_true", help="OA papers only")
    p_search.add_argument("--year-from", type=int, help="Min publication year")
    p_search.add_argument("--email", default="", help="Email for polite pool")
    p_search.add_argument("--collection", help="Save results to collection")

    # fetch
    p_fetch = subparsers.add_parser("fetch", help="Fetch paper content")
    p_fetch.add_argument("--collection", help="Fetch papers in collection")
    p_fetch.add_argument("--doi", help="Fetch single paper by DOI")
    p_fetch.add_argument("--email", default="", help="Email for API access")

    # status
    subparsers.add_parser("status", help="Show store status")

    # collection
    p_coll = subparsers.add_parser("collection", help="Manage collections")
    p_coll.add_argument("action", choices=["create", "list", "show"])
    p_coll.add_argument("name", nargs="?", help="Collection name")
    p_coll.add_argument("--dois", nargs="+", help="DOI list")

    # grobid-status
    subparsers.add_parser("grobid-status", help="Check GROBID service")

    args = parser.parse_args()

    if not args.command:
        parser.print_help()
        return

    commands = {
        "search": cmd_search,
        "fetch": cmd_fetch,
        "status": cmd_status,
        "collection": cmd_collection,
        "grobid-status": cmd_grobid_status,
    }

    commands[args.command](args)


if __name__ == "__main__":
    main()
