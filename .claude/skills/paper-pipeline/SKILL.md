# Paper Pipeline - 논문 검색/획득/분석/저장

## Overview

OpenAlex 기반 논문 검색, 원문 획득(Europe PMC/Unpaywall/GROBID), 계층적 분석(L0-L3), 저장소 관리.

## Quick Start

```python
from paper_pipeline.discovery import PaperDiscovery
from paper_pipeline.fetcher import PaperFetcher
from paper_pipeline.extractor import PaperExtractor
from paper_pipeline.store import PaperStore

# 1. 검색
discovery = PaperDiscovery(email="your@email.com")
papers = discovery.search("urban microbiome metagenomics", max_results=50)

# 2. 저장소 초기화
store = PaperStore("data/papers")

# 3. L0 메타데이터 저장
for paper in papers:
    store.save_layer(paper["doi"], "L0", paper)

# 4. 원문 획득
fetcher = PaperFetcher(email="your@email.com")
for paper in papers:
    result = fetcher.fetch_content(paper["doi"], work_data=paper)
    # result.content_type: "pmc_xml", "pdf", "abstract_only", "metadata_only"

# 5. 텍스트 추출
extractor = PaperExtractor()
extraction = extractor.extract(result, pdf_path=result.pdf_path)
# extraction.sections: {"Introduction": "...", "Methods": "...", ...}
```

## CLI Commands

```bash
# 검색
python cli.py search "urban microbiome" --max 50 --oa-only

# 원문 획득
python cli.py fetch --collection metasub --email user@example.com

# 저장소 상태 확인
python cli.py status

# 컬렉션 관리
python cli.py collection create metasub --dois "10.1038/xxx" "10.1016/yyy"
python cli.py collection list
python cli.py collection show metasub

# GROBID 상태 확인
python cli.py grobid-status
```

## Analysis Workflow (Claude Code Inline)

### Token Efficiency: 4-Layer System

| Layer | 내용 | 토큰/논문 | 생성 주체 |
|-------|------|-----------|-----------|
| L0 | 메타데이터 카드 | ~50 | Python (PyAlex 자동) |
| L1 | 구조화된 초록 | ~200-400 | Claude Code 인라인 |
| L2 | 섹션별 요약 | ~500-800 | Claude Code 인라인 |
| L3 | 심층 분석 | ~1500-2500 | Claude Code on-demand |

### L1 분석 생성

store에서 raw_abstract.txt를 읽고 다음 JSON 구조로 분석:

```json
{
  "objective": "1-2문장으로 연구 목적",
  "methods": "1-2문장으로 핵심 방법론",
  "key_findings": ["구체적 수치 포함 발견 1", "발견 2", "발견 3"],
  "significance": "1문장으로 학술적 의의"
}
```

결과를 `store.save_layer(doi, "L1", analysis)` 로 저장.

### L2 분석 생성 (full-text 필요)

store에서 content/fulltext.md를 읽고 섹션별 요약:

```json
{
  "introduction": "연구 배경 및 맥락 (2-3문장)",
  "methods": "핵심 방법론 요약 (2-3문장, 도구/데이터셋 포함)",
  "results": "주요 결과 (3-5 bullet points, 구체적 수치)",
  "discussion": "핵심 해석 및 시사점 (2-3문장)",
  "limitations": ["한계점 1", "한계점 2"]
}
```

extraction_method에 따른 분기:
- `"europe_pmc_xml"`: sections.json에 이미 구조화된 섹션 존재 → 직접 요약
- `"grobid"`: content/grobid.tei.xml 참조하여 구조적 정보 활용
- `"pymupdf4llm"`: fulltext.md만 존재, 섹션 경계 불명확할 수 있음

결과를 `store.save_layer(doi, "L2", analysis)` 로 저장.

### L3 심층 분석 (on-demand, 연구 질문 맥락)

L2 요약 + fulltext.md를 읽고:

```json
{
  "detailed_methodology": "재현 가능한 수준의 방법론 기술",
  "quantitative_results": ["결과 1 (p-value, CI 포함)", "..."],
  "limitations_by_authors": ["저자가 인정한 한계"],
  "open_questions": ["후속 연구 필요 사항"],
  "relevance_to_query": "연구 질문에 대한 이 논문의 기여도 및 연결점",
  "connections_to_corpus": ["관련 논문 DOI 및 연결 근거"]
}
```

결과를 `store.save_layer(doi, "L3", analysis)` 로 저장.

### Batch Analysis Workflow

```python
# 컬렉션의 모든 논문에 대해 L1 분석 생성
store = PaperStore("data/papers")
collection_dois = store.get_collection("metasub")

for doi in collection_dois:
    if store.has_layer(doi, "L1"):
        continue  # 이미 분석됨 → 스킵 (토큰 절약)

    abstract = store.load_content(doi, "abstract")
    if abstract:
        # Claude Code 인라인으로 L1 분석 생성
        analysis = generate_l1(abstract)  # → JSON dict
        store.save_layer(doi, "L1", analysis)
```

### Cache Utilization Pattern

```python
# 캐시된 L1 즉시 활용 (LLM 재호출 0회)
l1 = store.load_layer("10.1038/xxx", "L1")
if l1:
    print(f"Objective: {l1['objective']}")
    print(f"Key findings: {l1['key_findings']}")
```

## Graceful Degradation

| Tier | Source | Coverage | 추출 방법 |
|------|--------|----------|-----------|
| A | Europe PMC full-text XML | ~30-40% | XML 직접 파싱 (최선) |
| B | OA PDF + GROBID | ~40-55% | GROBID TEI XML → 섹션 추출 |
| C | OA PDF + pymupdf4llm | ~40-55% | GROBID 미가동 시 fallback |
| D | Abstract only (PyAlex) | ~85% | L0+L1만 가능 |
| E | Metadata only | 100% | L0만 가능 |

## GROBID Setup (Optional)

```bash
# Docker로 GROBID 시작
docker run --rm --init --ulimit core=0 -p 8070:8070 grobid/grobid:0.8.2-crf

# 또는 docker-compose
cd .claude/skills/paper-pipeline && docker-compose up -d

# 상태 확인
curl http://localhost:8070/api/isalive
```

## Dependencies

```bash
# 기본 설치
pip install -e ".claude/skills/paper-pipeline"

# GROBID 지원 포함
pip install -e ".claude/skills/paper-pipeline[grobid]"

# Deep Q&A 포함 (Python 3.11+)
pip install -e ".claude/skills/paper-pipeline[qa]"
```
