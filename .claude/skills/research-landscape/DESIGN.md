# Research Landscape Analyzer - Design Document

## Overview

독립적인 연구 분야 심층 분석 도구. 특정 주제 입력 시 리뷰 논문, 거점 논문, citation network, 최신 트렌드를 자동 추출.

**핵심 원칙**:
- Conference-advisor와 **독립적** (별도 skill)
- **모듈화** (다른 skill에서 import 가능)
- OpenAlex 기반 (검증된 인프라)

**Target Fields** (명시적 범위 제한):
- Traditional life sciences (5+ year research cycles)
- Citation-based analysis works well (1-3 year lag acceptable)
- **NOT for fast-moving fields** (AI/ML with 1-3 month cycles)

## Use Cases

### Primary Use Case: 새 연구 주제 파악
```
User: "single-cell spatial transcriptomics 연구 동향 파악해줘"

Analyzer:
1. 리뷰 논문 추출 (10-20편)
   → "Spatial transcriptomics: recent advances" (Nature Reviews, 2024)
   → 큰 그림 파악

2. 거점 논문 식별 (5-10편)
   → 10x Visium 원논문 (2019, 1200 citations)
   → Highly cited, foundational

3. Citation network
   → Visium (2019) → MERFISH (2020) → Stereo-seq (2022)
   → 계보 파악

4. 최근 파생 연구 (2023-2025, 20-50편)
   → "Deep learning for spatial transcriptomics" (2024)
   → "Multi-modal spatial omics" (2025)
   → 최신 트렌드

5. SOTA (benchmark 있으면)
   → Benchmark: Cell segmentation accuracy
   → Current SOTA: Method X (95.2% F1)
```

### Secondary Use Case: Conference-advisor에서 사용
```python
# conference-advisor/src/background_generator.py에서

from research_landscape import TopicAnalyzer

# 세션 주제 심층 분석
session_topic = "CRISPR prime editing"
landscape = TopicAnalyzer().analyze(session_topic)

# 배경 자료에 통합
background += landscape.review_papers  # 리뷰 논문
background += landscape.key_papers     # 거점 논문
background += landscape.recent_trends  # 최신 동향
```

## Architecture

### Module Structure

```
.claude/skills/research-landscape/
├── SKILL.md                    # Skill definition (for Claude Code)
├── DESIGN.md                   # This file
├── README.md                   # User guide
│
├── src/                        # Core modules (reusable)
│   ├── __init__.py
│   │
│   ├── openalex_client.py     # Symlink or copy from conference-advisor
│   │                          # (shared infrastructure)
│   │
│   ├── review_finder.py       # NEW: Review paper detection
│   │   - find_reviews(topic, limit=20)
│   │   - heuristic_filter(papers)  # "review|comprehensive" in title
│   │   - rank_by_citations()
│   │
│   ├── anchor_finder.py       # NEW: Anchor/foundation paper detection
│   │   - find_anchors(topic, years=10, limit=10)
│   │   - time_weighted_score(papers)
│   │   - filter_highly_cited(threshold=100)
│   │
│   ├── citation_network.py    # NEW: Citation network builder
│   │   - build_network(seed_papers, hops=2)
│   │   - calculate_metrics()  # PageRank, betweenness
│   │   - find_bridges()
│   │   - export_to_graphml()  # For Gephi visualization
│   │
│   ├── trend_tracker.py       # NEW: Recent derivative research
│   │   - find_derivatives(anchor_papers, years=2)
│   │   - detect_emerging_concepts()
│   │   - cluster_by_approach()
│   │
│   ├── sota_tracker.py        # NEW: SOTA tracking (if benchmark exists)
│   │   - check_papers_with_code(topic)
│   │   - fetch_leaderboard(benchmark_id)
│   │   - compare_methods()
│   │
│   └── report_generator.py   # NEW: Markdown report generator
│       - generate_full_report(analysis_result)
│       - generate_summary()
│       - export_csv()  # For spreadsheet users
│
├── cache/                      # SQLite cache (shared with conference-advisor)
│   └── openalex_cache.db
│
└── outputs/                    # Generated reports
    └── [topic]_[date].md
```

### Data Flow

