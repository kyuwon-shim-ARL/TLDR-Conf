"""
Anchor Paper Finder for Research Landscape Analyzer
Identifies foundational/highly-cited papers using time-weighted scoring.
"""

from typing import List, Dict, Any, Optional
from openalex_client import OpenAlexClient


class AnchorFinder:
    """
    Finds anchor (foundational) papers for a given research topic.

    Uses time-weighted citation scoring:
    - Recent papers (0-10 years): Citations per year
    - Old papers (>10 years): 0.5x penalty (foundational but less relevant)

    This prevents very old papers from dominating while keeping true anchors.
    """

    def __init__(self, email: Optional[str] = None):
        """
        Initialize finder.

        Args:
            email: Email for OpenAlex polite pool (recommended)
        """
        self.client = OpenAlexClient(email=email)
        self.current_year = 2025

    def find_anchors(
        self,
        topic: str,
        max_results: int = 10,
        years: int = 10,
        min_citations: int = 100
    ) -> List[Dict[str, Any]]:
        """
        Find anchor papers for a topic.

        Args:
            topic: Research topic (e.g., "CRISPR base editing")
            max_results: Maximum number of anchors to return
            years: Look back N years (default: 10)
            min_citations: Minimum citation count threshold

        Returns:
            List of anchor papers with metadata and scores, sorted by time-weighted score

        Example:
            finder = AnchorFinder(email="your@email.com")
            anchors = finder.find_anchors(
                "CRISPR base editing",
                max_results=8,
                years=10,
                min_citations=100
            )

            for a in anchors:
                print(f"{a['title']} ({a['publication_year']})")
                print(f"  Citations: {a['cited_by_count']}, Score: {a['anchor_score']:.2f}")
        """
        print(f"⚓ Finding anchor papers: '{topic}'")

        # Fetch highly cited papers
        print(f"  Searching last {years} years...")
        papers = self._fetch_highly_cited(topic, years, limit=500)
        print(f"  Found: {len(papers)} papers")

        # Calculate time-weighted scores
        scored_papers = []
        for paper in papers:
            score = self._calculate_anchor_score(paper)
            if score > 0:
                paper['anchor_score'] = score
                scored_papers.append(paper)

        # Filter by citation threshold
        filtered = [p for p in scored_papers if p.get('cited_by_count', 0) >= min_citations]
        print(f"  After citation filter (>={min_citations}): {len(filtered)} papers")

        # Rank by anchor score
        ranked = sorted(filtered, key=lambda x: x.get('anchor_score', 0), reverse=True)

        # Return top N
        result = ranked[:max_results]
        print(f"  ✅ Returning top {len(result)} anchors")

        return result

    def _fetch_highly_cited(
        self,
        topic: str,
        years: int,
        limit: int = 500
    ) -> List[Dict[str, Any]]:
        """
        Fetch highly cited papers for a topic.

        Args:
            topic: Research topic
            years: Look back N years
            limit: Max papers to fetch

        Returns:
            List of papers sorted by citations (descending)
        """
        # Build filter
        year_start = self.current_year - years
        filters = f"publication_year:{year_start}-{self.current_year}"

        # Search and sort by citations
        url = (f"{self.client.base_url}/works?"
               f"search={topic}&"
               f"filter={filters}&"
               f"sort=cited_by_count:desc&"
               f"per-page={min(limit, 200)}")  # OpenAlex max per page

        response = self.client._make_request(url)
        if not response:
            return []

        papers = response.get('results', [])

        # If we need more, paginate
        if limit > 200 and len(papers) == 200:
            # Fetch next page(s)
            for page in range(2, (limit // 200) + 2):
                url_page = url + f"&page={page}"
                response_page = self.client._make_request(url_page)
                if response_page and response_page.get('results'):
                    papers.extend(response_page['results'])
                else:
                    break

                if len(papers) >= limit:
                    break

        return papers[:limit]

    def _calculate_anchor_score(self, paper: Dict[str, Any]) -> float:
        """
        Calculate time-weighted anchor score.

        Formula:
        - Age = current_year - publication_year
        - Age penalty = 1.0 if age <= 10, else 0.5
        - Score = (citations / max(age, 1)) * age_penalty

        This gives recent impactful papers higher scores while
        keeping truly foundational old papers visible.

        Args:
            paper: Paper dict with 'publication_year' and 'cited_by_count'

        Returns:
            Anchor score (float)
        """
        year = paper.get('publication_year')
        citations = paper.get('cited_by_count', 0)

        if not year or citations == 0:
            return 0.0

        age = self.current_year - year

        # Age penalty for very old papers (>10 years)
        age_penalty = 1.0 if age <= 10 else 0.5

        # Citations per year, with age penalty
        score = (citations / max(age, 1)) * age_penalty

        return score


# Convenience function for quick use

def find_anchors(
    topic: str,
    max_results: int = 10,
    email: Optional[str] = None
) -> List[Dict[str, Any]]:
    """
    Quick wrapper to find anchor papers.

    Args:
        topic: Research topic
        max_results: Max number of anchors
        email: Email for polite pool

    Returns:
        List of anchor papers with scores

    Example:
        anchors = find_anchors("CRISPR base editing", max_results=8)
        for a in anchors:
            print(f"{a['title']}: {a['anchor_score']:.1f}")
    """
    finder = AnchorFinder(email=email)
    return finder.find_anchors(topic, max_results=max_results)
