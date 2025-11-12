#!/usr/bin/env python3
"""
Test Option 2: Conceptual Framework Builder

Tests automatic problem-solution framework generation.
"""

import sys
from pathlib import Path

# Add src to path
sys.path.insert(0, str(Path(__file__).parent / "src"))

from src import TopicAnalyzer, ConceptualFrameworkBuilder


def test_framework_generation():
    """Test conceptual framework generation."""

    print("="*80)
    print("Option 2 Test: Conceptual Framework Auto-Generation")
    print("="*80)

    # Step 1: Generate landscape
    print("\n1. Generating landscape...")
    print("-" * 80)

    analyzer = TopicAnalyzer(email="test@example.com")

    landscape = analyzer.analyze(
        topic="mycobacterial pathogenesis",
        max_reviews=10,
        max_anchors=8,
        years=10,
        include_trends=True,
        include_network=False  # Skip for faster test
    )

    print(f"   ✅ Landscape generated:")
    print(f"      Reviews: {len(landscape.reviews)}")
    print(f"      Anchors: {len(landscape.anchors)}")
    print(f"      Trends: {len(landscape.recent_trends) if landscape.recent_trends else 0}")

    # Convert to dict (framework builder expects dict)
    landscape_dict = {
        'topic': landscape.topic,
        'reviews': landscape.reviews,
        'anchors': landscape.anchors,
        'recent_trends': landscape.recent_trends,
        'trend_clusters': landscape.trend_clusters,
        'emerging_concepts': landscape.emerging_concepts
    }

    # Step 2: Build conceptual framework
    print("\n2. Building conceptual framework...")
    print("-" * 80)

    builder = ConceptualFrameworkBuilder()

    # Simulate speakers
    speakers = [
        {
            'name': 'Speaker A - Neutrophils',
            'research_areas': ['neutrophils', 'granulomas', 'immunity']
        },
        {
            'name': 'Speaker B - Host Therapy',
            'research_areas': ['host-directed therapy', 'immunomodulation']
        },
        {
            'name': 'Speaker C - Drug Targets',
            'research_areas': ['drug discovery', 'mycobacterium abscessus']
        }
    ]

    framework = builder.build_framework(
        landscape=landscape_dict,
        speakers=speakers,
        num_subcategories=3
    )

    # Step 3: Validate framework
    print("\n3. Validating framework...")
    print("-" * 80)

    print(f"   Topic: {framework['topic']}")
    print(f"   Key concepts: {len(framework['key_concepts'])}")
    print(f"\n   Framework structure:")
    print(f"      Core problems: {len(framework['core_problems'])} subcategories")
    print(f"      Approaches: {len(framework['approaches'])} subcategories")
    print(f"      Limitations: {len(framework['limitations'])} subcategories")
    print(f"      Future directions: {len(framework['future_directions'])} subcategories")

    # Show details
    print(f"\n   Core problems details:")
    for i, problem in enumerate(framework['core_problems'], 1):
        print(f"      {i}. {problem['name']} ({len(problem['papers'])} papers)")
        if problem['speakers']:
            print(f"         Speakers: {', '.join(problem['speakers'])}")

    print(f"\n   Approaches details:")
    for i, approach in enumerate(framework['approaches'], 1):
        print(f"      {i}. {approach['name']} ({len(approach['papers'])} papers)")
        if approach['speakers']:
            print(f"         Speakers: {', '.join(approach['speakers'])}")

    # Step 4: Generate markdown
    print("\n4. Generating markdown output...")
    print("-" * 80)

    md = builder.format_framework_markdown(framework)

    output_file = "test_option2_framework.md"
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(md)

    print(f"   ✅ Markdown generated:")
    print(f"      Length: {len(md):,} characters")
    print(f"      Lines: {md.count(chr(10))}")
    print(f"      Saved to: {output_file}")

    # Show preview
    print(f"\n   --- Preview (first 800 chars) ---")
    print(md[:800])
    print("   ...")

    return framework


def test_framework_validation(framework):
    """Validate framework quality."""

    print("\n\n" + "="*80)
    print("Framework Quality Validation")
    print("="*80)

    checks = []

    # Check 1: All categories have content
    check1 = (
        len(framework['core_problems']) > 0 and
        len(framework['approaches']) > 0
    )
    checks.append(("At least problems and approaches exist", check1))

    # Check 2: Key concepts are not all generic
    generic = {'Medicine', 'Biology', 'Chemistry'}
    non_generic = [c for c in framework['key_concepts'] if c not in generic]
    check2 = len(non_generic) >= 5
    checks.append(("At least 5 non-generic concepts", check2))

    # Check 3: Papers distributed across categories
    total_papers = sum(
        len(subcat['papers'])
        for category in ['core_problems', 'approaches', 'limitations', 'future_directions']
        for subcat in framework[category]
    )
    check3 = total_papers > 10
    checks.append(("At least 10 papers in framework", check3))

    # Check 4: Subcategories have meaningful names
    all_names = [
        subcat['name']
        for category in ['core_problems', 'approaches', 'limitations', 'future_directions']
        for subcat in framework[category]
    ]
    check4 = len(all_names) > 0 and all(name != "Unspecified" for name in all_names)
    checks.append(("All subcategories have meaningful names", check4))

    # Print results
    print("\n   Quality Checks:")
    all_passed = True
    for desc, passed in checks:
        status = "✅" if passed else "❌"
        print(f"      {status} {desc}")
        if not passed:
            all_passed = False

    return all_passed


def main():
    """Run all tests."""

    print("\n" + "="*80)
    print("OPTION 2: CONCEPTUAL FRAMEWORK BUILDER TEST")
    print("="*80)
    print("\nGenerating hierarchical problem-solution frameworks...\n")

    try:
        # Test 1: Framework generation
        framework = test_framework_generation()

        # Test 2: Validation
        all_passed = test_framework_validation(framework)

        # Final summary
        print("\n\n" + "="*80)
        if all_passed:
            print("✅ ALL TESTS PASSED - OPTION 2 COMPLETE")
        else:
            print("⚠️  TESTS COMPLETED WITH WARNINGS")
        print("="*80)

        print(f"\nConceptual Framework Builder is ready!")
        print(f"\nKey features:")
        print(f"  ✅ Automatic concept extraction")
        print(f"  ✅ Heuristic-based paper classification")
        print(f"  ✅ Hierarchical framework generation")
        print(f"  ✅ Speaker mapping to framework")
        print(f"  ✅ Markdown output")

        print(f"\nUsage:")
        print(f"  from research_landscape import build_conceptual_framework")
        print(f"  framework = build_conceptual_framework(landscape, speakers)")

        return 0 if all_passed else 1

    except Exception as e:
        print(f"\n❌ Test failed: {e}")
        import traceback
        traceback.print_exc()
        return 1


if __name__ == "__main__":
    sys.exit(main())
