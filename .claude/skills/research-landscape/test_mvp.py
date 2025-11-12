#!/usr/bin/env python3
"""
Test script for Research Landscape Analyzer MVP.

Tests with a real topic from traditional biology (should work well).
"""

import sys
from pathlib import Path

# Add src to path
sys.path.insert(0, str(Path(__file__).parent / "src"))

from src import TopicAnalyzer


def test_basic_analysis():
    """Test basic analysis with mycobacterial topic."""
    print("=" * 70)
    print("Research Landscape Analyzer - MVP Test")
    print("=" * 70)
    print()
    print("Testing with: 'mycobacterial pathogenesis'")
    print("(Traditional biology - should work well with citation-based approach)")
    print()

    # Initialize
    analyzer = TopicAnalyzer(email="kyuwon.shim@ip-korea.org")

    # Analyze
    result = analyzer.analyze(
        topic="mycobacterial pathogenesis",
        max_reviews=10,
        max_anchors=8,
        years=10
    )

    # Generate report
    output_file = "test_output_mycobacterial_pathogenesis.md"
    report = result.to_markdown(output_file)

    # Print summary
    print("\n" + "=" * 70)
    print("Test Results:")
    print("=" * 70)
    print(f"Topic: {result.topic}")
    print(f"Reviews found: {len(result.reviews)}")
    print(f"Anchors found: {len(result.anchors)}")
    print(f"Processing time: {result.metadata['processing_time']:.1f}s")
    print(f"API calls: {result.metadata['api_calls']}")
    print(f"\nReport saved to: {output_file}")
    print(f"Report length: {len(report)} characters (~{len(report.split())} words)")

    if result.reviews:
        print(f"\nTop review:")
        top = result.reviews[0]
        print(f"  - {top.get('title', 'Unknown')}")
        print(f"  - Year: {top.get('publication_year')}")
        print(f"  - Citations: {top.get('cited_by_count'):,}")

    if result.anchors:
        print(f"\nTop anchor:")
        top = result.anchors[0]
        print(f"  - {top.get('title', 'Unknown')}")
        print(f"  - Year: {top.get('publication_year')}")
        print(f"  - Citations: {top.get('cited_by_count'):,}")
        print(f"  - Anchor score: {top.get('anchor_score', 0):.2f}")

    print("\n" + "=" * 70)
    print("✅ MVP Test Complete!")
    print("=" * 70)

    return True


if __name__ == "__main__":
    try:
        success = test_basic_analysis()
        sys.exit(0 if success else 1)
    except Exception as e:
        print(f"\n❌ Test failed with error:")
        print(f"   {type(e).__name__}: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
