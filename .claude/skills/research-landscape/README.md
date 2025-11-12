# Research Landscape Analyzer

특정 연구 주제에 대한 자동 심층 문헌 분석 도구

## ⚠️ Scope & Limitations

### ✅ Supported Fields (Citation-based, 5+ year cycles)

- **Traditional Biology**: Microbiology, mycobacteriology, immunology, pathogenesis
- **Chemistry**: Organic synthesis, medicinal chemistry
- **Basic Medicine**: Disease mechanisms, drug discovery
- **Ecology & Evolution**: Microbial ecology, population genetics

**Why it works**: Citation stabilization (1-3 years) matches field pace

### ⚠️ Partial Support (Hybrid approach needed)

- **Computational Biology**: AlphaFold-type breakthroughs (use tool + manual)
- **Bioinformatics**: New algorithms (check benchmarks manually)
- **Medical Imaging AI**: If benchmarks exist (Papers with Code)

**Strategy**: Use tool for established base (5+ years) + manual for latest (0-2 years)

### ❌ NOT Supported (Manual curation required)

- **LLM/Foundation Models**: GPT, Claude, Gemini (changes monthly)
- **AI Agents**: AutoGPT, LangChain (no papers, blog posts only)
- **Generative AI**: DALL-E, Midjourney, Sora (too fast, citation meaningless)

**Why it fails**: Field changes every 1-3 months, citation lag 1-2 years → 10-20x gap

**Alternative**: See `docs/AI_ML_manual_curation.md` (coming soon)

## Quick Start

```python
from research_landscape import TopicAnalyzer

analyzer = TopicAnalyzer(email="your@email.com")
result = analyzer.analyze("CRISPR base editing")

# 5000-line comprehensive report
result.to_markdown("crispr_analysis.md")
```

## What It Does

주제 입력 → 자동으로:

1. **리뷰 논문** 추출 (큰 그림)
2. **거점 논문** 식별 (foundation)
3. **Citation network** 분석 (계보)
4. **최신 파생 연구** (트렌드)
5. **SOTA** 추적 (benchmark 있으면)

## Key Features

- OpenAlex 기반 (250M+ papers, 90M+ authors)
- Time-weighted citation scoring (최신 논문 가중치)
- Citation network with PageRank/betweenness
- Automatic clustering of recent trends
- SOTA leaderboard (PapersWithCode 통합)
- Modular design (다른 skill에서 import 가능)

## Output Example

```markdown
# Research Landscape: CRISPR Base Editing

## Executive Summary
Field maturity: Established (10+ years)
Key breakthrough: ABE/CBE (2016-2017)
Current focus: In vivo delivery, AI optimization

## Review Papers (15)
1. "CRISPR base editing: advances..." (Nat Rev, 2024, 345 cites)
   Reading time: 2-3 hours
   Why read: Most comprehensive overview

## Anchor Papers (8)
1. "Programmable base editing..." (2017, 2034 cites)
   Impact: Foundation - First ABE
   Network centrality: Top 1%

## Citation Network
Papers: 856 | Citations: 3,421
Key bridges: Prime editing (2019)

## Recent Trends (2023-2025)
- AI-optimized guide design (15 papers)
- Nanoparticle delivery (12 papers)
- In vivo models (18 papers)

## SOTA
Benchmark: Editing efficiency (HEK293T)
Current best: 78.3% (HypaBE, 2024)
Trend: +66% improvement over 7 years
```

## Status

**Current**: Design phase ✅
**Next**: MVP implementation (Week 1)

## Development Roadmap

- **Week 1**: MVP (리뷰 + 거점 논문)
- **Week 2**: Citation network
- **Week 3**: SOTA tracking + polish
- **Week 4**: Integration + docs

## Documentation

- [DESIGN.md](DESIGN.md) - Full technical design (750+ lines)
- [Examples](examples/) - Sample outputs (coming soon)

## Integration

Conference-advisor에서 사용 가능:

```python
# conference-advisor/src/background_generator.py
from research_landscape import TopicAnalyzer

landscape = TopicAnalyzer().analyze(session['topic'])
background += landscape.format_review_section()
```

---

**Version**: 1.0 (Design)
**Estimated Development**: 3-4 weeks
