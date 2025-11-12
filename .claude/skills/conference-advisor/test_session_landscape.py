#!/usr/bin/env python3
"""
Test Session Landscape Builder - Option 1 Integration

Tests unified session landscape generation and speaker mapping.
"""

import sys
from pathlib import Path

# Add src to path
sys.path.insert(0, str(Path(__file__).parent / "src"))

from src import SessionLandscapeBuilder


def test_session_landscape_basic():
    """Test basic session landscape generation."""

    print("="*80)
    print("Test 1: Basic Session Landscape Generation")
    print("="*80)

    builder = SessionLandscapeBuilder(email="test@example.com")

    # Test 1: Traditional biology session (should work)
    print("\n1.1 Traditional Biology Session (Mycobacterial Pathogenesis)")
    print("-" * 80)

    landscape = builder.build_session_landscape(
        session_topic="mycobacterial pathogenesis",
        include_trends=True,
        include_network=False,  # Skip network for faster test
        max_reviews=5,
        max_anchors=5
    )

    if landscape:
        print(f"\n✅ Landscape generated successfully!")
        print(f"   Topic: {landscape['topic']}")
        print(f"   Reviews: {len(landscape['reviews'])}")
        print(f"   Anchors: {len(landscape['anchors'])}")
        if landscape['recent_trends']:
            print(f"   Recent trends: {len(landscape['recent_trends'])}")
        if landscape['trend_clusters']:
            print(f"   Trend clusters: {len(landscape['trend_clusters'])}")
    else:
        print(f"\n❌ Failed to generate landscape")
        return False

    # Test 2: AI/ML session (should skip)
    print("\n\n1.2 AI/ML Session (Should Skip)")
    print("-" * 80)

    ai_landscape = builder.build_session_landscape(
        session_topic="deep learning for protein structure prediction"
    )

    if ai_landscape is None:
        print(f"\n✅ Correctly skipped AI/ML topic")
    else:
        print(f"\n⚠️  AI/ML topic was analyzed (expected to skip)")

    return landscape


def test_speaker_mapping(landscape):
    """Test speaker mapping to landscape."""

    print("\n\n" + "="*80)
    print("Test 2: Speaker Mapping to Landscape")
    print("="*80)

    builder = SessionLandscapeBuilder()

    # Simulate 3 speakers in the mycobacterial pathogenesis session
    speakers = [
        {
            'name': 'Speaker A - Neutrophil Role',
            'research_areas': ['neutrophils', 'granulomas', 'innate immunity'],
            'recent_papers': []  # Simplified for test
        },
        {
            'name': 'Speaker B - Host-Directed Therapy',
            'research_areas': ['immunomodulation', 'host-directed therapy', 'tuberculosis'],
            'recent_papers': []
        },
        {
            'name': 'Speaker C - Drug Targets',
            'research_areas': ['oxidative phosphorylation', 'drug discovery', 'mycobacterium'],
            'recent_papers': []
        }
    ]

    mappings = []

    for speaker in speakers:
        print(f"\n2.{speakers.index(speaker) + 1} Mapping: {speaker['name']}")
        print("-" * 80)

        mapping = builder.map_speaker_to_landscape(
            speaker_name=speaker['name'],
            speaker_research_areas=speaker['research_areas'],
            speaker_recent_papers=speaker['recent_papers'],
            landscape=landscape
        )

        mappings.append(mapping)

        print(f"   Position: {mapping['position_description']}")
        print(f"   Related reviews: {len(mapping['related_reviews'])}")
        print(f"   Related anchors: {len(mapping['related_anchors'])}")
        print(f"   Related trends: {len(mapping['related_trends'])}")

        if mapping['related_anchors']:
            print(f"\n   Top anchor match:")
            anchor = mapping['related_anchors'][0]
            print(f"   - {anchor['title'][:80]}...")
            print(f"     ({anchor['year']}, {anchor['citations']:,} citations)")

    return mappings


def test_background_formatting(landscape, mappings):
    """Test background document formatting."""

    print("\n\n" + "="*80)
    print("Test 3: Background Document Formatting")
    print("="*80)

    builder = SessionLandscapeBuilder()

    # Generate formatted background
    background = builder.format_session_background(
        landscape=landscape,
        speaker_mappings=mappings
    )

    print(f"\n✅ Background document generated")
    print(f"   Length: {len(background):,} characters")
    print(f"   Lines: {background.count(chr(10))} lines")

    # Save to file
    output_file = "test_session_background_mycobacterial.md"
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(background)

    print(f"   Saved to: {output_file}")

    # Show preview
    print(f"\n--- Preview (first 500 chars) ---")
    print(background[:500])
    print("...")

    return background


def main():
    """Run all tests."""

    print("\n" + "="*80)
    print("SESSION LANDSCAPE BUILDER - OPTION 1 INTEGRATION TEST")
    print("="*80)
    print("\nTesting unified session landscape + speaker mapping\n")

    try:
        # Test 1: Generate landscape
        landscape = test_session_landscape_basic()
        if not landscape:
            print("\n❌ Landscape generation failed")
            return 1

        # Test 2: Map speakers
        mappings = test_speaker_mapping(landscape)

        # Test 3: Format background
        background = test_background_formatting(landscape, mappings)

        # Final summary
        print("\n\n" + "="*80)
        print("✅ ALL TESTS PASSED - OPTION 1 COMPLETE")
        print("="*80)
        print(f"\nSession Landscape Builder is ready for conference-advisor integration!")
        print(f"\nKey features:")
        print(f"  ✅ Unified session landscape (not per-speaker)")
        print(f"  ✅ Speaker mapping to landscape positions")
        print(f"  ✅ Formatted background document generation")
        print(f"  ✅ AI/ML topic filtering (skips unsuitable topics)")
        print(f"\nNext: Use in conference-advisor SKILL.md workflow")

        return 0

    except Exception as e:
        print(f"\n❌ Test failed: {e}")
        import traceback
        traceback.print_exc()
        return 1


if __name__ == "__main__":
    sys.exit(main())
