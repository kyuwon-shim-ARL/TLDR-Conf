"""
Research Landscape Analyzer
Automated research topic analysis using OpenAlex citation data.
"""

from .review_finder import ReviewFinder, find_reviews
from .anchor_finder import AnchorFinder, find_anchors
from .report_generator import ReportGenerator, generate_report
from .citation_network import CitationNetworkBuilder
from .trend_tracker import TrendTracker
from .concept_framework_builder import ConceptualFrameworkBuilder, build_conceptual_framework

__version__ = "1.1.0"
__all__ = [
    'ReviewFinder',
    'AnchorFinder',
    'ReportGenerator',
    'CitationNetworkBuilder',
    'TrendTracker',
    'ConceptualFrameworkBuilder',
    'find_reviews',
    'find_anchors',
    'generate_report',
    'build_conceptual_framework',
    'TopicAnalyzer',
]


class TopicAnalyzer:
    """
    Main orchestrator for research landscape analysis.

    Usage:
        analyzer = TopicAnalyzer(email="your@email.com")
        result = analyzer.analyze("CRISPR base editing")
        result.to_markdown("output.md")
    """

    def __init__(self, email=None):
        """
        Initialize analyzer.

        Args:
            email: Email for OpenAlex polite pool (recommended)
        """
        self.email = email
        self.review_finder = ReviewFinder(email=email)
        self.anchor_finder = AnchorFinder(email=email)
        self.report_generator = ReportGenerator()
        self.network_builder = CitationNetworkBuilder(email=email)
        self.trend_tracker = TrendTracker(email=email)

    def analyze(
        self,
        topic,
        max_reviews=20,
        max_anchors=10,
        years=10,
        min_review_citations=50,
        min_anchor_citations=100,
        include_network=False,
        include_trends=False,
        network_hops=1,
        trend_years=2
    ):
        """
        Analyze research landscape for a topic.

        Args:
            topic: Research topic string
            max_reviews: Max number of review papers
            max_anchors: Max number of anchor papers
            years: Look back N years
            min_review_citations: Min citations for reviews
            min_anchor_citations: Min citations for anchors
            include_network: Build citation network (adds ~30-60s)
            include_trends: Track recent trends (adds ~10-20s)
            network_hops: Network depth (1 or 2)
            trend_years: Look back N years for trends (default: 2)

        Returns:
            AnalysisResult object

        Example:
            result = analyzer.analyze(
                "spatial transcriptomics",
                max_reviews=15,
                max_anchors=8,
                years=5,
                include_network=True,
                include_trends=True
            )
        """
        print(f"\n{'='*60}")
        print(f"Research Landscape Analysis: {topic}")
        print(f"{'='*60}\n")

        import time
        start_time = time.time()

        # Find reviews
        reviews = self.review_finder.find_reviews(
            topic=topic,
            max_results=max_reviews,
            min_citations=min_review_citations,
            years=years
        )

        # Find anchors
        anchors = self.anchor_finder.find_anchors(
            topic=topic,
            max_results=max_anchors,
            years=years,
            min_citations=min_anchor_citations
        )

        # Optional: Build citation network
        network_metrics = None
        bridge_papers = None
        if include_network and anchors:
            print(f"🕸️  Building citation network (this may take 30-60s)...")
            try:
                self.network_builder.build_network(
                    seed_papers=anchors,
                    hops=network_hops,
                    max_refs_per_paper=20,
                    max_cites_per_paper=50
                )
                network_metrics = self.network_builder.calculate_metrics()
                bridge_papers = self.network_builder.find_bridge_papers(top_k=5)
            except Exception as e:
                print(f"⚠️  Network analysis failed: {e}")

        # Optional: Track recent trends
        recent_trends = None
        trend_clusters = None
        emerging_concepts = None
        if include_trends and anchors:
            print(f"📈 Tracking recent trends...")
            try:
                recent_trends = self.trend_tracker.find_recent_derivatives(
                    anchor_papers=anchors,
                    years=trend_years,
                    min_citations=5,
                    max_papers=50
                )
                if recent_trends:
                    trend_clusters = self.trend_tracker.cluster_by_concepts(
                        papers=recent_trends,
                        max_clusters=5
                    )
                    emerging_concepts = self.trend_tracker.detect_emerging_concepts(
                        recent_papers=recent_trends,
                        anchor_papers=anchors,
                        top_k=10
                    )
            except Exception as e:
                print(f"⚠️  Trend analysis failed: {e}")

        processing_time = time.time() - start_time

        # Create result
        result = AnalysisResult(
            topic=topic,
            reviews=reviews,
            anchors=anchors,
            metadata={
                'years': years,
                'processing_time': processing_time,
                'api_calls': self.review_finder.client.request_count + self.anchor_finder.client.request_count
            },
            network_metrics=network_metrics,
            bridge_papers=bridge_papers,
            recent_trends=recent_trends,
            trend_clusters=trend_clusters,
            emerging_concepts=emerging_concepts,
            generator=self.report_generator
        )

        print(f"\n{'='*60}")
        print(f"✅ Analysis complete!")
        print(f"   Reviews: {len(reviews)}")
        print(f"   Anchors: {len(anchors)}")
        if include_network and network_metrics:
            print(f"   Network nodes: {network_metrics.get('num_nodes', 0)}")
            print(f"   Network edges: {network_metrics.get('num_edges', 0)}")
        if include_trends and recent_trends:
            print(f"   Recent trends: {len(recent_trends)}")
        print(f"   Time: {processing_time:.1f}s")
        print(f"{'='*60}\n")

        return result


class AnalysisResult:
    """
    Container for analysis results.

    Attributes:
        topic: Research topic
        reviews: List of review papers
        anchors: List of anchor papers
        metadata: Analysis metadata
        network_metrics: Optional citation network metrics
        bridge_papers: Optional bridge papers
        recent_trends: Optional recent derivative papers
        trend_clusters: Optional trend clusters
        emerging_concepts: Optional emerging concepts
    """

    def __init__(self, topic, reviews, anchors, metadata, generator,
                 network_metrics=None, bridge_papers=None,
                 recent_trends=None, trend_clusters=None, emerging_concepts=None):
        self.topic = topic
        self.reviews = reviews
        self.anchors = anchors
        self.metadata = metadata
        self.network_metrics = network_metrics
        self.bridge_papers = bridge_papers
        self.recent_trends = recent_trends
        self.trend_clusters = trend_clusters
        self.emerging_concepts = emerging_concepts
        self._generator = generator

    def to_markdown(self, output_file=None):
        """
        Generate markdown report.

        Args:
            output_file: Optional file path to save

        Returns:
            Markdown string
        """
        report = self._generator.generate(
            topic=self.topic,
            reviews=self.reviews,
            anchors=self.anchors,
            analysis_metadata=self.metadata,
            network_metrics=self.network_metrics,
            bridge_papers=self.bridge_papers,
            recent_trends=self.recent_trends,
            trend_clusters=self.trend_clusters,
            emerging_concepts=self.emerging_concepts
        )

        if output_file:
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write(report)
            print(f"📄 Report saved to: {output_file}")

        return report

    def __repr__(self):
        return (f"AnalysisResult(topic='{self.topic}', "
                f"reviews={len(self.reviews)}, "
                f"anchors={len(self.anchors)})")
