#!/usr/bin/env python3
"""
Generate OVERVIEW.md from Graph RAG community analysis.
Extracts top 15 communities (size >= 10) and creates a condensed report.
"""

import json
import re
from pathlib import Path


def load_communities(communities_file: Path) -> list[dict]:
    """Load communities from JSON file."""
    with open(communities_file) as f:
        return json.load(f)


def filter_and_sort_communities(communities: list[dict], min_size: int = 10, top_n: int = 15) -> list[dict]:
    """Filter communities by size and return top N sorted by size descending."""
    # Filter: only count paper DOIs (not entity members)
    filtered = []
    for comm in communities:
        paper_count = sum(1 for m in comm["members"] if m.startswith("https://doi.org/"))
        if paper_count >= min_size:
            comm["paper_count"] = paper_count
            filtered.append(comm)

    # Sort by paper_count descending
    filtered.sort(key=lambda x: x["paper_count"], reverse=True)

    return filtered[:top_n]


def parse_community_summary(summary_file: Path) -> dict:
    """Parse a community summary markdown file and extract key information."""
    if not summary_file.exists():
        return None

    content = summary_file.read_text()

    result = {
        "research_focus": "",
        "top_entities": [],
        "sample_papers": [],
        "dominant_category": "",
        "years": ""
    }

    # Extract dominant category
    cat_match = re.search(r"\*\*Dominant Category\*\*:\s*(\S+)", content)
    if cat_match:
        result["dominant_category"] = cat_match.group(1)

    # Extract years
    years_match = re.search(r"\*\*Years\*\*:\s*(.+)", content)
    if years_match:
        result["years"] = years_match.group(1).strip()

    # Extract research focus (first paragraph after **Research Focus**:)
    focus_match = re.search(r"\*\*Research Focus\*\*:\s*(.+?)(?=\n\n|\*\*Entity Type)", content, re.DOTALL)
    if focus_match:
        focus_text = focus_match.group(1).strip()
        # Take first sentence or two
        sentences = re.split(r'(?<=[.!?])\s+', focus_text)
        result["research_focus"] = sentences[0] if sentences else focus_text[:200]

    # Extract top 5 entities
    entities_section = re.search(r"\*\*Most Frequent Entities\*\*:\n((?:- .+\n)+)", content)
    if entities_section:
        entity_lines = entities_section.group(1).strip().split("\n")
        for line in entity_lines[:5]:
            # Parse: - metabolic (CONCEPT): 58 mentions
            match = re.match(r"- (.+?) \((\w+)\):", line)
            if match:
                result["top_entities"].append(match.group(1))

    # Extract sample papers (up to 3)
    papers_section = re.search(r"\*\*Sample Papers\*\*.+?:\n((?:- .+\n)+)", content)
    if papers_section:
        paper_lines = papers_section.group(1).strip().split("\n")
        for line in paper_lines[:3]:
            # Parse: - (2024) Paper title
            match = re.match(r"- \((\d{4})\) (.+)", line)
            if match:
                result["sample_papers"].append(f"({match.group(1)}) {match.group(2)}")

    return result


def get_community_name(summary: dict, community_id: int) -> str:
    """Generate a descriptive name for the community based on its content."""
    category = summary.get("dominant_category", "Research").replace("_", " ").title()

    # Use top entities to create a more descriptive name
    top_entities = summary.get("top_entities", [])[:3]
    if top_entities:
        entity_str = ", ".join(top_entities[:2])
        return f"{category}: {entity_str}"

    return f"{category} Community {community_id}"


