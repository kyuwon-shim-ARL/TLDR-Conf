# 🧬 MSK2025 핵심 세션 배경 자료 | 노션 공유용

> **연구자**: 박사후연구원
> **전문분야**: 메타지노믹스 기반 도심 미생물 AMR 감시·예측 & 항생제 개발
> **목표**: 최신 동향 + 네트워킹 + 신기법 학습

---

# 📌 Quick Navigation

- [S4: 항생제 신규 타겟](#s4-호흡기-세균-병원체의-항생제-신규-타겟) ⭐⭐⭐⭐⭐ (95점)
- [S8: AMR 진단 및 치료](#s8-세균-감염-진단-및-치료) ⭐⭐⭐⭐⭐ (98점) **← 최우선!**
- [S12: 환경 메타지노믹스](#s12-환경-미생물---hidden-jewels) ⭐⭐⭐⭐ (88점)
- [나머지 세션 추천](#나머지-세션-빠른-가이드)

---

# S4: 호흡기 세균 병원체의 항생제 신규 타겟

**📅 10/27 (월) 09:00-11:00 | 📍 Rm 301+302 | 🎯 95점**

<details>
<summary><b>⭐ 왜 필수인가?</b></summary>

- 신규 항생제 클래스 (glycolipid biosynthesis targeting)
- MRSA, Pseudomonas, Mycobacteria 최신 연구
- 도심 AMR 병원체 직결
- 메타지노믹스 마커 20+ 유전자 습득

</details>

## 📋 발표 요약

<details>
<summary><b>🔹 발표 1: Wonsik Lee (SKKU) - S. aureus Niche Adaptation</b></summary>

### 최근 연구 (2025 Nature Commun)

**Transposon sequencing (Tn-Seq)**으로 MRSA가 다양한 숙주 환경에서 생존에 필요한 유전자 분석

**핵심 발견**:
- 세포 내 vs. 혈액 환경 = 완전히 다른 유전자 세트 필요
- Host niche-specific fitness determinants 동정

### 당신의 연구 연결점

**도심 환경 적용**:
```yaml
도심 "niches":
  - 대기 (air)
  - 물 (water)
  - 토양 (soil)
  - 표면 (surfaces)

각 환경별 MRSA survival genes 파악 → 메타지노믹스 마커
```

### 질문

"Tn-Seq를 도심 환경 샘플에 적용한 연구가 있나요? 기술적 챌린지는?"

</details>

<details>
<summary><b>🔹 발표 2: Sung Jae Shin (Yonsei) - TB & NTM 치료 전략</b></summary>

### 전문 분야

- **M. tuberculosis**: 지질 대사 타겟팅
- **NTM (M. avium complex)**: 대식세포 기능 조절

### 핵심 차이점

| 특징 | TB | NTM |
|------|----|----|
| 전파 | 인간→인간 | 환경→인간 |
| 치료 기간 | 6-9개월 | 12-18개월+ |
| 환경 reservoir | - | **물, 토양** ← 도심 감시 중요! |

### 도심 AMR 연결

**NTM = 환경성 병원체**
- 도심 물 시스템 (샤워헤드, 수도관)
- 메타지노믹스로 환경 NTM + AMR genes 모니터링

### 질문

"도심 물 시스템에서 NTM AMR 확산 감시 전략은? 환경-임상 연결?"

</details>

<details open>
<summary><b>🔹 발표 3: Jinki Yeom (SNU) - Glycolipid Biosynthesis Targeting</b> ⭐ **핵심!**</summary>

### 신규 항생제 클래스

**타겟**: Outer layer glycolipid biosynthesis (LPS in Gram-negative)

**핵심 효소**:
- **KdsB** (CMP-Kdo synthetase)
- **WaaA** (Kdo transferase)

**왜 혁신적?**
- ✅ Essential for viability
- ✅ 인간에게 없음 (선택적 독성)
- ✅ Broad-spectrum (Gram-negative)

### 메타지노믹스 응용

```yaml
도심 AMR 마커:
  Glycolipid synthesis genes:
    - kdsA, kdsB, kdsC
    - waaA, waaC, waaF

  응용:
    - Gene variants → 항생제 감수성 예측
    - Gene abundance → AMR burden 평가
```

### 최우선 질문!

1. "KdsB inhibitor 구조와 작용 메커니즘? 메타지노믹 데이터에서 kdsB variants로 감수성 예측 가능한가요?"
2. "도심 환경 분리주에서 efficacy test 했나요?"

### 네트워킹 전략

⭐⭐⭐ **최우선 네트워킹!**
- 발표 직후 질문
- 명함 교환: "메타지노믹스로 glycolipid genes 분석 중"
- Follow-up: Collaborative study 제안

</details>

<details>
<summary><b>🔹 발표 4: Changhan Lee (Ajou) - Pseudomonas Proteostasis</b></summary>

### Acid-Responsive Proteostasis

**FtsH proteases**: P. aeruginosa의 단백질 품질 관리

**Acid stress environments**:
- Phagolysosome (pH 4.5-5.0)
- CF sputum (pH 5.5-6.5)
- **도심**: Acid rain, industrial pollution?

### 연결점

**메타지노믹스 마커**:
```yaml
Proteostasis genes:
  - ftsH
  - lon, clpP (proteases)
  - rpoS (stress response)

도심 환경 스트레스 → 발현 증가?
```

### 질문

"Acid stress가 항생제 내성에 미치는 영향? Metatranscriptomics로 모니터링 가능?"

</details>

<details>
<summary><b>🔹 발표 5: Junho Cho (Yonsei) - MRSA AMP Resistance</b></summary>

### AMP (Antimicrobial Peptide) 저항 메커니즘

**Surface charge modification**:
- **DltABCD**: Teichoic acid D-alanylation
- **MprF**: Lys-PG synthesis

**효과**: Cationic AMP repulsion

### AMR 마커

```yaml
AMP resistance genes:
  - dltABCD
  - mprF
  - graRS (regulation)

메타지노믹스 응용:
  - AMP resistance burden 평가
  - 도심 환경 MRSA profiling
```

</details>

## 🧠 S4 핵심 Takeaways

### Metagenomics AMR Markers

```yaml
MRSA:
  - mecA, dltABCD, mprF, graRS

P. aeruginosa:
  - ftsH, lon, rpoS, mexAB-oprM

Gram-negative MDR:
  - kdsA/B/C, waaA/C/F, blaKPC, blaNDM

Mycobacteria:
  - rpoB, katG, erm (NTM)
```

### 필수 준비

- [ ] Wonsik Lee (2025) 논문 읽기
- [ ] Glycolipid biosynthesis review
- [ ] 명함 준비 (한/영 각 10장)
- [ ] 질문 리스트 인쇄

### 네트워킹 Top 3

1. **Jinki Yeom** (SNU) - 신규 항생제
2. **Wonsik Lee** (SKKU) - Tn-Seq 전문가
3. **Sung Jae Shin** (Yonsei) - NTM 환경 감시

---

# S8: 세균 감염 진단 및 치료

**📅 10/27 (월) 13:50-15:50 | 📍 Rm 301+302 | 🎯 98점** **← 최우선!**

<details>
<summary><b>⭐ 왜 최우선인가?</b></summary>

- **즉시 적용 가능**: 도심 현장 진단 기술
- **공기 중 AMR 검출**: CN-TAR (KRIBB)
- **Portable 플랫폼**: Fidget spinner, Cell-free system
- **빠른 검출**: 30분-2시간 (vs. 48-72시간)

</details>

## 📋 발표 요약

<details>
<summary><b>🔹 발표 1: Jeong Wook Lee (POSTECH) - SENSR</b></summary>

### Cell-free RNA Detection

**SENSR** (SENsitive Splint-based one-pot isothermal RNA detection)

**성능**:
- 30-50분 검출
- 0.1 attomolar sensitivity
- **SNP discrimination** 가능!

### 메커니즘

```
Splint probe + SplintR ligase
  ↓
T7 RNA polymerase (Transcription cascade)
  ↓
Fluorescence detection
```

### AMR 응용

**RNA-based active AMR detection**:
```yaml
메타전사체 샘플:
  - mecA transcripts (active MRSA)
  - Carbapenemase mRNA (blaNDM, blaKPC)

장점:
  - DNA가 아닌 RNA = Actively expressed
  - 30-50분 rapid detection
```

### 질문

"메타전사체 샘플에 직접 적용 시 pre-amplification 필요? Multiplex 한계는?"

</details>

<details open>
<summary><b>🔹 발표 2: Eun-Kyung Lim (KRIBB) - CN-TAR</b> ⭐⭐⭐ **도심 AMR 핵심!**</summary>

### Airborne AMR Detection!

**CN-TAR** (Cas9 Nickase-Triggered Amplification Reaction)

**2025년 최신 연구**:
- **공기 중 MRSA/VRE 검출**
- Portable isothermal PCR device
- Real-time, <2시간

### 메커니즘

```
Air sampling → Filter
  ↓
DNA extraction
  ↓
Cas9 nickase (mecA/vanA specific)
  ↓
Rolling Circle Amplification (RCA)
  ↓
Real-time fluorescence
```

### 성능

| Target | Detection Limit |
|--------|-----------------|
| MRSA (mecA) | 1.40 copies/μL |
| VRE (vanA) | 1.13 copies/μL |

### 도심 감시 완벽한 도구!

**Application**:
```yaml
도심 대기 AMR 모니터링:
  Locations:
    - 지하철역
    - 병원
    - 요양원
    - 학교

  Workflow:
    1. Air filter sampling (10-60분)
    2. Simple lysis
    3. CN-TAR (60-90분)
    4. Result → Public health alert

  Expandable targets:
    - blaNDM, mcr-1 (Gram-negative)
    - M. tuberculosis
```

### 최우선 질문!

1. "도심 대기 샘플에서 air sampling 방법? Filter type과 volume?"
2. "**Multiplex** CN-TAR 가능? (mecA + vanA + blaNDM 동시)"
3. "Portable device 비용? Per-test reagent cost?"
4. "**Quantitative** CN-TAR? Airborne AMR bacteria 농도 측정?"
5. "Real-world deployment 경험? Pilot study?"

### Collaboration 제안!

"저는 도심 메타지노믹스 AMR 감시를 합니다. CN-TAR를 서울 지하철/병원에 적용하는 collaborative study 관심있으신가요?"

### 네트워킹

⭐⭐⭐ **최최우선!**
- 발표 직후 질문 필수
- Coffee break 직접 대화
- Collaborative study proposal (follow-up email)
- KRIBB 방문 약속

</details>

<details open>
<summary><b>🔹 발표 3: Yoon-Kyoung Cho (UNIST) - Fidget Spinner</b> ⭐⭐⭐ **혁신!**</summary>

### Plasmonic Fidget Spinner (P-FS)

**2025년 3월 발표** (Microsystems & Nanoengineering)

**혁신성**:
- **Hand-powered** (전기 불필요!)
- **SERS** (Surface-Enhanced Raman Spectroscopy)
- Species ID in 10-30분

### 구성

```
Fidget spinner
  ↓
Nanoplasmonic membrane (Au/Ag nanoparticles)
  ↓
Bacterial capture & SERS
  ↓
ML classification (E. coli, S. aureus, etc.)
```

### 장점

| Feature | Benefit |
|---------|---------|
| No electricity | Resource-limited settings |
| Portable | Pocket-size |
| Fast | 10-30분 |
| Species ID | Vibrational fingerprints |

### AMR 응용 가능성

**SERS-based AMR phenotyping?**
- MRSA vs. MSSA (cell wall structure difference)
- Resistant vs. susceptible strains

**도심 환경**:
```yaml
P-FS Use Cases:
  - 지하철 공기 (air filter rinse)
  - 하수 (wastewater)
  - 공공 화장실 수도꼭지

  Workflow:
    1. Sample collection
    2. Fidget spin (1-2분)
    3. SERS (5-10분)
    4. Species ID (+ AMR prediction?)
```

### 질문

1. "**SERS signature로 AMR 예측** 가능? MRSA vs. MSSA 구별?"
2. "환경 샘플 (복잡한 matrix)에서 species ID 정확도?"
3. "**Portable Raman spectrometer** 비용과 크기?"
4. "New species/strains로 ML 모델 확장? Transfer learning?"

### Collaboration

"도심 AMR 메타지노믹스 + **P-FS로 빠른 validation** 하고 싶습니다. UNIST-서울 협력 가능할까요?"

### 네트워킹

⭐⭐⭐ **매우 혁신적!**
- 발표 후 질문 (Environmental application)
- UNIST lab visit 제안 (울산 가까움)

</details>

<details>
<summary><b>🔹 발표 4: Moo-seung Lee (KRIBB) - Graphene FET</b></summary>

### Shiga Toxin Detection

**Graphene Field-Effect Transistor Biosensor**

**성능**:
- Femtogram (fg) level detection
- Label-free
- Real-time electrical signal

### AMR 확장 가능성

**Graphene FET for AMR genes?**
- Functionalize with AMR gene probes
- Ultra-sensitive environmental monitoring

### 질문

"Graphene FET를 AMR genes (mecA, blaNDM) 검출로 확장 가능?"

</details>

<details>
<summary><b>🔹 발표 5: Namil Lee (KAIST) - Streptomyces</b></summary>

### Synthetic Biology for Antibiotics

- **Streptomyces** = 자연 항생제의 50-60%
- BGC (Biosynthetic Gene Clusters) activation
- Novel antibiotic discovery

**AMR 관점**: 신규 항생제 개발

**우선순위**: 낮음 (시간 여유 시)

</details>

## 🧠 S8 핵심 Takeaways

### Portable Diagnostics 비교

| Technology | Speed | Portability | AMR Application |
|------------|-------|-------------|-----------------|
| **SENSR** | 30-50분 | Moderate | AMR gene RNA |
| **CN-TAR** | <2시간 | ✅ Portable | **Airborne MRSA/VRE** ⭐ |
| **P-FS** | 10-30분 | ✅✅ Hand-powered! | Species ID, AMR phenotype? |
| **Graphene FET** | <30분 | ✅ Small | Toxin/Gene detection |

### 도심 AMR 통합 전략

```yaml
Tier 1 (Weekly-Monthly):
  - Metagenomics: Broad surveillance

Tier 2 (Daily):
  - CN-TAR: Airborne MRSA/VRE at hotspots
  - P-FS: Species confirmation

Tier 3 (On-demand):
  - SENSR: RNA active AMR
  - Graphene FET: Ultra-sensitive
```

### 네트워킹 Top 2

1. **Eun-Kyung Lim** (KRIBB) - CN-TAR, Airborne AMR
2. **Yoon-Kyoung Cho** (UNIST) - P-FS, Portable platform

---

# S12: 환경 미생물 - Hidden Jewels

**📅 10/27 (월) 16:00-18:00 | 📍 Convention Hall 1 | 🎯 88점**

<details>
<summary><b>⭐ 왜 중요한가?</b></summary>

- **Single-cell genomics**: 배양 불가 미생물 연구
- **대규모 메타지노믹스**: Continental/global scale
- **샘플링 전략**: 환경 미생물 연구 best practices
- **Biogeography**: 공간 분포 패턴 이해

</details>

## 📋 발표 요약

<details>
<summary><b>🔹 발표 1: Yusuke Okazaki (Kyoto) - Single-cell Genomics</b> ⭐ **기법!**</summary>

### Genomic Individuality at Single-cell Level

**핵심 연구**:
- Lake bacteria single-cell genomics
- **Microdiversity** (strain-level variants)
- **Long-read metagenomics** (complete MAGs)

### 왜 Single-cell?

**Bulk metagenomics 한계**:
- Strain mixing
- Incomplete genomes
- Loss of microdiversity

**Single-cell 장점**:
- Strain-level resolution
- Complete genomes
- **AMR clone tracking** (ST131, ST410)

### 도심 AMR 응용

```yaml
도심 환경 = "Urban Lake":
  Oligotrophic:
    - Treated water
    - Air

  Copiotrophic:
    - Wastewater
    - Biofilms

Single-cell for AMR:
  - Individual clone genomes
  - AMR gene + Plasmid linkage
  - Transmission network reconstruction
```

### 질문

"도심 환경 샘플에 single-cell genomics 적용 시 technical challenges? FACS가 복잡한 matrix에서 가능?"

</details>

<details>
<summary><b>🔹 발표 2: Sung-Keun Rhee (Chungbuk) - Methanotrophs</b></summary>

### N₂O Respiring Methanotrophs

**2024 Nature Commun**: Acidophilic methanotrophs can reduce N₂O!

**Dual benefit**:
- CH₄ → CO₂ (methanotrophy)
- N₂O → N₂ (denitrification)

**도심 연결**: Constructed wetlands (수처리)

**우선순위**: 낮음 (AMR 직접 관련 적음)

</details>

<details>
<summary><b>🔹 발표 3: Haiyan Chu (Chinese Academy) - Soil Biogeography</b></summary>

### Global Soil Microbial Distribution

**연구 범위**:
- China + Global
- **Drivers**: pH (strongest!), Climate, Vegetation

### 도심 응용

**Urban soil AMR biogeography**:
```yaml
Sampling:
  - Parks (20+ sites)
  - Playgrounds
  - Street trees

Drivers:
  - pH
  - Distance to hospitals
  - Land use (residential, commercial)
  - Pollution (heavy metals)
```

### 질문

"Urban soil AMR biogeography 연구 시 sampling strategy? pH 외 주요 drivers?"

</details>

<details>
<summary><b>🔹 발표 4-5: Antarctic & Freshwater (Short talks)</b></summary>

**Hanbyul Lee (KOPRI)**: Antarctic extreme environments
**Hongjae Park (Inha)**: Continental-scale freshwater gene catalogue

**도심 연결** (간접):
- Extreme environments → Urban "extremes" (deep subway)
- Gene catalogue → Urban water AMR gene inventory

**우선순위**: 낮음-중간

</details>

## 🧠 S12 핵심 Takeaways

### Metagenomics Methods

| Method | Pros | Cons | AMR Application |
|--------|------|------|-----------------|
| **Bulk metagenomics** | High throughput | Strain mixing | Community profiling |
| **Single-cell** | Strain-level | Low throughput | Clone tracking |
| **Long-read** | Complete MAGs | High cost | Plasmid context |

### 도심 AMR 통합

```yaml
Tier 1 - Broad (Urban gene catalogue):
  - 100+ sites
  - AMR gene inventory

Tier 2 - Medium (Community):
  - District-level
  - Diversity, drivers

Tier 3 - High Resolution (Strain):
  - Hotspots
  - Single-cell genomics
```

### 네트워킹

1. **Yusuke Okazaki** (Kyoto) - Single-cell expertise
2. **Hongjae Park** (Inha) - 국내, Freshwater genomics

---

# 나머지 세션 빠른 가이드

## 📅 Day 1 (10/26 일요일)

<details>
<summary><b>13:30-15:30 | 첫 세션 선택</b></summary>

| 세션 | 점수 | 추천 이유 | 대안 시 |
|------|------|-----------|---------|
| **W1: Bacterial Genome Analysis** ⭐ | 85 | 메타지노믹스 실습, 사전 등록 필요 | S1으로 |
| **S1: Bacterial Pathogenesis** | 75 | AMR 병원성 기초, VI형 분비, VBNC | W1 불가 시 |
| S2: Diet-Microbiome | 50 | 마이크로바이옴 (간접 관련) | - |

**추천**: **W1 (등록 가능 시)** → S1 (대안)

</details>

## 📅 Day 2 (10/27 월요일) ⭐ **가장 중요!**

<details>
<summary><b>09:00-11:00 | 아침 세션 (필수!)</b></summary>

**추천**: **S4 - Respiratory Bacterial Pathogens** (95점)
- 항생제 신규 타겟
- MRSA, Pseudomonas, Mycobacteria
- **필수 참석!**

**대안**: 없음 (S4 필수)

</details>

<details>
<summary><b>13:50-15:50 | 오후 세션 (최우선!)</b></summary>

**추천**: **S8 - Diagnosis & Treatment** (98점)
- AMR 진단 기술
- CN-TAR, P-FS, SENSR
- **최우선 필수!**

**대안**: S10 Green Microbiome (75점) - 메타지노믹스 기법

</details>

<details>
<summary><b>16:00-18:00 | 저녁 세션</b></summary>

**추천**: **S12 - Environment** (88점)
- Single-cell genomics
- 환경 메타지노믹스

**대안**: S14 Proteomics (70점) - 멀티오믹스 통합

</details>

## 📅 Day 3 (10/28 화요일)

<details>
<summary><b>09:00-11:00 | 아침 세션</b></summary>

| 세션 | 점수 | 추천 이유 |
|------|------|-----------|
| **S17: Zoonosis** ⭐ | 80 | One Health AMR, 항균 stewardship |
| S18: Biosystems | 65 | 합성생물학 항생제 생산 |
| S19: Biosafety | 40 | 규제 중심 (낮은 관련성) |

**추천**: **S17**

</details>

<details>
<summary><b>14:00-16:00 | 마지막 세션</b></summary>

| 세션 | 점수 | 추천 이유 |
|------|------|-----------|
| **W5: Statistics Workshop** ⭐ | 82 | 메타지노믹스 통계, 사전 등록 필요 |
| **S20: Epidemic Disasters** | 78 | 국가 감시 체계, mRNA 백신 |
| S21: Microbial Biotechnology | 68 | 산업 응용 |

**추천**: **W5 (등록 가능 시)** → S20 (대안)

</details>

---

# 📊 최종 일정표 (한눈에)

## Day 1 (10/26 일)

```
13:30 ┃ W1 게놈 분석* (85) or S1 병원성 (75)
15:40 ┃ PL1 Plenary ✓
16:30 ┃ Poster Session 1 + Reception 🤝
```

## Day 2 (10/27 월) ⭐

```
09:00 ┃ S4 호흡기 병원체 - 항생제 타겟 (95) ← 필수!
11:10 ┃ PL2 Plenary ✓
11:50 ┃ Lunch
13:00 ┃ PL3 Plenary ✓
13:50 ┃ S8 진단·치료 - AMR 검출 (98) ← 최우선!
16:00 ┃ S12 환경 - 메타지노믹스 (88)
18:00 ┃ Poster Session 2 + Reception 🤝
```

## Day 3 (10/28 화)

```
09:00 ┃ S17 인수공통감염병 (80)
11:10 ┃ PL4 Plenary ✓
13:00 ┃ MSK Award Lecture ✓
14:00 ┃ W5 통계* (82) or S20 감염병 (78)
16:00 ┃ Closing Ceremony ✓
```

`*유료 워크샵 - 사전 등록 필요`

---

# ⚡ 전체 준비 체크리스트

## 📚 사전 준비 (학회 전)

- [ ] **워크샵 등록 확인** (W1, W5) - 유료, 마감 확인!
- [ ] 논문 읽기
  - [ ] Wonsik Lee (2025) - S. aureus niche adaptation
  - [ ] Eun-Kyung Lim (2025) - CN-TAR airborne AMR
  - [ ] Yoon-Kyoung Cho (2025) - Fidget spinner SERS
  - [ ] Okazaki (2022) - Long-read metagenomics
  - [ ] Rhee (2024) - Methanotroph N2O respiration
- [ ] 명함 준비 (한글/영문 각 20장)
- [ ] 질문 리스트 정리 (각 세션별)
- [ ] 노트북/태블릿 + 충전기

## 🎯 세션별 핵심 질문

### S4 (항생제 타겟)

1. **[Yeom]** KdsB inhibitor 구조? 메타지노믹 kdsB variants로 감수성 예측?
2. **[Lee W]** Tn-Seq 도심 환경 적용 가능성?
3. **[Shin]** NTM 환경 감시 전략?

### S8 (진단)

1. **[Lim]** CN-TAR air sampling 방법? Multiplex 가능?
2. **[Cho]** P-FS SERS로 AMR phenotype 구별? 환경 샘플 적용?
3. **[Lee J]** SENSR 메타전사체 적용? Multiplex 한계?

### S12 (환경)

1. **[Okazaki]** 도심 환경 single-cell genomics 기술적 챌린지?
2. **[Chu]** Urban soil AMR biogeography sampling strategy?
3. **[Park]** Urban water gene catalogue 권장 샘플 수?

## 🤝 최우선 네트워킹 (Top 5)

1. **Eun-Kyung Lim** (KRIBB) - CN-TAR, Airborne AMR ⭐⭐⭐
2. **Jinki Yeom** (SNU) - 신규 항생제 ⭐⭐⭐
3. **Yoon-Kyoung Cho** (UNIST) - P-FS, Portable ⭐⭐⭐
4. **Wonsik Lee** (SKKU) - Tn-Seq, Niche adaptation ⭐⭐
5. **Sung Jae Shin** (Yonsei) - NTM 환경 감시 ⭐⭐

## 📱 Notion 활용 팁

### 모바일에서

- 노션 앱 설치
- 오프라인 모드 활성화 (학회장 WiFi 불안정 대비)
- 각 세션 checkbox 실시간 체크
- 메모 추가 (연사 코멘트, 추가 질문)

### 공유하기

- 우측 상단 `Share` → `Copy link`
- 팀원/동료와 공유
- 댓글로 실시간 협업

### Toggle 활용

- 각 발표 details를 접었다 펼 수 있음
- 필요한 부분만 focus
- 모바일에서 스크롤 최소화

---

# 🎯 예상 성과

학회 참석 후 얻을 수 있는 것:

## 기술/방법론

✅ 신규 항생제 타겟 발굴 전략 (S4)
✅ 현장 AMR 진단 플랫폼 (S8: CN-TAR, P-FS, SENSR)
✅ 환경 메타지노믹스 sampling & 분석 (S12: Single-cell, Biogeography)
✅ 게놈/통계 분석 실습 (W1, W5)

## 네트워킹

✅ KRIBB, UNIST, SNU 핵심 연구자 5명+ 연결
✅ Collaborative study 기회 (CN-TAR, P-FS)
✅ 기술 자문 가능 (Single-cell genomics, Tn-Seq)

## 연구 아이디어

✅ 도심 대기 AMR 실시간 감시 시스템 (CN-TAR)
✅ Portable 진단 플랫폼 통합 (P-FS + SENSR)
✅ 메타지노믹스 + Targeted diagnostics 통합 전략
✅ Urban AMR biogeography 연구 설계

---

**마지막 Tip**: 각 세션 후 5분 내로 핵심 내용 메모, 명함 뒷면에 대화 내용 기록, 3일 내 follow-up email 발송! 🚀