```
User Input: "CRISPR prime editing"
    ↓
[TopicAnalyzer] (main orchestrator)
    ↓
    ├─→ [ReviewFinder]
    │   └─→ OpenAlex: type=review OR title contains "review"
    │       + filter: cited_by_count > 50
    │       → 15 review papers
    │
    ├─→ [AnchorFinder]
    │   └─→ OpenAlex: topic search + sort by citations
    │       + time_weighted_score (recent papers 가중치)
    │       → 8 anchor papers (2015-2023, 200-2000 citations)
    │
    ├─→ [CitationNetwork]
    │   └─→ For each anchor: fetch citing_papers + referenced_works
    │       + build directed graph
    │       + calculate PageRank, betweenness
    │       → Network with 500-1000 nodes
    │
    ├─→ [TrendTracker]
    │   └─→ From network: filter papers (2023-2025)
    │       + cluster by concepts (ML methods, delivery, applications)
    │       → 30 recent papers grouped by approach
    │
    └─→ [SOTATracker]
        └─→ Query PapersWithCode API
            + if benchmark exists: fetch leaderboard
            → SOTA method + scores (if available)
    ↓
[ReportGenerator]
    ↓
Markdown Report (5000-10000 lines):
    - Executive Summary
    - Review Papers (annotated)
    - Anchor Papers (timeline)
    - Citation Network (metrics + visualization)
    - Recent Trends (clustered)
    - SOTA Comparison (if applicable)
    - Recommended Reading Path
```

## Core Features (MVP)

### Phase 1: Basic Analysis (Week 1)
**Goal**: 주제 입력 → 리뷰 + 거점 논문 추출

**Modules**:
- `review_finder.py`
- `anchor_finder.py`
- `report_generator.py` (basic)

**Output**:
```markdown
# Research Landscape: [Topic]

## Review Papers (10)
1. "Title..." (Nature Reviews, 2024, 345 citations)
   - Coverage: Basic mechanisms, applications
   - Key insights: ...

## Anchor Papers (8)
1. "Original paper..." (2015, 2034 citations)
   - Contribution: First demonstration
   - Impact: Foundation for field
```

**Development Time**: 2-3 days

---

### Phase 2: Citation Network (Week 2)
**Goal**: 거점 논문 → citation network → 파생 연구

**Modules**:
- `citation_network.py`
- `trend_tracker.py`

**Output**:
```markdown
## Citation Network Analysis

**Network Stats**:
- Nodes: 856 papers
- Edges: 3421 citations
- Diameter: 5 hops

**Key Bridge Papers** (betweenness centrality):
1. "Paper X" (2018) - Connects basic research ↔ applications

## Recent Derivatives (2023-2025, 32 papers)

**Cluster 1: ML-based optimization** (12 papers)
- "Deep learning for guide design" (2024, 3 citations)
- ...

**Cluster 2: Delivery systems** (10 papers)
- "Nanoparticle delivery of prime editors" (2024, 1 citation)
- ...
```

**Development Time**: 4-5 days

---

### Phase 3: SOTA Tracking (Week 3)
**Goal**: Benchmark 존재 시 SOTA 추적

**Modules**:
- `sota_tracker.py`
- Integration with PapersWithCode API

**Output**:
```markdown
## State-of-the-Art (SOTA)

**Benchmark**: Prime editing efficiency (HEK293T cells)

| Rank | Method | Efficiency | Year | Paper |
|------|--------|-----------|------|-------|
| 1 | Method A | 47.2% | 2024 | "Paper..." |
| 2 | Method B | 43.1% | 2023 | "Paper..." |
| 3 | Original | 35.5% | 2019 | "Paper..." |

**Trend**: +33% improvement over 5 years
```

**Development Time**: 3-4 days

---

## API Design (for Modular Use)

### Python API

```python
from research_landscape import TopicAnalyzer

# Basic usage
analyzer = TopicAnalyzer(email="your@email.com")  # OpenAlex polite pool

result = analyzer.analyze(
    topic="CRISPR prime editing",
    years=10,           # Look back 10 years
    max_reviews=20,     # Max review papers
    max_anchors=10,     # Max anchor papers
    network_hops=2,     # Citation network depth
    include_sota=True   # Check for benchmarks
)

# Access results
print(result.reviews)          # List[Paper]
print(result.anchors)          # List[Paper]
print(result.network)          # NetworkX graph
print(result.recent_trends)    # Dict[cluster -> List[Paper]]
print(result.sota)             # SOTAInfo or None

# Generate report
result.to_markdown("prime_editing_analysis.md")
result.to_json("prime_editing_analysis.json")

# Export network for visualization
result.network.export_graphml("network.graphml")  # Open in Gephi
```

### CLI Usage

```bash
# Basic analysis
research-landscape analyze "CRISPR prime editing"

# Advanced options
research-landscape analyze "spatial transcriptomics" \
    --years 5 \
    --max-reviews 15 \
    --network-hops 3 \
    --output report.md

# Quick summary
research-landscape summary "AlphaFold"

# SOTA only
research-landscape sota "protein structure prediction"
```

