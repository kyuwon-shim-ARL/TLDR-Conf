# Conference-Advisor Skill v3.0 Upgrade Plan
## From WebSearch to Research Landscape Analysis

## 📊 현재 상태 (v2.0)

### 연사 뒷조사 방법
```python
# 현재: 단순 WebSearch
WebSearch("[Speaker name] research 2024-2025")
→ 최신 논문 몇 개
→ 소속 기관
→ 일반적인 연구 방향
```

### 한계점
- ❌ 연구 생태계에서의 **위치**를 모름
- ❌ 영향력 수준을 **정량화** 못함
- ❌ 주요 **협력자 네트워크** 파악 불가
- ❌ **인용 패턴**과 연구 흐름 모름
- ❌ **리뷰 논문** 저자 여부 (synthesis capability) 모름

**결과**: 표면적인 정보만 제공

---

## 🚀 목표 (v3.0)

### 연사 뒷조사의 목표
학회 참가자가 알고 싶은 것:
1. **이 사람이 해당 분야에서 얼마나 중요한가?** (centrality)
2. **어떤 특정 기여를 했는가?** (contribution type)
3. **누구와 협력하는가?** (collaboration network)
4. **연구 궤적은 어떤가?** (trajectory)
5. **왜 이 발표를 들어야 하는가?** (significance)

### 새로운 연사 분석 깊이
```python
# v3.0: 연구 landscape 분석
OpenAlex + Citation Network + Review Paper Analysis
→ h-index, citation count, impact factor
→ Citation network centrality (PageRank, betweenness)
→ Co-author network (key collaborators)
→ Research trajectory (topic evolution)
→ Review paper authorship (synthesis capability)
→ Field positioning (niche vs mainstream)
```

**결과**: 연구 생태계에서의 정확한 위치와 영향력 파악

---

## 🔧 기술 인프라 (재사용 가능!)

### KoreanClimateDiseaseSpecify에서 검증된 컴포넌트

#### 1. OpenAlex API Client
**위치**: `/home/kyuwon/projects/KoreanClimateDiseaseSpecify/src/services/openalex_citation_client.py`

**기능**:
- OpenAlex API 호출 (polite pool: 10 req/sec)
- Exponential backoff retry
- Rate limiting (adaptive)
- Response caching

**활용**:
```python
# 연사 이름 → OpenAlex author ID → works
client = OpenAlexClient(email="your@email.com")
author_data = client.fetch_author("Sung Jae Shin")
works = client.fetch_author_works(author_id)

# 결과:
# - h-index
# - citation count
# - top-cited papers
# - recent works
# - co-authors
```

#### 2. Citation Network Builder
**위치**: `/home/kyuwon/projects/KoreanClimateDiseaseSpecify/src/services/citation_network_builder.py`

**기능**:
- Seed papers → citation network (2-hop)
- Referenced works (outgoing citations)
- Citing papers (incoming citations)
- Network metrics (PageRank, betweenness, clustering)

**활용**:
```python
# 연사의 주요 논문 → citation network
builder = CitationNetworkBuilder(cache=cache)
network = builder.build_network(speaker_papers)

# 결과:
# - Citation graph (directed)
# - Centrality scores
# - Key influential papers
# - Citation patterns
```

#### 3. OpenAlex Cache
**위치**: `/home/kyuwon/projects/KoreanClimateDiseaseSpecify/src/utils/openalex_cache.py`

**기능**:
- SQLite-based cache
- API 응답 저장 (중복 방지)
- Timestamp tracking
- Cache hit/miss stats

**활용**:
- 동일 학회/연사 재분석 시 API 호출 감소
- 빠른 응답 (cache hit 시)

---

## 📋 구현 계획

### Phase 1: 기본 OpenAlex 통합 (Quick Win)

**목표**: 연사당 기본 메트릭 추가

**구현**:
```python
# conference-advisor/src/speaker_analyzer.py (NEW)
from openalex_client import OpenAlexClient

class SpeakerAnalyzer:
    def analyze_speaker(self, name: str, affiliation: str):
        """Fetch basic OpenAlex metrics."""
        author = self.client.search_author(name, affiliation)

        return {
            "h_index": author["summary_stats"]["h_index"],
            "citation_count": author["cited_by_count"],
            "works_count": author["works_count"],
            "top_concepts": author["x_concepts"][:5],
            "recent_works": self._fetch_recent(author["id"], limit=5)
        }
```

