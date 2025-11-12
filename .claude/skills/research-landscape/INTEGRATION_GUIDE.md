# Research Landscape Analyzer - Integration Guide

## Integration with Conference-Advisor Skill

### Overview

Research Landscape Analyzer can enhance conference-advisor's background generation by providing:
- **Review papers** for preliminary reading섹션
- **Foundational papers** for topic deep dives
- **Recent trends** to supplement speaker/session analysis
- **Citation networks** to understand field structure

### When to Use

✅ **Use Research Landscape Analyzer for:**
- Traditional biology sessions (microbiology, immunology, pathogenesis)
- Chemistry/medicinal chemistry topics
- Established fields (5+ years old)
- Sessions where foundational understanding is needed

❌ **Do NOT use for:**
- AI/ML sessions (use WebSearch instead)
- Industry product launches (no academic literature)
- Clinical practice updates (use WebSearch for guidelines)
- Very new topics (<2 years old, not enough citations)

### Integration Methods

#### Method 1: Quick Import (Recommended)

```python
# In conference-advisor/src/background_generator.py (or similar)
import sys
from pathlib import Path

# Add research-landscape to path
landscape_path = Path(__file__).parent.parent.parent / "research-landscape" / "src"
sys.path.insert(0, str(landscape_path))

from research_landscape import TopicAnalyzer

def generate_background_with_landscape(session_topic, session_data):
    """Generate background using research landscape analysis."""

    # Step 1: Analyze topic using Research Landscape Analyzer
    analyzer = TopicAnalyzer(email="your@email.com")
    landscape = analyzer.analyze(
        topic=session_topic,
        max_reviews=10,
        max_anchors=8,
        years=10,
        include_trends=True  # Get recent trends (2023-2025)
    )

    # Step 2: Use results to enrich background sections

    ## For "📚 사전 읽기" section:
    review_papers = landscape.reviews[:5]  # Top 5 review papers
    for paper in review_papers:
        title = paper['title']
        year = paper['publication_year']
        citations = paper['cited_by_count']
        doi = paper.get('doi', 'N/A')
        # Format into reading list...

    ## For "최근 연구 배경" (연사 분석):
    if landscape.recent_trends:
        # Get recent papers related to session topic
        trends = landscape.recent_trends[:10]
        # Cross-reference with speaker's work...

    ## For "예상 발표 내용":
    anchor_papers = landscape.anchors[:3]  # Top 3 foundational papers
    # Use to understand theoretical foundations...

    return background_document
```

#### Method 2: CLI Wrapper

```python
import subprocess
import json

def get_landscape_via_cli(topic):
    """Get landscape analysis via CLI (no import needed)."""

    # Run CLI command
    cmd = [
        "python",
        "../research-landscape/cli.py",
        "analyze",
        topic,
        "--reviews", "10",
        "--anchors", "8",
        "--trends",
        "--output", f"landscape_{topic.replace(' ', '_')}.md"
    ]

    subprocess.run(cmd)

    # Read generated markdown file
    with open(f"landscape_{topic.replace(' ', '_')}.md", 'r') as f:
        return f.read()
```

### Usage Examples

#### Example 1: Mycobacterial Pathogenesis Session

```python
# Session S17: "Mycobacterial Pathogenesis & Host Interactions"
topic = "mycobacterial pathogenesis"

landscape = analyzer.analyze(topic, max_reviews=10, max_anchors=8)

# Extract review papers for preliminary reading
reviews = landscape.reviews[:5]

# Background template 📚 section:
"""
📚 사전 읽기 (Preliminary Reading)

**필수 리뷰 논문** (Research Landscape Analysis):

1. "Histopathologic review of granulomatous inflammation" (2017, 323 citations)
   - 핵심 내용: Granuloma formation mechanisms across mycobacterial infections
   - 읽기 시간: 2-3 hours
   - 중요도: ⭐⭐⭐⭐⭐ (Foundation for understanding session talks)
   - [DOI: 10.1016/j.jctube.2017.02.001]

2. "General Overview of Nontuberculous Mycobacteria..." (2020, 221 citations)
   - 핵심 내용: M. avium and M. abscessus pathogenesis mechanisms
   - 읽기 시간: 1.5-2 hours
   - 중요도: ⭐⭐⭐⭐ (Directly relevant to Talk #2)
   - [DOI: 10.3390/jcm9082541]

...
"""
```

#### Example 2: CRISPR/Gene Editing Session

```python
topic = "CRISPR base editing"

landscape = analyzer.analyze(
    topic,
    max_reviews=15,
    max_anchors=10,
    years=7,
    include_network=True,
    include_trends=True
)

# Use anchor papers to understand field evolution
anchors = landscape.anchors  # Time-weighted foundational papers

# Background template "🌟 쉬운말 풀이" section:
"""
🌟 쉬운말 풀이 - CRISPR Base Editing의 역사와 발전

**[1장: 배경 - CRISPR의 한계와 돌파구]**

2012년 CRISPR-Cas9이 등장하며 유전자 편집이 혁명적으로 변했습니다. 하지만 큰 문제가 있었습니다...
(Use anchor papers to understand early challenges)

**Foundation papers:**
- "Programmable base editing of A•T to G•C" (Liu lab, 2017, 2034 citations)
  → First adenine base editor (ABE)
- "Search-and-replace genome editing without double-strand breaks" (2016, 1523 citations)
  → First cytosine base editor (CBE)

**[2장: 메커니즘 - 어떻게 작동하나?]**

Base editing의 핵심 메커니즘은...
(Use review papers for detailed mechanism explanation)

**[3장: 최근 발전 - 2023-2025 트렌드]**

Research Landscape Analysis에서 확인된 최신 트렌드:
- In vivo delivery systems (18 papers, 2023-2024)
- AI-optimized guide design (15 papers, 2024)
  → Emerging concept: Deep learning optimization (12.3x growth)
...
"""
```

