"""
OpenAlex API Client for Conference-Advisor v3.0
Fetches author metrics and paper metadata for speaker analysis.
"""

import requests
import time
from typing import Optional, Dict, Any, List
from urllib.parse import quote


class OpenAlexClient:
    """
    OpenAlex API client with retry logic and rate limiting.

    Usage:
        client = OpenAlexClient(email="your@email.com")
        author = client.search_author("Sung Jae Shin", "Yonsei University")
        works = client.fetch_author_works(author['id'], limit=10)
    """

    def __init__(self, email: Optional[str] = None):
        """
        Initialize client.

        Args:
            email: Email for OpenAlex polite pool (10 req/sec vs 100k/day limit)
                  If provided, adds to User-Agent for better rate limits
        """
        self.base_url = "https://api.openalex.org"
        self.email = email
        self.headers = {}
        if email:
            self.headers["User-Agent"] = f"ConferenceAdvisor/3.0 (mailto:{email})"

        # Rate limiting
        self.request_delay = 0.1  # 100ms between requests (safe for polite pool)
        self.last_request_time = 0

        # Tracking
        self.failed_requests = []
        self.request_count = 0

    def _rate_limit(self):
        """Enforce rate limiting between requests."""
        elapsed = time.time() - self.last_request_time
        if elapsed < self.request_delay:
            time.sleep(self.request_delay - elapsed)
        self.last_request_time = time.time()

    def _make_request(self, url: str, max_retries: int = 3) -> Optional[Dict[str, Any]]:
        """
        Make HTTP request with retry logic.

        Args:
            url: Full URL to request
            max_retries: Number of retry attempts

        Returns:
            JSON response or None if failed
        """
        self._rate_limit()
        self.request_count += 1

        for attempt in range(max_retries):
            try:
                response = requests.get(url, headers=self.headers, timeout=10)

                if response.status_code == 200:
                    return response.json()
                elif response.status_code == 429:
                    # Rate limited - exponential backoff
                    wait_time = 2 ** attempt
                    print(f"Rate limited, waiting {wait_time}s...")
                    time.sleep(wait_time)
                    continue
                elif response.status_code == 404:
                    # Not found
                    return None
                else:
                    response.raise_for_status()

            except (requests.exceptions.Timeout, requests.exceptions.RequestException) as e:
                if attempt < max_retries - 1:
                    wait_time = 2 ** attempt
                    print(f"Request failed ({e}), retrying in {wait_time}s...")
                    time.sleep(wait_time)
                    continue
                else:
                    print(f"Request failed after {max_retries} attempts: {url}")
                    self.failed_requests.append(url)
                    return None

        return None

    def search_author(self, name: str, affiliation: Optional[str] = None) -> Optional[Dict[str, Any]]:
        """
        Search for author by name and optional affiliation.

        Args:
            name: Author name (e.g., "Sung Jae Shin")
            affiliation: Institution name (e.g., "Yonsei University")

        Returns:
            Author data with metrics, or None if not found

        Example:
            author = client.search_author("Sung Jae Shin", "Yonsei")
            print(author['summary_stats']['h_index'])  # 45
        """
        # Build search URL - use search parameter only
        # Complex filters cause 403, so we'll search broadly and filter in code
        search_query = quote(name)
        url = f"{self.base_url}/authors?search={search_query}&per-page=10"

        response = self._make_request(url)
        if not response or not response.get('results'):
            return None

        results = response['results']

        # If affiliation provided, try to find best match
        if affiliation and len(results) > 1:
            affiliation_lower = affiliation.lower()
            for result in results:
                # Check if affiliation matches in any listed institution
                for aff in result.get('affiliations', []):
                    inst_name = aff.get('institution', {}).get('display_name', '').lower()
                    if affiliation_lower in inst_name or inst_name in affiliation_lower:
                        return result

        # Return first match (best relevance score)
        return results[0]

    def fetch_author_works(
        self,
        author_id: str,
        limit: int = 10,
        sort: str = "cited_by_count:desc"
    ) -> List[Dict[str, Any]]:
        """
        Fetch author's works (papers).

        Args:
            author_id: OpenAlex author ID (e.g., "A1234567890")
            limit: Number of works to fetch
            sort: Sort order (default: most cited first)

        Returns:
            List of work metadata

        Example:
            works = client.fetch_author_works("A1234567890", limit=5)
            for work in works:
                print(f"{work['title']} - {work['cited_by_count']} citations")
        """
        # Clean author ID (remove URL prefix if present)
        if author_id.startswith('http'):
            author_id = author_id.split('/')[-1]

        url = f"{self.base_url}/works?filter=author.id:{author_id}&sort={sort}&per-page={limit}"

        response = self._make_request(url)
        if not response:
            return []

        return response.get('results', [])

    def fetch_work(self, work_id: str) -> Optional[Dict[str, Any]]:
        """
        Fetch single work by ID.

        Args:
            work_id: OpenAlex work ID (e.g., "W1234567890") or DOI

        Returns:
            Work metadata or None
        """
        # Clean work ID
        if work_id.startswith('http'):
            work_id = work_id.split('/')[-1]

        url = f"{self.base_url}/works/{work_id}"
        return self._make_request(url)

    def get_stats(self) -> Dict[str, Any]:
        """Get client statistics."""
        return {
            "total_requests": self.request_count,
            "failed_requests": len(self.failed_requests),
            "success_rate": 1.0 - (len(self.failed_requests) / max(self.request_count, 1))
        }


# Convenience functions for direct use in SKILL.md

def fetch_speaker_metrics(name: str, affiliation: str, email: Optional[str] = None) -> Optional[Dict[str, Any]]:
    """
    Fetch basic speaker metrics from OpenAlex.

    Convenience function for use in conference-advisor skill.

    Args:
        name: Speaker name
        affiliation: Institution
        email: Your email for polite pool (recommended)

    Returns:
        Dict with h_index, citation_count, works_count, top_papers

    Example usage in SKILL.md:
        metrics = fetch_speaker_metrics("Sung Jae Shin", "Yonsei", "your@email.com")
        if metrics:
            print(f"h-index: {metrics['h_index']}")
    """
    client = OpenAlexClient(email=email)

    # Search for author
    author = client.search_author(name, affiliation)
    if not author:
        return None

    # Fetch top papers
    works = client.fetch_author_works(author['id'], limit=5)

    # Extract summary stats
    stats = author.get('summary_stats', {})

    return {
        "author_id": author['id'],
        "h_index": stats.get('h_index', 0),
        "citation_count": author.get('cited_by_count', 0),
        "works_count": author.get('works_count', 0),
        "top_concepts": [c['display_name'] for c in author.get('x_concepts', [])[:5]],
        "top_papers": [
            {
                "title": w.get('title', 'Unknown'),
                "year": w.get('publication_year'),
                "citations": w.get('cited_by_count', 0),
                "doi": w.get('doi')
            }
            for w in works[:5]
        ],
        "openalex_url": f"https://openalex.org/{author['id']}"
    }