**배경 자료 변화**:
```markdown
# BEFORE (v2.0)
### 연사: Sung Jae Shin (Yonsei University)
- 전공: Mycobacterial pathogenesis
- 최근 연구: MTB vs NTM 차이

# AFTER (v3.0)
### 연사: Sung Jae Shin (Yonsei University)

**연구 영향력**:
- h-index: 45
- Total citations: 8,234
- Works: 156 papers

**최근 5년 주요 논문**:
1. "Mtb vs MAC pathogenesis..." (2023, 234 citations)
2. "ESX-1 system role..." (2022, 189 citations)
...

**연구 주제**:
- Mycobacterium tuberculosis (relevance: 92%)
- Innate immunity (relevance: 78%)
- Vaccine development (relevance: 65%)
```

**개발 시간**: 1-2 days

---

### Phase 2: Citation Network 분석 (Medium)

**목표**: 연사의 네트워크 중심성 분석

**구현**:
```python
# conference-advisor/src/network_analyzer.py (NEW)
class NetworkAnalyzer:
    def analyze_speaker_network(self, author_id: str):
        """Build citation network around speaker's works."""
        # 1. Fetch speaker's top 10 papers
        papers = self.fetch_top_papers(author_id, limit=10)

        # 2. Build citation network (1-hop)
        network = self.builder.build_network(papers, hops=1)

        # 3. Calculate centrality metrics
        metrics = {
            "pagerank": network.pagerank(author_papers),
            "betweenness": network.betweenness(author_papers),
            "clustering": network.clustering(author_papers)
        }

        # 4. Identify key papers (bridges)
        bridges = network.find_bridges(author_papers)

        return metrics, bridges
```

**배경 자료 변화**:
```markdown
**네트워크 분석**:
- PageRank: 0.0234 (상위 5% in mycobacterial research)
- Betweenness: 0.12 (연구 분야를 연결하는 bridge 역할)
- 주요 bridge papers:
  - "ESX-1 system..." → Connects tuberculosis & innate immunity

**협력 네트워크**:
- 주요 공동 연구자:
  1. Eun-Kyeong Jo (Chungnam National) - 23 papers
  2. John Chan (Albert Einstein) - 15 papers
  3. ... (자동으로 같은 학회 참석자 하이라이트!)
```

**개발 시간**: 3-5 days

---

### Phase 3: Review Paper & Synthesis Analysis (Advanced)

**목표**: 연사의 종합 능력 평가 (리뷰 논문 저자 여부)

**구현**:
```python
# conference-advisor/src/review_analyzer.py (NEW)
class ReviewAnalyzer:
    def analyze_review_contributions(self, author_id: str):
        """Identify review papers and synthesis capability."""
        works = self.fetch_author_works(author_id)

        # Filter review papers (type='review')
        reviews = [w for w in works if w['type'] == 'review']

        # Calculate synthesis metrics
        metrics = {
            "review_count": len(reviews),
            "review_citation_avg": mean([r['cited_by_count'] for r in reviews]),
            "influential_reviews": [r for r in reviews if r['cited_by_count'] > 100],
            "topics_synthesized": self._extract_topics(reviews)
        }

        return metrics, reviews
```

**배경 자료 변화**:
```markdown
**종합 능력 (Synthesis)**:
- 리뷰 논문: 8편 (총 156편 중 5%)
- 평균 인용: 287회 (일반 논문의 3.2배)
- 주요 리뷰:
  1. "Mycobacterial pathogenesis: a comprehensive review" (2021, 567 citations)
     → 분야 전체를 조망하는 능력 입증

**추천 이유**:
- ✅ 단순 실험가가 아닌 **분야 전체를 이해하는 연구자**
- ✅ 리뷰 논문 저자 = 발표에서 **큰 그림**을 기대 가능
- ✅ 교육적 가치 높음 (특히 포닥/학생)
```

**개발 시간**: 2-3 days

---

### Phase 4: Field Positioning & Trajectory (Expert)

**목표**: 연구 궤적과 분야 내 포지션 분석