#### Example 3: Conditional Use (Check Topic Suitability)

```python
def should_use_landscape_analyzer(session_topic):
    """Determine if topic is suitable for citation-based analysis."""

    # AI/ML topics (too fast-moving)
    ai_ml_keywords = ["AI", "machine learning", "deep learning", "LLM", "GPT", "neural network"]
    if any(kw.lower() in session_topic.lower() for kw in ai_ml_keywords):
        return False

    # Very new techniques (<2 years)
    very_new = ["2024", "2025", "breakthrough", "first-in-human"]
    if any(kw in session_topic.lower() for kw in very_new):
        return False

    # Traditional biology (good for citation analysis)
    traditional_bio = ["pathogen", "microb", "immun", "metabol", "protein", "gene", "cell"]
    if any(kw in session_topic.lower() for kw in traditional_bio):
        return True

    return False  # Default: don't use

# Usage in background generator
if should_use_landscape_analyzer(session_topic):
    landscape = TopicAnalyzer().analyze(session_topic, include_trends=True)
    # Use landscape data in background template
else:
    # Fall back to WebSearch only
    pass
```

### Template Integration Points

Research Landscape Analyzer outputs can be inserted into these sections of `comprehensive_background_template.md`:

| Template Section | Landscape Data | How to Use |
|------------------|----------------|------------|
| **📚 사전 읽기** | `landscape.reviews` | Top 3-5 review papers for preliminary reading |
| **🌟 쉬운말 풀이** (Chapter 1-2) | `landscape.anchors` | Use foundational papers to explain historical context |
| **최근 연구 배경** | `landscape.recent_trends` | Recent papers (2023-2025) to supplement speaker analysis |
| **최근 연구 배경** | `landscape.emerging_concepts` | New research directions (concept growth rates) |
| **🎤 질문 리스트** (과학적 질문) | `landscape.bridge_papers` | Papers that connect different subfields → basis for interdisciplinary questions |
| **📊 예상 학습 성과** | `landscape.metadata` | Field maturity indicators (number of reviews, citation density) |

### Best Practices

1. **Run analysis before background generation**
   - Takes 15-60 seconds (basic) or 2-7 minutes (with network/trends)
   - Cache results to avoid repeated API calls

2. **Combine with WebSearch**
   - Use Research Landscape for **established knowledge** (reviews, foundations)
   - Use WebSearch for **latest news** (conference announcements, preprints, industry)

3. **Verify paper relevance**
   - Not all highly-cited papers are relevant to the specific session
   - Cross-check with session abstract and speaker's recent work

4. **Email for faster API**
   - Provide email to OpenAlex polite pool: `TopicAnalyzer(email="your@email.com")`
   - 10 req/sec (vs 5 req/sec without email)

5. **Error handling**
   - If topic is too niche: `landscape.reviews` may be empty
   - If topic is too new: `landscape.anchors` may have <5 papers
   - Always check `len(landscape.reviews) > 0` before using

### Example Integration Workflow

```
1. User requests background for Session S17 (Mycobacterial Pathogenesis)

2. Conference-advisor checks if topic is suitable
   → Yes (traditional microbiology, established field)

3. Run Research Landscape Analyzer:
   landscape = TopicAnalyzer().analyze("mycobacterial pathogenesis", include_trends=True)
   → 10 reviews, 8 anchors, 50 recent trends found

4. Generate background template sections:
   - 📚 사전 읽기: Use top 5 reviews with reading time estimates
   - 🌟 쉬운말 풀이: Use anchors to explain field evolution (Chapter 1-2)
   - 최근 연구 배경: Use recent_trends to identify 2023-2025 directions

5. Supplement with WebSearch:
   - Speaker's latest papers (not in landscape if too recent)
   - Conference-specific announcements
   - Industry applications

6. Combine all sources into comprehensive background document (1000+ lines)
```

### Performance Considerations

| Analysis Type | Time | Use Case |
|---------------|------|----------|
| Basic (reviews + anchors) | 15-20s | Quick preliminary reading list |
| + Trends | 30-45s | Recent developments (2023-2025) |
| + Network | 2-7min | Deep field analysis (optional) |

**Recommendation**: For conference backgrounds, use Basic + Trends (30-45s total). Skip network analysis unless field structure is critical.

### Troubleshooting

**Problem**: No review papers found
- **Cause**: Topic too niche or too new
- **Solution**: Try broader topic or skip landscape analysis

**Problem**: Landscape results don't match session focus
- **Cause**: Topic string too generic (e.g., "immunology" vs "T cell exhaustion")
- **Solution**: Use more specific topic string from session abstract

**Problem**: API rate limit errors
- **Cause**: Too many requests without email
- **Solution**: Add email to TopicAnalyzer(email="...") for polite pool

**Problem**: Takes too long (>2 minutes)
- **Cause**: Network analysis enabled
- **Solution**: Disable network (`include_network=False`) for faster results

### Full Integration Example

See `examples/conference_integration_example.py` (coming soon) for a complete implementation.

---

**Version**: 1.0
**Last Updated**: 2024-11-12
**Compatibility**: Conference-advisor v2.0+
