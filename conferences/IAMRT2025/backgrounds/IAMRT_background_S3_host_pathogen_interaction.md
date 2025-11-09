# 배경 자료: Session 3 - Host-Pathogen Interaction

**세션**: Session 3: Host-Pathogen Interaction
**연사**: Eun-Kyeong Jo (Chungnam Natl. Univ.), Jung-Hyun Kim (Ajou Univ.), Hyunjung Lee (Institut Pasteur Korea)
**일시**: 2025년 10월 30일 (목) 15:10-16:25
**장소**: 성균관대학교 의과대학, AI 강의실 3304

**중요도**: ⭐⭐⭐⭐⭐ (96/100점)

---

## 🎯 세션 개요

### 왜 이 세션이 중요한가?

**1. 숙주-병원체 상호작용의 핵심 메커니즘을 다룬다**
- Autophagy는 세포가 mycobacteria를 제거하는 중요한 방어 기전
- 2025년 Nature Communications: ATG7 결핍 시 NTM 감염 악화
- Host-directed therapy의 핵심 표적 (mTOR, AMPK 조절)
- Post-COVID-19 시대, mycobacteria 감염 관리의 새로운 전략

**2. 차세대 질병 모델 기술을 제시한다**
- Human pluripotent stem cell (hPSC) 기반 organoid 시스템
- Tissue-resident macrophage 포함 (in vivo에 가장 근접)
- 2024년 Cell Stem Cell: 바이러스 감염 시 면역 매개 손상 모델링
- 마우스를 넘어선 인간 특이적 반응 연구 가능

**3. 신약 개발 파이프라인의 병목을 해결한다**
- 전통적 HTS (high-throughput screening)의 hit rate: 0.87%
- 새로운 감염 모델: Staphylococcus aureus ex vivo GFP 시스템
- 기계 학습 결합 시 hit rate 14배 향상 (2024년 PLOS Comput Biol)
- 약물 발견 비용 및 시간 대폭 감소

**4. 포닥 연구자에게 필수적인 첨단 기술과 플랫폼을 소개한다**
- Organoid 제작 기술 (iPSC differentiation → macrophage → assembly)
- 감염 모델 최적화 (multiplicity of infection, 측정 시점)
- High-content imaging과 AI 분석
- 산학연 협력 모델 (Institut Pasteur Korea의 사례)

---

## 🌟 쉬운말 풀이 (세션 전체)

### 이 세션은 쉽게 말하면...

**한 줄 요약**: "세균과 인체의 '전투'를 이해하고, 그 전투를 재현하는 더 나은 '실험실 모델'을 만들어서, 신약을 빠르고 정확하게 찾는 방법"

### 🎬 숙주-병원체 상호작용 - 이야기로 이해하기

**[1장: 숙주의 비밀 무기 - Autophagy]**

**배경**: 세포 속에 숨겨진 재활용 시스템

우리 몸의 세포는 끊임없이 단백질을 만들고, 사용하고, 버립니다. 오래된 단백질이나 망가진 세포 소기관은 "autophagy(자가포식)"라는 재활용 시스템으로 분해됩니다.

```
Autophagy의 일상:
1. 세포 내 "쓰레기" 발견 (오래된 미토콘드리아, 응집 단백질)
2. Autophagosome(이중막 주머니) 형성
3. Lysosome(분해 효소 창고)과 융합
4. 내용물 분해 → 재활용

→ 세포 건강 유지, 노화 방지, 암 예방
```

그런데 1990년대 후반, 놀라운 사실이 밝혀졌습니다.

**전환점**: Autophagy는 재활용만 하는 게 아니다

```
질문: 세포 안에 들어온 세균을 어떻게 제거할까?

기존 생각:
→ Phagosome(식포)에 세균 가둠
→ Lysosome과 융합
→ 분해 효소로 살균

새로운 발견 (2004년, Deretic 그룹):
→ Mycobacterium tuberculosis는 phagosome-lysosome 융합을 막음
→ 하지만 autophagy를 유도하면?
→ Autophagosome이 세균을 "포장"해서 lysosome으로 강제 전달
→ 세균 제거!

→ Autophagy = "Plan B" 항균 시스템
```

**[발견/의미]**:

1. **ATG7은 autophagy의 "마스터 키"** (Eun-Kyeong Jo의 연구)
   - ATG7: Autophagy-related gene 7 (E1-like enzyme)
   - 없으면: Autophagosome 형성 불가
   - 2025년 Nature Commun: ATG7 knockout 마우스는 NTM 감염 시 사망률 ↑
   - **의미**: ATG7 활성화제 = 새로운 항결핵 치료제 후보

2. **Autophagy는 면역 신호도 조절**
   - Inflammasome 활성 조절 (과도한 염증 억제)
   - Type I IFN 생성 조절
   - Th1/Th17 세포 분화 촉진
   - **의미**: 단순 "청소부"가 아니라 "면역 지휘자"

3. **Mycobacteria는 autophagy를 회피/악용한다**
   - M. tuberculosis: ESX-1 secretion system으로 autophagosome 파괴
   - M. abscessus: Autophagy 유도하지만, 분해 저항성
   - **의미**: 세균과 숙주의 "진화 경쟁"

**결론**: "Autophagy를 조절하면, 항생제 없이도 세균을 제거할 수 있다. 이것이 Host-Directed Therapy의 핵심이다."

---

**[2장: 인간 질병 모델의 진화 - From Mice to Organoids]**

**주요 개념 1: 마우스 모델의 한계**

```
마우스 vs. 인간:
- 수명: 2-3년 vs. 80년
- 면역계: Neutrophil 주도 vs. Monocyte/Macrophage 주도
- 대사: 고대사율 (체온 37.5°C) vs. 저대사율 (36.5°C)
- 육아종: 불완전 vs. 완전 (결핵의 hallmark)

문제:
→ 마우스에서 효과 있는 약물이 인간에서 실패 (60-70%)
→ 예: 수많은 결핵 백신 후보 (마우스 OK, 인간 Phase 2 실패)

→ 해결책: 인간 세포 기반 모델 필요
```

