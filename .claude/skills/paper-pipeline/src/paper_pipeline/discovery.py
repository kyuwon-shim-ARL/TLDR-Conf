"""
Paper Discovery module using PyAlex for OpenAlex search.

Replaces custom 246-line OpenAlexClient with PyAlex library.
PyAlex handles: search, filter, cursor pagination, abstract restoration, rate limiting.
"""

import pyalex
from pyalex import Works, Authors
from typing import Optional
from tqdm import tqdm


class PaperDiscovery:
    """PyAlex-based paper search with progress tracking.

    Usage:
        discovery = PaperDiscovery(email="your@email.com")
        papers = discovery.search("urban microbiome", max_results=50)
    """

    def __init__(self, email: str):
        """Initialize with email for OpenAlex polite pool (10 req/sec).

        Args:
            email: Email for polite pool access
        """
        pyalex.config.email = email
        pyalex.config.max_retries = 3
        pyalex.config.retry_backoff_factor = 0.1
        pyalex.config.retry_http_codes = [429, 500, 503]

    def search(
        self,
        query: str,
        max_results: int = 50,
        filters: Optional[dict] = None,
        sort_by: str = "cited_by_count",
        sort_order: str = "desc",
    ) -> list[dict]:
        """Search papers via PyAlex. Abstracts are automatically restored.

        Args:
            query: Search query string
            max_results: Maximum number of results to return
            filters: OpenAlex filter dict (e.g., {"publication_year": ">2020", "is_oa": True})
            sort_by: Sort field name
            sort_order: "desc" or "asc"

        Returns:
            List of normalized paper dicts
        """
        q = Works().search(query)
        if filters:
            q = q.filter(**filters)
        q = q.sort(**{sort_by: sort_order})

        results = []
        per_page = min(200, max_results)
        with tqdm(total=max_results, desc="Searching papers", unit="paper") as pbar:
            for page in q.paginate(per_page=per_page, n_max=max_results):
                for work in page:
                    results.append(self._normalize_work(work))
                    pbar.update(1)
                    if len(results) >= max_results:
                        break
                if len(results) >= max_results:
                    break

        return results[:max_results]

    def search_by_doi(self, doi: str) -> Optional[dict]:
        """Search single paper by DOI.

        Args:
            doi: DOI string (with or without https://doi.org/ prefix)

        Returns:
            Normalized paper dict or None
        """
        clean_doi = doi.replace("https://doi.org/", "").replace("http://doi.org/", "")
        try:
            work = Works()[f"https://doi.org/{clean_doi}"]
            if work:
                return self._normalize_work(work)
        except Exception:
            pass
        return None

    def search_by_dois(self, dois: list[str], batch_size: int = 30) -> list[dict]:
        """Batch search by DOIs. Splits into batches to avoid URL length limits.

        Args:
            dois: List of DOI strings
            batch_size: Number of DOIs per batch (max 30 to avoid URL limit)

        Returns:
            List of normalized paper dicts
        """
        results = []
        for i in tqdm(range(0, len(dois), batch_size), desc="Fetching DOIs", unit="batch"):
            batch = dois[i : i + batch_size]
            doi_filter = "|".join(
                d.replace("https://doi.org/", "").replace("http://doi.org/", "")
                for d in batch
            )
            try:
                for page in Works().filter(doi=doi_filter).paginate(
                    per_page=batch_size, n_max=batch_size
                ):
                    for work in page:
                        results.append(self._normalize_work(work))
            except Exception as e:
                print(f"Batch fetch failed: {e}")
                continue
        return results

    def search_by_topic(self, topic_id: str, max_results: int = 50, **filters) -> list[dict]:
        """Search papers by OpenAlex topic ID.

        Args:
            topic_id: OpenAlex topic ID (e.g., "T12345")
            max_results: Maximum results
            **filters: Additional OpenAlex filters

        Returns:
            List of normalized paper dicts
        """
        q = Works().filter(topics={"id": topic_id}, **filters)
        q = q.sort(cited_by_count="desc")

        results = []
        for page in q.paginate(per_page=min(200, max_results), n_max=max_results):
            for work in page:
                results.append(self._normalize_work(work))
        return results[:max_results]

    def get_oa_pdf_url(self, work: dict) -> Optional[str]:
        """Extract OA PDF URL from work data with fallback chain.

        Priority: primary_location → open_access.oa_url → locations

        Args:
            work: Raw PyAlex work dict

        Returns:
            PDF URL string or None
        """
        # 1. primary_location pdf_url
        primary = work.get("primary_location") or {}
        if primary.get("pdf_url"):
            return primary["pdf_url"]

        # 2. open_access.oa_url
        oa = work.get("open_access") or {}
        if oa.get("oa_url"):
            return oa["oa_url"]

        # 3. Scan all locations
        for loc in work.get("locations") or []:
            if loc.get("pdf_url"):
                return loc["pdf_url"]

        return None

    def _normalize_work(self, work: dict) -> dict:
        """Convert PyAlex work to internal schema.

        PyAlex automatically restores abstract from inverted index.

        Args:
            work: Raw PyAlex work dict

        Returns:
            Normalized paper dict
        """
        doi_raw = work.get("doi") or ""
        doi = doi_raw.replace("https://doi.org/", "").replace("http://doi.org/", "")

        primary_loc = work.get("primary_location") or {}
        source = primary_loc.get("source") or {}

        return {
            "doi": doi,
            "openalex_id": work.get("id", ""),
            "title": work.get("title", ""),
            "abstract": work.get("abstract"),  # PyAlex restores automatically
            "publication_year": work.get("publication_year"),
            "publication_date": work.get("publication_date"),
            "journal": source.get("display_name"),
            "cited_by_count": work.get("cited_by_count", 0),
            "is_oa": (work.get("open_access") or {}).get("is_oa", False),
            "oa_status": (work.get("open_access") or {}).get("oa_status"),
            "oa_url": (work.get("open_access") or {}).get("oa_url"),
            "pdf_url": self.get_oa_pdf_url(work),
            "authorships": work.get("authorships", []),
            "topics": [t.get("display_name") for t in (work.get("topics") or [])[:5]],
            "type": work.get("type"),
        }
