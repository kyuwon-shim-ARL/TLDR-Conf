# 배경 자료: Session 4 - Antibiotic Development

**세션**: Session 4: Antibiotic Development
**연사**: Jaehoon Yu (CAMP Therapeutics), Hee-Jong Hwang (A&J Science), Yan Lee (Seoul Natl. Univ.)
**일시**: 2025년 10월 30일 (목) 16:40-17:55
**장소**: 성균관대학교 의과대학, AI 강의실 3304

**중요도**: ⭐⭐⭐⭐⭐ (98/100점)

---

## 🎯 세션 개요

### 왜 이 세션이 중요한가?

**1. 실제 신약 후보 물질을 다룬다 (학계를 넘어 산업으로)**
- CAMP Therapeutics: methotrexate-CPP conjugate (preclinical)
- A&J Science: Thiopeptide antibiotics (GMP 생산, 임상 준비)
- Seoul National Univ.: pH-responsive peptides (in vivo 효과 확인)
- 모두 실제 개발 단계 (논문이 아닌 제품)

**2. 그람음성균 문제를 정면 돌파한다**
- 외막(outer membrane) = 항생제 개발의 최대 난제
- 2024년 FDA 승인 항생제: 그람음성균용 거의 없음
- 이 세션의 3가지 접근: 모두 그람음성균 타겟팅
  - CPP (cell-penetrating peptide): 외막 통과
  - Thiopeptides: 리보솜 표적 (광범위)
  - Hinged peptides: pH 변화로 선택적 활성화

**3. 차세대 항생제의 3가지 핵심 전략을 제시한다**
- **Drug repurposing**: Methotrexate (항암제) → Antibiotic
- **Natural products**: Thiopeptides (해양 미생물)
- **Rational design**: pH-responsive peptides (감염 부위 특이적)