def generate_overview(
    base_dir: Path,
    communities_file: Path,
    summaries_dir: Path,
    stats_file: Path,
    output_file: Path
):
    """Generate the OVERVIEW.md file."""

    # Load data
    communities = load_communities(communities_file)
    with open(stats_file) as f:
        stats = json.load(f)

    # Filter and sort communities
    top_communities = filter_and_sort_communities(communities, min_size=10, top_n=15)

    # Calculate coverage
    total_papers = stats["total_papers"]
    top_community_papers = sum(c["paper_count"] for c in top_communities)
    coverage_pct = (top_community_papers / total_papers) * 100 if total_papers > 0 else 0

    # Build OVERVIEW content
    lines = []
    lines.append("# Virtual Cell Research Landscape (748 Papers)")
    lines.append("")
    lines.append("## Executive Summary")
    lines.append("")
    lines.append(f"This overview synthesizes {total_papers} papers into {len(top_communities)} major research themes,")
    lines.append(f"representing {top_community_papers} papers ({coverage_pct:.1f}% of the collection).")
    lines.append("")
    lines.append("**Research Domains**:")
    for cat, count in stats["category_distribution"].items():
        cat_display = cat.replace("_", " ").title()
        lines.append(f"- {cat_display}: {count} papers")
    lines.append("")
    lines.append("**Graph Statistics**:")
    lines.append(f"- Paper nodes: {stats['graph_stats']['paper_nodes']}")
    lines.append(f"- Entity nodes: {stats['graph_stats']['entity_nodes']}")
    lines.append(f"- Edges: {stats['graph_stats']['edges']}")
    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append("## Core Research Themes")
    lines.append("")

    # Process each top community
    for rank, comm in enumerate(top_communities, 1):
        comm_id = comm["community_id"]
        paper_count = comm["paper_count"]

        summary_file = summaries_dir / f"community_{comm_id}.md"
        summary = parse_community_summary(summary_file)

        if summary is None:
            lines.append(f"### {rank}. Community {comm_id} ({paper_count} papers)")
            lines.append("")
            lines.append("*Summary not available*")
            lines.append("")
            continue

        community_name = get_community_name(summary, comm_id)

        lines.append(f"### {rank}. {community_name} ({paper_count} papers)")
        lines.append("")

        if summary["years"]:
            lines.append(f"**Period**: {summary['years']}")
            lines.append("")

        if summary["research_focus"]:
            lines.append(f"**Research Focus**: {summary['research_focus']}")
            lines.append("")

        if summary["top_entities"]:
            entities_str = ", ".join(summary["top_entities"])
            lines.append(f"**Key Entities**: {entities_str}")
            lines.append("")

        if summary["sample_papers"]:
            lines.append("**Representative Papers**:")
            for paper in summary["sample_papers"]:
                lines.append(f"- {paper}")
            lines.append("")

        lines.append("---")
        lines.append("")

    # Coverage statistics
    lines.append("## Coverage Statistics")
    lines.append("")
    lines.append(f"- **Total Papers**: {total_papers}")
    lines.append(f"- **Top {len(top_communities)} Themes**: {top_community_papers} papers ({coverage_pct:.1f}%)")
    lines.append(f"- **Total Communities (level 0.5)**: {stats['communities']['level_0.5']['num_communities']}")
    lines.append("")
    lines.append("### Community Size Distribution")
    lines.append("")
    size_dist = stats['communities']['level_0.5']['size_distribution']
    lines.append(f"- Small (<10 papers): {size_dist['small (<10)']} communities")
    lines.append(f"- Medium (10-50 papers): {size_dist['medium (10-50)']} communities")
    lines.append(f"- Large (50-100 papers): {size_dist['large (50-100)']} communities")
    lines.append(f"- Very Large (>=100 papers): {size_dist['very_large (>=100)']} communities")
    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append("*Generated by Graph RAG analysis pipeline*")

    # Write output
    output_file.write_text("\n".join(lines))
    print(f"Generated: {output_file}")
    print(f"  - Top {len(top_communities)} communities covering {top_community_papers}/{total_papers} papers ({coverage_pct:.1f}%)")


def main():
    base_dir = Path("/home/kyuwon/projects/MSK2025/data/papers/by-collection/virtual-cell-50/graph-rag-748")

    communities_file = base_dir / "communities" / "level_0.5.json"
    summaries_dir = base_dir / "summaries" / "level_0.5"
    stats_file = base_dir / "stats.json"
    output_file = base_dir / "OVERVIEW.md"

    generate_overview(base_dir, communities_file, summaries_dir, stats_file, output_file)


if __name__ == "__main__":
    main()
