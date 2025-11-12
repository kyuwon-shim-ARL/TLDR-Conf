"""
Review Paper Finder for Research Landscape Analyzer
Identifies review papers using OpenAlex type filter + heuristics.
"""

import re
from typing import List, Dict, Any, Optional
from openalex_client import OpenAlexClient


class ReviewFinder:
    """
    Finds review papers for a given research topic.

    Combines two methods:
    1. OpenAlex official type='review' (low recall ~10-15%)
    2. Title heuristics (higher recall ~50-60%)

    Then deduplicates and ranks by citations.
    """

    def __init__(self, email: Optional[str] = None):
        """
        Initialize finder.

        Args:
            email: Email for OpenAlex polite pool (recommended)
        """
        self.client = OpenAlexClient(email=email)

        # Review paper keywords (for heuristic detection)
        self.review_keywords = [
            'review', 'comprehensive', 'perspective', 'survey',
            'overview', 'state of the art', 'state-of-the-art',
            'recent advances', 'recent progress', 'current status'
        ]

        # Exclude patterns (not real reviews)
        self.exclude_keywords = [
            'case report', 'patient', 'clinical case',
            'book review', 'systematic review'  # systematic reviews are meta-analyses
        ]

    def find_reviews(
        self,
        topic: str,
        max_results: int = 20,
        min_citations: int = 50,
        years: Optional[int] = None
    ) -> List[Dict[str, Any]]:
        """
        Find review papers for a topic.

        Args:
            topic: Research topic (e.g., "CRISPR base editing")
            max_results: Maximum number of reviews to return
            min_citations: Minimum citation count threshold
            years: Look back N years (None = all time)

        Returns:
            List of review papers with metadata, sorted by citations

        Example:
            finder = ReviewFinder(email="your@email.com")
            reviews = finder.find_reviews(
                "CRISPR base editing",
                max_results=15,
                min_citations=50,
                years=5
            )

            for r in reviews:
                print(f"{r['title']} ({r['publication_year']}, {r['cited_by_count']} cites)")
        """
        print(f"🔍 Searching for review papers: '{topic}'")

        # Method 1: Official type=review
        print("  Method 1: OpenAlex type='review'...")
        official_reviews = self._fetch_official_reviews(topic, years)
        print(f"    Found: {len(official_reviews)} papers")

        # Method 2: Heuristic (title matching)
        print("  Method 2: Title heuristics...")
        heuristic_reviews = self._fetch_heuristic_reviews(topic, years)
        print(f"    Found: {len(heuristic_reviews)} papers")

        # Deduplicate
        all_reviews = self._deduplicate(official_reviews + heuristic_reviews)
        print(f"  Total unique: {len(all_reviews)} papers")

        # Filter by citations
        filtered = [r for r in all_reviews if r.get('cited_by_count', 0) >= min_citations]
        print(f"  After citation filter (>={min_citations}): {len(filtered)} papers")

        # Rank by citations
        ranked = sorted(filtered, key=lambda x: x.get('cited_by_count', 0), reverse=True)

        # Return top N
        result = ranked[:max_results]
        print(f"  ✅ Returning top {len(result)} reviews")

        return result

    def _fetch_official_reviews(
        self,
        topic: str,
        years: Optional[int]
    ) -> List[Dict[str, Any]]:
        """Fetch papers with OpenAlex type='review'."""
        # Build filter
        filters = [f"type:review"]

        if years:
            year_start = 2025 - years
            filters.append(f"publication_year:{year_start}-2025")

        # Search
        url = f"{self.client.base_url}/works?search={topic}&filter={','.join(filters)}&per-page=50"

        response = self.client._make_request(url)
        if not response:
            return []

        return response.get('results', [])

    def _fetch_heuristic_reviews(
        self,
        topic: str,
        years: Optional[int]
    ) -> List[Dict[str, Any]]:
        """Fetch papers with review keywords in title."""
        # Build year filter
        filters = []
        if years:
            year_start = 2025 - years
            filters.append(f"publication_year:{year_start}-2025")

        # Search broadly
        filter_str = ','.join(filters) if filters else None
        if filter_str:
            url = f"{self.client.base_url}/works?search={topic}&filter={filter_str}&per-page=200"
        else:
            url = f"{self.client.base_url}/works?search={topic}&per-page=200"

        response = self.client._make_request(url)
        if not response:
            return []

        papers = response.get('results', [])

        # Filter by title heuristics
        reviews = []
        for paper in papers:
            if self._is_likely_review(paper):
                reviews.append(paper)

        return reviews

    def _is_likely_review(self, paper: Dict[str, Any]) -> bool:
        """
        Check if paper is likely a review based on title.

        Returns True if:
        - Title contains review keywords
        - Title does NOT contain exclude keywords
        """
        title = paper.get('title', '').lower()

        # Check exclude patterns first
        for exclude in self.exclude_keywords:
            if exclude in title:
                return False

        # Check review keywords
        for keyword in self.review_keywords:
            if keyword in title:
                return True

        return False

    def _deduplicate(self, papers: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """
        Remove duplicate papers (same OpenAlex ID).

        Args:
            papers: List of paper dicts

        Returns:
            Deduplicated list
        """
        seen_ids = set()
        unique = []

        for paper in papers:
            paper_id = paper.get('id')
            if paper_id and paper_id not in seen_ids:
                seen_ids.add(paper_id)
                unique.append(paper)

        return unique


# Convenience function for quick use

def find_reviews(
    topic: str,
    max_results: int = 20,
    email: Optional[str] = None
) -> List[Dict[str, Any]]:
    """
    Quick wrapper to find review papers.

    Args:
        topic: Research topic
        max_results: Max number of reviews
        email: Email for polite pool

    Returns:
        List of review papers

    Example:
        reviews = find_reviews("CRISPR base editing", max_results=10)
        for r in reviews:
            print(r['title'])
    """
    finder = ReviewFinder(email=email)
    return finder.find_reviews(topic, max_results=max_results)
