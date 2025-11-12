#!/usr/bin/env python3
"""
Command-line interface for Research Landscape Analyzer.

Usage:
    python cli.py analyze "spatial transcriptomics" --output report.md
    python cli.py analyze "CRISPR base editing" --network --trends
    python cli.py --help
"""

import argparse
import sys
from pathlib import Path

# Add src to path
sys.path.insert(0, str(Path(__file__).parent / "src"))

from src import TopicAnalyzer


def main():
    """Main CLI entry point."""
    parser = argparse.ArgumentParser(
        description="Research Landscape Analyzer - Automated literature analysis using OpenAlex",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Basic analysis
  python cli.py analyze "spatial transcriptomics"

  # With network analysis and trends
  python cli.py analyze "CRISPR base editing" --network --trends

  # Custom parameters
  python cli.py analyze "mycobacterial pathogenesis" \\
    --reviews 15 --anchors 10 --years 5 --output myreport.md

  # Full analysis with all options
  python cli.py analyze "protein structure prediction" \\
    --network --trends --network-hops 2 --trend-years 3 \\
    --email your@email.com --output full_analysis.md

Scope:
  - ✅ Traditional sciences (biology, chemistry, medicine)
  - ❌ Fast-moving AI/ML (use manual curation instead)

  See docs/AI_ML_manual_curation.md for AI/ML research strategies.
        """
    )

    # Subcommands
    subparsers = parser.add_subparsers(dest='command', help='Commands')

    # Analyze command
    analyze_parser = subparsers.add_parser(
        'analyze',
        help='Analyze research landscape for a topic'
    )

    # Required arguments
    analyze_parser.add_argument(
        'topic',
        type=str,
        help='Research topic to analyze (e.g., "spatial transcriptomics")'
    )

    # Optional arguments - Basic
    analyze_parser.add_argument(
        '--reviews',
        type=int,
        default=20,
        metavar='N',
        help='Maximum number of review papers (default: 20)'
    )

    analyze_parser.add_argument(
        '--anchors',
        type=int,
        default=10,
        metavar='N',
        help='Maximum number of anchor papers (default: 10)'
    )

    analyze_parser.add_argument(
        '--years',
        type=int,
        default=10,
        metavar='N',
        help='Look back N years (default: 10)'
    )

    analyze_parser.add_argument(
        '--min-review-citations',
        type=int,
        default=50,
        metavar='N',
        help='Minimum citations for review papers (default: 50)'
    )

    analyze_parser.add_argument(
        '--min-anchor-citations',
        type=int,
        default=100,
        metavar='N',
        help='Minimum citations for anchor papers (default: 100)'
    )

    # Optional arguments - Week 2 features
    analyze_parser.add_argument(
        '--network',
        action='store_true',
        help='Build citation network (adds ~30-60s)'
    )

    analyze_parser.add_argument(
        '--trends',
        action='store_true',
        help='Track recent trends (adds ~10-20s)'
    )

    analyze_parser.add_argument(
        '--network-hops',
        type=int,
        default=1,
        choices=[1, 2],
        metavar='N',
        help='Citation network depth (1 or 2, default: 1)'
    )

    analyze_parser.add_argument(
        '--trend-years',
        type=int,
        default=2,
        metavar='N',
        help='Look back N years for trends (default: 2)'
    )

    # Output options
    analyze_parser.add_argument(
        '--output', '-o',
        type=str,
        metavar='FILE',
        help='Output markdown file (default: print to stdout)'
    )

    analyze_parser.add_argument(
        '--email',
        type=str,
        metavar='EMAIL',
        help='Email for OpenAlex polite pool (recommended for faster API)'
    )

    # Parse arguments
    args = parser.parse_args()

    # Check command
    if not args.command:
        parser.print_help()
        return 0

    # Execute command
    if args.command == 'analyze':
        return run_analyze(args)

    return 0


def run_analyze(args):
    """Run analysis command."""

    # Initialize analyzer
    print(f"🔬 Research Landscape Analyzer v1.0")
    print(f"📊 Topic: {args.topic}\n")

    analyzer = TopicAnalyzer(email=args.email)

    # Run analysis
    try:
        result = analyzer.analyze(
            topic=args.topic,
            max_reviews=args.reviews,
            max_anchors=args.anchors,
            years=args.years,
            min_review_citations=args.min_review_citations,
            min_anchor_citations=args.min_anchor_citations,
            include_network=args.network,
            include_trends=args.trends,
            network_hops=args.network_hops,
            trend_years=args.trend_years
        )

        # Generate report
        report = result.to_markdown(output_file=args.output)

        # Print to stdout if no output file
        if not args.output:
            print("\n" + "="*80)
            print("REPORT")
            print("="*80 + "\n")
            print(report)

        return 0

    except KeyboardInterrupt:
        print("\n\n⚠️  Analysis interrupted by user")
        return 1
    except Exception as e:
        print(f"\n❌ Error: {e}")
        import traceback
        traceback.print_exc()
        return 1


if __name__ == "__main__":
    sys.exit(main())
