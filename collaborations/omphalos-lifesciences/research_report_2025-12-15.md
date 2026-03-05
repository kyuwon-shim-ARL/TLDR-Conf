# Omphalos Lifesciences 협업 미팅 사전 조사 보고서

> **작성일:** 2025-12-15
> **관련 미팅:** Paratus Non-Dilutive Funding Project DEV Discussion
> **원본 자료:** `data/raw/Project Evaluation Meeting.pdf`

---

## 1. 회사 개요

| 항목 | 내용 |
|------|------|
| **회사명** | Omphalos Lifesciences Inc. |
| **설립** | 2021년 |
| **본사** | Dallas, Texas, USA |
| **펀딩 단계** | Series A (금액 미공개) |
| **웹사이트** | [omphaloslifesci.com](https://omphaloslifesci.com/) |
| **사업 분야** | 생물학 시뮬레이션 플랫폼, Virtual Cell 기술 |

---

## 2. 경영진 배경 검증

### Daehwan Kim, Ph.D. (Founder, Co-CEO, CTO)

| 항목 | 내용 | 검증 결과 |
|------|------|-----------|
| **학력** | University of Maryland - CS Ph.D. | **검증됨** |
| **경력** | Johns Hopkins Postdoc → UT Southwestern 조교수 | **검증됨** |
| **인용수** | 66,000+ (PDF 기재) → **실제 69,000+** | **검증됨 (더 높음)** |
| **대표 업적** | HISAT, HISAT2, TopHat2 개발 | **검증됨** |

**핵심 논문 (인용수 기준):**
- HISAT2 (Nature Biotechnology, 2019): **7,862 인용**
- HISAT/StringTie/Ballgown (Nature Protocols, 2016): **4,863 인용**

**평가:** 세계적 수준의 생물정보학자. HISAT는 RNA-seq 분석의 업계 표준 도구로, 학계에서의 신뢰도 매우 높음.

---

### Donghoon Lee, Ph.D. (Co-Founder, Co-CEO, CSO)

| 항목 | 내용 | 검증 결과 |
|------|------|-----------|
| **학력** | University of Toronto - Cell & Systems Biology Ph.D. | **검증됨** |
| **경력** | Johns Hopkins Postdoc (Elizabeth Chen Lab) → UT Southwestern Instructor | **검증됨** |
| **연구분야** | 세포융합 메커니즘, 발생생물학 | **검증됨** |

**평가:** 실험 생물학자 배경. 계산 전문가인 Daehwan Kim과 상호보완적 팀 구성.

---

## 3. 핵심 기술 - 쉬운말 풀이

### L++ (Life Programming Language)

**한 줄 설명:**
> "생물학을 코딩하는 프로그래밍 언어"

**쉬운 비유:**
```
C++이 컴퓨터 프로그램을 만드는 언어라면,
L++는 가상의 세포/생물체를 만드는 언어
```

**특징:**

| 기능 | 설명 |
|------|------|
| 생물학 문법 | 화학반응, 단백질, 유전자를 코드로 표현 |
| 단위 지원 | uM, nM, mg/L 등 생물학 단위 자동 처리 |
| SMILES 지원 | 화학구조식을 코드에 직접 입력 가능 |
| 다중 스케일 | 분자 → 세포 → 조직 → 개체 수준까지 모델링 |

**코드 예시 (PDF 7페이지):**
```cpp
protein AACT(2 acetyl-CoA -> acetoacetyl-CoA + CoA, k = 1)
// 두 개의 acetyl-CoA가 반응해서 acetoacetyl-CoA를 만든다
```

---

### Virtual Cell (가상 세포)

**한 줄 설명:**
> "컴퓨터 안에서 작동하는 디지털 세포"

**왜 중요한가:**
```
기존: 신약 → 세포실험 → 동물실험 → 임상 (비용/시간 많음)
미래: 신약 → 가상세포 시뮬레이션 → 검증된 후보만 실험 (비용/시간 절감)
```

**Omphalos 주장 vs 경쟁사:**

| 회사/기관 | 접근법 | 모델 크기 | 특징 |
|-----------|--------|-----------|------|
| **Omphalos** | 하이브리드 (규칙+AI) | 200K 파라미터 | 효율적, 해석 가능 |
| CZI/NVIDIA | 순수 AI | 수십억 파라미터 | 데이터 의존적 |
| Stanford (Karr) | 순수 규칙 기반 | - | 구축 느림 |

---

## 4. 프로젝트 분석: Virtual *A. baumannii*

### 타겟 병원체 배경

**Acinetobacter baumannii:**
- WHO **"Critical Priority" 1순위** 병원체
- CDC **"Urgent Threat"** 지정
- 병원 내 감염의 주요 원인균
- **다제내성(MDR)** 균주 급증으로 치료 옵션 제한

**왜 이 균을 선택했나:**
1. 임상적 긴급성 (BARDA 우선순위와 일치)
2. 풍부한 공개 데이터 (multi-omics, GEM 모델)
3. E. coli와 유사점 많아 모델 확장 용이

---

### 프로젝트 예산 분석 (PDF 13페이지)

| 항목 | 금액 | 비율 |
|------|------|------|
| 병원체 모델 개발 | $32,000 | 80% |
| 프로젝트 관리 | $2,000 | 5% |
| 데이터 통합 | $2,000 | 5% |
| 검증/벤치마킹 | $1,600 | 4% |
| 문서화 | $800 | 2% |
| 운영비 | $1,600 | 4% |
| **총계** | **$40,000** | 100% |

**평가:**
- 96% 직접 인건비 → 초기 스타트업의 린(lean) 운영
- 6주 / 3개 마일스톤 → 빠른 프로토타이핑 목표
- $40K는 작은 규모지만, **비희석(non-dilutive) 펀딩**으로 가치 있음

---

## 5. 경쟁 환경 분석

### Virtual Cell 분야 주요 플레이어

| 기관 | 펀딩/자원 | 접근법 | 현황 |
|------|-----------|--------|------|
| **CZI + NVIDIA** | 수십억 달러 | 순수 AI, 대규모 데이터 | 2025.10 협력 확대, VCP 플랫폼 공개 |
| **DeepMind** | 무제한 | AlphaFold 확장 | 단백질 구조 중심 |
| **Stanford (Covert Lab)** | 학술 | 규칙 기반 | M. genitalium 최초 whole-cell model |
| **Omphalos** | Series A + BARDA | 하이브리드 | E. coli 모델 완성, A. baumannii 착수 |

**Omphalos의 차별점:**
1. **효율성:** 200K vs 20B 파라미터 (100,000배 적음)
2. **해석가능성:** 블랙박스 AI가 아닌 메커니즘 기반
3. **실용성:** 병원체 + 항생제 시뮬레이션 특화

**리스크:**
- CZI/NVIDIA의 자원 규모 압도적
- 학술 검증 논문 부재 (공개된 peer-reviewed 논문 없음)

---

## 6. BARDA/Paratus 프로그램

### 프로그램 개요

| 항목 | 내용 |
|------|------|
| **운영기관** | MATTER (시카고 기반 헬스케어 액셀러레이터) |
| **자금원** | BARDA (미국 보건복지부 산하) |
| **목적** | 보건안보 위협 대응 디지털 헬스 솔루션 |
| **펀딩 범위** | $50,000 ~ $200,000 (일반) / 최대 $2M (TBI) |

### Omphalos 선정 (2025.12.11 발표)

- **의미:** 미국 정부 기관의 기술 검증
- **조건:** Non-dilutive (지분 희석 없음)
- **목표:** 2026년 Q1 프로토타입 배포

---

## 7. 객관적 연구 수준 평가

### 강점

| 항목 | 평가 |
|------|------|
| 창업자 학술 역량 | **상** (HISAT 69K 인용, 세계적 수준) |
| 기술 차별성 | **중상** (하이브리드 접근법 독창적) |
| 시장 타이밍 | **상** (Virtual Cell, AMR 모두 핫토픽) |
| 정부 인증 | **중상** (BARDA 선정) |

### 약점/불확실성

| 항목 | 우려사항 |
|------|----------|
| 학술 검증 | Peer-reviewed 논문 미발표 |
| 펀딩 규모 | Series A 금액 미공개, 경쟁사 대비 작을 가능성 |
| 팀 규모 | 2인 창업자 중심, 확장성 불명확 |
| E. coli 검증 | 실제 실험 데이터와 비교한 벤치마크 제한적 |

---

## 8. 미팅 시 확인해볼 질문들

### 기술 관련
1. L++ 코드의 공개 계획 (오픈소스 여부)?
2. E. coli 모델의 실험적 검증 데이터는?
3. 기존 GEM(Genome-scale metabolic model)과의 비교 결과?

### 비즈니스 관련
4. Series A 펀딩 규모 및 런웨이?
5. 현재 팀 규모 및 채용 계획?
6. 제약사/연구기관 파트너십 현황?

### 협업 관련
7. 어떤 형태의 협업을 원하는가? (데이터? 검증? 공동연구?)
8. A. baumannii 외에 관심 있는 병원체?

---

## 9. 핵심 용어 정리

| 용어 | 쉬운 설명 |
|------|-----------|
| **Virtual Cell** | 컴퓨터 안에서 실제 세포처럼 작동하는 시뮬레이션 |
| **L++** | 생물학을 코딩하기 위해 만든 새로운 프로그래밍 언어 |
| **Whole-cell model** | 세포의 모든 유전자와 반응을 포함한 완전한 모델 |
| **GEM** | 세포의 대사반응만 모델링한 것 (whole-cell보다 단순) |
| **MDR** | Multi-Drug Resistant, 여러 항생제에 내성인 균 |
| **ESKAPE** | 병원 내 위험 내성균 6종의 약자 |
| **Non-dilutive funding** | 지분을 주지 않고 받는 펀딩 (보조금) |
| **In silico** | 컴퓨터 시뮬레이션으로 (in vitro=시험관, in vivo=생체) |

---

## 10. 요약 (Executive Summary)

**Omphalos Lifesciences**는 2021년 Dallas에서 설립된 바이오테크 스타트업으로, 세계적 생물정보학자 **Daehwan Kim** (HISAT 개발자, 69K 인용)과 실험생물학자 **Donghoon Lee**가 공동 창업했습니다.

**핵심 기술**인 **L++**는 생물학 시뮬레이션을 위한 독자 프로그래밍 언어로, CZI/NVIDIA의 순수 AI 접근법과 달리 **규칙+AI 하이브리드** 방식을 채택하여 효율성과 해석가능성을 강조합니다.

2025년 12월 **BARDA/Paratus 프로그램 선정**으로 미국 정부의 기술 검증을 받았으며, WHO 1순위 위험 병원체인 **A. baumannii**의 whole-cell model 개발에 착수했습니다.

**주의점:** 창업자의 학술 역량은 검증되었으나, L++ 및 Virtual Cell 기술 자체의 peer-reviewed 논문은 아직 없으며, 경쟁사(CZI/NVIDIA) 대비 자원 규모가 작습니다. 협업 시 기술의 실제 성숙도와 검증 데이터를 확인하는 것이 중요합니다.

---

## References

- [Omphalos Lifesciences 공식 웹사이트](https://omphaloslifesci.com/)
- [BARDA 지원 발표 (2025.12.11)](https://omphaloslifesci.com/2025/12/11/omphalos-secures-barda-support-for-pathogen-agnostic-antimicrobial-strategy-simulation/)
- [Daehwan Kim Google Scholar](https://scholar.google.com/citations?user=RotyhxEAAAAJ&hl=en)
- [CZI-NVIDIA Virtual Cell 협력](https://chanzuckerberg.com/newsroom/nvidia-partnership-virtual-cell-model/)
- [MATTER Paratus 프로그램](https://matter.health/paratus/)
- [CDC Acinetobacter 정보](https://www.cdc.gov/acinetobacter/about/index.html)
- [WHO Priority Pathogens](https://www.who.int/news/item/27-02-2017-who-publishes-list-of-bacteria-for-which-new-antibiotics-are-urgently-needed)
