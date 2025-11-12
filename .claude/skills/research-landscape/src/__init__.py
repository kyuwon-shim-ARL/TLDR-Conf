"""
Research Landscape Analyzer
Automated research topic analysis using OpenAlex citation data.
"""

from .review_finder import ReviewFinder, find_reviews
from .anchor_finder import AnchorFinder, find_anchors
from .report_generator import ReportGenerator, generate_report

__version__ = "1.0.0-mvp"
__all__ = [
    'ReviewFinder',
    'AnchorFinder',
    'ReportGenerator',
    'find_reviews',
    'find_anchors',
    'generate_report',
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

    def analyze(
        self,
        topic,
        max_reviews=20,
        max_anchors=10,
        years=10,
        min_review_citations=50,
        min_anchor_citations=100
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

        Returns:
            AnalysisResult object

        Example:
            result = analyzer.analyze(
                "spatial transcriptomics",
                max_reviews=15,
                max_anchors=8,
                years=5
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
            generator=self.report_generator
        )

        print(f"\n{'='*60}")
        print(f"✅ Analysis complete!")
        print(f"   Reviews: {len(reviews)}")
        print(f"   Anchors: {len(anchors)}")
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
    """

    def __init__(self, topic, reviews, anchors, metadata, generator):
        self.topic = topic
        self.reviews = reviews
        self.anchors = anchors
        self.metadata = metadata
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
            analysis_metadata=self.metadata
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
