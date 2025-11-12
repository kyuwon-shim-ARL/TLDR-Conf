#!/usr/bin/env python3
"""
Example: Conference-Advisor Integration

Demonstrates how to use Research Landscape Analyzer within conference-advisor
to generate enriched background documents.
"""

import sys
from pathlib import Path

# Add src to path
sys.path.insert(0, str(Path(__file__).parent / "src"))

from src import TopicAnalyzer


def should_use_landscape_analyzer(session_topic):
    """
    Determine if topic is suitable for citation-based analysis.

    Returns:
        bool: True if should use Research Landscape Analyzer, False otherwise
    """
    # AI/ML topics (too fast-moving)
    ai_ml_keywords = ["AI", "machine learning", "deep learning", "LLM", "GPT", "neural network"]
    if any(kw.lower() in session_topic.lower() for kw in ai_ml_keywords):
        print(f"   ❌ AI/ML topic detected → Use WebSearch instead")
        return False

    # Very new techniques (<2 years)
    very_new = ["2024", "2025", "breakthrough", "first-in-human"]
    if any(kw in session_topic.lower() for kw in very_new):
        print(f"   ❌ Very new topic → Use WebSearch for latest")
        return False

    # Traditional biology (good for citation analysis)
    traditional_bio = ["pathogen", "microb", "immun", "metabol", "protein", "gene", "cell"]
    if any(kw in session_topic.lower() for kw in traditional_bio):
        print(f"   ✅ Traditional biology → Research Landscape Analyzer suitable")
        return True

    print(f"   ⚠️  Uncertain topic → Defaulting to WebSearch")
    return False


def generate_reading_list(landscape_result):
    """
    Generate "📚 사전 읽기" section from landscape analysis.

    Args:
        landscape_result: AnalysisResult object

    Returns:
        str: Formatted reading list section
    """
    section = "## 📚 사전 읽기 (Preliminary Reading)\n\n"
    section += "**필수 리뷰 논문** (Research Landscape Analysis):\n\n"

    for i, paper in enumerate(landscape_result.reviews[:5], 1):
        title = paper.get('title', 'Unknown')
        year = paper.get('publication_year', 'N/A')
        citations = paper.get('cited_by_count', 0)
        doi = paper.get('doi', 'N/A')

        # Estimate reading time based on citation count (proxy for comprehensiveness)
        reading_time = "2-3 hours" if citations > 200 else "1.5-2 hours"

        # Importance stars (based on citations and recency)
        importance = "⭐⭐⭐⭐⭐" if i == 1 else "⭐⭐⭐⭐"

        section += f"{i}. \"{title}\" ({year}, {citations:,} citations)\n"
        section += f"   - 읽기 시간: {reading_time}\n"
        section += f"   - 중요도: {importance}\n"
        section += f"   - [DOI: {doi}]\n\n"

    return section


def generate_historical_context(landscape_result):
    """
    Generate historical context using anchor papers.

    Args:
        landscape_result: AnalysisResult object

    Returns:
        str: Historical context narrative
    """
    section = "## 🌟 쉬운말 풀이 - 분야의 역사와 발전\n\n"

    if not landscape_result.anchors:
        section += "*No anchor papers available for historical context.*\n"
        return section

    section += "**[1장: 배경 - 분야의 기초]**\n\n"

    # Get top 3 anchor papers
    anchors = landscape_result.anchors[:3]

    section += f"이 분야는 {anchors[0]['publication_year']}년경부터 본격적으로 발전하기 시작했습니다.\n\n"
    section += "**핵심 거점 논문들:**\n\n"

    for paper in anchors:
        title = paper.get('title', 'Unknown')
        year = paper.get('publication_year', 'N/A')
        citations = paper.get('cited_by_count', 0)
        score = paper.get('anchor_score', 0)

        section += f"- \"{title}\" ({year}, {citations:,} citations, score: {score:.1f})\n"

    section += "\n이 논문들은 현재 연구의 이론적 기초를 제공합니다.\n"

    return section