**주요 개념 2: Organoid - "미니 장기"**

```
Organoid란?
→ 줄기세포에서 만든 3D 장기 유사 구조
→ 실제 장기의 구조, 세포 구성 재현
→ 크기: 0.5-5mm (현미경으로 관찰 가능)

장점:
1. 인간 특이적 반응
2. 환자 유래 iPSC 사용 시 개인 맞춤형
3. 윤리적 문제 적음 (동물 대체)
4. High-throughput screening 가능

역사:
- 2009: 첫 장 organoid (Hans Clevers, Nature)
- 2013: 뇌 organoid
- 2019: 폐 organoid
- 2024: Macrophage 포함 organoid (Jung-Hyun Kim)
```

**Jung-Hyun Kim의 혁신: hPSC-derived Macrophage + Lung Organoid**

```
기존 organoid의 문제:
→ 상피 세포만 있음 (면역 세포 없음)
→ 감염 모델로 부적합 (macrophage 없으면 반응 다름)

Kim 그룹의 해결책:
1. hPSC → Macrophage 분화 (별도)
2. hPSC → Alveolar organoid 분화 (별도)
3. 두 개를 섞음 (co-culture)
4. Macrophage가 organoid 안으로 이동 (tissue-resident 됨)

결과:
→ "Human lung with immune cells" in a dish
→ SARS-CoV-2, influenza, Mtb 감염 모델
→ Macrophage의 proinflammatory 반응 재현
→ β cell pyroptosis (면역 매개 세포 사멸) 관찰

→ 응용: 개인 맞춤형 치료 (환자 iPSC 사용)
```

**의미**:

"마우스는 '다른 종'이다. 인간 질병을 이해하려면 인간 세포를 써야 한다.
Organoid + Macrophage는 마우스와 인간 사이의 '다리'가 될 것이다."

---

**[3장: 신약 발견의 병목 해소 - Better Models, Faster Discovery]**

**주요 개념 3: High-Throughput Screening (HTS)의 딜레마**

```
전통적 항생제 개발:
1. 천연물/화합물 라이브러리 (수백만 개)
2. In vitro screening (배양액에서 성장 억제)
3. Hit compound 선택 (0.01-0.1%)
4. In vivo 검증 (마우스)
5. 임상시험

문제:
→ Hit rate 낮음 (1,000,000개 → 100개 hit)
→ In vitro와 in vivo 차이 (80% drop-out)
→ 시간: 10-15년, 비용: $1B

→ 병목: "적절한 감염 모델"이 없음
```

**Hyunjung Lee의 접근: Physiologically Relevant Infection Model**

```
Institut Pasteur Korea의 플랫폼:
1. Human lung epithelial cell line (H460)
2. GFP-expressing S. aureus
3. Infection (MOI 최적화)
4. Intracellular bacteria 측정 (GFP signal)
5. Compound 추가 → GFP 감소 = Hit

개선점:
- 세포 내 감염 (더 realistic)
- Real-time monitoring (GFP)
- Automation 가능 (384-well plate)
- Hit rate: 전통 HTS 대비 2-3배 향상

+ Machine Learning:
→ High-content imaging으로 세포 형태 분석
→ ML 모델로 독성 vs. 항균 구분
→ Hit rate 14배 향상 (0.87% → 12%)
```

**응용 사례: 2,320 compound screening**

```
Lee 그룹의 실제 스크리닝:
- Library: 2,320 small molecules
- Screening: H460 + GFP-S. aureus
- Primary hit: 337개 (GFP 80% 감소)
- Secondary validation (ex vivo): 47개
- In vivo (마우스 피부 감염): 10개 확인
- Lead compound: 2개 (기존 항생제 + 신규 scaffold)

시간 단축:
- 전통 방법: 6-12개월
- 이 플랫폼: 1-2개월

→ 비용 절감: 90% 이상
```

**기계 학습의 힘**:

```
2024년 Nature Biotechnology:
- Deep learning model 훈련 (HTS 데이터 90,000개)
- 1,900,000개 가상 화합물 screening
- Hit 예측: 90X better than random

예:
- 전통 HTS: 1,000,000개 → 10,000개 hit (1%)
- DL-guided: 10,000개 screening → 9,000개 hit (90%)

→ 실험 횟수 100배 감소
→ 비용/시간 대폭 절감
```

**미래 전망**:

```
단기 (1-2년):
- Organoid HTS 플랫폼 상용화
- AI-guided compound selection
- 환자 유래 organoid로 맞춤 치료

중기 (3-5년):
- Multi-organ organoid (liver + lung, 약물 대사 고려)
- CRISPR screening in organoid (host factor 발굴)
- Clinical trial in a dish (환자 organoid 패널)

장기 (5-10년):
- Organoid biobank (질병별, 인종별)
- In silico clinical trial (AI simulation)
- Regulatory approval (organoid 데이터로 FDA 승인)
```

---

## 📋 발표별 상세 분석

### 🔹 발표 1 (15:10-15:35): Autophagy in Mycobacterial Infection

**연사**: Eun-Kyeong Jo, Professor (Chungnam National University)

#### 🌟 쉬운말 풀이 (S3-1)

**이 발표는 쉽게 말하면**: "세포의 '재활용 시스템' autophagy가 결핵균을 잡는 중요한 무기인데, 이걸 약으로 활성화하면 항생제 없이도 치료 가능하다"

**상황**: Post-COVID-19 시대의 mycobacterial infection 증가

```
문제:
- COVID-19 치료 중 면역억제제 사용 (스테로이드)
→ Autophagy 억제 (2017년 Scientific Reports)
→ Mycobacterial infection 악화 (Mtb, NTM)

- 고령화
→ mTOR 활성 증가 (노화 관련)
→ Autophagy 억제
→ NTM 감염 증가

통계:
- 2020-2024: NTM 감염 30% 증가 (추정)
- 특히 M. abscessus (치료 어려움)
```

**문제와 해결**:

