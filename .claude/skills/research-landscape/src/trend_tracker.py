"""
Trend Tracker for Research Landscape Analyzer
Identifies recent derivative research and emerging trends.
"""

from typing import List, Dict, Any, Optional
from collections import Counter
from openalex_client import OpenAlexClient


class TrendTracker:
    """
    Tracks recent trends by analyzing papers that cite anchor papers.

    Identifies:
    - Recent derivative research (2023-2025)
    - Emerging concepts (topic shifts)
    - Cluster by approach/application
    """

    def __init__(self, email: Optional[str] = None):
        """
        Initialize tracker.

        Args:
            email: Email for OpenAlex polite pool (recommended)
        """
        self.client = OpenAlexClient(email=email)
        self.current_year = 2025

    def find_recent_derivatives(
        self,
        anchor_papers: List[Dict[str, Any]],
        years: int = 2,
        min_citations: int = 5,
        max_papers: int = 50
    ) -> List[Dict[str, Any]]:
        """
        Find recent papers citing anchor papers.

        Args:
            anchor_papers: Foundational papers to track from
            years: Look at papers from last N years (default: 2 = 2023-2025)
            min_citations: Min citation threshold (even recent papers should have some)
            max_papers: Max papers to return

        Returns:
            List of recent papers with metadata

        Example:
            tracker = TrendTracker(email="your@email.com")
            recent = tracker.find_recent_derivatives(
                anchor_papers=anchors,
                years=2,
                min_citations=5,
                max_papers=30
            )

            print(f"Found {len(recent)} recent papers")
            for p in recent[:5]:
                print(f"- {p['title']} ({p['publication_year']})")
        """
        print(f"\n📈 Finding recent derivatives (last {years} years)...")

        year_start = self.current_year - years

        all_recent = []
        seen_ids = set()

        # For each anchor, find recent papers citing it
        for anchor in anchor_papers:
            anchor_id = self._extract_id(anchor.get('id'))
            if not anchor_id:
                continue

            # Fetch citing papers from recent years
            url = (f"{self.client.base_url}/works?"
                   f"filter=cites:{anchor_id},publication_year:{year_start}-{self.current_year}&"
                   f"sort=cited_by_count:desc&"
                   f"per-page=50")

            response = self.client._make_request(url)
            if not response:
                continue

            papers = response.get('results', [])

            for paper in papers:
                paper_id = self._extract_id(paper.get('id'))
                if paper_id and paper_id not in seen_ids:
                    if paper.get('cited_by_count', 0) >= min_citations:
                        all_recent.append(paper)
                        seen_ids.add(paper_id)

        # Sort by citations and limit
        sorted_recent = sorted(
            all_recent,
            key=lambda x: x.get('cited_by_count', 0),
            reverse=True
        )[:max_papers]

        print(f"   Found {len(sorted_recent)} recent papers ({year_start}-{self.current_year})")

        return sorted_recent

    def cluster_by_concepts(
        self,
        papers: List[Dict[str, Any]],
        max_clusters: int = 5
    ) -> Dict[str, List[Dict[str, Any]]]:
        """
        Cluster papers by primary research concepts.

        Args:
            papers: Papers to cluster
            max_clusters: Maximum number of clusters

        Returns:
            Dict mapping concept name to list of papers

        Example:
            clusters = tracker.cluster_by_concepts(recent_papers)
            for concept, papers in clusters.items():
                print(f"\n{concept} ({len(papers)} papers):")
                for p in papers[:3]:
                    print(f"  - {p['title']}")
        """
        print(f"\n🗂️  Clustering papers by concepts...")

        # Extract top concepts from all papers
        concept_counts = Counter()
        paper_concepts = {}  # paper_id -> primary concept

        for paper in papers:
            paper_id = self._extract_id(paper.get('id'))
            concepts = paper.get('concepts', [])

            if concepts:
                # Primary concept is first (highest score)
                primary = concepts[0].get('display_name')
                if primary:
                    concept_counts[primary] += 1
                    paper_concepts[paper_id] = primary

        # Get top N concepts
        top_concepts = [c for c, _ in concept_counts.most_common(max_clusters)]

        # Cluster papers
        clusters = {concept: [] for concept in top_concepts}

        for paper in papers:
            paper_id = self._extract_id(paper.get('id'))
            primary_concept = paper_concepts.get(paper_id)

            if primary_concept in clusters:
                clusters[primary_concept].append(paper)

        # Remove empty clusters
        clusters = {k: v for k, v in clusters.items() if v}

        print(f"   Created {len(clusters)} clusters")
        for concept, papers_in_cluster in clusters.items():
            print(f"      {concept}: {len(papers_in_cluster)} papers")

        return clusters

    def detect_emerging_concepts(
        self,
        recent_papers: List[Dict[str, Any]],
        anchor_papers: List[Dict[str, Any]],
        top_k: int = 10
    ) -> List[Dict[str, Any]]:
        """
        Detect concepts that are emerging (frequent in recent vs anchor papers).

        Args:
            recent_papers: Recent derivative papers
            anchor_papers: Foundational anchor papers
            top_k: Number of top emerging concepts

        Returns:
            List of dicts with concept name, recent_count, anchor_count, growth_rate

        Example:
            emerging = tracker.detect_emerging_concepts(recent, anchors)
            for concept in emerging[:5]:
                print(f"{concept['name']}: {concept['growth_rate']:.1f}x growth")
        """
        print(f"\n🌱 Detecting emerging concepts...")

        # Count concepts in anchor papers
        anchor_concepts = Counter()
        for paper in anchor_papers:
            for concept in paper.get('concepts', []):
                name = concept.get('display_name')
                if name:
                    anchor_concepts[name] += 1

        # Count concepts in recent papers
        recent_concepts = Counter()
        for paper in recent_papers:
            for concept in paper.get('concepts', []):
                name = concept.get('display_name')
                if name:
                    recent_concepts[name] += 1

        # Calculate growth rates
        emerging = []
        for concept, recent_count in recent_concepts.most_common(50):
            anchor_count = anchor_concepts.get(concept, 0)

            # Calculate growth rate (avoid division by zero)
            if anchor_count > 0:
                growth_rate = recent_count / anchor_count
            else:
                growth_rate = float('inf')  # New concept (not in anchors)

            # Filter: must appear in recent but grow significantly
            if recent_count >= 3 and growth_rate > 1.5:
                emerging.append({
                    'name': concept,
                    'recent_count': recent_count,
                    'anchor_count': anchor_count,
                    'growth_rate': growth_rate,
                    'is_new': anchor_count == 0
                })

        # Sort by growth rate
        emerging = sorted(emerging, key=lambda x: x['growth_rate'], reverse=True)[:top_k]

        print(f"   Found {len(emerging)} emerging concepts")
        for concept in emerging[:3]:
            if concept['is_new']:
                print(f"      {concept['name']}: NEW (not in anchors)")
            else:
                print(f"      {concept['name']}: {concept['growth_rate']:.1f}x growth")

        return emerging

    def _extract_id(self, openalex_id: str) -> Optional[str]:
        """Extract clean ID from OpenAlex ID."""
        if not openalex_id:
            return None

        if openalex_id.startswith('http'):
            return openalex_id.split('/')[-1]
        return openalex_id


# Convenience functions

def find_recent_trends(
    anchor_papers: List[Dict[str, Any]],
    years: int = 2,
    email: Optional[str] = None
) -> List[Dict[str, Any]]:
    """
    Quick wrapper to find recent derivative papers.

    Args:
        anchor_papers: Foundational papers
        years: Look back N years
        email: Email for polite pool

    Returns:
        List of recent papers

    Example:
        recent = find_recent_trends(anchors, years=2)
        print(f"{len(recent)} papers in last 2 years")
    """
    tracker = TrendTracker(email=email)
    return tracker.find_recent_derivatives(anchor_papers, years=years)