def generate_recent_trends(landscape_result):
    """
    Generate recent trends section.

    Args:
        landscape_result: AnalysisResult object

    Returns:
        str: Recent trends summary
    """
    section = "## 📈 최근 연구 동향 (2023-2025)\n\n"

    if not landscape_result.recent_trends:
        section += "*No recent trends available (try enabling --trends in analysis).*\n"
        return section

    section += f"Research Landscape Analysis에서 확인된 최근 {len(landscape_result.recent_trends)}편의 논문:\n\n"

    if landscape_result.trend_clusters:
        section += "**트렌드 클러스터:**\n\n"
        for concept, papers in list(landscape_result.trend_clusters.items())[:3]:
            section += f"### {concept} ({len(papers)} papers)\n"
            for paper in papers[:2]:  # Top 2 per cluster
                title = paper.get('title', 'Unknown')
                year = paper.get('publication_year', 'N/A')
                cites = paper.get('cited_by_count', 0)
                section += f"- \"{title}\" ({year}, {cites} citations)\n"
            section += "\n"

    if landscape_result.emerging_concepts:
        section += "**새롭게 등장하는 개념들:**\n\n"
        for concept in landscape_result.emerging_concepts[:5]:
            name = concept['name']
            is_new = concept['is_new']
            growth = concept.get('growth_rate', 0)

            if is_new:
                section += f"- **{name}**: NEW (거점 논문에 없던 새 개념)\n"
            else:
                section += f"- **{name}**: {growth:.1f}x 성장률\n"

    return section


def generate_conference_background(session_topic, session_abstract=None):
    """
    Generate conference background document using Research Landscape Analyzer.

    Args:
        session_topic: Session title or research topic
        session_abstract: Optional session abstract

    Returns:
        str: Complete background document
    """
    print(f"\n{'='*80}")
    print(f"Conference Background Generator")
    print(f"{'='*80}\n")
    print(f"Session Topic: {session_topic}")

    # Step 1: Check if topic is suitable
    print(f"\n1. Checking topic suitability...")
    if not should_use_landscape_analyzer(session_topic):
        print("\n→ Skipping Research Landscape Analyzer (use WebSearch instead)\n")
        return None

    # Step 2: Run landscape analysis
    print(f"\n2. Running Research Landscape Analysis...")
    analyzer = TopicAnalyzer(email="test@example.com")

    try:
        landscape = analyzer.analyze(
            topic=session_topic,
            max_reviews=10,
            max_anchors=8,
            years=10,
            include_trends=True  # Get recent trends for 2023-2025 section
        )
    except Exception as e:
        print(f"   ❌ Error during analysis: {e}")
        return None

    # Step 3: Generate background sections
    print(f"\n3. Generating background document sections...")

    background = f"# Background Document: {session_topic}\n\n"
    background += f"*Generated using Research Landscape Analyzer v1.0*\n\n"
    background += "---\n\n"

    # Reading list
    print("   - 📚 사전 읽기 (Reading list)")
    background += generate_reading_list(landscape)
    background += "\n---\n\n"

    # Historical context
    print("   - 🌟 쉬운말 풀이 (Historical context)")
    background += generate_historical_context(landscape)
    background += "\n---\n\n"

    # Recent trends
    print("   - 📈 최근 연구 동향 (Recent trends)")
    background += generate_recent_trends(landscape)
    background += "\n---\n\n"

    print(f"\n✅ Background document generated ({len(background)} characters)")

    return background


def main():
    """Main function demonstrating conference integration."""

    # Example 1: Mycobacterial pathogenesis session
    print("\n" + "="*80)
    print("EXAMPLE 1: Mycobacterial Pathogenesis Session")
    print("="*80)

    background1 = generate_conference_background(
        session_topic="mycobacterial pathogenesis"
    )

    if background1:
        # Save to file
        output_file = "example_background_mycobacterial.md"
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(background1)
        print(f"\n📄 Saved to: {output_file}")

    # Example 2: AI topic (should skip)
    print("\n\n" + "="*80)
    print("EXAMPLE 2: AI/ML Topic (should skip)")
    print("="*80)

    background2 = generate_conference_background(
        session_topic="deep learning for protein structure prediction"
    )

    if not background2:
        print("\n✅ Correctly skipped AI/ML topic")


if __name__ == "__main__":
    main()