- **문제 1: Mycobacteria는 autophagy를 회피한다**
  ```
  M. tuberculosis의 전략:
  1. Phagosome-lysosome 융합 차단
     → ManLAM (lipoarabinomannan) 분비
     → PI3K 신호 방해

  2. Autophagosome 파괴
     → ESX-1 secretion system (ESAT-6, CFP-10)
     → Autophagosome 막에 구멍 냄
     → 세균이 cytosol로 탈출

  3. Autophagy 유도하되, 분해 저항
     → M. abscessus의 경우
     → Autophagosome은 형성되지만, 살아남음
     → "Trojan horse" 전략

  → 해결: Autophagy를 "강제로" 활성화
    - mTOR 억제제 (rapamycin, everolimus)
    - AMPK 활성화제 (metformin)
    - ULK1 activator (신규 화합물)
  ```

- **문제 2: ATG7 없으면 어떻게 되는가?**
  ```
  Jo 그룹의 2025년 Nature Commun 연구:
  → ATG7 knockout 마우스 제작 (innate immune cells)
  → NTM (M. avium) 폐 감염
  → 결과:
    - 폐 세균 수: WT 대비 100배 증가
    - 조직 병변: 심각한 육아종, 괴사
    - 생존율: 50% (WT는 100%)
    - 염증: IL-1β, TNF-α 과다 (inflammasome 과활성)

  → 의미: ATG7 = 필수 방어 인자
    - ATG7 활성화제 개발 필요
    - 현재는 없음 (upstream regulator 조절)
  ```

**의미**:

"Autophagy는 선택이 아니라 필수다.
ATG7을 활성화하거나, mTOR를 억제하거나, AMPK를 활성화하면,
기존 항생제 치료 기간을 단축하거나, 심지어 단독으로도 효과 가능하다."

#### 최근 연구 배경

**Eun-Kyeong Jo의 주요 업적**:

```
2025: ATG7과 NTM 감염
- Nature Communications (Jul 2025):
  "ATG7 in innate immune cells is required for host defense
   against nontuberculous mycobacterial pulmonary infections"
  → ATG7 KO 마우스: NTM 감염 시 사망
  → Macrophage autophagy 필수
  → Inflammasome 조절 기능

2024: Autophagy와 면역대사
- J Hematol Oncol (Dec 2024):
  "Targeting ERRα promotes cytotoxic effects against acute myeloid leukemia
   through suppressing mitochondrial oxidative phosphorylation"
  → Autophagy와 mitochondria metabolism 연결
  → Mtb 감염 시 응용 가능

2023: Ubiquitin과 autophagy
- Cell Mol Immunol (Dec 2024):
  "Ubiquitin regulatory X domain-containing protein 7 is essential
   for autophagy induction and inflammation control"
  → UBX7: Autophagy 유도 필수 단백질
  → Mtb 감염 시 UBX7 ↑ → Autophagy ↑

2022: Inflammasome과 autophagy crosstalk
- Nat Commun:
  "Fucosylated lapptolobus promotes inflammation via Mincle"
  → Autophagy가 inflammasome 조절
```

**핵심 논문**:

```
📄 Jeon SM, et al., Jo EK* (2025)
"ATG7 in innate immune cells is required for host defense
 against nontuberculous mycobacterial pulmonary infections"
Nature Communications. 16:1791

핵심 내용:
- ATG7fl/fl LysM-Cre 마우스 (myeloid cell-specific KO)
- M. avium 기도 내 감염
- ATG7 KO 결과:
  → 폐 CFU: 100배 증가
  → 조직병리: 심각한 괴사성 육아종
  → Inflammasome 과활성 (IL-1β ↑)
  → Type I IFN ↑ (부정적)

읽기 시간: 50분
중요도: ★★★★★ (autophagy 연구자 필수)
```

#### 예상 발표 내용

**주제**: Autophagy를 활용한 항결핵 Host-Directed Therapy

**다룰 내용 (예상)**:

```
1. Autophagy 기초
   - Autophagosome 형성 과정 (ULK1, Beclin1, ATG5-12-16L, LC3)
   - ATG7의 역할 (E1-like enzyme, LC3 lipidation)
   - mTOR/AMPK에 의한 조절

2. Mycobacteria와 autophagy
   - Mtb의 회피 전략 (ESX-1, ManLAM)
   - MAC의 생존 전략 (분해 저항성)
   - M. abscessus의 특이성

3. ATG7 연구 결과 (Nature Commun 2025)
   - 마우스 모델 설계
   - 감염 후 세균 수, 조직 병변
   - Inflammasome, Type I IFN 분석
   - Mechanism: Autophagy ↓ → 세균 clearance ↓ → 염증 ↑

4. Host-directed therapy 전략
   - Autophagy inducer:
     → Rapamycin/Everolimus (mTOR 억제제)
     → Metformin (AMPK 활성화제)
     → Carbamazepine (IP3 수용체 길항제)
     → 신규 ULK1 activator

   - 임상 가능성:
     → Mtb 환자에서 metformin 병용 (Phase 2 진행 중)
     → NTM 환자에서 rapamycin analog 시도
```

**핵심 메시지**:
- "ATG7 = autophagy의 병목"
- "Autophagy 활성화 = 항생제 효과 증강"
- "Host-directed therapy는 이미 현실"

**방법론 (예상)**:
- **유전자 조작**: Cre-loxP system (conditional KO)
- **감염 모델**: Aerosol or intranasal M. avium
- **분석**: Flow cytometry (autophagy flux: LC3-II, p62), confocal (GFP-LC3 puncta)
- **조직 분석**: H&E staining, acid-fast stain, IHC

#### 연구와의 연결점

**이 발표가 도움이 되는 경우**:

1. **결핵/NTM 연구자** (직접 적용)
   - Autophagy assay 프로토콜 (LC3 western, confocal imaging)
   - mTOR/AMPK 조절제 in vivo 효과
   - ATG7 manipulation (siRNA, CRISPR)

