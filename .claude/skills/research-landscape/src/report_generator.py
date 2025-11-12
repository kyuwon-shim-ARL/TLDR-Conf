"""
Report Generator for Research Landscape Analyzer (MVP)
Generates markdown reports from analysis results.
"""

from typing import List, Dict, Any
from datetime import datetime


class ReportGenerator:
    """
    Generates markdown reports for research landscape analysis.

    MVP version: Basic review + anchor paper sections
    """

    def __init__(self):
        """Initialize generator."""
        pass

    def generate(
        self,
        topic: str,
        reviews: List[Dict[str, Any]],
        anchors: List[Dict[str, Any]],
        analysis_metadata: Dict[str, Any] = None,
        network_metrics: Dict[str, Any] = None,
        bridge_papers: List[Dict[str, Any]] = None,
        recent_trends: List[Dict[str, Any]] = None,
        trend_clusters: Dict[str, List[Dict[str, Any]]] = None,
        emerging_concepts: List[Dict[str, Any]] = None
    ) -> str:
        """
        Generate full markdown report.

        Args:
            topic: Research topic analyzed
            reviews: List of review papers
            anchors: List of anchor papers
            analysis_metadata: Optional metadata (API calls, time, etc.)
            network_metrics: Optional citation network metrics
            bridge_papers: Optional list of bridge papers
            recent_trends: Optional list of recent derivative papers
            trend_clusters: Optional concept-based clustering of trends
            emerging_concepts: Optional list of emerging concepts

        Returns:
            Markdown string

        Example:
            generator = ReportGenerator()
            report = generator.generate(
                topic="CRISPR base editing",
                reviews=review_papers,
                anchors=anchor_papers,
                network_metrics=metrics,
                recent_trends=trends
            )

            with open("analysis.md", "w") as f:
                f.write(report)
        """
        sections = []

        # Header
        sections.append(self._generate_header(topic, analysis_metadata))

        # Executive summary
        sections.append(self._generate_summary(topic, reviews, anchors))

        # Review papers
        sections.append(self._generate_review_section(reviews))

        # Anchor papers
        sections.append(self._generate_anchor_section(anchors))

        # Citation network (if available)
        if network_metrics:
            sections.append(self._generate_network_section(network_metrics, bridge_papers))

        # Recent trends (if available)
        if recent_trends:
            sections.append(self._generate_trends_section(recent_trends, trend_clusters, emerging_concepts))

        # Footer
        sections.append(self._generate_footer(analysis_metadata))

        return "\n\n".join(sections)

    def _generate_header(
        self,
        topic: str,
        metadata: Dict[str, Any] = None
    ) -> str:
        """Generate report header."""
        date_str = datetime.now().strftime("%Y-%m-%d")

        header = f"""# Research Landscape Analysis: {topic}

*Generated: {date_str}*
*Tool: Research Landscape Analyzer v1.0 (MVP)*"""

        if metadata:
            years = metadata.get('years', 'all time')
            header += f"\n*Analysis period: {years}*"

        header += "\n\n---"

        return header

    def _generate_summary(
        self,
        topic: str,
        reviews: List[Dict[str, Any]],
        anchors: List[Dict[str, Any]]
    ) -> str:
        """Generate executive summary."""
        summary = f"""## Executive Summary

**Topic**: {topic}
**Review papers found**: {len(reviews)}
**Anchor papers found**: {len(anchors)}

"""

        if reviews:
            top_review = reviews[0]
            summary += f"**Top review**: \"{top_review.get('title', 'Unknown')}\" "
            summary += f"({top_review.get('publication_year', 'N/A')}, "
            summary += f"{top_review.get('cited_by_count', 0):,} citations)\n\n"

        if anchors:
            top_anchor = anchors[0]
            summary += f"**Top anchor**: \"{top_anchor.get('title', 'Unknown')}\" "
            summary += f"({top_anchor.get('publication_year', 'N/A')}, "
            summary += f"{top_anchor.get('cited_by_count', 0):,} citations, "
            summary += f"score: {top_anchor.get('anchor_score', 0):.1f})\n\n"

        summary += "**Reading recommendation**: Start with top review paper for comprehensive overview."

        summary += "\n\n---"

        return summary

    def _generate_review_section(self, reviews: List[Dict[str, Any]]) -> str:
        """Generate review papers section."""
        if not reviews:
            return "## Review Papers\n\n*No review papers found.*"

        section = f"""## Review Papers ({len(reviews)})

*Comprehensive overviews and synthesis papers*

"""

        for i, paper in enumerate(reviews, 1):
            section += self._format_paper(i, paper, is_review=True)
            section += "\n"

        return section.rstrip()

    def _generate_anchor_section(self, anchors: List[Dict[str, Any]]) -> str:
        """Generate anchor papers section."""
        if not anchors:
            return "## Anchor Papers\n\n*No anchor papers found.*"

        section = f"""## Anchor Papers ({len(anchors)})

*Foundational highly-cited papers (time-weighted scoring)*

"""

        for i, paper in enumerate(anchors, 1):
            section += self._format_paper(i, paper, is_anchor=True)
            section += "\n"

        return section.rstrip()

    def _format_paper(
        self,
        number: int,
        paper: Dict[str, Any],
        is_review: bool = False,
        is_anchor: bool = False
    ) -> str:
        """
        Format a single paper entry.

        Args:
            number: Paper number in list
            paper: Paper dict
            is_review: Is this a review paper?
            is_anchor: Is this an anchor paper?

        Returns:
            Formatted markdown string
        """
        title = paper.get('title', 'Unknown Title')
        year = paper.get('publication_year', 'N/A')
        citations = paper.get('cited_by_count', 0)

        # Journal/venue
        venue = paper.get('host_venue', {})
        journal = venue.get('display_name', 'Unknown Journal')

        # Authors (first author + et al)
        authors_list = paper.get('authorships', [])
        if authors_list:
            first_author = authors_list[0].get('author', {}).get('display_name', 'Unknown')
            if len(authors_list) > 1:
                authors = f"{first_author} et al."
            else:
                authors = first_author
        else:
            authors = "Unknown Authors"

        # DOI
        doi = paper.get('doi')
        doi_str = f"[DOI]({doi})" if doi else "DOI: N/A"

        # Build entry
        entry = f"### {number}. \"{title}\"\n\n"
        entry += f"- **Year**: {year}\n"
        entry += f"- **Citations**: {citations:,}\n"
        entry += f"- **Journal**: {journal}\n"
        entry += f"- **Authors**: {authors}\n"

        if is_anchor:
            score = paper.get('anchor_score', 0)
            entry += f"- **Anchor Score**: {score:.2f} (citations/year, time-weighted)\n"

        entry += f"- **Link**: {doi_str}\n"

        return entry

    def _generate_network_section(
        self,
        metrics: Dict[str, Any],
        bridge_papers: List[Dict[str, Any]] = None
    ) -> str:
        """Generate citation network analysis section."""
        section = "## Citation Network Analysis\n\n"
        section += "*Network topology and influence metrics*\n\n"

        # Network statistics
        section += "**Network Statistics**:\n"
        section += f"- **Nodes (papers)**: {metrics.get('num_nodes', 0):,}\n"
        section += f"- **Edges (citations)**: {metrics.get('num_edges', 0):,}\n"
        section += f"- **Density**: {metrics.get('density', 0):.4f}\n"
        section += f"- **Average clustering**: {metrics.get('clustering', 0):.3f}\n"

        if metrics.get('diameter'):
            section += f"- **Diameter**: {metrics['diameter']} hops\n"

        section += "\n"

        # Bridge papers (if available)
        if bridge_papers:
            section += "**Key Bridge Papers** (high betweenness centrality):\n\n"
            section += "*Papers that connect different research communities*\n\n"

            for i, paper in enumerate(bridge_papers[:5], 1):
                section += f"{i}. \"{paper.get('title', 'Unknown')}\"\n"
                section += f"   - Year: {paper.get('year', 'N/A')}\n"
                section += f"   - Citations: {paper.get('citations', 0):,}\n"
                section += f"   - Betweenness: {paper.get('betweenness', 0):.4f}\n"
                section += f"   - **Role**: Connects different subfields/approaches\n\n"

        section += "**Interpretation**:\n"
        section += "- High betweenness papers are methodological bridges\n"
        section += "- Clustering coefficient shows field cohesion\n"
        section += "- Network density indicates field maturity\n"

        section += "\n---"

        return section

    def _generate_trends_section(
        self,
        recent_papers: List[Dict[str, Any]],
        clusters: Dict[str, List[Dict[str, Any]]] = None,
        emerging_concepts: List[Dict[str, Any]] = None
    ) -> str:
        """Generate recent trends section."""
        section = f"## Recent Trends (2023-2025)\n\n"
        section += f"*Latest developments and derivative research ({len(recent_papers)} papers)*\n\n"

        # Clustered trends (if available)
        if clusters:
            for i, (concept, papers) in enumerate(clusters.items(), 1):
                section += f"### Trend {i}: {concept}\n\n"
                section += f"**{len(papers)} papers in this cluster**\n\n"

                # Show top 3 papers per cluster
                for j, paper in enumerate(papers[:3], 1):
                    title = paper.get('title', 'Unknown')
                    year = paper.get('publication_year', 'N/A')
                    cites = paper.get('cited_by_count', 0)

                    section += f"{j}. \"{title}\" ({year}, {cites} citations)\n"

                if len(papers) > 3:
                    section += f"\n   *...and {len(papers) - 3} more papers*\n"

                section += "\n"

        else:
            # No clustering, just list top recent papers
            section += "**Top Recent Papers**:\n\n"
            for i, paper in enumerate(recent_papers[:10], 1):
                title = paper.get('title', 'Unknown')
                year = paper.get('publication_year', 'N/A')
                cites = paper.get('cited_by_count', 0)

                section += f"{i}. \"{title}\" ({year}, {cites} citations)\n"

            section += "\n"

        # Emerging concepts (if available)
        if emerging_concepts:
            section += "**Emerging Concepts** (growing rapidly vs anchor papers):\n\n"

            for concept in emerging_concepts[:5]:
                name = concept['name']
                growth = concept['growth_rate']
                is_new = concept['is_new']

                if is_new:
                    section += f"- **{name}**: NEW (not in foundational papers)\n"
                else:
                    section += f"- **{name}**: {growth:.1f}x growth\n"

            section += "\n"

        section += "**Interpretation**:\n"
        section += "- Recent papers show field evolution\n"
        section += "- Emerging concepts indicate new research directions\n"
        section += "- Citation counts reflect early impact\n"

        section += "\n---"

        return section

    def _generate_footer(self, metadata: Dict[str, Any] = None) -> str:
        """Generate report footer."""
        footer = "---\n\n"
        footer += "*Generated by Research Landscape Analyzer*  \n"
        footer += "*Data source: OpenAlex*  \n"

        if metadata:
            if 'api_calls' in metadata:
                footer += f"*API calls: {metadata['api_calls']}*  \n"
            if 'processing_time' in metadata:
                footer += f"*Processing time: {metadata['processing_time']:.1f}s*  \n"

        return footer


# Convenience function for quick use

def generate_report(
    topic: str,
    reviews: List[Dict[str, Any]],
    anchors: List[Dict[str, Any]],
    output_file: str = None
) -> str:
    """
    Quick wrapper to generate report.

    Args:
        topic: Research topic
        reviews: Review papers
        anchors: Anchor papers
        output_file: Optional file path to write

    Returns:
        Markdown report string

    Example:
        report = generate_report(
            topic="CRISPR base editing",
            reviews=reviews,
            anchors=anchors,
            output_file="crispr_analysis.md"
        )
    """
    generator = ReportGenerator()
    report = generator.generate(topic, reviews, anchors)

    if output_file:
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(report)
        print(f"📄 Report saved to: {output_file}")

    return report
