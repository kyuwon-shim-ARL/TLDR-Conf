#!/usr/bin/env python3
"""
Quick test for Conference-Advisor v3.0 MVP
Tests OpenAlex integration with real speaker from IAMRT2025.
"""

import sys
from pathlib import Path

# Add src to path
sys.path.insert(0, str(Path(__file__).parent / "src"))

from speaker_analyzer import quick_speaker_analysis

def test_speaker():
    """Test with Sung Jae Shin from IAMRT2025 Session 2."""
    print("=" * 60)
    print("Conference-Advisor v3.0 MVP Test")
    print("=" * 60)
    print()

    print("Testing speaker: Sung Jae Shin (Yonsei University)")
    print("Expected: High h-index, MTB/mycobacterial research")
    print()
    print("Fetching from OpenAlex...")
    print()

    # Run analysis
    result = quick_speaker_analysis(
        name="Sung Jae Shin",
        affiliation="Yonsei",
        email="kyuwon.shim@ip-korea.org"  # Using your email for polite pool
    )

    if result:
        print("✅ SUCCESS! OpenAlex data retrieved:")
        print()
        print(result)
    else:
        print("❌ FAILED: Could not find speaker or API error")
        return False

    print("=" * 60)
    print("Test completed successfully!")
    print("=" * 60)
    return True

if __name__ == "__main__":
    success = test_speaker()
    sys.exit(0 if success else 1)