**구현**:
```python
# conference-advisor/src/trajectory_analyzer.py (NEW)
class TrajectoryAnalyzer:
    def analyze_research_trajectory(self, author_id: str):
        """Track research evolution over time."""
        works = self.fetch_author_works(author_id, sort="publication_date")

        # Group by 5-year periods
        periods = self._group_by_period(works, period=5)

        # Extract topic evolution
        trajectory = []
        for period, papers in periods:
            topics = self._extract_topics(papers)
            trajectory.append({
                "period": period,
                "topics": topics,
                "citation_avg": mean([p['cited_by_count'] for p in papers]),
                "impact_trend": self._calculate_trend(papers)
            })

        # Identify shifts (e.g., basic → translational)
        shifts = self._detect_shifts(trajectory)

        return trajectory, shifts
```

**배경 자료 변화**:
```markdown
**연구 궤적**:

**2015-2020: 기초 면역학**
- 주제: MTB pathogenesis, innate immunity
- 평균 인용: 124회
- 주요 발견: ESX-1 system role

**2020-2025: 응용 및 백신 개발**
- 주제: Vaccine development, drug targets
- 평균 인용: 287회 (2.3배 증가!)
- 주요 전환: Basic → Translational

**포지션 분석**:
- Niche vs Mainstream: **Mainstream with niche expertise**
- Basic vs Applied: **Both (균형 잡힌 연구자)**
- Trend: **상승세** (최근 5년 인용 증가)

**발표 예상**:
- 기초 메커니즘 + 응용 가능성 **모두** 다룰 것으로 예상
- 특히 **백신 개발** 파트 주목 (최근 전환점)
```

**개발 시간**: 5-7 days

---

## 🎯 최종 결과물 (v3.0)

### 기존 배경 자료 (v2.0) vs 업그레이드 (v3.0)

**v2.0 배경 자료** (현재):
```markdown
### Session 2 - Speaker 1: Sung Jae Shin

**소속**: Yonsei University
**발표 제목**: Mtb vs MAC pathogenesis

**최근 연구** (WebSearch):
- MTB와 NTM의 병원성 차이 연구
- 2023년 Nature Microbiology 논문 발표
- 면역 회피 메커니즘 전문가

(500 단어)
```

**v3.0 배경 자료** (업그레이드):
```markdown
### Session 2 - Speaker 1: Sung Jae Shin

#### 📊 연구 영향력 (OpenAlex)
- **h-index**: 45 (mycobacterial research 상위 5%)
- **Total citations**: 8,234
- **Works**: 156 papers (1997-2025)
- **Career stage**: Senior investigator (28년 경력)

#### 🌟 주요 기여 (Top-Cited Papers)
1. "ESX-1 system in MTB pathogenesis" (2018, 567 citations)
   → **분야 표준 논문** (highly influential)
2. "MTB vs NTM immune evasion" (2023, 234 citations)
   → **오늘 발표 주제!** (최신 연구)

#### 🔗 네트워크 분석 (Citation Network)
- **PageRank**: 0.0234 (상위 5%)
- **Betweenness**: 0.12 → **Bridge researcher**
  - Connects: Tuberculosis ↔ Innate immunity
  - Key paper: "ESX-1 system..." (567 citations)

#### 👥 협력 네트워크
- **Eun-Kyeong Jo** (Chungnam National) - 23 papers
  → ⚠️ **같은 학회 참석!** (Session 3 발표자)
  → 네트워킹 전략: 두 발표 연결해서 질문 준비
- John Chan (Albert Einstein) - 15 papers
- Clifton Barry (NIAID) - 12 papers

#### 📖 종합 능력 (Review Papers)
- **리뷰 논문**: 8편 (5% of total works)
- **평균 인용**: 287회 (일반 논문의 3.2배)
- **주요 리뷰**:
  - "Mycobacterial pathogenesis: comprehensive review" (2021, 567 citations)

**→ 의미**: 단순 실험가가 아닌 **분야 전체를 이해하는 연구자**
**→ 발표 기대치**: 큰 그림 + 최신 발견 **모두** 커버할 것

#### 📈 연구 궤적 (Trajectory)
**2015-2020**: 기초 면역학 (ESX-1, innate immunity)
**2020-2025**: 응용/백신 개발 (translational shift)

**트렌드**: **상승세** (최근 5년 인용 2.3배 증가)
**포지션**: Mainstream with niche expertise

#### 💡 왜 이 발표를 들어야 하는가?

1. **분야 Top 5% 연구자** (h-index 45)
2. **Bridge 역할** → 다양한 관점 제공
3. **리뷰 저자** → 교육적 가치 높음
4. **최신 전환점** → 백신 개발 인사이트
5. **같은 학회 협력자** → 네트워킹 기회 (Eun-Kyeong Jo)

#### 🎤 질문 제안 (Network-Informed)

**과학적** (협력자 연구 기반):
1. "Eun-Kyeong Jo 교수님의 autophagy 연구와 선생님의 ESX-1 연구를 어떻게 연결할 수 있을까요?"
   → 두 발표자 bridge 질문 (네트워킹!)

**기술적** (최신 논문 기반):
2. "2023 Nature Microbiology 논문에서 MTB와 MAC의 immune evasion 차이를..."

**응용** (trajectory 기반):
3. "최근 백신 개발로 전환하셨는데, 기초 연구에서 얻은 어떤 인사이트가 translational application에...?"

(2000 단어)
```