### Skill Usage (in Claude Code)

```
User: "CRISPR base editing 연구 동향 분석해줘"

Skill:
  1. Calls TopicAnalyzer.analyze("CRISPR base editing")
  2. Generates comprehensive report
  3. Returns markdown to user

Output: 5000-line analysis ready to read
```

## Integration with Conference-Advisor

### Use Case: Session Background Enhancement

```python
# In conference-advisor/src/background_generator.py

from research_landscape import TopicAnalyzer

def generate_session_background(session):
    """Enhanced background with research landscape."""

    # Basic session info (existing)
    background = format_session_info(session)

    # NEW: Deep dive into session topic
    landscape = TopicAnalyzer().analyze(
        topic=session['topic'],
        years=5,  # Focus on recent
        max_reviews=5,
        max_anchors=5,
        network_hops=1,  # Shallow for speed
        include_sota=True
    )

    # Add to background
    background += f"\n\n## 분야 배경 (Research Landscape)\n"
    background += landscape.format_review_section()
    background += landscape.format_anchor_section()
    background += landscape.format_trends_section()

    return background
```

**Benefit**: Conference-advisor 배경 자료가 자동으로 더 풍부해짐

---

## Technical Specifications

### OpenAlex Query Strategy

**Review Paper Detection**:
```python
# Method 1: Official type
url = f"{base_url}/works?filter=type:review,concepts.id:{concept_id}"

# Method 2: Heuristic (higher recall)
url = f"{base_url}/works?search={topic}"
# Then filter:
#   - title contains: "review|comprehensive|perspective|survey"
#   - cited_by_count > 50
#   - exclude: "case report|patient"

# Combine both methods
reviews = deduplicate(method1_results + method2_results)
```

**Anchor Paper Selection**:
```python
# Time-weighted citation score
def anchor_score(paper):
    years = 2025 - paper['publication_year']
    citations = paper['cited_by_count']

    # Penalty for very old papers (>10 years)
    age_penalty = 1.0 if years <= 10 else 0.5

    # Citations per year, with age penalty
    score = (citations / max(years, 1)) * age_penalty

    return score

# Fetch and rank
papers = fetch_works(topic, limit=500, sort="cited_by_count:desc")
ranked = sorted(papers, key=anchor_score, reverse=True)
anchors = ranked[:10]
```

**Citation Network Construction**:
```python
# 2-hop network
def build_network(seed_papers, hops=2):
    G = nx.DiGraph()

    # Add seed papers
    for paper in seed_papers:
        G.add_node(paper['id'], **paper)

    # Hop 1: Backward (references)
    for paper in seed_papers:
        refs = paper['referenced_works'][:20]  # Limit to top 20
        for ref_id in refs:
            ref_data = fetch_work(ref_id)
            G.add_node(ref_id, **ref_data)
            G.add_edge(paper['id'], ref_id, type='cites')

    # Hop 1: Forward (citing papers)
    for paper in seed_papers:
        citing = fetch_citing_papers(paper['id'], limit=50)  # Top 50
        for cite in citing:
            G.add_node(cite['id'], **cite)
            G.add_edge(cite['id'], paper['id'], type='cites')

    # Hop 2: (optional, expensive)
    # ...

    return G
```

### Rate Limiting Strategy

**OpenAlex Polite Pool**:
- 10 requests/second
- Daily limit: 100,000 requests
- Use email in User-Agent

**Estimated API Calls**:
```
Review search:        1 request
Anchor search:        1 request
Each paper details:   10-20 requests (for top papers)
Citation network:     100-500 requests (2-hop, 100 seeds)
Recent derivatives:   50-100 requests

Total per analysis:   ~200-700 requests
Time estimate:        20-70 seconds (at 10 req/sec)
```

**Optimization**:
```python
# Use batch endpoints where possible
url = f"{base_url}/works?filter=openalex_id:{id1}|{id2}|{id3}"

# Cache aggressively (SQLite)
# TTL: 30 days for papers, 7 days for citations

# Parallel requests (threading)
from concurrent.futures import ThreadPoolExecutor
with ThreadPoolExecutor(max_workers=10) as executor:
    results = executor.map(fetch_work, paper_ids)
```

---

## Output Format

### Markdown Report Structure

