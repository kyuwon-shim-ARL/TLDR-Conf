"""
Speaker Analyzer for Conference-Advisor v3.0 MVP (Phase 1)
Analyzes speaker impact using OpenAlex metrics.
"""

from typing import Dict, Any, Optional, List

try:
    from .openalex_client import OpenAlexClient
except ImportError:
    from openalex_client import OpenAlexClient


class SpeakerAnalyzer:
    """
    Analyzes conference speakers using OpenAlex data.

    Phase 1 (MVP) capabilities:
    - Basic metrics (h-index, citations, works count)
    - Top papers identification
    - Research topic extraction
    """

    def __init__(self, email: Optional[str] = None):
        """
        Initialize analyzer.

        Args:
            email: Email for OpenAlex polite pool (recommended)
        """
        self.client = OpenAlexClient(email=email)

    def analyze_speaker(
        self,
        name: str,
        affiliation: str,
        talk_title: Optional[str] = None
    ) -> Optional[Dict[str, Any]]:
        """
        Analyze speaker's research impact.

        Args:
            name: Speaker name
            affiliation: Institution
            talk_title: Talk title (optional, for context)

        Returns:
            Analysis dict or None if not found

        Example:
            analyzer = SpeakerAnalyzer(email="your@email.com")
            result = analyzer.analyze_speaker(
                "Sung Jae Shin",
                "Yonsei University",
                "Mtb vs MAC pathogenesis"
            )

            if result:
                print(f"h-index: {result['metrics']['h_index']}")
                print(f"Impact tier: {result['impact_tier']}")
        """
        # Search for author
        author = self.client.search_author(name, affiliation)
        if not author:
            return {
                "status": "not_found",
                "message": f"Could not find author: {name} ({affiliation})"
            }

        # Fetch top works
        works = self.client.fetch_author_works(author['id'], limit=10, sort="cited_by_count:desc")

        # Extract metrics
        stats = author.get('summary_stats', {})
        h_index = stats.get('h_index', 0)
        citation_count = author.get('cited_by_count', 0)
        works_count = author.get('works_count', 0)

        # Determine impact tier
        impact_tier = self._calculate_impact_tier(h_index, citation_count)

        # Extract top concepts
        concepts = [c['display_name'] for c in author.get('x_concepts', [])[:5]]

        # Format top papers
        top_papers = self._format_top_papers(works[:5])

        # Calculate career metrics
        career_metrics = self._calculate_career_metrics(works)

        return {
            "status": "found",
            "author_id": author['id'],
            "openalex_url": f"https://openalex.org/{author['id']}",
            "metrics": {
                "h_index": h_index,
                "citation_count": citation_count,
                "works_count": works_count,
                "citations_per_paper": round(citation_count / max(works_count, 1), 1)
            },
            "impact_tier": impact_tier,
            "top_concepts": concepts,
            "top_papers": top_papers,
            "career_metrics": career_metrics,
            "recommendation": self._generate_recommendation(
                impact_tier, h_index, top_papers, talk_title
            )
        }

    def _calculate_impact_tier(self, h_index: int, citations: int) -> Dict[str, Any]:
        """
        Categorize researcher impact tier.

        Tiers:
        - Elite: h-index >= 50
        - Senior Leader: h-index >= 30
        - Established: h-index >= 20
        - Mid-Career: h-index >= 10
        - Early Career: h-index < 10
        """
        if h_index >= 50:
            tier = "Elite"
            percentile = "Top 1%"
            description = "World-leading researcher with exceptional impact"
        elif h_index >= 30:
            tier = "Senior Leader"
            percentile = "Top 5%"
            description = "Highly influential senior researcher"
        elif h_index >= 20:
            tier = "Established"
            percentile = "Top 10%"
            description = "Well-established researcher with significant impact"
        elif h_index >= 10:
            tier = "Mid-Career"
            percentile = "Top 25%"
            description = "Growing impact in the field"
        else:
            tier = "Early Career"
            percentile = "Emerging"
            description = "Early-stage researcher or niche specialist"

        return {
            "tier": tier,
            "percentile": percentile,
            "description": description,
            "h_index": h_index,
            "citations": citations
        }

    def _format_top_papers(self, works: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """Format top papers for display."""
        papers = []
        for w in works:
            papers.append({
                "title": w.get('title', 'Unknown'),
                "year": w.get('publication_year'),
                "citations": w.get('cited_by_count', 0),
                "journal": w.get('host_venue', {}).get('display_name', 'Unknown'),
                "doi": w.get('doi'),
                "openalex_id": w.get('id', '').split('/')[-1] if w.get('id') else None
            })
        return papers

    def _calculate_career_metrics(self, works: List[Dict[str, Any]]) -> Dict[str, Any]:
        """Calculate career-stage metrics."""
        if not works:
            return {
                "career_length": 0,
                "recent_activity": "Unknown",
                "trend": "Unknown"
            }

        # Get year range
        years = [w.get('publication_year') for w in works if w.get('publication_year')]
        if not years:
            return {
                "career_length": 0,
                "recent_activity": "Unknown",
                "trend": "Unknown"
            }

        earliest_year = min(years)
        latest_year = max(years)
        career_length = latest_year - earliest_year + 1

        # Recent activity (last 3 years)
        recent_papers = [w for w in works if w.get('publication_year', 0) >= latest_year - 2]
        recent_citations = sum(w.get('cited_by_count', 0) for w in recent_papers)
        avg_recent = round(recent_citations / max(len(recent_papers), 1), 1)

        # Overall average
        total_citations = sum(w.get('cited_by_count', 0) for w in works)
        avg_overall = round(total_citations / len(works), 1)

        # Determine trend
        if avg_recent > avg_overall * 1.5:
            trend = "Rising (recent work highly cited)"
        elif avg_recent > avg_overall * 0.8:
            trend = "Stable (consistent impact)"
        else:
            trend = "Established (foundational work cited)"

        return {
            "career_length": career_length,
            "earliest_work": earliest_year,
            "latest_work": latest_year,
            "recent_activity": f"{len(recent_papers)} papers in last 3 years",
            "trend": trend,
            "avg_citations_recent": avg_recent,
            "avg_citations_overall": avg_overall
        }

    def _generate_recommendation(
        self,
        impact_tier: Dict[str, Any],
        h_index: int,
        top_papers: List[Dict[str, Any]],
        talk_title: Optional[str]
    ) -> str:
        """Generate attendance recommendation."""
        tier = impact_tier['tier']

        # Base recommendation
        if tier in ['Elite', 'Senior Leader']:
            rec = f"🌟 **Highly Recommended** - {impact_tier['description']} (h-index: {h_index})"
        elif tier == 'Established':
            rec = f"✅ **Recommended** - {impact_tier['description']} (h-index: {h_index})"
        elif tier == 'Mid-Career':
            rec = f"⭕ **Valuable** - {impact_tier['description']} (h-index: {h_index})"
        else:
            rec = f"📌 **Niche/Emerging** - {impact_tier['description']} (h-index: {h_index})"

        # Add paper context
        if top_papers:
            top = top_papers[0]
            rec += f"\n   Most cited work: \"{top['title']}\" ({top['year']}, {top['citations']} citations)"

        return rec


# Convenience function for skill usage

def quick_speaker_analysis(name: str, affiliation: str, email: Optional[str] = None) -> Optional[str]:
    """
    Quick speaker analysis for markdown output.

    Returns formatted markdown string ready for background document.

    Example usage in SKILL.md:
        analysis = quick_speaker_analysis("Sung Jae Shin", "Yonsei", "your@email.com")
        if analysis:
            # Insert into background document
            background += analysis
    """
    analyzer = SpeakerAnalyzer(email=email)
    result = analyzer.analyze_speaker(name, affiliation)

    if not result or result.get('status') != 'found':
        return None

    # Format as markdown
    metrics = result['metrics']
    tier = result['impact_tier']
    papers = result['top_papers']
    career = result['career_metrics']

    md = f"""
#### 📊 연구 영향력 (OpenAlex)

**Impact Tier**: {tier['tier']} ({tier['percentile']})
- **h-index**: {metrics['h_index']}
- **Total Citations**: {metrics['citation_count']:,}
- **Total Works**: {metrics['works_count']}
- **Citations per Paper**: {metrics['citations_per_paper']}

**Career**: {career['career_length']} years ({career['earliest_work']}-{career['latest_work']})
**Trend**: {career['trend']}

#### 🌟 주요 논문 (Top-Cited)

"""

    for i, paper in enumerate(papers[:5], 1):
        md += f"{i}. \"{paper['title']}\" ({paper['year']})\n"
        md += f"   - Citations: {paper['citations']:,} | Journal: {paper['journal']}\n"
        if paper['doi']:
            md += f"   - DOI: {paper['doi']}\n"
        md += "\n"

    md += f"""
#### 💡 참석 추천

{result['recommendation']}

#### 🔗 More Info
- OpenAlex Profile: {result['openalex_url']}

"""

    return md