**4. 포닥/산업계 진로에 직접 도움이 된다**
- 바이오텍 창업 사례 (CAMP, A&J)
- 대학-산업 연계 (Seoul Nat'l - 기술이전)
- Regulatory pathway (FDA, MFDS) 경험 공유

---

## 🌟 쉬운말 풀이 (세션 전체)

### 이 세션은 쉽게 말하면...

**한 줄 요약**: "그람음성균을 잡기 어려운 이유는 '외막'인데, 그 외막을 뚫거나, 우회하거나, 선택적으로 공략하는 3가지 신약 후보를 소개"

### 🎬 그람음성균과의 전쟁 - 이야기로 이해하기

**[1장: 외막의 저주 - Why Gram-Negative Bacteria Are Hard to Kill]**

**배경**: 항생제의 "베를린 장벽"

```
그람양성균 vs. 그람음성균:

그람양성균 (S. aureus, Streptococcus):
- 세포벽: Peptidoglycan (PG) 두꺼움 (20-80 nm)
- 외막: 없음
- 항생제 투과: 상대적으로 쉬움
→ 많은 항생제 개발 성공 (penicillin, vancomycin, daptomycin)

그람음성균 (E. coli, P. aeruginosa, K. pneumoniae):
- 세포벽: PG 얇음 (7-8 nm)
- 외막 (OM): 있음!
  → Lipopolysaccharide (LPS): 음전하 띔
  → Porin channels: 크기/전하 선택성
  → Efflux pumps: 약물 배출

- 항생제 투과: 매우 어려움
→ 신약 개발 거의 없음 (2010-2020: FDA 승인 그람음성균 항생제 3개뿐)
```

**전환점**: 외막을 어떻게 돌파할 것인가?

```
문제: 외막의 3중 방어선
1. LPS (lipopolysaccharide)
   - 음전하 → 양전하 항생제 정전기 상호작용
   - 하지만 완벽한 장벽은 아님 (일부는 통과)

2. Porin channels
   - 크기 제한: ~600 Da
   - 친수성 분자만 통과
   → 대부분의 항생제 (친유성, 큰 분자량) 차단

3. Efflux pumps
   - AcrAB-TolC (E. coli), MexAB-OprM (P. aeruginosa)
   - 세포 내 들어온 약물도 다시 배출
   → 내성의 주요 메커니즘

기존 해결책:
- Polymyxin (colistin): LPS와 결합, 외막 파괴
  → 문제: 독성 (신독성), 내성 출현
- Carbapenem: Porin 통과 가능
  → 문제: 내성 (carbapenemase)

→ 새로운 해결책 필요!
```

**[발견/의미]**:

1. **Jaehoon Yu (CAMP)의 접근: "Trojan Horse" 전략**
   - Methotrexate (MTX): 항암제 (DHFR 억제제)
   - 문제: 그람음성균 외막 통과 못함
   - 해결: Cell-Penetrating Peptide (CPP) 결합
     → 1403 peptide: Proline-rich, helical structure
     → 외막 통과 → cytosol 도달
   - 결과: E. coli NDM1 (carbapenem 내성) 사멸
     - MIC: 15 mg/kg dose로 10⁵-fold CFU ↓
   - **의미**: 기존 약물 (FDA 승인) 재활용 가능

2. **Hee-Jong Hwang (A&J)의 접근: 자연의 무기고**
   - Thiopeptides: 해양 미생물 천연물
   - 특징: 황(S) 함유 고리형 펩타이드
     → Ribosome (50S subunit) 표적
     → Protein synthesis 억제
   - 예: Micrococcin P2 derivatives
     - C. difficile (장독소): MIC < 1 μg/mL
     - NTM (M. avium, P. aeruginosa): 효과 확인
   - 문제: 수용성 낮음, 독성
   - 해결: 화학 구조 최적화
     → 200,000배 수용성 향상 (decagram scale)
   - **의미**: 새로운 화학 scaffold, 광범위 스펙트럼

3. **Yan Lee (Seoul Nat'l)의 접근: 스마트 펩타이드**
   - Hinged Amphipathic Peptides (HAP)
   - 설계: Lysine → Histidine 치환
     → pH 7.4 (혈액): 중성 (비활성)
     → pH 6.5 (감염 부위): 양전하 (활성)
   - 메커니즘:
     → pH ↓ → Histidine protonation → 양전하 ↑
     → Bacterial membrane 결합 → disruption
   - 효과:
     - A. baumannii skin infection: 병변 크기 ↓
     - E. coli NDM-1 bacteremia: 생존율 ↑
   - **의미**: 부위 특이적, 선택독성 낮음

**결론**: "그람음성균을 잡으려면, 외막을 '뚫거나'(CPP), '우회하거나'(Ribosome 표적), '조건부로 활성화'(pH-responsive) 해야 한다."

---

**[2장: Drug Repurposing - 오래된 약의 새로운 용도]**

**주요 개념 1: Methotrexate (MTX)의 이중 생활**

```
MTX의 원래 용도:
- 항암제: Leukemia, lymphoma 치료
- 면역억제제: 류마티스 관절염, psoriasis
- 메커니즘: Dihydrofolate reductase (DHFR) 억제
  → Tetrahydrofolate (THF) 합성 ↓
  → Purine, Pyrimidine 합성 ↓
  → DNA 합성 차단 → 세포 성장 정지

세균에도 DHFR 있음:
- E. coli, P. aeruginosa, K. pneumoniae: DHFR 필수
- MTX가 세균 DHFR도 억제 가능 (in vitro)
- 문제: 외막 통과 못함 → MIC 매우 높음 (>256 μg/mL)

→ CPP로 해결
```

**주요 개념 2: Cell-Penetrating Peptide (CPP)**

```
CPP란?
- 10-30 아미노산 짧은 펩타이드
- 특징: 양전하 많음 (Arg, Lys) 또는 양친매성
- 기능: 세포막 통과 촉진
  → 약물, DNA, protein 전달

역사:
- 1988: TAT peptide (HIV-1 Tat protein 유래)
- 1990s: Penetratin, pAntp
- 2000s: 합성 CPP (oligo-arginine, R9)

메커니즘 (논쟁 중):
1. Direct penetration: 막을 직접 뚫음
2. Endocytosis: 세포내이입 → endosome escape
3. Transient pore: 일시적 구멍 형성

그람음성균 외막 통과:
- 기존 CPP: 대부분 진핵 세포용
- 1403 peptide (CAMP의 개발):
  → Proline-rich, helical
  → LPS와 상호작용
  → Porin 우회, 외막 통과
```

**Jaehoon Yu의 혁신: MTX-CPP Conjugate**

```
설계:
- MTX (DHFR 억제제)
- Linker (cleavable, e.g., ester bond)
- 1403 CPP (proline-rich, 외막 통과)

메커니즘:
1. CPP가 외막 통과 (E. coli)
2. Periplasm 도달
3. Linker cleavage (esterase)
4. MTX 방출
5. MTX가 cytosol 이동 → DHFR 억제
6. DNA 합성 차단 → 세균 사멸

In vitro 효과:
- E. coli NDM1 (carbapenem 내성): MIC 16 μg/mL (MTX alone >256)
- P. aeruginosa: MIC 32 μg/mL

In vivo 효과 (마우스 bacteremia):
- E. coli NDM1 감염 (복강)
- MTX-CPP 투여 (15 mg/kg, i.p.)
- 결과: CFU 10⁵-fold ↓, 생존율 100%

독성:
- MTX alone: 골수억제, 간독성 (화학요법 용량)
- MTX-CPP: 낮은 용량 (15 mg/kg), 선택독성
- 정상 세포: CPP 없으면 MTX 진입 어려움

→ 치료 지수 (TI): MTX alone보다 10배 이상 향상
```

**의미**:

"FDA 승인 약물 (MTX)을 재활용하면:
1. 안전성 데이터 이미 있음 (50년 사용 역사)
2. 개발 기간 단축 (10년 → 3-5년?)
3. 비용 절감 (신약 개발 대비 1/10)

CPP 기술은 다른 약물에도 적용 가능:
- Fluoroquinolone-CPP (내성균)
- Aminoglycoside-CPP (biofilm)
- Antifungal-CPP (Candida 외막)"

---

**[3장: Natural Products - 자연이 만든 항생제]**

**주요 개념 3: Thiopeptides의 재발견**

```
Thiopeptides란?
- 천연 항생제 (1940s 발견)
- 생산: 방선균 (Streptomyces), 해양 미생물
- 구조: 황(S) 함유 고리형 펩타이드 (30-50 amino acids)
  → Thiazole, oxazole rings
  → Macrocyclic structure

대표 물질:
- Micrococcin (1948 발견)
- Thiostrepton (수의용)
- Nosiheptide
- LFF571 (Merck, Phase 2 for C. difficile)

메커니즘:
- 50S ribosomal subunit 결합
- L11 protein + 23S rRNA 인근
- Elongation factor (EF-G, EF-Tu) 억제
→ Protein synthesis 차단

왜 잊혀졌나?
1. 수용성 낮음 (임상 투여 어려움)
2. 초기 독성 데이터 (동물 실험)
3. 다른 항생제 개발 성공 (β-lactam, fluoroquinolone)

왜 재부상?
1. AMR 위기 (신규 scaffold 필요)
2. 화학 합성 기술 발전 (수정 가능)
3. C. difficile 증가 (thiopeptides 효과적)
```

**Hee-Jong Hwang의 접근: Thiopeptides 최적화**

```
A&J Science 플랫폼:
1. 천연물 탐색
   - 해양 미생물 (>10,000 strains)
   - Fermentation 최적화
   - Micrococcin P2 발견

2. 구조-활성 관계 (SAR) 연구
   - Core macrocycle: 유지 (ribosome 결합 필수)
   - Side chain: 수정 (수용성, PK 개선)
   - Derivatization: 200+ analogs

3. Lead optimization
   - Micrococcin P2 derivatives:
     → 수용성: 200,000배 향상
     → 용해도: < 1 μg/mL → 20 mg/mL
     → GMP 생산: decagram scale (10-100 g)

   - Activity spectrum:
     → C. difficile: MIC 0.06-0.25 μg/mL (vancomycin 대비)
     → MRSA: MIC 2 μg/mL
     → P. aeruginosa: MIC 16 μg/mL
     → M. avium (NTM): MIC 8 μg/mL

4. Preclinical development
   - PK/PD: Half-life 2-4h (마우스), Cmax 적절
   - Toxicity: MTD > 100 mg/kg (마우스)
   - Efficacy (마우스 C. diff 감염):
     → Vancomycin 대비 동등 또는 우수
     → Recurrence 낮음 (microbiome 보존)

5. Regulatory path
   - FDA orphan drug designation (C. difficile)
   - Phase 1 준비 중 (2025-2026 예상)
```

**응용 사례: C. difficile 치료**

```
C. difficile infection (CDI):
- 미국: 연간 500,000 cases, 29,000 deaths
- 한국: 증가 추세 (고령화, 항생제 오남용)
- 문제: Vancomycin/metronidazole 후 재발률 20-30%

Thiopeptides의 장점:
1. Narrow spectrum:
   - C. difficile만 죽임
   - 정상 장내 균총 보존 → 재발 ↓

2. Resistance 낮음:
   - Ribosome 표적 (conserved)
   - Cross-resistance 적음

3. 경구 투여 가능:
   - 장에서 흡수 안 됨 (수용성 낮음이 오히려 장점)
   - Local action

→ Vancomycin 대체제로 유망
```

**의미**:

"자연은 이미 수백만 년 동안 항생제를 만들어왔다.
우리는 그것을 '찾아서', '개선해서', '임상에 적용'하면 된다.
Thiopeptides는 잊혀진 보물이었고, 이제 다시 빛을 본다."

---

**[4장: Rational Design - 맞춤형 항생제 설계]**

**주요 개념 4: pH-Responsive Peptides**

```
감염 부위의 pH:
- 정상 조직: pH 7.4
- 감염/염증: pH 6.0-6.5
  → 이유: Bacterial metabolism (lactic acid)
         Immune cell activity (acidification)
         Hypoxia (혐기성 대사)

pH 변화 활용:
- Tumor targeting (종양도 pH 낮음)
- Infection-specific activation

Histidine (His)의 특성:
- pKa ~6.0 (physiological range)
- pH 7.4: 중성 (비양성자화)
- pH 6.0: 양전하 (양성자화)

→ Histidine-rich peptides = pH-responsive
```

**Yan Lee의 설계: KLH3/KLH4 Peptides**

```
기존 peptide: KL4-9P (Lys-Leu rich)
- 구조: Hinged amphipathic
  → Hydrophobic face (Leu)
  → Hydrophilic face (Lys)
- 문제: 항상 양전하 → 비선택적
  → 정상 세포 독성 (Hemolysis)

Lee의 수정: Lys → His 치환
- KLH3: 3개 Lys → His
- KLH4: 4개 Lys → His

pH 의존성:
- pH 7.4 (혈액):
  → His 중성 → 양전하 감소
  → Membrane binding 약함
  → Hemolysis < 5%

- pH 6.5 (감염):
  → His 양성자화 → 양전하 증가
  → Membrane binding 강함
  → Bacterial lysis ↑

메커니즘:
1. Peptide가 감염 부위 도달
2. pH 감지 (His protonation)
3. 양전하 증가 → 세균막 결합
4. Membrane disruption (pore formation)
5. 세균 사멸

In vitro activity:
- A. baumannii: MIC 4-8 μg/mL (KLH3/4)
  vs. 16 μg/mL (KL4-9P, pH 7.4에서도)
- E. coli: MIC 8-16 μg/mL

In vivo efficacy:
- A. baumannii skin infection (마우스):
  → KLH3 topical: 병변 크기 70% ↓
  → Superior to mupirocin

- E. coli NDM1 bacteremia:
  → KLH3 i.p.: 생존율 80% (control 20%)
  → KL4-9P: 독성으로 60% 사망

Selectivity:
- pH 7.4: MPS (mononuclear phagocyte system) 안전
- pH 6.5: 감염 부위만 활성
→ Therapeutic index: 10배 향상
```

**의미**:

"항생제는 '언제나 ON'일 필요 없다.
감염 부위에서만 '스위치 ON'되면 된다.
pH-responsive peptides는 '스마트 항생제'의 첫 걸음이다.

미래 응용:
- Temperature-responsive (열 감지)
- Enzyme-responsive (protease cleavage)
- Light-responsive (photodynamic)

→ Precision antibiotics의 시대"

---

## 📋 발표별 상세 분석

### 🔹 발표 1 (16:40-17:05): Repositioning methotrexate for an antibiotic by conjugating to Gram-negative specific penetrating peptide

**연사**: Jaehoon Yu, CEO (CAMP Therapeutics)

#### 🌟 쉬운말 풀이 (S4-1)

**이 발표는 쉽게 말하면**: "항암제 methotrexate에 '외막 통과 펩타이드'를 붙이면, carbapenem 내성 E. coli도 잡는 신약이 된다"

**상황**: Carbapenem 내성의 공포

```
Carbapenem:
- "Last-resort" 항생제
- 그람음성균 중증 감염 (패혈증, 폐렴)
- 내성 메커니즘:
  → NDM-1, KPC, OXA-48 (carbapenemase)
  → Metallo-β-lactamase

문제:
- Carbapenem 내성 E. coli, K. pneumoniae 증가
- 미국: CRE (carbapenem-resistant Enterobacteriaceae)
  → 연간 13,000 감염, 1,100 사망
- 한국: 2020-2024, NDM-1 급증

대안:
- Colistin: 독성 높음 (신독성)
- Tigecycline: Bacteriostatic (살균 아님)
- Ceftazidime-avibactam: 비싼, NDM에 무효

→ 새로운 메커니즘 필요
```

**해결: MTX-CPP**

```
Why MTX?
- DHFR 억제제 (세균도 가짐)
- FDA 승인 (1953년)
- 안전성 데이터 풍부

Why CPP?
- 1403 peptide: 외막 통과
- Proline-rich, helical structure
- LPS binding → membrane insertion

결과:
- E. coli NDM1: MIC 16 μg/mL (단독 MTX >256)
- 15 mg/kg dose로 마우스 bacteremia 치료
- 부작용: 최소 (MTX 단독 대비)
```

#### 최근 연구 배경

**CAMP Therapeutics**:
- 설립: 2019년 (Seoul National University spin-off)
- CEO: Jaehoon Yu (Ph.D., 서울대)
- Pipeline: CPP-antibiotic conjugates
- 투자: Seed round $5M (2023)

**핵심 논문**:

```
📄 Choi Y, Choe HW, Kim Y, Yu J* (2024)
"Proline-Hinged Amphipathic α-Helical Peptide Targets
 Cardiolipin, Rescuing Eukaryotic Membranes from Influx
 of Anticancer Drugs to Triple-negative Breast Cancer"
J Med Chem. 67: 3385-3399

관련성: CPP 기술의 기초 (cancer cell도 외막 유사 장벽)

읽기 시간: 40분
중요도: ★★★★☆
```

#### 예상 발표 내용

```
1. AMR 위기와 그람음성균 문제
2. Drug repurposing 전략
3. MTX 메커니즘 (DHFR 억제)
4. 1403 CPP 설계 및 특성
5. MTX-CPP conjugate 합성
6. In vitro efficacy (E. coli, P. aeruginosa)
7. In vivo efficacy (마우스 bacteremia)
8. Toxicity & PK/PD
9. Clinical development plan
```

**핵심 메시지**:
- "기존 약물도 CPP와 결합하면 새 생명"
- "Carbapenem 내성균에 희망"
- "FDA 경로 단축 가능"

#### 예상 질문

**Q1**: MTX의 면역억제 효과가 감염 치료 시 문제되지 않는가?
**Q2**: CPP의 immunogenicity는? (반복 투여 시)
**Q3**: Resistance 발생 가능성은? (DHFR mutation)

---

### 🔹 발표 2 (17:05-17:30): Developing New Antibiotics from Thiopeptide Natural Products

**연사**: Hee-Jong Hwang, CEO (A&J Science)

#### 🌟 쉬운말 풀이 (S4-2)

**이 발표는 쉽게 말하면**: "바다 미생물이 만드는 '황 펩타이드' 항생제를 찾아서, 물에 잘 녹게 개량하면, C. difficile과 NTM을 잡는 신약이 된다"

**상황**: C. difficile의 재앙

```
CDI 증가:
- 고령화, 항생제 오남용
- 재발률: 20-30% (vancomycin 후)
- 사망률: 5-10% (중증)

기존 치료:
- Vancomycin (경구): 효과 있지만 재발
- Metronidazole: 효과 감소
- Fidaxomicin: 비쌈 ($3,000/course)

문제: Broad-spectrum 항생제
→ 정상 장내 균총 파괴
→ C. diff 재증식 기회

→ Narrow-spectrum 필요
```

**해결: Thiopeptides**

```
Micrococcin P2:
- C. difficile MIC: 0.06-0.25 μg/mL
- 정상 균총: 영향 적음
- Ribosome 표적 (내성 어려움)

개선:
- 수용성: 200,000배 ↑
- GMP 생산: decagram scale
- 경구 제형 개발

→ Phase 1 준비 (2025-2026)
```

#### 최근 연구 배경

**A&J Science**:
- 설립: 2021년
- CEO: Hee-Jong Hwang (Ph.D., UBC)
- 기술: Marine microbial natural products
- Pipeline: Thiopeptides for CDI, NTM

**핵심 논문**:

```
📄 Park J, Kim D, Hwang HJ* et al. (2023)
"Identification of Micrococcin P2-Derivatives as
 Antibiotic Candidates Against Two Gram-Positive Pathogens"
J Med Chem. 66: 14265-14277

핵심 내용:
- 200+ Micrococcin analogs
- SAR study
- C. difficile, MRSA activity

읽기 시간: 50분
중요도: ★★★★★
```

#### 예상 발표 내용

```
1. Thiopeptides 역사 및 재부상
2. Micrococcin P2 발견 (해양 미생물)
3. Ribosome 표적 메커니즘
4. Structure optimization (수용성, PK)
5. Spectrum (C. diff, MRSA, NTM)
6. Preclinical data (efficacy, toxicity)
7. GMP production (decagram scale)
8. Regulatory strategy (Orphan drug)
9. Clinical development timeline
```

**핵심 메시지**:
- "자연이 만든 항생제를 개량"
- "C. difficile 재발 문제 해결"
- "NTM에도 효과 (보너스)"

#### 예상 질문

**Q1**: 경구 흡수율은? (bioavailability)
**Q2**: Microbiome에 미치는 영향은? (16S sequencing data)
**Q3**: Thiostrepton과의 차별점은?

---

### 🔹 발표 3 (17:30-17:55): Hinged amphipathic peptides with pH-inducible positive charges against Gram-negative bacteria in infection sites

**연사**: Yan Lee, Professor (Seoul National University)

#### 🌟 쉬운말 풀이 (S4-3)

**이 발표는 쉽게 말하면**: "감염 부위는 pH가 낮은데, 그 pH 변화를 감지해서 '활성화'되는 펩타이드 항생제를 만들면, 정상 조직은 안전하고 세균만 죽인다"

**상황**: Antimicrobial peptides의 딜레마

```
AMPs (항균 펩타이드):
- 장점: 내성 어려움, 광범위 효과
- 단점: Hemolysis (적혈구 파괴), 독성

문제: 선택성 부족
- 세균막과 인간 세포막 유사 (lipid bilayer)
- 양전하 AMP: 둘 다 공격

→ 선택적 활성화 필요
```

**해결: pH-Responsive Peptides**

```
KLH3/KLH4:
- Histidine-rich (pKa 6.0)
- pH 7.4: 중성 → 독성 낮음
- pH 6.5: 양전하 → 항균 활성

결과:
- Hemolysis: < 5% (pH 7.4)
- A. baumannii killing: > 90% (pH 6.5)
- In vivo: 피부 감염, bacteremia 모두 효과

→ Therapeutic index: 10배 향상
```

#### 최근 연구 배경

**Yan Lee**:
- Professor, Dept of Chemistry, Seoul National Univ.
- 전문: Peptide chemistry, drug delivery
- 2024: Associate Dean (연구 부학장)

**핵심 논문**:

```
📄 Seleci M, et al., Lee Y* (2023)
"Selective delivery of protein drug function control of protein drug
 function Choi S, Lee Y, Hwang J, Chun D, Koo H, Lee Y*"
Chem Eng J. 457: 141229

관련성: pH-responsive delivery system

읽기 시간: 30분
중요도: ★★★★☆
```

#### 예상 발표 내용

```
1. AMPs 개요 및 한계
2. pH-responsive 전략
3. Histidine 화학 (pKa)
4. KLH3/KLH4 설계
5. In vitro activity (pH 의존성)
6. Hemolysis assay
7. In vivo efficacy (A. baumannii, E. coli)
8. Mechanism (membrane disruption)
9. Future: 다른 stimuli-responsive
```

**핵심 메시지**:
- "스마트 항생제 = 필요할 때만 ON"
- "Selectivity가 독성을 결정"
- "Precision medicine의 시작"

#### 예상 질문

**Q1**: pH 6.5는 모든 감염 부위에서 보장되는가?
**Q2**: Protease stability는? (혈액 내)
**Q3**: Chronic infection (biofilm)에서 pH는?

---

## 🧠 세션 핵심 요약 (10가지)

1. **그람음성균 외막 = 항생제 개발 최대 난제**
2. **CPP technology로 기존 약물 재활용 가능**
3. **Thiopeptides = 잊혀진 보물, 다시 부상**
4. **pH-responsive = 감염 부위 특이적 치료**
5. **Drug repurposing이 신약 개발보다 빠르고 저렴**
6. **자연물 (marine microbes)에서 신규 scaffold 발굴**
7. **Selectivity가 독성과 efficacy 모두 결정**
8. **Carbapenem 내성균에 희망 (MTX-CPP)**
9. **C. difficile 재발 문제 해결 가능 (thiopeptides)**
10. **산학 협력 모델 (CAMP, A&J 바이오텍 사례)**

---

## 🎤 질문 리스트 (30개)

### 과학적 질문 (10개)

**Q1-3**: MTX, Thiopeptides, KLH3 각각의 resistance 발생 가능성은?

**Q4**: CPP의 immunogenicity가 반복 투여 시 문제되지 않는가?

**Q5**: Thiopeptides가 정상 장내 균총에 미치는 영향은? (Microbiome data)

**Q6**: pH 6.5가 모든 감염 부위에서 보장되는가? (Biofilm 내부는?)

**Q7**: MTX-CPP가 인간 세포에 진입 가능한가? (독성 우려)

**Q8**: Thiopeptides의 ribosome 표적이 mitochondrial ribosome에도 영향?

**Q9**: KLH peptides가 protease에 의해 분해되는가?

**Q10**: 3가지 접근법을 병용하면 시너지 효과가 있을까?

### 기술/방법론 질문 (10개)

**Q11-13**: MTX-CPP linker cleavage 효율은? Thiopeptides GMP 수율은? KLH peptides 합성 비용은?

**Q14**: CPP의 외막 통과 메커니즘 증명 방법은? (형광, EM?)

**Q15**: Thiopeptides 경구 제형은? (캡슐, 정제?)

**Q16**: KLH peptides의 최적 pH는? (6.0? 6.5? 7.0?)

**Q17**: In vivo PK/PD 파라미터는? (Cmax, AUC, half-life)

**Q18**: Resistance selection study 했는가? (serial passage)

**Q19**: Animal model 선택 기준은? (마우스 외 다른 동물?)

**Q20**: Safety pharmacology study 범위는?

### 응용/산업 질문 (7개)

**Q21**: CAMP의 MTX-CPP Phase 1 시기는?

**Q22**: A&J의 Thiopeptides FDA orphan drug 지정 받았나?

**Q23**: Seoul Nat'l의 KLH peptides 기술이전 계획은?

**Q24**: 제조 원가는? (투여 1회당)

**Q25**: 특허 상황은? (CPP, Thiopeptides, KLH)

**Q26**: Reimbursement 전략은? (보험 적용)

**Q27**: 글로벌 시장 vs. 한국 시장 우선순위는?

### 진로 질문 (3개)

**Q28**: 바이오텍 창업 시 가장 어려운 점은?

**Q29**: 대학 연구실 vs. 바이오텍 career path?

**Q30**: 포닥을 CAMP/A&J에서 채용하나?

---

## 🤝 네트워킹 우선순위

### Tier 1: CEO/Professor

#### Jaehoon Yu (CAMP Therapeutics)
- 바이오텍 창업 경험
- CPP technology licensing 가능
- 포닥/연구원 채용 가능성

#### Hee-Jong Hwang (A&J Science)
- Marine natural products 전문
- GMP 생산 경험
- Partnership 기회

#### Yan Lee (Seoul National University)
- Peptide chemistry 권위자
- 기술이전 경험
- 학생/포닥 모집

### Tier 2: 산업계 인사

- 제약사 BD (business development)
- 투자자 (VC, angel)
- CRO/CDO (preclinical service)

### Tier 3: 정부/규제

- MFDS (식약처) 담당자
- KHIDI (보건산업진흥원)
- NRF (연구재단) PM

---

## ⚡ 당일 체크리스트

### D-1
- [ ] 배경 자료 2차 정독
- [ ] 3명 연사 회사/연구실 웹사이트 확인
- [ ] Pipeline, publication 파악
- [ ] 명함 30장

### 세션 중
- [ ] 핵심 슬라이드 사진
- [ ] 질문 2-3개
- [ ] Networking 대상 파악

### 세션 후
- [ ] 연사 접근 (각 3분)
- [ ] 명함 교환
- [ ] Follow-up 계획

---

## 📊 학습 성과

### 지식
- Drug repurposing 전략 이해
- CPP, Thiopeptides, pH-responsive 메커니즘
- Regulatory pathway (FDA, MFDS)

### 기술
- Conjugation chemistry
- Natural product optimization
- Peptide design

### 태도
- 산학 협력 가치
- 창업 가능성
- 번역 연구 (bench-to-bedside)

### 네트워크
- CEO 2명, Professor 1명
- 바이오텍 업계 진입점
- 투자자/CRO 접점

---

**문서 작성**: 2025-10-29
**버전**: 2.0
**학회**: IAMRT 2025

**이 세션은 '실제 신약 개발'을 다룹니다. 포닥/산업 진로에 직접 도움됩니다!**

**Good luck! 🎉🔬💊**