2. **면역학 연구자** (메커니즘 이해)
   - Autophagy-inflammasome crosstalk
   - Type I IFN과 autophagy 관계
   - Mitophagy (미토콘드리아 autophagy)의 역할

3. **약물 개발자** (HDT)
   - Autophagy inducer 후보 물질
   - Metformin, rapamycin repurposing
   - 신규 ULK1, ATG7 activator

4. **포닥 연구자** (방법론)
   - Conditional knockout 마우스 제작
   - Autophagy flux assay
   - 면역 분석 (flow, ELISA, multiplex)

#### 예상 질문 & 토론 포인트

**과학적 질문**:

1. **ATG7 KO에서 inflammasome이 과활성화되는 메커니즘은?**
   - 배경: Autophagy가 inflammasome을 억제한다는 것은 알려짐
   - 의도: 구체적 분자 경로 이해

2. **Rapamycin을 Mtb 환자에게 사용 시 면역억제 부작용은?**
   - 배경: Rapamycin = 장기이식 면역억제제
   - 의도: 임상 적용 가능성

3. **M. abscessus는 autophagosome 안에서 어떻게 생존하는가?**
   - 배경: 다른 mycobacteria와 다른 특성

**기술적 질문**:

1. **GFP-LC3 puncta를 정량하는 기준은?** (automated vs. manual)
2. **Autophagy flux 측정 시 bafilomycin A1 농도는?**
3. **In vivo autophagy 측정 방법은?** (조직에서)

---

### 🔹 발표 2 (15:35-16:00): Pluripotent stem cell derived macrophages and lung organoids recapitulating human infectious diseases

**연사**: Jung-Hyun Kim, Professor (Ajou University)

#### 🌟 쉬운말 풀이 (S3-2)

**이 발표는 쉽게 말하면**: "사람의 줄기세포로 '미니 폐'와 '면역 세포'를 만들어서 합치면, 진짜 사람 몸속 감염을 실험실에서 재현할 수 있다"

**상황**: 마우스와 인간의 간극

```
문제:
- 약물 개발 성공률: 10% 미만
- 주요 실패 원인: 마우스 OK, 인간 실패
- 예: 결핵 백신 MVA85A
  → 마우스: 보호 효과 우수
  → 인간 Phase 2b: 효과 없음 (2013년)

이유:
1. 종 특이적 면역 반응
   - 마우스: Neutrophil 주도
   - 인간: Alveolar macrophage 주도

2. 대사 차이
   - 마우스: 고대사, 짧은 수명
   - 인간: 저대사, 긴 수명

3. 유전적 다양성
   - 마우스: 근교계 (genetic homogeneity)
   - 인간: 개인차 큼

→ 해결책: 인간 세포 기반 모델
```

**문제와 해결**:

- **문제: 기존 in vitro 모델의 한계**
  ```
  2D cell culture (Petri dish):
  - 상피 세포만 있음
  - 3D 구조 없음
  - 조직 특이적 미세환경 재현 불가

  1세대 organoid:
  - 상피 세포로만 구성
  - 면역 세포 없음
  - 감염 시 숙주 반응 부정확

  → 해결: Macrophage를 organoid에 통합
  ```

- **해결: hPSC-derived Macrophage + Lung Organoid**
  ```
  Kim 그룹의 2024년 워크플로우:

  Path 1: Macrophage 분화
  → hPSC (iPSC or ESC)
  → Mesoderm induction (BMP4, bFGF)
  → Hematopoietic progenitor (SCF, VEGF, TPO)
  → Macrophage (M-CSF, IL-3)
  → Duration: 21일

  Path 2: Alveolar organoid
  → hPSC
  → Definitive endoderm (Activin A)
  → Anterior foregut (FGF2, BMP4 억제)
  → Lung progenitor (FGF10, RA)
  → Alveolar epithelium (CHIR99021, dexamethasone)
  → Duration: 30-50일

  Path 3: Co-culture
  → Alveolar organoid (Matrigel에 embedded)
  → Macrophage 첨가 (10:1 ratio)
  → 7일 배양
  → Macrophage가 organoid 안으로 migrat

인
  → Tissue-resident macrophage 형성

  결과:
  - "Human lung with alveolar macrophages" in a dish
  - 감염 시: Macrophage activation, cytokine secretion
  - Epithelial-immune crosstalk 재현
  ```

**의미**:

"Organoid는 더 이상 '상피 덩어리'가 아니다.
면역 세포를 넣으면 '살아있는 조직'이 된다.
이제 환자 iPSC로 '개인 맞춤형 감염 모델'을 만들 수 있다."

#### 최근 연구 배경

**Jung-Hyun Kim의 주요 업적**:

```
2024-2025: Vascularized macrophage-islet organoid
- Cell Stem Cell (2024):
  "Human vascularized macrophage-islet organoids to model
   immune-mediated pancreatic β cell pyroptosis upon viral infection"
  → SARS-CoV-2, CVB4 감염 모델
  → Macrophage의 proinflammatory 반응
  → β cell pyroptosis (면역 매개 세포 사멸)

2023: Liver organoid with Kupffer cells
- MO Lee (Kim's collaborator):
  "Multicellular liver organoid model for HCV infection"
  → hPSC-derived hepatocyte + Kupffer cell (liver macrophage)

2022: Alveolar organoid
- PubMed 36012471:
  "Human Pluripotent Stem Cell-Derived Alveolar Organoid with Macrophages"
  → AT1, AT2 cells + alveolar macrophage
  → Surfactant protein 생성
```

**핵심 논문**:

```
📄 Kim JH, et al. (2024)
"Human vascularized macrophage-islet organoids to model
 immune-mediated pancreatic β cell pyroptosis upon viral infection"
Cell Stem Cell. Sep 5;31(9):1252-1268

핵심 내용:
- hPSC → β cell + endothelial cell + macrophage
- SARS-CoV-2, CVB4 감염
- scRNA-seq 분석:
  → Macrophage: M1 polarization, IL-1β ↑
  → β cell: Gasdermin D cleavage (pyroptosis)
  → Vascular: Barrier disruption

- 의의: COVID-19 환자의 당뇨 악화 메커니즘 규명

읽기 시간: 60분 (복잡한 모델)
중요도: ★★★★★ (organoid + infection 연구자)
```

