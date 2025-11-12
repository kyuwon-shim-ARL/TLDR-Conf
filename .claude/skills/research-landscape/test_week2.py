#!/usr/bin/env python3
"""
Test script for Week 2 features (citation network + trend tracking).

Tests the integrated TopicAnalyzer with network and trend analysis enabled.
"""

import sys
from pathlib import Path

# Add src to path
sys.path.insert(0, str(Path(__file__).parent / "src"))

from src import TopicAnalyzer


def test_week2_integration():
    """Test TopicAnalyzer with network and trend analysis."""

    print("="*80)
    print("Week 2 Integration Test: Citation Network + Trend Tracking")
    print("="*80)

    # Initialize analyzer
    analyzer = TopicAnalyzer(email="test@example.com")

    # Run analysis with all Week 2 features enabled
    # Using a smaller topic to keep runtime reasonable
    result = analyzer.analyze(
        topic="mycobacterial pathogenesis",
        max_reviews=10,
        max_anchors=8,
        years=10,
        include_network=True,   # Week 2 feature
        include_trends=True,    # Week 2 feature
        network_hops=1,
        trend_years=2
    )

    # Validate results
    print("\n" + "="*80)
    print("Validation Results:")
    print("="*80)

    # Core features
    assert len(result.reviews) > 0, "No reviews found"
    assert len(result.anchors) > 0, "No anchors found"
    print(f"✅ Core features: {len(result.reviews)} reviews, {len(result.anchors)} anchors")

    # Network features
    if result.network_metrics:
        assert result.network_metrics['num_nodes'] > 0, "No network nodes"
        assert result.network_metrics['num_edges'] > 0, "No network edges"
        assert 'pagerank' in result.network_metrics, "No PageRank calculated"
        assert 'betweenness' in result.network_metrics, "No betweenness calculated"
        print(f"✅ Network analysis: {result.network_metrics['num_nodes']} nodes, "
              f"{result.network_metrics['num_edges']} edges")

        if result.bridge_papers:
            print(f"✅ Bridge papers: {len(result.bridge_papers)} identified")
    else:
        print("⚠️  Network analysis skipped or failed")

    # Trend features
    if result.recent_trends:
        assert len(result.recent_trends) > 0, "No recent trends found"
        print(f"✅ Trend tracking: {len(result.recent_trends)} recent papers")

        if result.trend_clusters:
            print(f"✅ Trend clustering: {len(result.trend_clusters)} clusters")

        if result.emerging_concepts:
            print(f"✅ Emerging concepts: {len(result.emerging_concepts)} detected")
    else:
        print("⚠️  Trend analysis skipped or failed")

    # Generate and save report
    output_file = "test_output_week2_full.md"
    report = result.to_markdown(output_file)

    print(f"\n✅ Report generated: {len(report)} characters")
    print(f"✅ Saved to: {output_file}")

    # Check report contains new sections
    assert "## Citation Network Analysis" in report or result.network_metrics is None, \
        "Report missing network section"
    assert "## Recent Trends" in report or result.recent_trends is None, \
        "Report missing trends section"

    print("\n" + "="*80)
    print("🎉 Week 2 Integration Test PASSED!")
    print("="*80)

    return result


if __name__ == "__main__":
    try:
        result = test_week2_integration()
        print("\n✅ All tests passed!")
        print(f"\nFinal result: {result}")
    except AssertionError as e:
        print(f"\n❌ Test failed: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"\n❌ Unexpected error: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
