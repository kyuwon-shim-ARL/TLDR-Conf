"""PyAlex-based adapter. Maintains existing OpenAlexClient API compatibility.

Replaces custom 246-line implementation with PyAlex library.
All public methods (search_author, fetch_author_works, fetch_work, get_stats)
and fetch_speaker_metrics() function maintain identical signatures and return types.
"""

import pyalex
from pyalex import Authors, Works
from typing import Optional, Dict, Any, List


class OpenAlexClient:
    """OpenAlex API client using PyAlex. Drop-in replacement for original."""

    def __init__(self, email: Optional[str] = None):
        if email:
            pyalex.config.email = email
        pyalex.config.max_retries = 3
        self.base_url: str = "https://api.openalex.org"
        self.failed_requests: list = []
        self.request_count: int = 0

    def _make_request(self, url: str) -> Optional[Dict[str, Any]]:
        """Make raw HTTP request to OpenAlex API.

        Args:
            url: Full OpenAlex API URL

        Returns:
            JSON response dict or None on failure
        """
        import requests
        self.request_count += 1
        try:
            headers = {}
            if pyalex.config.email:
                headers["User-Agent"] = f"mailto:{pyalex.config.email}"
            resp = requests.get(url, headers=headers, timeout=30)
            resp.raise_for_status()
            return resp.json()
        except Exception:
            self.failed_requests.append(url[:120])
            return None

    def search_author(self, name: str, affiliation: Optional[str] = None) -> Optional[Dict[str, Any]]:
        """Search for author by name and optional affiliation.

        Args:
            name: Author name (e.g., "Sung Jae Shin")
            affiliation: Institution name (e.g., "Yonsei University")

        Returns:
            Author data with metrics, or None if not found
        """
        self.request_count += 1
        try:
            results = Authors().search(name).get()
        except Exception:
            self.failed_requests.append(f"search_author:{name}")
            return None

        if not results:
            return None

        # Affiliation matching (mirrors original lines 123-133)
        if affiliation and len(results) > 1:
            affiliation_lower = affiliation.lower()
            for result in results:
                for aff in result.get('affiliations', []):
                    inst_name = aff.get('institution', {}).get('display_name', '').lower()
                    if affiliation_lower in inst_name or inst_name in affiliation_lower:
                        return result

        return results[0]

    def fetch_author_works(
        self,
        author_id: str,
        limit: int = 10,
        sort: str = "cited_by_count:desc"
    ) -> List[Dict[str, Any]]:
        """Fetch author's works (papers).

        Args:
            author_id: OpenAlex author ID (e.g., "A1234567890")
            limit: Number of works to fetch
            sort: Sort order (default: most cited first)

        Returns:
            List of work metadata
        """
        self.request_count += 1
        if author_id.startswith('http'):
            author_id = author_id.split('/')[-1]

        sort_field, sort_dir = sort.split(":")
        try:
            results = []
            for page in Works().filter(
                authorships={"author": {"id": author_id}}
            ).sort(**{sort_field: sort_dir}).paginate(per_page=limit, n_max=limit):
                results.extend(page)
            return results[:limit]
        except Exception:
            self.failed_requests.append(f"fetch_author_works:{author_id}")
            return []

    def fetch_work(self, work_id: str) -> Optional[Dict[str, Any]]:
        """Fetch single work by ID.

        Args:
            work_id: OpenAlex work ID (e.g., "W1234567890") or DOI

        Returns:
            Work metadata or None
        """
        self.request_count += 1
        if work_id.startswith('http'):
            work_id = work_id.split('/')[-1]
        try:
            return Works()[work_id]
        except Exception:
            self.failed_requests.append(work_id)
            return None

    def get_stats(self) -> Dict[str, Any]:
        """Get client statistics."""
        return {
            "total_requests": self.request_count,
            "failed_requests": len(self.failed_requests),
            "success_rate": 1.0 - (len(self.failed_requests) / max(self.request_count, 1))
        }


def fetch_speaker_metrics(name: str, affiliation: str, email: Optional[str] = None) -> Optional[Dict[str, Any]]:
    """Fetch basic speaker metrics from OpenAlex.

    Args:
        name: Speaker name
        affiliation: Institution
        email: Your email for polite pool (recommended)

    Returns:
        Dict with h_index, citation_count, works_count, top_papers
    """
    client = OpenAlexClient(email=email)
    author = client.search_author(name, affiliation)
    if not author:
        return None

    works = client.fetch_author_works(author['id'], limit=5)
    stats = author.get('summary_stats', {})

    return {
        "author_id": author['id'],
        "h_index": stats.get('h_index', 0),
        "citation_count": author.get('cited_by_count', 0),
        "works_count": author.get('works_count', 0),
        "top_concepts": [t['display_name'] for t in author.get('topics', [])[:5]],
        "top_papers": [
            {"title": w.get('title', 'Unknown'), "year": w.get('publication_year'),
             "citations": w.get('cited_by_count', 0), "doi": w.get('doi')}
            for w in works[:5]
        ],
        "openalex_url": f"https://openalex.org/{author['id']}"
    }