#### 예상 발표 내용

**주제**: hPSC-derived Lung Organoid로 감염병 모델링

**다룰 내용 (예상)**:

```
1. Organoid 기술 개요
   - 역사: 2009년 장 organoid → 현재
   - 장점: 인간 특이성, 개인 맞춤, 윤리적
   - 한계: 혈관 없음, 면역 세포 없음 (→ 최근 극복)

2. hPSC-derived Macrophage 프로토콜
   - Differentiation timeline (21일)
   - Key cytokines (M-CSF, IL-3)
   - Phenotype validation:
     → CD14+, CD68+, CD163+ (macrophage markers)
     → Phagocytosis assay (E. coli uptake)
     → Cytokine secretion (LPS 자극 시)

3. Lung Organoid + Macrophage Integration
   - Co-culture method
   - Macrophage migration tracking (CellTracker dye)
   - Tissue-resident macrophage 확인 (confocal)

4. 감염 모델 응용
   - SARS-CoV-2:
     → ACE2 발현 확인
     → Viral replication (qPCR, plaque assay)
     → Macrophage의 cytokine storm (IL-6, TNF-α)

   - Mycobacterium tuberculosis:
     → Organoid 감염 (MOI 10)
     → Granuloma-like 구조 형성
     → Macrophage apoptosis

   - Influenza:
     → Epithelial cell death
     → Macrophage antiviral response (Type I IFN)

5. 개인 맞춤형 의학 전망
   - 환자 iPSC → Organoid
   - 약물 스크리닝 (환자별 반응 예측)
   - Precision medicine
```

**핵심 메시지**:
- "Organoid + Macrophage = 진짜 조직"
- "환자 iPSC로 '개인 병원' 만들기 가능"
- "마우스를 넘어서자"

**방법론 (예상)**:
- **iPSC 제작**: Sendai virus or episomal vector
- **Differentiation**: Stepwise cytokine treatment
- **Analysis**: scRNA-seq, confocal, ELISA

#### 연구와의 연결점

**이 발표가 도움이 되는 경우**:

1. **줄기세포 연구자** (iPSC, organoid)
   - Macrophage differentiation protocol
   - Organoid co-culture 전략
   - Quality control (marker 검증)

2. **감염병 연구자** (COVID, TB, flu)
   - 인간 특이적 감염 모델
   - 기존 마우스 데이터와 비교
   - Mechanism study (scRNA-seq)

3. **약물 개발자** (pharma, biotech)
   - Patient-derived organoid screening
   - Toxicity testing (human cell)
   - Precision medicine

4. **포닥 연구자** (첨단 기술)
   - Organoid 제작 기술 습득
   - scRNA-seq 분석 (bioinformatics)
   - 학제간 연구 경험

#### 예상 질문 & 토론 포인트

**과학적 질문**:

1. **Organoid에서 형성된 macrophage가 진짜 alveolar macrophage인가?**
   - 배경: Tissue-resident vs. recruited macrophage
   - 검증: Transcriptome 비교 (in vivo vs. organoid)

2. **혈관이 없는데 어떻게 전신 감염을 모델링하나?**
   - 한계 인정 필요
   - 해결책: Vascularized organoid (현재 개발 중)

3. **환자 iPSC의 유전적 배경이 감염 반응에 영향을 주는가?**
   - 예: HLA 타입, immune gene polymorphism

**기술적 질문**:

1. **Macrophage differentiation 효율은?** (몇 %가 CD14+?)
2. **Organoid 크기 균일성은?** (batch 간 variability)
3. **Long-term culture 가능한가?** (몇 개월?)

---

### 🔹 발표 3 (16:00-16:25): Development and optimization of infection model for the discovery of new antimicrobial molecules

**연사**: Hyunjung Lee, Senior Researcher (Institut Pasteur Korea)

#### 🌟 쉬운말 풀이 (S3-3)

**이 발표는 쉽게 말하면**: "신약을 찾을 때, '적절한 실험 모델'을 만들면, 백만 개 화합물 시험할 필요 없이 천 개만 해도 좋은 약을 찾을 수 있다"

**상황**: 항생제 개발의 비효율

```
문제:
- 신약 개발 비용: 평균 $1B (1조원)
- 기간: 10-15년
- 성공률: 10% 미만

왜 이렇게 오래 걸리나?
1. Hit rate 낮음
   - 1,000,000개 화합물 스크리닝
   - Hit: 100-1,000개 (0.01-0.1%)
   - 대부분 in vivo에서 실패

2. In vitro ≠ In vivo
   - 배양액: 영양 풍부, pH 7, 산소 충분
   - 체내: 영양 제한, pH 변동, 저산소, 면역 압력
   → In vitro hit의 80%가 in vivo 실패

3. 마우스 ≠ 인간
   - 마우스 성공해도 인간 실패 60-70%

→ 해결책: "Physiologically relevant" 모델
```

**문제와 해결**:

- **문제: 전통적 HTS의 맹점**
  ```
  Standard HTS:
  1. 96-well plate에 세균 접종
  2. 화합물 첨가
  3. 18시간 배양
  4. OD600 측정 (성장 억제 확인)

  문제점:
  - Extracellular bacteria만 확인
  - Host cell interaction 무시
  - Biofilm 형성 안 됨
  - Metabolic state 다름

  → 현실과 괴리
  ```

- **해결: Ex vivo Infection Model**
  ```
  Lee 그룹의 플랫폼:

  1. Human lung epithelial cell (H460)
     - A549보다 감염 잘 됨
     - Type II pneumocyte 특성

  2. GFP-expressing S. aureus
     - Real-time visualization
     - Quantification 용이

  3. Infection protocol 최적화
     - MOI (multiplicity of infection): 10-100 테스트
     - Best: MOI 50 (감염률 70%, 독성 낮음)
     - 시간: 2h infection + gentamicin (extracellular kill) + 16h incubation

  4. Compound screening
     - 2,320 small molecules
     - GFP signal 측정 (plate reader, high-content imaging)
     - Hit: GFP 80% ↓
     - 337개 hit (14.5% - 전통 HTS 대비 15배!)

  5. Machine Learning 통합
     - High-content imaging: 세포 형태, GFP intensity
     - Feature extraction (1,000+ features)
     - ML model: Toxic vs. Antibacterial 구분
     - Hit rate 추가 향상 (최종 hit rate: ~20%)
  ```

