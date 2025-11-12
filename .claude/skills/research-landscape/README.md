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

### Option 1: Command Line (Recommended)

```bash
# Basic analysis
python cli.py analyze "spatial transcriptomics"

# With citation network and trends
python cli.py analyze "CRISPR base editing" --network --trends --output report.md

# Custom parameters
python cli.py analyze "mycobacterial pathogenesis" \
  --reviews 15 --anchors 10 --years 5 \
  --email your@email.com --output myreport.md

# See all options
python cli.py analyze --help
```

### Option 2: Python API

```python
from research_landscape import TopicAnalyzer

analyzer = TopicAnalyzer(email="your@email.com")
result = analyzer.analyze(
    "CRISPR base editing",
    include_network=True,
    include_trends=True
)

# Generate comprehensive report
result.to_markdown("crispr_analysis.md")
```

## What It Does

주제 입력 → 자동으로:

1. **리뷰 논문** 추출 (큰 그림 파악)
2. **거점 논문** 식별 (foundational papers)
3. **Citation network** 분석 (학문 계보, 연결 구조)
4. **최신 파생 연구** 추적 (2023-2025 트렌드)
5. **Emerging concepts** 탐지 (새롭게 등장하는 연구 방향)

## Key Features

- ✅ **OpenAlex API** 기반 (250M+ papers, 90M+ authors)
- ✅ **Time-weighted scoring** (오래된 논문 패널티, 최근 논문 가중치)
- ✅ **Citation network analysis** (PageRank, betweenness centrality, bridge papers)
- ✅ **Trend clustering** (concept 기반 자동 그룹화)
- ✅ **Emerging concept detection** (anchor vs recent 비교)
- ✅ **CLI + Python API** (편리한 사용)
- ✅ **Modular design** (다른 skill에서 import 가능)

## Output Example

```markdown
# Research Landscape: CRISPR Base Editing

## Executive Summary
**Topic**: CRISPR base editing
**Review papers found**: 15
**Anchor papers found**: 8
**Top review**: "CRISPR base editing: advances..." (2024, 345 citations)
**Reading recommendation**: Start with top review paper for comprehensive overview.

## Review Papers (15)
1. "CRISPR base editing: advances..." (Nat Rev, 2024, 345 cites)
   - Year: 2024
   - Citations: 345
   - Journal: Nature Reviews Genetics
   - Link: [DOI]

## Anchor Papers (8)
1. "Programmable base editing of A•T to G•C" (2017, 2034 cites)
   - Year: 2017
   - Citations: 2,034
   - Anchor Score: 254.25 (time-weighted)
   - Link: [DOI]

## Citation Network Analysis (optional)
**Network Statistics**:
- Nodes (papers): 856
- Edges (citations): 3,421
- Density: 0.0046
- Average clustering: 0.123

**Key Bridge Papers**:
1. "Prime editing" (2019) - Betweenness: 0.0234
   - Connects base editing and gene correction communities

## Recent Trends (2023-2025) (optional)
**50 papers in recent trends**

### Trend 1: In vivo delivery (18 papers)
1. "Lipid nanoparticle delivery..." (2024, 42 citations)
2. "AAV-mediated base editing..." (2023, 35 citations)

### Trend 2: AI-optimized guide design (15 papers)
...

**Emerging Concepts**:
- Deep learning optimization: 12.3x growth (NEW)
- Organoid models: 8.7x growth
```

## Status

**Version**: 1.0 ✅
**Completed**:
- ✅ Week 1: MVP (review finder, anchor finder, report generator)
- ✅ Week 2: Citation network + trend tracking
- ✅ Week 3: CLI interface

**Next**: Conference-advisor integration + documentation

## Development Roadmap

- ✅ **Week 1**: MVP (리뷰 + 거점 논문) - DONE
- ✅ **Week 2**: Citation network + trends - DONE
- ✅ **Week 3**: CLI interface - DONE
- ⏳ **Week 4**: Conference-advisor integration + final docs

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

**Version**: 1.0
**Status**: Core features complete ✅
**License**: MIT