---

## 📦 구현 아키텍처

### 디렉토리 구조

```
.claude/skills/conference-advisor/
├── SKILL.md                              # v3.0 업데이트
├── comprehensive_background_template.md  # v3.0 섹션 추가
│
├── src/                                  # NEW!
│   ├── openalex_client.py               # OpenAlex API (from KoreanClimate)
│   ├── citation_network_builder.py      # Network builder (from KoreanClimate)
│   ├── openalex_cache.py                # SQLite cache (from KoreanClimate)
│   │
│   ├── speaker_analyzer.py              # NEW: Phase 1
│   ├── network_analyzer.py              # NEW: Phase 2
│   ├── review_analyzer.py               # NEW: Phase 3
│   └── trajectory_analyzer.py           # NEW: Phase 4
│
├── templates/
│   └── speaker_profile_template.md      # NEW: v3.0 연사 프로필
│
└── configs/
    └── openalex_config.yml              # NEW: API settings
```

### 데이터 흐름

```
User: /conference-advisor
  ↓
1. Conference Selection (MSK2025, IAMRT2025, ...)
  ↓
2. Read conference materials (PDF, abstracts)
  ↓
3. Extract speakers + talks
  ↓
4. [NEW] For each speaker:
   │
   ├→ OpenAlex Author Search
   │  ├→ Fetch h-index, citations, works
   │  └→ Cache results
   │
   ├→ Citation Network Builder
   │  ├→ Fetch top 10 papers
   │  ├→ Build 1-hop network
   │  ├→ Calculate centrality metrics
   │  └→ Cache network
   │
   ├→ Review Paper Analyzer
   │  ├→ Filter review-type works
   │  ├→ Calculate synthesis metrics
   │  └→ Rank influential reviews
   │
   └→ Trajectory Analyzer
      ├→ Group works by period
      ├→ Extract topic evolution
      └→ Detect research shifts
  ↓
5. Generate comprehensive background
   ├→ Basic info (v2.0)
   ├→ OpenAlex metrics (NEW)
   ├→ Network analysis (NEW)
   ├→ Review contributions (NEW)
   ├→ Trajectory (NEW)
   └→ Network-informed questions (NEW)
  ↓
6. Output: Enhanced background file (1500-2500 lines)
```

---

## 🔄 마이그레이션 계획

### Step 1: Code Extraction (KoreanClimate → Conference-Advisor)

```bash
# Copy reusable components
cp /home/kyuwon/projects/KoreanClimateDiseaseSpecify/src/services/openalex_citation_client.py \
   .claude/skills/conference-advisor/src/openalex_client.py

cp /home/kyuwon/projects/KoreanClimateDiseaseSpecify/src/services/citation_network_builder.py \
   .claude/skills/conference-advisor/src/citation_network_builder.py

cp /home/kyuwon/projects/KoreanClimateDiseaseSpecify/src/utils/openalex_cache.py \
   .claude/skills/conference-advisor/src/openalex_cache.py
```

**수정 필요**:
- Import paths 업데이트
- Conference 도메인에 맞게 조정
- Email config externalize

### Step 2: New Analyzers 개발

```python
# Phase 1: speaker_analyzer.py (1-2 days)
# Phase 2: network_analyzer.py (3-5 days)
# Phase 3: review_analyzer.py (2-3 days)
# Phase 4: trajectory_analyzer.py (5-7 days)
```

