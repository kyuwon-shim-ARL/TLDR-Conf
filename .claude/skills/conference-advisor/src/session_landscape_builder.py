"""
Session Landscape Builder for Conference-Advisor

Integrates Research Landscape Analyzer to create unified session landscapes
and map individual speakers to their positions within the landscape.
"""

import sys
from pathlib import Path
from typing import List, Dict, Any, Optional

# Import Research Landscape Analyzer
# Path: conference-advisor/src -> .claude/skills -> research-landscape/src
landscape_path = Path(__file__).parent.parent.parent / "research-landscape" / "src"
if landscape_path.exists():
    sys.path.insert(0, str(landscape_path))

try:
    # Import modules from research-landscape
    from review_finder import ReviewFinder
    from anchor_finder import AnchorFinder
    from citation_network import CitationNetworkBuilder
    from trend_tracker import TrendTracker
    from report_generator import ReportGenerator

    # Create a simple TopicAnalyzer equivalent
    class TopicAnalyzer:
        def __init__(self, email=None):
            self.email = email
            self.review_finder = ReviewFinder(email=email)
            self.anchor_finder = AnchorFinder(email=email)
            self.network_builder = CitationNetworkBuilder(email=email)
            self.trend_tracker = TrendTracker(email=email)
            self.report_generator = ReportGenerator()

        def analyze(self, topic, max_reviews=20, max_anchors=10, years=10,
                   min_review_citations=50, min_anchor_citations=100,
                   include_network=False, include_trends=False,
                   network_hops=1, trend_years=2):
            import time
            start_time = time.time()

            # Find reviews
            reviews = self.review_finder.find_reviews(
                topic=topic, max_results=max_reviews,
                min_citations=min_review_citations, years=years
            )

            # Find anchors
            anchors = self.anchor_finder.find_anchors(
                topic=topic, max_results=max_anchors,
                years=years, min_citations=min_anchor_citations
            )

            # Optional: Network
            network_metrics = None
            bridge_papers = None
            if include_network and anchors:
                self.network_builder.build_network(
                    seed_papers=anchors, hops=network_hops
                )
                network_metrics = self.network_builder.calculate_metrics()
                bridge_papers = self.network_builder.find_bridge_papers(top_k=5)

            # Optional: Trends
            recent_trends = None
            trend_clusters = None
            emerging_concepts = None
            if include_trends and anchors:
                recent_trends = self.trend_tracker.find_recent_derivatives(
                    anchor_papers=anchors, years=trend_years
                )
                if recent_trends:
                    trend_clusters = self.trend_tracker.cluster_by_concepts(recent_trends)
                    emerging_concepts = self.trend_tracker.detect_emerging_concepts(
                        recent_trends, anchors
                    )

            processing_time = time.time() - start_time

            # Create result object
            class Result:
                def __init__(self, **kwargs):
                    for k, v in kwargs.items():
                        setattr(self, k, v)

            return Result(
                topic=topic,
                reviews=reviews,
                anchors=anchors,
                metadata={'processing_time': processing_time},
                network_metrics=network_metrics,
                bridge_papers=bridge_papers,
                recent_trends=recent_trends,
                trend_clusters=trend_clusters,
                emerging_concepts=emerging_concepts
            )

    LANDSCAPE_AVAILABLE = True
except ImportError as e:
    LANDSCAPE_AVAILABLE = False
    print(f"⚠️  Research Landscape Analyzer not available: {e}")