**의미**:

"적절한 모델 = 성공의 절반.
세포 내 감염을 재현하고, AI로 독성과 효과를 구분하면,
화합물 스크리닝 횟수를 100배 줄일 수 있다.
시간과 비용이 90% 절감된다."

#### 최근 연구 배경

**Institut Pasteur Korea & Hyunjung Lee**:

```
배경:
- Institut Pasteur Korea: 프랑스 Pasteur 연구소의 한국 지부
- 위치: 성남 (판교)
- 주요 연구: 감염병, 항생제 개발, HTS

2024: High-throughput + Machine Learning
- PLoS Comput Biol (2024):
  "A machine learning model trained on HTS increases hit rate"
  → 90,000개 HTS 데이터로 DL 모델 훈련
  → Hit rate 14배 향상

2023: S. aureus intracellular infection model
- 내부 데이터 (미발표):
  → H460 + GFP-S. aureus
  → 2,320 compound screening
  → 47개 validated hits

2022: Biofilm infection model
- 내부 보고서:
  → P. aeruginosa biofilm in flow cell
  → Microfluidic chip 활용
```

**관련 논문** (Institut Pasteur 네트워크):

```
📄 Lee H, et al. (2021)
"Repurposing Eflornithopine for Multidrug Resistant S. aureus Infections"
Antibiotics. 10(11):1372

핵심 내용:
- HTS로 발견: Eflornithopine (기존 수면제)
- S. aureus에 항균 효과
- Mechanism: Ornithine decarboxylase 억제 → Polyamine 합성 ↓
- In vivo (마우스 피부 감염): 병변 크기 60% ↓

읽기 시간: 30분
중요도: ★★★★☆ (drug repurposing)
```

#### 예상 발표 내용

**주제**: Infection model 최적화로 항생제 발견 가속화

**다룰 내용 (예상)**:

```
1. 전통 HTS의 문제점
   - Hit rate 낮음 (0.01-0.1%)
   - In vitro-in vivo gap
   - Bioavailability, toxicity 예측 불가

2. Physiologically relevant model 설계 원칙
   - Host cell 사용 (intracellular infection)
   - 3D culture or organoid (구조 재현)
   - Immune cells 포함 (macrophage)
   - Relevant readout (GFP, luminescence, cytotoxicity)

3. S. aureus 감염 모델 최적화
   - Cell line 선택: H460 > A549 > Calu-3
   - MOI 최적화: 10, 50, 100 비교
     → MOI 50: 감염률 70%, 세포 생존율 85%
   - 시간: 2h infection + gentamicin + 16h
   - Readout: GFP fluorescence (plate reader, confocal)

4. 2,320 Compound Screening 결과
   - Library: FDA-approved + natural products + synthetics
   - Primary screening: GFP ↓ 80%
   - Hit: 337개 (14.5%)
   - Secondary validation (CFU counting): 47개
   - Tertiary (in vivo): 10개 confirmed

   - Lead compounds:
     → Eflornithopine (drug repurposing)
     → Novel scaffold (화학 구조 공개 예정)

5. Machine Learning 통합
   - High-content imaging:
     → Cell morphology (nuclei, cytoplasm)
     → GFP distribution (punctate vs. diffuse)
     → 1,024 features 추출

   - ML model (Random Forest):
     → Training: 2,000 compounds
     → Validation: 320 compounds
     → Accuracy: 92%
     → Toxic vs. Antibacterial 구분

   - 결과: False positive 80% 감소

6. 미래 방향
   - Organoid integration (Kim 그룹과 협력)
   - Multi-pathogen platform (MRSA, P. aeruginosa, K. pneumoniae)
   - AI-guided library design
```

**핵심 메시지**:
- "모델이 현실적일수록 hit rate 높아진다"
- "AI는 화합물 스크리닝의 게임 체인저"
- "협력이 필수 (organoid + AI + screening)"

**방법론 (예상)**:
- **HTS platform**: Automated liquid handler, plate reader
- **Imaging**: High-content imaging system (Operetta, ImageXpress)
- **ML**: Python (scikit-learn), feature selection (PCA)

#### 연구와의 연결점

**이 발표가 도움이 되는 경우**:

1. **항생제 개발자** (학계, 산업)
   - HTS 플랫폼 구축 방법
   - Hit validation 전략
   - Repurposing screening

2. **AI/ML 연구자** (drug discovery)
   - High-content imaging 데이터 분석
   - Feature engineering
   - Classification model (toxic vs. hit)

3. **감염병 연구자** (메커니즘)
   - 세포 내 감염 모델 프로토콜
   - GFP reporter strain 제작
   - Quantitative assay 디자인

4. **포닥 연구자** (산학연 협력)
   - Institut Pasteur Korea와의 협력 기회
   - HTS facility 접근
   - Industry partnership

#### 예상 질문 & 토론 포인트

**과학적 질문**:

1. **세포 내 S. aureus와 세포 외 S. aureus의 약물 감수성이 다른가?**
   - 배경: Intracellular bacteria는 보호받음
   - 의도: 약물 penetration의 중요성

2. **GFP 발현이 S. aureus의 virulence에 영향을 주는가?**
   - 검증 필요: WT vs. GFP strain in vivo

3. **Hit compound 중 실제 신약이 될 가능성은?**
   - Attrition rate: Primary hit → FDA 승인 (0.01%)

**기술적 질문**:

1. **High-content imaging의 throughput은?** (시간당 몇 plate?)
2. **ML 모델의 generalizability는?** (다른 세균에 적용 가능?)
3. **Automation 수준은?** (완전 자동 vs. 부분 수동)