```markdown
# Research Landscape Analysis: [Topic]
*Generated: 2025-01-15*
*Analysis period: 2015-2025*

---

## Executive Summary

**Field maturity**: Established (10+ years)
**Publication velocity**: 234 papers/year (2023-2024)
**Key breakthrough**: CRISPR base editing (2016)
**Current focus**: Delivery optimization, in vivo applications

**Reading recommendation**: Start with Review #1 (Nature Reviews, 2024)

---

## 1. Review Papers (Foundational Reading)

*Papers that provide comprehensive overview of the field*

### R1. "CRISPR base editing: recent advances and applications"
- **Journal**: Nature Reviews Genetics (2024)
- **Citations**: 345
- **Authors**: Komor AC, Badran AH, Liu DR (Harvard)
- **Coverage**:
  - Mechanisms (ABE, CBE, dual editors)
  - Delivery methods (viral, nanoparticle)
  - Applications (disease modeling, therapy)
  - Future directions
- **Why read**: Most comprehensive recent overview
- **Reading time**: 2-3 hours
- **Link**: DOI: 10.1038/...

[... 9 more review papers ...]

---

## 2. Anchor Papers (Field Foundations)

*Highly-cited papers that defined the field*

### A1. "Programmable base editing of A•T to G•C in genomic DNA"
- **Year**: 2017
- **Citations**: 2,034 (203 citations/year)
- **Impact**: **Foundation paper** - First ABE demonstration
- **Authors**: Gaudelli NM et al. (Broad Institute)
- **Key contribution**: TadA-dCas9 fusion for A-to-G editing
- **Cited by**: 1,200+ papers (including 50+ in 2024)
- **Network centrality**: PageRank 0.0342 (Top 1%)
- **Link**: DOI: 10.1038/...

**Why important**:
- Opened new editing modality beyond CBE
- Enabled correction of 47% of pathogenic SNPs
- Spawned 200+ derivative studies

[... 7 more anchor papers ...]

---

## 3. Citation Network Analysis

**Network statistics**:
- Papers: 856
- Citations: 3,421
- Average degree: 8.0
- Diameter: 5 hops
- Clustering coefficient: 0.23

**Key bridge papers** (connect sub-communities):
1. "Prime editing" (2019) - Connects base editing ↔ precision editing
2. "AAV delivery" (2020) - Connects in vitro ↔ in vivo applications

**Network visualization**: See `network.graphml` (open in Gephi)

---

## 4. Recent Trends (2023-2025)

*Emerging directions and latest developments*

### Trend 1: AI-Optimized Guide Design (15 papers)

**Approach**: Machine learning for predicting editing efficiency

**Representative papers**:
1. "Deep learning predicts base editing outcomes" (2024, 5 citations)
   - Method: Transformer model trained on 50k edits
   - Performance: R² = 0.82 (vs 0.65 previous)
   - Dataset: Available on GitHub

2. "Attention-based guide optimization" (2024, 2 citations)
   - Innovation: Multi-task learning (on/off-target jointly)
   - Result: 30% reduction in off-targets

[... 13 more papers in this cluster ...]

### Trend 2: Nanoparticle Delivery (12 papers)

**Motivation**: Overcome AAV size limitations

[... details ...]

### Trend 3: In Vivo Disease Models (18 papers)

[... details ...]

---

## 5. State-of-the-Art (SOTA)

### Benchmark: Base editing efficiency (HEK293T cells)

**Leaderboard** (PapersWithCode):

| Rank | Method | Efficiency | Specificity | Year | Paper |
|------|--------|-----------|-------------|------|-------|
| 1 | HypaBE | 78.3% | 99.2% | 2024 | "Enhanced..." |
| 2 | NG-ABE | 74.1% | 98.9% | 2023 | "Next-gen..." |
| 3 | ABE8e | 68.5% | 99.1% | 2022 | "Evolution..." |
| ... | Original ABE | 47.2% | 97.5% | 2017 | "First..." |

**Trend**: +66% efficiency improvement over 7 years

**Current frontier**: Reaching >80% efficiency with minimal off-targets

---

## 6. Recommended Reading Path

### For Beginners (PhD students, new to field):
1. Start: Review #1 (Nature Reviews, 2024) - 3 hours
2. Then: Anchor #1 (Original ABE, 2017) - 1 hour
3. Then: Anchor #5 (Prime editing, 2019) - 1 hour
4. Survey recent trends: Skim Trend papers - 2 hours

**Total time**: 1 day of focused reading
**Outcome**: Solid foundation + current awareness

### For Experts (applying to own research):
1. Skim: Review #1 (know the landscape)
2. Deep dive: Anchor papers in your specific niche
3. Focus: Recent papers in relevant trend cluster
4. Check: SOTA leaderboard for your application

---

## 7. Collaboration Opportunities

**Authors to watch** (based on recent high-impact work):
- David Liu (Harvard) - 12 papers, 3 in Top 10 cited
- Akihiko Kondo (Kobe) - Emerging leader, 8 papers 2023-2024
- ...

**Institutions with multiple groups**:
- Broad Institute: 3 active groups
- Harvard Medical School: 2 groups
- ...

---

## 8. Research Gaps & Future Directions

**Identified gaps** (from citation analysis):
1. **Large-scale multiplexing**: Only 3 papers, limited citations
2. **Regulatory approval pathway**: Underexplored (1 paper)
3. **Long-term safety in vivo**: Early stage (5 papers, all 2024)

**Predicted hot topics** (based on concept trends):
- Single-cell base editing (concept mentions +300% in 2024)
- Epigenome editing (co-occurring with base editing +150%)

---

## Appendices

### A. Full Paper List (CSV)
See: `base_editing_papers.csv` (856 papers with metadata)

### B. Network Data
See: `network.graphml` (Gephi), `network.json` (D3.js)

### C. Analysis Metadata
- Query: "CRISPR base editing"
- Date: 2025-01-15
- Papers analyzed: 856
- API calls: 423
- Processing time: 34 seconds
- OpenAlex coverage: 94% (48 papers missing DOI)

---

*Generated by Research Landscape Analyzer v1.0*
*OpenAlex data | Papers with Code integration*
```