class SessionLandscapeBuilder:
    """
    Build unified research landscape for conference sessions.

    Strategy: Analyze session topic once (not per speaker) and map each
    speaker to their position in the landscape.
    """

    def __init__(self, email: Optional[str] = None):
        """
        Initialize builder.

        Args:
            email: Email for OpenAlex polite pool
        """
        self.email = email
        self.analyzer = TopicAnalyzer(email=email) if LANDSCAPE_AVAILABLE else None

    def should_use_landscape(self, session_topic: str) -> bool:
        """
        Check if topic is suitable for citation-based landscape analysis.

        Args:
            session_topic: Session title or topic

        Returns:
            bool: True if landscape analysis recommended
        """
        if not LANDSCAPE_AVAILABLE:
            return False

        # AI/ML topics (too fast-moving)
        ai_ml_keywords = [
            "AI", "machine learning", "deep learning", "LLM", "GPT",
            "neural network", "artificial intelligence", "transformer"
        ]
        if any(kw.lower() in session_topic.lower() for kw in ai_ml_keywords):
            return False

        # Very new techniques (<2 years)
        very_new = ["2024", "2025", "breakthrough", "first-in-human", "novel"]
        if any(kw in session_topic.lower() for kw in very_new):
            return False

        # Traditional biology (good for citation analysis)
        traditional_bio = [
            "pathogen", "microb", "immun", "metabol", "protein",
            "gene", "cell", "molecular", "biochem", "microbiology"
        ]
        if any(kw in session_topic.lower() for kw in traditional_bio):
            return True

        return False

    def build_session_landscape(
        self,
        session_topic: str,
        include_network: bool = False,
        include_trends: bool = True,
        max_reviews: int = 10,
        max_anchors: int = 8
    ) -> Optional[Dict[str, Any]]:
        """
        Build unified landscape for entire session.

        Args:
            session_topic: Session title or main topic
            include_network: Build citation network (adds 2-7 min)
            include_trends: Include recent trends (adds 10-20s)
            max_reviews: Max review papers
            max_anchors: Max anchor papers

        Returns:
            Dict with landscape data or None if not suitable
        """
        if not self.should_use_landscape(session_topic):
            print(f"⚠️  Session '{session_topic}' not suitable for landscape analysis")
            print(f"   → Use WebSearch for latest information instead")
            return None

        if not self.analyzer:
            print(f"❌ Research Landscape Analyzer not available")
            return None

        print(f"\n🌍 Building session landscape: {session_topic}")

        try:
            result = self.analyzer.analyze(
                topic=session_topic,
                max_reviews=max_reviews,
                max_anchors=max_anchors,
                years=10,
                include_network=include_network,
                include_trends=include_trends
            )

            # Package landscape data
            landscape = {
                'topic': session_topic,
                'reviews': result.reviews,
                'anchors': result.anchors,
                'metadata': result.metadata,
                'network_metrics': result.network_metrics,
                'bridge_papers': result.bridge_papers,
                'recent_trends': result.recent_trends,
                'trend_clusters': result.trend_clusters,
                'emerging_concepts': result.emerging_concepts
            }

            print(f"   ✅ Landscape built:")
            print(f"      Reviews: {len(result.reviews)}")
            print(f"      Anchors: {len(result.anchors)}")
            if result.recent_trends:
                print(f"      Recent trends: {len(result.recent_trends)}")

            return landscape

        except Exception as e:
            print(f"❌ Failed to build landscape: {e}")
            return None

    def map_speaker_to_landscape(
        self,
        speaker_name: str,
        speaker_research_areas: List[str],
        speaker_recent_papers: List[Dict[str, Any]],
        landscape: Dict[str, Any]
    ) -> Dict[str, Any]:
        """
        Map speaker to their position in the session landscape.

        Args:
            speaker_name: Speaker name
            speaker_research_areas: List of research keywords
            speaker_recent_papers: Speaker's recent publications
            landscape: Session landscape from build_session_landscape()

        Returns:
            Dict with speaker's landscape mapping
        """
        mapping = {
            'speaker': speaker_name,
            'related_reviews': [],
            'related_anchors': [],
            'related_trends': [],
            'position_description': ""
        }

        # Match with review papers (by concept overlap)
        for review in landscape['reviews'][:5]:
            review_concepts = [c.get('display_name', '').lower()
                             for c in review.get('concepts', [])]

            # Check overlap with speaker's research areas
            overlap = any(area.lower() in ' '.join(review_concepts)
                         for area in speaker_research_areas)

            if overlap:
                mapping['related_reviews'].append({
                    'title': review.get('title'),
                    'year': review.get('publication_year'),
                    'citations': review.get('cited_by_count', 0),
                    'relevance': 'Covers broader context of speaker\'s work'
                })

        # Match with anchor papers
        for anchor in landscape['anchors'][:5]:
            anchor_concepts = [c.get('display_name', '').lower()
                             for c in anchor.get('concepts', [])]

            overlap = any(area.lower() in ' '.join(anchor_concepts)
                         for area in speaker_research_areas)

            if overlap:
                mapping['related_anchors'].append({
                    'title': anchor.get('title'),
                    'year': anchor.get('publication_year'),
                    'citations': anchor.get('cited_by_count', 0),
                    'score': anchor.get('anchor_score', 0),
                    'relevance': 'Foundational paper related to speaker\'s approach'
                })

        # Match with recent trends
        if landscape.get('trend_clusters'):
            for concept, papers in landscape['trend_clusters'].items():
                # Check if speaker's work aligns with this trend
                concept_match = any(area.lower() in concept.lower()
                                   for area in speaker_research_areas)

                if concept_match:
                    mapping['related_trends'].append({
                        'cluster': concept,
                        'papers_count': len(papers),
                        'top_paper': papers[0].get('title') if papers else None,
                        'relevance': f'Speaker\'s work aligns with {concept} trend'
                    })

        # Generate position description
        position_parts = []

        if mapping['related_anchors']:
            position_parts.append(
                f"Builds on foundational work (Anchor #{len(mapping['related_anchors'])} papers)"
            )

        if mapping['related_trends']:
            trend_names = [t['cluster'] for t in mapping['related_trends']]
            position_parts.append(
                f"Part of recent trends: {', '.join(trend_names[:2])}"
            )

        if not position_parts:
            position_parts.append("Contributes specialized perspective to session")

        mapping['position_description'] = "; ".join(position_parts)

        return mapping

    def format_session_background(
        self,
        landscape: Dict[str, Any],
        speaker_mappings: List[Dict[str, Any]] = None
    ) -> str:
        """
        Format session landscape into markdown background section.

        Args:
            landscape: Session landscape data
            speaker_mappings: Optional list of speaker mappings

        Returns:
            Markdown formatted background section
        """
        md = f"## 🌍 세션 전체 Research Landscape: {landscape['topic']}\n\n"
        md += "*통합 문헌 분석 - Research Landscape Analyzer*\n\n"

        # Reviews section
        md += "### 📚 핵심 리뷰 논문 (세션 전체 이해용)\n\n"
        md += "*세션 참석 전 필수 읽기 자료*\n\n"

        for i, review in enumerate(landscape['reviews'][:5], 1):
            title = review.get('title', 'Unknown')
            year = review.get('publication_year', 'N/A')
            citations = review.get('cited_by_count', 0)
            doi = review.get('doi', 'N/A')

            # Estimate reading time
            reading_time = "2-3시간" if citations > 200 else "1.5-2시간"

            md += f"{i}. **\"{title}\"** ({year}, {citations:,} citations)\n"
            md += f"   - 읽기 시간: {reading_time}\n"
            md += f"   - 중요도: {'⭐' * (6 - i)}\n"
            md += f"   - DOI: {doi}\n\n"

        # Anchors section
        md += "### ⚓ 거점 논문 (이론적 기초)\n\n"
        md += "*이 분야의 토대를 만든 핵심 연구*\n\n"

        for i, anchor in enumerate(landscape['anchors'][:5], 1):
            title = anchor.get('title', 'Unknown')
            year = anchor.get('publication_year', 'N/A')
            citations = anchor.get('cited_by_count', 0)
            score = anchor.get('anchor_score', 0)

            md += f"{i}. **\"{title}\"** ({year})\n"
            md += f"   - Citations: {citations:,}\n"
            md += f"   - Anchor Score: {score:.1f} (time-weighted impact)\n\n"

        # Network analysis (if available)
        if landscape.get('network_metrics'):
            metrics = landscape['network_metrics']
            md += "### 🕸️ 연구 네트워크 구조\n\n"
            md += f"- **논문 수**: {metrics.get('num_nodes', 0):,}개\n"
            md += f"- **인용 관계**: {metrics.get('num_edges', 0):,}개\n"
            md += f"- **네트워크 밀도**: {metrics.get('density', 0):.4f}\n"
            md += f"- **평균 클러스터링**: {metrics.get('clustering', 0):.3f}\n\n"

            if landscape.get('bridge_papers'):
                md += "**핵심 연결 논문** (다른 분야를 연결하는 논문):\n\n"
                for bridge in landscape['bridge_papers'][:3]:
                    md += f"- {bridge.get('title')} ({bridge.get('year')})\n"
                md += "\n"

        # Recent trends
        if landscape.get('trend_clusters'):
            md += "### 📈 최신 연구 동향 (2023-2025)\n\n"

            for i, (concept, papers) in enumerate(list(landscape['trend_clusters'].items())[:3], 1):
                md += f"**Trend {i}: {concept}** ({len(papers)} papers)\n\n"
                for paper in papers[:2]:
                    title = paper.get('title', 'Unknown')
                    year = paper.get('publication_year', 'N/A')
                    cites = paper.get('cited_by_count', 0)
                    md += f"- {title} ({year}, {cites} citations)\n"
                md += "\n"

        # Emerging concepts
        if landscape.get('emerging_concepts'):
            md += "**새롭게 등장하는 개념들**:\n\n"
            for concept in landscape['emerging_concepts'][:5]:
                name = concept['name']
                is_new = concept['is_new']
                growth = concept.get('growth_rate', 0)

                if is_new:
                    md += f"- **{name}**: 🆕 NEW (거점 논문에 없던 새 개념)\n"
                else:
                    md += f"- **{name}**: 📈 {growth:.1f}x 성장률\n"
            md += "\n"

        # Speaker mappings (if provided)
        if speaker_mappings:
            md += "---\n\n"
            md += "## 🎤 연사별 Landscape 내 위치\n\n"

            for mapping in speaker_mappings:
                speaker = mapping['speaker']
                position = mapping['position_description']

                md += f"### {speaker}\n\n"
                md += f"**Landscape 내 위치**: {position}\n\n"

                if mapping['related_anchors']:
                    md += "**관련 거점 논문**:\n"
                    for anchor in mapping['related_anchors'][:2]:
                        md += f"- {anchor['title']} ({anchor['year']})\n"
                    md += "\n"

                if mapping['related_trends']:
                    md += "**관련 최신 트렌드**:\n"
                    for trend in mapping['related_trends'][:2]:
                        md += f"- {trend['cluster']}: {trend['papers_count']} papers\n"
                    md += "\n"

        md += "---\n\n"
        md += "*Generated by Research Landscape Analyzer v1.0*\n"

        return md


# Convenience functions

def build_session_landscape(
    session_topic: str,
    email: Optional[str] = None,
    include_trends: bool = True
) -> Optional[Dict[str, Any]]:
    """
    Quick wrapper to build session landscape.

    Args:
        session_topic: Session title or main topic
        email: Email for OpenAlex polite pool
        include_trends: Include recent trends

    Returns:
        Landscape dict or None
    """
    builder = SessionLandscapeBuilder(email=email)
    return builder.build_session_landscape(
        session_topic=session_topic,
        include_trends=include_trends
    )