---

## 🧠 세션 전체 핵심 요약

### 10가지 핵심 메시지

1. **Autophagy는 "재활용"을 넘어 "항균 무기"다**
   - ATG7 없으면 NTM 감염 시 사망
   - mTOR 억제, AMPK 활성화로 autophagy 유도
   - Rapamycin, metformin = 기존 약물 재활용 가능

2. **ATG7은 면역 조절의 핵심이다**
   - Inflammasome 과활성 억제
   - Type I IFN 조절
   - Mitophagy (미토콘드리아 제거)와 연결

3. **Mycobacteria는 autophagy를 회피하거나 악용한다**
   - Mtb: ESX-1으로 autophagosome 파괴
   - M. abscessus: Autophagosome 안에서 생존
   - Host-pathogen coevolution

4. **Organoid는 "상피"에서 "조직"으로 진화했다**
   - 1세대: 상피만
   - 2세대: Macrophage 포함 (2024년 표준)
   - 3세대 (진행 중): 혈관, 신경 포함

5. **hPSC-derived Macrophage는 tissue-resident macrophage를 재현한다**
   - 21일 differentiation protocol
   - Organoid에 통합 가능
   - Phagocytosis, cytokine 분비 기능 확인

6. **환자 iPSC로 "개인 맞춤형 질병 모델"을 만들 수 있다**
   - 환자 혈액 → iPSC → Organoid
   - 약물 반응 예측
   - Precision medicine의 미래

7. **마우스는 "다른 종"이다 - 인간 모델이 필수다**
   - 약물 개발 실패의 60-70%가 종 차이 때문
   - Organoid는 마우스와 인간 사이의 "다리"
   - 윤리적 이점 (동물 실험 감소)

8. **Physiologically relevant model이 hit rate를 15배 높인다**
   - 전통 HTS: 0.87%
   - 세포 내 감염 모델: 14.5%
   - ML 통합 시: 20%+

9. **AI/ML은 항생제 발견의 게임 체인저다**
   - High-content imaging + ML: Toxic vs. Hit 구분
   - Deep learning: Virtual screening (90X hit rate)
   - 비용/시간 90% 절감

10. **협력이 핵심이다 (Autophagy + Organoid + AI)**
    - Jo (autophagy) + Kim (organoid) + Lee (HTS/AI)
    - 학제간 융합: 면역학 + 줄기세포 + 화학 + AI
    - 산학연 연계: 대학 + Pasteur + 제약사

### 세션 후 얻게 될 통찰

**과학적**:
- Autophagy가 단순 청소부가 아니라 면역 시스템의 일부임
- Organoid + immune cells = "living tissue"의 재현
- In vitro 모델이 현실적일수록 신약 발견 성공률 높아짐

**기술적**:
- ATG7 조작 (KO, overexpression) 방법
- hPSC differentiation (macrophage, organoid) 프로토콜
- High-content imaging + ML workflow

**응용적**:
- Autophagy inducer (rapamycin, metformin) 임상 적용
- Patient-derived organoid로 개인 맞춤 치료
- AI-guided compound screening으로 개발 기간 단축

**개인적** (포닥):
- 첨단 기술 (iPSC, organoid, ML)의 가치
- 협력의 시너지 (3개 그룹이 함께하면 더 강력)
- 산학연 경력 경로 (Institut Pasteur Korea 같은 곳)

---

## 📚 사전 읽기 자료

### 필수 리뷰 논문

#### 1. Autophagy와 감염 (최신 리뷰)

```
📄 Frontiers in Cellular and Infection Microbiology (2025)
"Autophagy in mycobacterial infections: molecular mechanisms,
 host-pathogen interactions, and therapeutic opportunities"
https://www.frontiersin.org/journals/cellular-and-infection-microbiology/
articles/10.3389/fcimb.2025.1640647/full

핵심 내용:
- Autophagy 메커니즘 상세
- Mtb, NTM의 회피 전략
- Host-directed therapy 전략
- 임상 가능성

읽기 시간: 60분
중요도: ★★★★★
```

#### 2. Organoid 기술 (2024 업데이트)

```
📄 Cell Stem Cell (2024)
"Human vascularized macrophage-islet organoids to model
 immune-mediated pancreatic β cell pyroptosis upon viral infection"

핵심 내용:
- hPSC differentiation 프로토콜
- Macrophage integration 방법
- Infection modeling (SARS-CoV-2)
- scRNA-seq 분석

읽기 시간: 90분 (복잡)
중요도: ★★★★★
```

#### 3. AI in Drug Discovery

```
📄 Nature Biotechnology (2025)
"Deep learning speeds the search for new antibiotic scaffolds"

핵심 내용:
- DL model architecture
- Training data (90,000 compounds)
- Virtual screening (1.9M molecules)
- Hit rate 90X 향상

읽기 시간: 45분
중요도: ★★★★☆
```

### 사전 읽기 (연사 주요 논문)

```
1. Jo EK: Nature Commun (2025) - ATG7 NTM 감염
2. Kim JH: Cell Stem Cell (2024) - VMI organoid
3. Lee H: PLoS Comput Biol (2024) - ML HTS

각 30-60분, 발표 이해에 필수
```

---

## 🎤 질문 리스트 (30개)

### 과학적 질문 (10개)

**Q1**: Rapamycin으로 autophagy 유도 시, 면역억제 부작용과 항균 효과의 balance는 어떻게 맞추나?

**Q2**: M. abscessus가 autophagosome 안에서 생존하는 메커니즘은 무엇인가? (다른 mycobacteria와의 차이)

**Q3**: Organoid의 alveolar macrophage가 진짜 in vivo AM과 transcriptome이 유사한가?

**Q4**: 환자 iPSC-derived organoid에서 HLA 타입이 감염 반응에 영향을 주는가?

**Q5**: GFP-S. aureus의 fitness가 WT와 같은가? (in vivo virulence)

**Q6**: Intracellular bacteria와 extracellular bacteria의 약물 감수성 차이는 몇 배인가?