---

## Implementation Roadmap

### Week 1: MVP (Basic Analysis)
- [ ] Set up directory structure
- [ ] Copy/adapt openalex_client.py from conference-advisor
- [ ] Implement review_finder.py
- [ ] Implement anchor_finder.py
- [ ] Implement basic report_generator.py
- [ ] Test with 3-5 topics
- [ ] Documentation (README.md, examples)

**Deliverable**: Working tool that outputs review + anchor papers

### Week 2: Citation Network
- [ ] Implement citation_network.py
- [ ] NetworkX integration
- [ ] Calculate centrality metrics
- [ ] GraphML export
- [ ] Implement trend_tracker.py
- [ ] Clustering recent papers
- [ ] Enhanced report with network analysis

**Deliverable**: Full citation network analysis

### Week 3: SOTA & Polish
- [ ] Implement sota_tracker.py
- [ ] PapersWithCode API integration
- [ ] Leaderboard fetching
- [ ] CLI interface
- [ ] Python package setup (pip installable)
- [ ] Comprehensive testing
- [ ] Example outputs for 10+ topics

**Deliverable**: Production-ready tool

### Week 4: Integration & Documentation
- [ ] Conference-advisor integration example
- [ ] Performance optimization
- [ ] Caching strategy refinement
- [ ] User guide (with videos?)
- [ ] Deployment guide for lab sharing

**Deliverable**: Integrated, documented system

---

## Success Metrics

**Quantitative**:
- Analysis time: < 60 seconds for typical topic
- Review paper recall: > 60% (vs manual search)
- Anchor paper precision: > 80% (expert validation)
- API efficiency: < 500 calls per analysis
- Report length: 5,000-10,000 lines

**Qualitative**:
- User feedback: "Saved 2-3 days of literature review"
- Adoption: Used for 5+ different research topics
- Integration: Successfully used in conference-advisor

---

## Future Enhancements (Post-MVP)

1. **Multi-language support**: 한국어 리포트 생성
2. **Semantic Scholar integration**: Complement OpenAlex
3. **PubMed integration**: Clinical papers
4. **Auto-update**: Weekly runs for tracked topics
5. **Visualization dashboard**: Web UI with D3.js
6. **Collaboration graph**: Author network analysis
7. **Funding analysis**: NIH Reporter integration
8. **Patent analysis**: Google Patents API

---

## Appendix: Alternative Approaches Considered

### Rejected: Semantic Scholar API
**Pros**: Good paper embeddings, recommendation engine
**Cons**: Lower coverage than OpenAlex, rate limits stricter
**Decision**: Use OpenAlex as primary, S2 as fallback

### Rejected: Full-text analysis (PubMed Central)
**Pros**: Methods/results section analysis
**Cons**: Expensive (NLP), coverage limited, rate limits
**Decision**: Stick to metadata (title/abstract) for MVP

### Rejected: Real-time SNS monitoring
**Pros**: Catch buzz early
**Cons**: High false positive, field bias, ROI low
**Decision**: Focus on citation-based (proven signal)

---

**Version**: 1.0 (Design Phase)
**Last Updated**: 2025-01-15
**Status**: Ready for implementation
**Estimated Development**: 3-4 weeks (MVP)