### Step 3: Template 업데이트

```markdown
# comprehensive_background_template.md 추가 섹션

## 🔬 연사 상세 분석 (NEW in v3.0)

### [SPEAKER_NAME]

#### 📊 연구 영향력
- h-index: [H_INDEX]
- Citations: [TOTAL_CITATIONS]
- Works: [WORKS_COUNT]

#### 🌟 주요 기여
[TOP_PAPERS with citations]

#### 🔗 네트워크 분석
- PageRank: [SCORE]
- Betweenness: [SCORE]
- Bridge papers: [LIST]

#### 👥 협력 네트워크
[CO_AUTHORS]
⚠️ 같은 학회 참석자 하이라이트!

#### 📖 종합 능력
- Review papers: [COUNT]
- Synthesis score: [SCORE]

#### 📈 연구 궤적
[TRAJECTORY by period]

#### 💡 발표 추천 이유
[NETWORK-INFORMED reasons]

#### 🎤 네트워크 기반 질문
[QUESTIONS leveraging collaborations]
```

### Step 4: SKILL.md 업데이트

```markdown
# v3.0 Features

## New Tools Required
- OpenAlexClient (API calls)
- CitationNetworkBuilder (network analysis)
- SpeakerAnalyzer (Phase 1-4)

## New Data Sources
- OpenAlex API (https://api.openalex.org)
- Citation networks (2-hop)
- Review paper metadata

## Output Enhancements
- Speaker profiles: +800 words per speaker
- Network visualizations (optional)
- Collaboration highlights
- Trajectory charts (optional)
```

---

## 📊 예상 개선 효과

### 정량적 개선

| 메트릭 | v2.0 (현재) | v3.0 (목표) | 개선 |
|--------|------------|------------|------|
| 연사당 정보량 | 500 단어 | 2000 단어 | **4배** |
| 정량적 메트릭 | 0개 | 10+ | **신규** |
| 네트워크 인사이트 | 없음 | 협력자, 중심성 | **신규** |
| 질문 품질 | 일반적 | Network-informed | **고급** |
| 네트워킹 전략 | 기본 | 협력자 하이라이트 | **구체적** |

### 정성적 개선

**v2.0 사용자 경험**:
> "이 연사가 유명한 것 같은데, 왜 유명한지 잘 모르겠어요."

**v3.0 사용자 경험**:
> "h-index 45로 상위 5%네요! PageRank도 높고, Eun-Kyeong Jo와 협력 관계라서 두 발표를 연결해서 들어야겠어요. 리뷰 논문도 많이 써서 발표에서 큰 그림을 기대할 수 있겠네요!"

**학습 효과**:
- ✅ 연구 생태계 이해 증가
- ✅ 네트워킹 전략 구체화
- ✅ 질문 품질 향상
- ✅ 발표 선택 근거 명확

---

## ⚠️ 고려사항

### 1. API Rate Limits

**OpenAlex**:
- Anonymous: 10 req/sec (max)
- Polite pool (with email): 10 req/sec (recommended)
- 학회당 평균 연사: 50-100명
- API 호출: ~500-1000 (speaker + papers + network)
- 예상 시간: **5-10 minutes per conference**

**해결책**:
- Cache 활용 (SQLite)
- Batch processing
- 진행 상황 표시

### 2. 데이터 품질

**OpenAlex 한계**:
- 한국 연구자 coverage: ~80% (일부 누락)
- Author disambiguation 이슈 (동명이인)
- 최신 논문 반영 시차 (~1주)

**해결책**:
- Fallback to WebSearch (OpenAlex 없을 시)
- Affiliation matching으로 disambiguation
- 캐시 업데이트 주기 설정

### 3. 실행 시간

**v2.0**: ~30 seconds (WebSearch만)
**v3.0**: ~5-10 minutes (OpenAlex + Network)

**해결책**:
- 진행 상황 표시 (`tqdm` 스타일)
- 병렬 처리 (concurrent.futures)
- 선택적 분석 (빠른 모드 / 상세 모드)

### 4. 저장 공간

**Cache 크기**:
- OpenAlex responses: ~1-5 MB per conference
- Citation networks: ~10-50 MB per conference
- SQLite DB: ~100 MB (10개 학회)