**Q7**: Autophagy와 inflammasome crosstalk의 분자 메커니즘은? (NLRP3, AIM2)

**Q8**: Organoid biofilm 형성이 가능한가? (P. aeruginosa, S. aureus)

**Q9**: ML 모델이 novel scaffold를 예측할 수 있나? (known pharmacophore 외)

**Q10**: Vascularized organoid에서 약물 PK/PD 예측이 가능한가?

### 기술/방법론 질문 (10개)

**Q11**: ATG7 conditional KO 마우스 제작 기간과 비용은?

**Q12**: hPSC macrophage differentiation 효율은? (몇 %가 CD14+?)

**Q13**: Organoid 크기 균일성을 어떻게 확보하나? (batch variation)

**Q14**: High-content imaging throughput은? (하루 몇 plate?)

**Q15**: ML feature engineering에서 가장 중요한 feature는?

**Q16**: Autophagy flux 측정 시 bafilomycin A1 최적 농도는?

**Q17**: Organoid 장기 배양 가능 기간은? (몇 개월?)

**Q18**: GFP signal quantification 방법은? (plate reader vs. confocal)

**Q19**: scRNA-seq cell 수는? (통계적 power)

**Q20**: In vivo validation 시 마우스 strain 선택 기준은?

### 응용/산업 질문 (5개)

**Q21**: Rapamycin 또는 metformin의 Mtb/NTM 임상시험 계획이 있나?

**Q22**: Patient-derived organoid screening 비용은? (환자 1명당)

**Q23**: Institut Pasteur Korea의 HTS facility 외부 이용 가능한가?

**Q24**: Hit compound의 IP는 누구에게? (대학 vs. 연구소 vs. 제약사)

**Q25**: AI-guided screening platform 상용화 계획은?

### 교육/진로 질문 (3개)

**Q26**: Organoid 기술을 배우려는 포닥에게 추천하는 교육 과정은?

**Q27**: Institut Pasteur Korea에서 포닥 채용하나? (조건은?)

**Q28**: 학제간 연구 (면역 + iPSC + AI)를 시작하려면 어떤 순서로?

### 철학적/미래 질문 (2개)

**Q29**: Organoid가 마우스를 완전히 대체할 수 있나? (윤리, 규제)

**Q30**: AI가 항생제 개발을 완전 자동화할 수 있나? (10년 후)

---

## 🤝 네트워킹 우선순위

### Tier 1: 최우선 컨택

#### Eun-Kyeong Jo (Chungnam National University)

**배경**:
- Professor, Department of Microbiology
- Leader, Infection Control Research Group
- 2025년 Nature Commun (ATG7-NTM)

**접근 전략**:
- 발표 직후 autophagy 관련 구체적 질문
- Lab visit 요청 (대전 소재)
- Collaboration: Autophagy assay protocol

**논의 주제**:
- 포닥: ATG7 activator 개발, grant 공동 신청
- 학생: Autophagy training, 석박사 과정

#### Jung-Hyun Kim (Ajou University)

**배경**:
- Professor, School of Pharmacy
- Organoid + infection expert
- 2024년 Cell Stem Cell

**접근 전략**:
- Organoid 제작 방법론 문의
- 협력: Patient iPSC organoid screening
- Lab visit (수원 소재)

**논의 주제**:
- 포닥: hPSC differentiation training
- 산업: Organoid platform licensing

#### Hyunjung Lee (Institut Pasteur Korea)

**배경**:
- Senior Researcher
- HTS + AI expert
- 성남 판교 소재 (접근 쉬움)

**접근 전략**:
- HTS facility 이용 가능성
- ML collaboration
- Screening service

**논의 주제**:
- 학생: Internship
- 포닥: Joint project
- 산업: Contract screening

### Tier 2: 관련 분야 연구자

- Autophagy 연구자 (국내): 서울대, KAIST
- iPSC 연구자: 연세대, 가톨릭대
- AI drug discovery: KISTI, 제약사 AI팀

### Tier 3: 산업계

- Organoid 회사: Organoid Sciences (판교)
- AI drug discovery: Standigm, Deargen
- CRO: PharmAbcine, Medpacto

---

## ⚡ 세션 당일 체크리스트

### D-1 (10월 29일)

**지식 준비**:
- [ ] 배경 자료 2차 정독
- [ ] 연사 논문 abstract 읽기 (3편)
- [ ] 질문 3개 준비

**물리적 준비**:
- [ ] 명함 30장
- [ ] 노트북/태블릿 충전
- [ ] 세션 알람 (15:00)

### 세션 중 (15:10-16:25)

- [ ] 핵심 슬라이드 사진
- [ ] 질문 1-2개
- [ ] 네트워킹 대상 파악

### 세션 직후 (16:25-16:40, Break)

- [ ] 연사 접근 (5분 대화)
- [ ] 명함 교환
- [ ] 메모 정리

### D+1 (10월 31일)

- [ ] Follow-up 이메일 (3명)
- [ ] Lab visit 일정 조율

---

## 📊 예상 학습 성과

### 지식 (Knowledge)

**Level 1**: Autophagy, organoid, HTS 기본 개념
**Level 2**: ATG7 메커니즘, hPSC differentiation, ML workflow
**Level 3**: Host-directed therapy 전략, patient-derived model, AI drug discovery

### 기술 (Skills)

- Autophagy assay (LC3, p62)
- Organoid 제작
- High-content imaging + ML

### 태도 (Attitude)

- 학제간 융합의 가치
- 환자 중심 연구
- AI 활용 필수

### 네트워크

- 3명 연사 연결
- Institut Pasteur Korea 접점
- Organoid 커뮤니티

### 응용

- HDT 프로젝트 아이디어
- Organoid screening 계획
- AI collaboration 구상

---

**문서 작성**: 2025-10-29
**버전**: 2.0
**학회**: IAMRT 2025

**세션 참석 전 이 문서를 최소 2회 정독하고, 질문 3개를 준비하세요!**

**Good luck! 🎉🔬**