**해결책**:
- Cache expiry (90일)
- Compression (gzip)
- Cleanup script

---

## 🎓 사용 시나리오

### Scenario 1: 포닥 연구자 (바이오인포)

**Before (v2.0)**:
```
User: IAMRT2025 준비, 바이오인포 관심
Skill: WebSearch → 일반적인 세션 추천
User: "Wonsik Lee가 누구지? Tn-seq가 뭐지?"
```

**After (v3.0)**:
```
User: IAMRT2025 준비, 바이오인포 관심
Skill:
  - OpenAlex 분석 → Wonsik Lee (h-index 32, Tn-seq expert)
  - Citation network → Hyunjung Lee와 협력 (ML/AI)
  - Recommendation: "두 연사 모두 참석! 네트워크 효과 극대화"

User: "아! Wonsik Lee는 Tn-seq 권위자고 (h-index 32),
      Hyunjung Lee와 협력해서 ML/AI 연구도 하는구나!
      두 발표 연결해서 질문 준비해야겠다!"
```

### Scenario 2: PI (그룹 리더)

**Before (v2.0)**:
```
User: MSK2025, microbiome 관심
Skill: WebSearch → 일반적인 세션 리스트
User: "누가 중요한 사람인지 모르겠어..."
```

**After (v3.0)**:
```
User: MSK2025, microbiome 관심
Skill:
  - Network 분석 → Top 3 central researchers identified
  - Review papers → Synthesis leaders highlighted
  - Trajectory → Emerging vs established

User: "아! KoBioLabs CEO는 h-index 38로 업계 리더고,
      리뷰 논문도 많아서 산업 동향 파악에 최적이네!
      반면 X 교수는 최근 급상승 중이라 최신 기술 배울 수 있겠다!"
```

---

## 🚀 출시 계획

### MVP (Minimum Viable Product)

**목표**: Phase 1만 구현 (빠른 출시)

**기능**:
- OpenAlex basic metrics (h-index, citations, works)
- Top papers (5개)
- Research topics

**개발 시간**: **1-2 days**

**가치**:
- 즉시 개선 (정량적 메트릭 추가)
- 인프라 검증
- 사용자 피드백 수집

### v3.0 Full (Complete)

**목표**: Phase 1-4 모두 구현

**기능**:
- OpenAlex metrics
- Citation network analysis
- Review paper contributions
- Research trajectory
- Network-informed questions

**개발 시간**: **2-3 weeks**

**가치**:
- 완전한 연구 landscape 분석
- 네트워킹 전략 극대화
- 교육적 가치 극대화

---

## 📞 다음 단계

### 1. 사용자 피드백
- v2.0 사용자에게 v3.0 계획 공유
- 우선순위 확인 (Phase 1 vs Full)

### 2. 인프라 준비
- OpenAlex API key (email 등록)
- SQLite cache 설정
- KoreanClimate 코드 extract

### 3. 개발 시작
- MVP (Phase 1) 먼저
- 피드백 반영
- Phase 2-4 순차 개발

### 4. 문서화
- TEAM_DEPLOYMENT_GUIDE 업데이트
- v3.0 features 설명
- OpenAlex 사용법 추가

---

## 💡 추가 아이디어

### Future Enhancements (v4.0?)

1. **시각화**:
   - Citation network graph (Gephi/NetworkX)
   - Trajectory timeline
   - Co-author network

2. **AI 요약**:
   - Top papers 자동 요약 (Claude API)
   - Research trajectory narrative

3. **실시간 업데이트**:
   - OpenAlex webhook (새 논문 알림)
   - Citation count tracking

4. **협력 추천**:
   - "Your research + Speaker X → Collaboration opportunity"
   - Common interests detection

5. **학회 간 비교**:
   - "MSK2025 vs IAMRT2025 speaker quality"
   - Network overlap analysis

---

**Version**: 3.0 (Proposed)
**Author**: Conference-Advisor Development Team
**Date**: 2025-11-07
**Status**: Design Phase (Ready for Implementation)

**Estimated Development**:
- MVP (Phase 1): 1-2 days
- Full (Phase 1-4): 2-3 weeks

**Expected Impact**:
- Information quality: **4x improvement**
- Networking value: **10x improvement**
- Educational value: **Significant increase**

**Ready to proceed?** 🚀
