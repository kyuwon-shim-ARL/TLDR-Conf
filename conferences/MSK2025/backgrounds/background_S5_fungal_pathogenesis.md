# 배경 자료: S5 진균 병원성

**세션**: S5 - Fungal Pathogenesis
**일시**: 2025년 10월 27일 (월) 09:00-11:00
**장소**: Rm 304+305
**Co-organized**: Kangwon Intelligence Convergence Research Center
**Chair**: Jaehyuk Choi (Incheon National University) & Jung-Shin Lee (Kangwon National University)
**중요도**: ⭐⭐⭐⭐ (85/100점) - **진균 연구자 필수!**

---

## 🎯 세션 개요

이 세션은 **병원성 진균의 최신 연구**를 다룹니다. 특히 **다제내성 Candida auris**, **세포 외 소포체 (Extracellular Vesicles)**, **칼시뉴린 신호전달**, **N-glycan 품질관리** 등 2024-2025년 최신 발견이 포함되어 있습니다.

### 왜 이 세션이 중요한가?

- 🦠 **Candida auris 위기**: 전 세계 확산 중인 MDR 진균 (CDC "Urgent Threat")
- 🔬 **Extracellular Vesicles**: 진균-숙주 상호작용의 새로운 패러다임
- 💊 **Calcineurin 타겟팅**: 신규 항진균제 개발 전략
- 🧬 **N-glycan QC**: 진균 특이적 품질관리 시스템

### 이 세션의 공통 테마

```
진균 생존 & 병원성
├─ 유전자 조절 (C. auris transcription networks)
├─ 세포 간 통신 (Extracellular vesicles)
├─ 신호 전달 (Calcineurin pathway)
└─ 품질 관리 (N-glycan-dependent ERQC)
```

---

## 📋 발표별 상세 분석

### 🔹 발표 1 (09:00-09:30)

**연사**: Yong-Sun Bahn (반용선)
**소속**: Yonsei University (연세대학교)
**제목**: Systematic functional analysis of the transcription factor networks in the emerging multidrug-resistant fungal pathogen *Candida auris*

#### 최근 연구 배경 (2025)

Bahn 교수팀은 **2025년 4월 mBio**에 주요 리뷰를 발표했습니다:

**"Signaling pathways governing the pathobiological features and antifungal drug resistance of Candida auris"**

**핵심 발견**:
- **Transcription factor (TF) networks** 체계적 분석
- **Rpn4**: Efflux pump 과발현 → Fluconazole 저항성
- **Mrr1/Mdr1 pathway**: Azole 저항성 핵심 경로
- **Upc2**: Ergosterol biosynthesis 조절
- **GFC1**: C2H2 zinc finger TF, 필라멘트 형성 + 피부 colonization

#### 예상 발표 내용

**1. Candida auris: 글로벌 위협**

**특징**:
- **다제내성 (MDR)**: Azoles, Echinocandins, Polyenes
  - Some strains: Pan-resistant (모든 항진균제 저항)
- **전염성**: Healthcare-associated transmission
  - Contact precautions 필요
  - Biofilm on medical devices
- **Identification 어려움**: Misidentified as C. haemulonii
- **Thermotolerance**: 37-42°C growth (체온 + 발열)

**역학**:
```yaml
발견: 2009년 (일본, 환자 귀에서)
확산: 2013~ 전 세계 (6 clades)
  - South Asian clade (India, Pakistan)
  - East Asian clade (Japan, Korea)
  - African clade
  - South American clades (2개)
  - Iranian clade (2024 발견)

사망률: 30-60% (혈류 감염)
위험군: ICU, 면역저하자
```

**CDC Classification**: "Urgent Threat" (가장 높은 등급)

**2. Transcription Factor Networks**

**체계적 접근**:
```
1. C. auris genome annotation → ~150 TFs 예측
2. Deletion library 구축 (각 TF knockout)
3. Phenotypic screening:
   - 항진균제 감수성
   - Biofilm 형성
   - Filamentation
   - Thermotolerance
   - Virulence (마우스 모델)
4. Transcriptomics (RNA-seq)
5. Network reconstruction
```

**주요 TF와 기능**:

**A. 항진균제 저항성 TFs**:

| TF | Target Pathway | Antifungal | Mechanism |
|----|---------------|------------|-----------|
| **Rpn4** | Proteasome + Efflux | Fluconazole | MDR1, CDR1 ↑ |
| **Mrr1** | Multidrug efflux | Azoles | MDR1 과발현 |
| **Upc2** | Ergosterol biosynthesis | Azoles | ERG genes ↑ |
| **Tac1** | ABC transporters | Fluconazole | CDR1/CDR2 ↑ |

**B. 병원성 TFs**:

| TF | Function | Phenotype |
|----|----------|-----------|
| **GFC1** | Filamentation | Hyphal formation, 피부 colonization ↑ |
| **Efg1** | Morphogenesis | 백색-투명 switching |
| **Ahr1** | Adhesion | 숙주 세포 부착 |

**3. Rpn4: 핵심 조절자**

**Rpn4 (Regulatory particle non-ATPase 4)**:
- **원래 기능**: Proteasome 유전자 전사 조절
- **C. auris에서 발견**: Efflux pump도 조절!

**메커니즘**:
```
Azole exposure
  ↓
Rpn4 activation (자가 조절)
  ↓
Rpn4 binds to promoters:
  - Proteasome genes (PACE, 26S subunits)
  - Efflux pump genes (MDR1, CDR1)
  ↓
Increased expression
  ↓
Azole efflux ↑ + Protein degradation ↑
  ↓
Drug resistance
```

**Rpn4 deletion (rpn4Δ)**:
- Fluconazole MIC 감소 (8-16배)
- Proteasome function ↓
- Stress sensitivity ↑

**4. Mrr1/Mdr1 Pathway**

**Mrr1 (Multidrug Resistance Regulator 1)**:
- **C2H2 zinc finger TF**
- **Constitutive activation** in clinical isolates
  - Gain-of-function mutations
  - N-terminal truncations

**Mdr1 (Major facilitator superfamily transporter)**:
- **Target**: Mrr1의 주요 downstream gene
- **Function**: Azole efflux
- **Overexpression**: Mrr1 GOF mutations → Mdr1 ↑↑

**Clinical relevance**:
```yaml
Fluconazole-resistant C. auris isolates:
  - 70-80%: Mrr1 GOF mutations
  - Mdr1 expression: 50-100배 증가
  - MIC: >256 μg/mL (WT: 1-2 μg/mL)
```

**5. Upc2 & Ergosterol Biosynthesis**

**Upc2 (Uptake control 2)**:
- **Zinc cluster TF**
- **Ergosterol biosynthesis genes** 조절
  - ERG1, ERG3, ERG11 (lanosterol 14α-demethylase = azole target)

**Azole 저항 메커니즘**:
```
Upc2 GOF mutations
  ↓
ERG11 overexpression
  ↓
더 많은 Erg11 enzyme
  ↓
Azole binding 포화 (competitive)
  ↓
일부 Erg11 활성 유지
  ↓
Ergosterol 합성 계속
  ↓
Azole resistance
```

**6. GFC1 & Filamentation**

**GFC1 (Germ tube Formation Control 1)**:
- **C2H2 zinc finger TF**
- **Filamentation 필수**: gfc1Δ → No hyphae

**Phenotypes**:
```yaml
Wild-type:
  - Yeast ↔ Hyphal switching
  - Skin colonization: High

gfc1Δ mutant:
  - Yeast only (no hyphae)
  - Skin colonization: Reduced
  - Biofilm: Normal
  - Virulence (systemic): Normal
```

**의미**:
- Filamentation = **피부 침투** 중요
- 혈류 감염에는 덜 중요?

**7. Network Reconstruction**

**TF-TF interactions**:
```
Azole stress
  ↓
Rpn4 ──→ Upc2 (indirect)
  ↓
Efflux ↑   Erg11 ↑
```

**Feedback loops**:
- Rpn4 자가 조절 (positive feedback)
- Mrr1-Mdr1 (feed-forward loop)

**Redundancy**:
- 여러 TF가 같은 efflux pump 조절
- → Single TF deletion만으로 완전 감수성 회복 어려움

#### 연구와의 연결점

**진균학 실험실 관점**:

**1. TF Deletion Library**:
```python
# Systematic approach
1. TF list (genome annotation, PFAM domains)
2. CRISPR-Cas9 or homologous recombination
3. Confirm deletion (PCR, Southern blot)
4. Phenotypic screens:
   - Drug susceptibility (E-test, broth dilution)
   - Growth curves
   - Biofilm assays
   - Virulence (Galleria, mouse)
5. RNA-seq (regulon identification)
```

**2. 항진균제 개발 타겟**:
- **Rpn4 inhibitors**: Proteasome + efflux 동시 차단
- **Mrr1 inhibitors**: GOF mutation 효과 중화
- **TF-DNA binding blockers**: Small molecules

**3. 진단 마커**:
- **Mrr1 sequencing**: GOF mutations → Azole 저항 예측
- **Mdr1 expression**: qRT-PCR → 치료 선택

**4. Comparative genomics**:
```yaml
C. auris vs. other Candida:
  - C. albicans: Efg1, Tec1 (hyphal regulation)
  - C. glabrata: Pdr1 (efflux regulation)
  - C. auris: Unique Rpn4-efflux link?
```

#### 필수 배경 지식

**1. Ergosterol Biosynthesis Pathway**
```
Acetyl-CoA
  ↓ (HMG-CoA reductase)
Mevalonate
  ↓ (multiple steps)
Lanosterol
  ↓ (ERG11 = Lanosterol 14α-demethylase) ← Azole target!
14α-Demethylation
  ↓
Ergosterol (진균 막 sterol)
```

**vs. Cholesterol** (인간):
- 인간: Lanosterol → Cholesterol (다른 경로)
- Azoles: ERG11 특이적 (인간 CYP51 낮은 친화성)

**2. Azole Antifungals**
| Drug | Generation | Spectrum |
|------|------------|----------|
| Fluconazole | 1st | Candida, Cryptococcus |
| Itraconazole | 2nd | Aspergillus, dimorphic |
| Voriconazole | 2nd | Broad |
| Posaconazole | 2nd | Mucorales |
| Isavuconazole | 3rd | Broad |

**C. auris 저항성**:
- Fluconazole: 90% isolates resistant
- Voriconazole: 70%
- Isavuconazole: 50%

**3. ABC vs. MFS Transporters**

**ABC (ATP-Binding Cassette)**:
- **Examples**: CDR1, CDR2 (C. auris)
- **Energy**: ATP hydrolysis
- **Broad substrate**: Azoles, other drugs

**MFS (Major Facilitator Superfamily)**:
- **Examples**: MDR1, FLU1 (C. auris)
- **Energy**: Proton gradient (H⁺ symport/antiport)
- **Substrate**: More specific

**4. Zinc Finger Transcription Factors**

**C2H2 type** (Cys2-His2):
- **Structure**: ββα fold, Zn²⁺ coordination
- **DNA binding**: Major groove
- **Examples**: Mrr1, GFC1

**Zinc cluster type** (Zn₂Cys₆):
- **Fungal-specific!**
- **Examples**: Upc2, Pdr1

#### 예상 질문 & 토론 포인트

**당신이 물어볼 질문**:

1. "**Rpn4 deletion mutant**가 proteasome 기능도 손상되는데, in vivo fitness는? Virulence 감소하나요?"

2. "**다른 Candida species** (C. albicans, C. glabrata)에도 Rpn4-efflux 연결이 있나요? C. auris만의 특징인가요?"

3. "**Triple knockout** (rpn4Δ mrr1Δ upc2Δ)을 만들면 pan-azole susceptible해지나요? Synthetic lethality는?"

4. "**Filamentation (GFC1) 없는 C. auris**도 혈류 감염 일으킬 수 있는데, 왜 C. albicans에서는 filamentation이 virulence 필수인가요?"

5. "**Rpn4 inhibitor** 스크리닝 가능성? Azole + Rpn4i combination therapy?"

**토론 예상**:
- C. auris의 **진화적 기원**: 왜 갑자기 출현?
- **환경 reservoir**: 병원 외 어디서 오나?
- **Clade-specific differences**: 6 clades의 TF network 차이?
- **Pan-resistant strains**: 어떻게 대응?

---

### 🔹 발표 2 (09:30-10:00)

**연사**: Fausto Almeida
**소속**: University of São Paulo, Brazil
**제목**: Cellular symphony: The role of extracellular vesicles as the maestros of fungal infections

#### 최근 연구 배경 (2024-2025)

Almeida 교수는 **진균 세포 외 소포체 (Extracellular Vesicles, EVs)** 전문가입니다.

**최신 연구 (2025)**:

**1. Journal of Extracellular Biology (2025)**:
"Extracellular Vesicles From Fungal Infection in Humans: A Key Player in Immunological Responses"

- **최초**: 인간 샘플에서 진균 감염 시 EV 역할 연구
- **발견**: EV가 숙주 면역 반응 조절
- **연간 사망**: 진균 감염 ~1.6 million deaths

**2. bioRxiv (2025 Feb)**:
"Cross-Species Communication via Fungal Extracellular Vesicles"
- Arturo Casadevall (Johns Hopkins) 협력
- 진균-숙주, 진균-진균 간 EV-mediated communication

**3. Candida haemulonii EVs (2025)**:
- Antifungal resistance
- Immune evasion
- Virulence

#### 예상 발표 내용

**1. Fungal Extracellular Vesicles (EVs) 개요**

**정의**:
- 세포막으로 둘러싸인 나노입자 (30-1000 nm)
- 세포 밖으로 분비
- Proteins, lipids, nucleic acids, carbohydrates 함유

**진균 EV 특징**:
```yaml
Composition:
  - Membrane: Ergosterol, phospholipids, glycans
  - Proteins: Virulence factors, enzymes
  - Polysaccharides: β-glucan, mannans
  - RNA: mRNA, miRNA, lncRNA
  - Metabolites: Melanin, siderophores

Size:
  - Small EVs: 30-150 nm (exosome-like)
  - Large EVs: 150-1000 nm (microvesicle-like)
```

**Biogenesis**:
```
다양한 경로:
1. Multivesicular body (MVB) pathway
   - Endosomal sorting
   - ESCRT-dependent/independent
   - Exosome-like EVs

2. Plasma membrane budding
   - Direct shedding
   - Microvesicle-like EVs

3. Cell wall passage (진균 특이!)
   - Cell wall → EV release
   - β-glucan, chitin layers 통과
```

**2. EVs in Fungal-Host Interactions**

**면역 조절**:

**A. Pro-inflammatory** (감염 초기):
```
Fungal EVs
  ↓
Macrophage uptake
  ↓
TLR2/TLR4/Dectin-1 activation
  ↓
NF-κB pathway
  ↓
Cytokines: TNF-α, IL-6, IL-1β ↑
  ↓
Inflammation
```

**B. Immune evasion** (감염 진행):
```
EVs carry:
  - Proteases (macrophage function 억제)
  - Polysaccharides (capsule-like, complement 회피)
  - Melanin (oxidative stress 저항)
  ↓
Immune suppression
  - M2 macrophage polarization
  - IL-10 ↑ (anti-inflammatory)
  - T-cell anergy
```

**3. EVs as Virulence Vehicles**

**Cargo 예시** (*Cryptococcus*, *Candida*, *Aspergillus*):

| Virulence Factor | Function | EV-mediated Effect |
|------------------|----------|-------------------|
| **Urease** | Ammonia production | BBB 투과성 ↑ (뇌 감염) |
| **Laccase** | Melanin synthesis | Oxidative stress 저항 |
| **Phospholipase B** | Membrane degradation | 세포 손상 |
| **Glucuronoxylomannan (GXM)** | Capsule polysaccharide | Immune suppression |
| **β-glucan** | Cell wall component | Dectin-1 activation |

**EV 이점 vs. 직접 분비**:
- **보호**: EV membrane = cargo 안정화
- **Targeted delivery**: Host cell uptake (endocytosis)
- **Long-range**: Bloodstream, 멀리 전달

**4. Cross-Species Communication (2025 연구)**

**진균-진균 간**:
- **Quorum sensing-like**: EV로 정보 전달
- **Biofilm 형성**: EV가 matrix component
- **Drug resistance 전파**: EV에 efflux pump mRNA

**진균-세균 간**:
- **Microbiome interactions**: 장내 미생물과 교차
- **Synergy/Antagonism**: EV-mediated

**진균-숙주 간**:
- **RNA transfer**: Fungal miRNA → 숙주 세포
- **Gene expression 조절**: 숙주 면역 유전자 억제

**5. EVs and Antifungal Resistance**

**메커니즘**:
```yaml
EVs contain:
  - Efflux pumps (Mdr1, Cdr1)
  - Drug-degrading enzymes
  - Stress response proteins

Function:
  - Drug sequestration (EV 내부로 약물 포획)
  - Horizontal transfer (다른 진균 세포에 저항성 전파)
  - Decoy effect (EV가 약물 흡수 → 세포 보호)
```

**Candida auris EVs (2025 발견)**:
- Azole-resistant isolates: EV 생산 ↑
- EV cargo: Mrr1, Mdr1 protein
- EV uptake by azole-sensitive cells → Transient resistance

**6. EVs as Diagnostic Biomarkers**

**잠재력**:
```yaml
Blood/CSF EV isolation:
  ↓
Fungal EV markers detection:
  - Ergosterol (lipid)
  - β-glucan (polysaccharide)
  - Fungal-specific proteins (e.g., Laccase)
  - Fungal RNA (18S rRNA, ITS)
  ↓
Early diagnosis:
  - Before culture positive
  - Non-invasive (혈액)
  - Quantitative (EV concentration = fungal burden)
```

**vs. 기존 진단**:
- **Culture**: 느림 (days), 일부 fastidious
- **Galactomannan**: Aspergillus only
- **β-D-glucan**: Non-specific (all fungi)
- **EV-based**: 빠름, 종 특이적 (proteomics)

**7. EVs as Vaccine Platforms**

**장점**:
- **Adjuvant-like**: Innate immune activation
- **Antigen presentation**: EV surface에 virulence factors
- **Safety**: 살아있는 진균 불필요

**실험 결과**:
```
Mice immunization with Cryptococcus EVs:
  ↓
Antibody production (IgG)
  ↓
Challenge with live Cryptococcus
  ↓
Survival ↑ (30% → 70%)
```

#### 연구와의 연결점

**진균학 실험실 관점**:

**1. EV Isolation**:
```python
# Protocol (Ultracentrifugation)
1. Fungal culture (broth, 48-72h)
2. Supernatant collection (cell-free)
3. Sequential centrifugation:
   - 300 g (10 min) - Remove cells
   - 2,000 g (20 min) - Remove debris
   - 10,000 g (30 min) - Remove large vesicles
   - 100,000 g (90 min) - Pellet EVs
4. Wash (PBS)
5. Resuspend in PBS
6. Characterization
```

**2. EV Characterization**:
| Method | Parameter |
|--------|-----------|
| **Nanoparticle Tracking Analysis (NTA)** | Size distribution, concentration |
| **Transmission Electron Microscopy (TEM)** | Morphology |
| **Western blot** | Protein markers (TSG101, CD63-like) |
| **Lipidomics** | Ergosterol, sphingolipids |
| **Proteomics** | LC-MS/MS |
| **RNA-seq** | Cargo RNA |

**3. Functional Assays**:
```yaml
Immune response:
  - Macrophage stimulation (cytokine ELISA)
  - TLR activation (reporter assays)

Virulence:
  - Cell cytotoxicity (LDH release)
  - Phagocytosis (Flow cytometry)
  - In vivo (Galleria, mouse)

Drug interaction:
  - EV + antifungal → Cellular uptake
  - EV-mediated resistance transfer
```

**4. 임상 응용**:
- **Liquid biopsy**: 혈액에서 진균 EV 검출
- **Precision medicine**: EV cargo → Drug resistance 예측
- **Immunotherapy**: EV-based vaccine

#### 필수 배경 지식

**1. Exosomes vs. Microvesicles**
| Feature | Exosomes | Microvesicles |
|---------|----------|---------------|
| **Size** | 30-150 nm | 100-1000 nm |
| **Origin** | MVB (endosomes) | Plasma membrane |
| **Markers** | TSG101, Alix, CD63 | ARF6, selectins |
| **Biogenesis** | ESCRT pathway | Direct budding |

**2. ESCRT Pathway**
- **Endosomal Sorting Complexes Required for Transport**
- **ESCRT-0/I/II/III**: Sequential recruitment
- **Function**: Membrane invagination → ILV (intraluminal vesicles)
- **MVB fusion**: Plasma membrane → Exosome release

**3. Pattern Recognition Receptors (PRRs)**
| PRR | Fungal Ligand | Location |
|-----|---------------|----------|
| **TLR2** | Zymosan, mannans | Cell surface |
| **TLR4** | Mannans (C. albicans) | Cell surface |
| **Dectin-1** | β-glucan | Cell surface |
| **Dectin-2** | α-mannans | Cell surface |
| **TLR9** | Fungal DNA | Endosome |

**4. M1 vs. M2 Macrophages**
| Type | Stimulus | Cytokines | Function |
|------|----------|-----------|----------|
| **M1** | IFN-γ, LPS | TNF-α, IL-12, IL-6 | Pro-inflammatory, microbicidal |
| **M2** | IL-4, IL-13 | IL-10, TGF-β | Anti-inflammatory, repair |

**EVs → M2 polarization**:
- Immune evasion strategy
- Chronic infection

#### 예상 질문 & 토론 포인트

**당신이 물어볼 질문**:

1. "**C. auris EVs**의 특징은? 다른 Candida species와 cargo composition 차이?"

2. "**EV-mediated drug resistance transfer**가 in vivo에서도 일어나나요? Clinical isolates에서 증거?"

3. "**진단 응용**: 혈액 샘플에서 진균 EV를 sensitive하게 검출하는 방법? Enrichment 전략?"

4. "**EV biogenesis inhibitors** (예: GW4869)가 항진균 효과 있나요? Adjunct therapy?"

5. "**Cross-kingdom EVs**: 진균 EVs가 인간 세포의 EV biogenesis에 영향?"

**토론 예상**:
- EV as **drug delivery vehicles**: 항진균제 담기?
- **Vaccine development timeline**: Clinical trials?
- **Standardization**: EV isolation/characterization 표준화
- **In vivo tracking**: Fluorescent EVs

---

### 🔹 발표 3 (10:00-10:30)

**연사**: Soo Chan Lee (이수찬)
**소속**: Texas Tech University Health Sciences Center, USA
**제목**: An amino acid permease, a novel downstream target of fungal calcineurin in pathogenic fungi

#### 최근 연구 배경 (2024)

Lee 교수팀은 **2024년 2월 bioRxiv**에 연구를 발표했습니다:

"The amino acid permease Byc1 is involved in calcineurin-dependent thermotolerance in *Cryptococcus neoformans*"

**핵심 발견**:
- **Byc1 (amino acid permease)** = Calcineurin의 novel downstream target
- **Negative regulation**: Calcineurin이 BYC1 발현 억제
- **byc1Δ mutant**: Partial FK506 resistance
- **BYC1 overexpression**: Thermosensitive, FK506 sensitive, 낮은 virulence

#### 예상 발표 내용

**1. Calcineurin in Fungi**

**구조**:
- **Catalytic subunit**: CnA (Calcineurin A)
- **Regulatory subunit**: CnB (Calcineurin B)
- **Ca²⁺/Calmodulin-dependent** phosphatase

**기능**:
```
Ca²⁺ influx (stress signals)
  ↓
Ca²⁺-Calmodulin
  ↓
Calcineurin activation
  ↓
Dephosphorylation of targets:
  - Crz1 (transcription factor)
  - Rcn1 (feedback inhibitor)
  ↓
Stress response genes
  ↓
Thermotolerance, Cell wall integrity, Virulence
```

**병원성 진균에서 필수**:
- *C. neoformans*: 37°C growth (체온)
- *Aspergillus fumigatus*: Hyphal growth
- *Candida* spp.: Azole tolerance

**2. Calcineurin Inhibitors**

| Drug | Mechanism | Clinical Use (non-fungal) |
|------|-----------|---------------------------|
| **FK506 (Tacrolimus)** | FKBP12 binding → Calcineurin inhibition | Immunosuppressant (organ transplant) |
| **Cyclosporin A** | Cyclophilin binding → Calcineurin inhibition | Immunosuppressant |

**문제점**:
- **면역억제**: 진균 감염 환자에게 사용 불가!
- → **진균-특이적 calcineurin pathway components** 필요

**3. Byc1: Amino Acid Permease**

**발견 과정**:
```
FK506 suppressor screen (byc1Δ)
  ↓
byc1Δ = Partial FK506 resistance
  ↓
(Why? BYC1 absence → Less calcineurin dependence)
  ↓
Calcineurin → Byc1 regulation 추정
```

**Byc1 (Bypass of Calcineurin 1)**:
- **Amino acid permease family**
- **Function**: 세포 외 amino acids 흡수
- **Regulation**: Calcineurin이 **BYC1 발현 억제**

**4. Calcineurin-Byc1-Pka1 Axis**

**모델**:
```
Normal condition (37°C):
  Calcineurin active
    ↓ (억제)
  BYC1 expression low
    ↓
  Amino acid uptake moderate
    ↓
  Pka1 (PKA) activity balanced
    ↓
  Cell growth OK

Calcineurin inhibition (FK506) or mutation:
  Calcineurin inactive
    ↓ (억제 해제)
  BYC1 expression high!
    ↓
  Amino acid uptake ↑↑
    ↓
  Pka1 hyperactivation
    ↓
  Thermosensitivity (37°C growth defect)
```

**Pka1 (Protein Kinase A)**:
- **cAMP-dependent**
- **Glucose sensing**: High glucose → cAMP ↑ → Pka1 ↑
- **Byc1 connection**: Amino acids → Tor pathway → PKA?

**5. Phenotypes**

**byc1Δ mutant**:
```yaml
FK506 response:
  - Partial resistance (MIC 2-4배 증가)
  - Still thermosensitive at high FK506

Thermotolerance:
  - 37°C growth: Normal

Virulence:
  - Mouse model: Wild-type level
```

**BYC1 overexpression (PBYC1-BYC1)**:
```yaml
Phenotype mimics cnA/cnBΔ:
  - Thermosensitive (30°C OK, 37°C No)
  - FK506 hypersensitivity
  - Virulence: Reduced (mouse survival ↑)

Mechanism:
  - Excessive amino acid uptake
  - Pka1 hyperactivation
  - Cell stress
```

**6. Therapeutic Implications**

**New target**: **Byc1 inhibitor**?
- **Rationale**: Byc1 억제 → BYC1 OE와 반대 효과 → 항진균?
- **Problem**: Byc1Δ는 virulence 정상... (효과 없을 듯)

**Better target**: **Calcineurin-specific pathway components**
- Byc1 자체보다, **Byc1 regulation mechanism**
- 진균-특이적 Crz1 inhibitors?

**Combination therapy**:
```
Azole + FK506 analogs (면역억제 없는 버전)
  ↓
Synergy:
  - Azole: Ergosterol 합성 억제
  - FK506: Stress response 억제
  ↓
Fungicidal effect
```

#### 연구와의 연결점

**진균학 실험실 관점**:

**1. Suppressor Screens**:
```python
# 원리
1. Calcineurin mutant or FK506 (thermosensitive)
2. Random mutagenesis (EMS, UV)
3. 37°C에서 자라는 colony 선별
4. Suppressor gene 동정 (whole-genome sequencing)
5. Validation (deletion, complementation)
```

**2. Amino Acid Transporters in Fungi**:
- **14 families**: AAP, APC, ATF, etc.
- **Functions**: Nutrition, pH homeostasis, signaling
- **Pathogenicity**: Auxotrophic mutants → Avirulent
- **Example**: Lys2Δ (*C. albicans*) → No lysine biosynthesis → Avirulent

**3. PKA Pathway in Fungi**:
```
Glucose/Amino acids
  ↓
Gpr1 (GPCR) / TORC1
  ↓
Gpa2 / Ras
  ↓
Adenylyl cyclase (Cyr1/Cac1)
  ↓
cAMP ↑
  ↓
PKA (Pka1/Tpk2)
  ↓
Stress response, Morphogenesis
```

**Byc1 → PKA connection**: Unclear, future work

#### 필수 배경 지식

**1. Calcineurin Structure**
- **CnA**: ~60 kDa, catalytic
  - Catalytic domain
  - CnB-binding domain
  - Calmodulin-binding domain
  - Autoinhibitory domain
- **CnB**: ~19 kDa, regulatory
  - 4 EF-hand Ca²⁺-binding motifs

**2. FK506 Mechanism**
```
FK506 + FKBP12 (immunophilin)
  ↓
FK506-FKBP12 complex
  ↓
Binds to Calcineurin
  ↓
Blocks substrate access
  ↓
Phosphatase activity ↓
```

**3. Crz1 (Calcineurin-Responsive Zinc finger 1)**
- **Transcription factor**
- **Calcineurin substrate**: Dephosphorylation → Nuclear import
- **Target genes**: FKS2 (β-glucan synthase), PMC1 (Ca²⁺ ATPase)

**4. Amino Acid Sensing (TORC1)**
- **TORC1** (Target of Rapamycin Complex 1)
- **Sensors**: Amino acids, glucose
- **Outputs**: Protein synthesis, autophagy
- **Byc1 → TORC1?**: Possible link

#### 예상 질문 & 토론 포인트

**당신이 물어볼 질문**:

1. "**Byc1-PKA 연결 메커니즘**은 정확히 무엇인가요? Amino acids → TORC1 → PKA?"

2. "**다른 병원성 진균** (Candida, Aspergillus)에도 Byc1 homolog와 calcineurin regulation 보존되나요?"

3. "**Byc1 overexpression + azole** combination은? Synergy 있나요?"

4. "**진균-특이적 calcineurin inhibitors** 개발 전략? CnA/CnB 구조 차이 (인간 vs. 진균)를 이용?"

5. "**In vivo amino acid levels**가 Byc1 활성에 영향? 숙주 환경 (혈액, 폐)에 따라 달라지나요?"

**토론 예상**:
- Calcineurin as **pan-fungal target**: Broad-spectrum?
- **Resistance mechanisms**: Calcineurin mutations?
- **Host calcineurin**: Off-target effects 최소화
- **Clinical translation**: FK506 analogs

---

### 🔹 발표 4 (10:30-10:50)

**연사**: Catia Mota
**소속**: Korea Basic Science Institute (KBSI)
**제목**: Beyond folding: *N*-Glycan-driven protein quality control modulates extracellular vesicle biogenesis and cargo export in *Cryptococcus neoformans*

#### 최근 연구 배경 (2024)

Mota 박사팀은 **2024년 9월 bioRxiv**에 연구를 발표했습니다:

"Evolutionary unique N-glycan-dependent protein quality control system plays pivotal roles in cellular fitness and extracellular vesicle transport in *Cryptococcus neoformans*"

**Collaborators**: Yong-Sun Bahn (Yonsei), Hyun Ah Kang (Yonsei), J. Andrew Alspaugh (Duke)

**핵심 발견**:
- **C. neoformans의 unique N-glycosylation pathway**: Glucose 추가 단계 없음!
- **ERQC (ER Quality Control) mutants**: Fitness ↓, Virulence ↓
- **EV alterations**: ugg1Δ mutant → EV 개수, 크기, cargo 변화
- **연결**: N-glycan QC → EV biogenesis/secretion

#### 예상 발표 내용

**1. N-Glycosylation in Fungi**

**일반적 경로 (Yeast, mammals)**:
```
ER lumen:
  1. Dol-PP-GlcNAc2Man9Glc3 (precursor)
  2. Oligosaccharyltransferase (OST) → Asn-X-Ser/Thr
  3. Glucosidase I → Remove Glc (1개)
  4. Glucosidase II → Remove Glc (2개) → Man9GlcNAc2
  5. Mannosidase → Man8GlcNAc2

Calnexin/Calreticulin cycle:
  - Mono-glucosylated glycoproteins binding
  - Folding assistance
  - UGGT (UDP-glucose:glycoprotein glucosyltransferase)
    → Misfolded protein re-glucosylation
  - Repeat until folded

ERAD (ER-Associated Degradation):
  - Terminally misfolded → Mannose trimming
  - Extraction → Proteasome
```

**C. neoformans의 unique pathway**:
```
ER lumen:
  1. Dol-PP-GlcNAc2Man9 (NO Glc3!)
     ↓
  2. OST → Protein
     ↓
  3. NO Glc trimming (이미 없음)
     ↓
  4. Mannosidase → Man8

ERQC:
  - NO calnexin/calreticulin cycle (Glc 없어서)
  - BUT, UGGT1 homolog exists!
  - → **What does it do?**
```

**2. ERQC Components in C. neoformans**

**Mutants analyzed**:

| Gene | Function | Phenotype (deletion) |
|------|----------|---------------------|
| **UGG1** | UGGT homolog (putative sensor) | Thermosensitive, ↓Virulence, EV ↓ |
| **MNS1** | α1,2-Mannosidase | Moderate defects |
| **MNS101** | α1,2-Mannosidase (ER) | Severe defects |
| **MNL1** | Mannosidase-like | Mild defects |
| **MNL2** | Mannosidase-like | Mild defects |

**3. ugg1Δ Phenotypes (핵심 mutant)**

**Growth & Stress**:
```yaml
Temperature:
  - 30°C: Normal
  - 37°C: Reduced growth
  - 39°C: Severe defect

Cell wall stress:
  - Congo Red: Sensitive
  - Calcofluor White: Sensitive
  - → Cell wall integrity ↓

Oxidative stress:
  - H2O2: Sensitive

Survival in macrophages:
  - Phagocytosis: Normal
  - Intracellular survival: Reduced (50%)
```

**Virulence**:
```
Mouse inhalation model:
  - Wild-type: Median survival 18 days
  - ugg1Δ: Median survival >60 days (all survive!)
  - Complementation: Restored
```

**4. N-Glycan Profile Changes**

**Glycan analysis (MALDI-TOF MS)**:
```yaml
Wild-type:
  - Man8-10GlcNAc2 (predominant)
  - Phosphomannosylation (virulence factor)

ugg1Δ:
  - Altered Man distribution
  - Abnormal mannosylation
  - Hypermannosylation (일부 proteins)
```

**Cell surface organization**:
- **Capsule**: GXM (glucuronoxylomannan) - Major virulence factor
  - ugg1Δ: Capsule size slightly ↓
  - Structure: Disorganized

**5. Extracellular Vesicle Alterations** ⭐

**EV isolation & characterization**:

**Wild-type EVs**:
```yaml
Concentration: ~10^10 particles/mL culture
Size:
  - Mode: 120 nm
  - Range: 50-300 nm
Cargo:
  - Proteins: ~500 (proteomics)
  - Polysaccharides: GXM, glucan
  - Lipids: Ergosterol, sphingolipids
  - RNA: mRNA, ncRNA
```

**ugg1Δ EVs**:
```yaml
Concentration: ~5 x 10^9 particles/mL (50% ↓)
Size:
  - Mode: 80 nm (smaller!)
  - Range: Narrower distribution
Cargo (Proteomics):
  - Total proteins: ~300 (40% ↓)
  - Altered composition:
    - Cell wall proteins ↓
    - ER chaperones ↑
    - Secretory pathway proteins ↓
```

**6. N-Glycan QC → EV Biogenesis Link**

**메커니즘 (추정)**:
```
Proper N-glycan QC (UGG1)
  ↓
Glycoprotein folding & trafficking
  ↓
Secretory pathway homeostasis
  ↓
MVB (Multivesicular Body) formation
  ↓
ILV (Intraluminal Vesicle) budding
  ↓
MVB-plasma membrane fusion
  ↓
EV release

UGG1 deficiency:
  ↓
Misfolded glycoproteins accumulate
  ↓
ER stress
  ↓
UPR (Unfolded Protein Response)
  ↓
Secretory pathway disruption
  ↓
Altered MVB dynamics
  ↓
EV biogenesis ↓ + Cargo selection change
```

**Key point**: **ERQC는 단순히 protein folding만이 아니라, EV 생산/분비까지 조절!**

**7. Functional Implications**

**EV-mediated virulence**:
```
Normal EVs (WT):
  - GXM delivery → Immune suppression
  - Urease → BBB penetration
  - Melanin → Oxidative stress resistance
  ↓
High virulence

ugg1Δ EVs:
  - Reduced number
  - Altered cargo (less virulence factors?)
  ↓
Low virulence
```

**Therapeutic potential**:
- **UGG1 inhibitors**: EV biogenesis 억제 → Virulence ↓
- **N-glycosylation inhibitors**: Tunicamycin (독성 높음)
  - → **진균-특이적 glycosylation inhibitors** 필요

#### 연구와의 연결점

**진균학 실험실 관점**:

**1. Glycomics**:
```python
# N-glycan profiling
1. Protein extraction
2. PNGase F treatment (N-glycan 절단)
3. Glycan labeling (2-AB, 2-AA)
4. HILIC-UPLC or MALDI-TOF MS
5. Structural analysis (Exoglycosidase digests)
```

**2. EV Proteomics**:
```yaml
Workflow:
  1. EV isolation (ultracentrifugation)
  2. Protein extraction (lysis buffer)
  3. Tryptic digestion
  4. LC-MS/MS
  5. Database search (C. neoformans proteome)
  6. GO enrichment analysis

Findings (ugg1Δ):
  - Enriched: ER chaperones (BiP, PDI)
  - Depleted: Cell wall proteins (Cda1, Cda2)
```

**3. ER Stress Assays**:
```yaml
Markers:
  - Spliced XBP1 (XBP1s) - qRT-PCR
  - Phospho-eIF2α - Western blot
  - BiP (GRP78) expression - qRT-PCR

Inducers:
  - Tunicamycin (N-glycosylation inhibitor)
  - Dithiothreitol (DTT, reducing agent)
```

**4. Virulence Assays**:
- **Galleria mellonella** (waxworm): Rapid, cheap
- **Mouse inhalation**: Gold standard (C. neoformans meningitis model)
- **Macrophage survival**: Intracellular replication

#### 필수 배경 지식

**1. N-Glycan Structure**
```
   GlcNAc-GlcNAc
       |
   Man-Man-Man
   / |     | \
Man Man  Man Man
```
- **Core**: GlcNAc2-Man3
- **Branches**: High-mannose, Complex, Hybrid

**2. UGGT (UDP-Glucose:Glycoprotein Glucosyltransferase)**
- **Function**: "Folding sensor"
  - Detects exposed hydrophobic residues (misfolded protein)
  - Re-glucosylates N-glycan (Glc1Man9GlcNAc2)
  - → Calnexin/Calreticulin re-binding
- **C. neoformans UGG1**: Homolog exists, but **no Glc substrate!**
  - → **Alternative function?** (Mota's discovery)

**3. Multivesicular Body (MVB)**
```
Early Endosome
  ↓ (ESCRT pathway)
Membrane invagination
  ↓
ILVs formation (Intraluminal Vesicles)
  ↓
MVB (filled with ILVs)
  ↓
Option 1: Lysosome fusion (degradation)
Option 2: Plasma membrane fusion → ILVs = Exosomes
```

**4. C. neoformans Virulence Factors**
| Factor | Function |
|--------|----------|
| **Capsule (GXM)** | Complement resistance, phagocytosis ↓ |
| **Melanin** | Oxidative stress, antifungal resistance |
| **Urease** | Ammonia → Brain invasion (BBB ↑) |
| **Phospholipase B** | Membrane degradation |
| **Laccase** | Melanin synthesis, Fe³⁺ reduction |

#### 예상 질문 & 토론 포인트

**당신이 물어볼 질문**:

1. "**UGG1의 실제 substrate**는 무엇인가요? Glc가 없는데 어떻게 glycoprotein을 recognize?"

2. "**EV cargo selection 메커니즘**은? ERQC가 어떻게 특정 단백질을 EV로 보내나요?"

3. "**다른 진균** (Candida, Aspergillus)의 N-glycosylation pathway는 C. neoformans와 다른가요? ERQC-EV link 보존?"

4. "**UGG1 inhibitors** 스크리닝 가능성? Structure-based drug design?"

5. "**EV-free culture supernatant**로 virulence 차이 보이나요? (EV specific effect인지 확인)"

**토론 예상**:
- **Evolutionary origin**: 왜 C. neoformans는 Glc-free N-glycan?
- **ERQC-EV link**: 다른 세포 시스템에도 있나?
- **Therapeutic window**: ERQC 억제 = Host cell toxicity?
- **EV as drug carriers**: 역이용 가능?

---

## 🧠 세션 전체 핵심 요약

### S5의 핵심 메시지

**"진균은 다층적 조절 시스템으로 숙주와 상호작용하고 생존한다"**

| 발표 | 주제 | 핵심 메커니즘 | 치료 타겟 |
|------|------|--------------|----------|
| **Bahn** | C. auris TF networks | Rpn4/Mrr1/Upc2 → Efflux ↑ | TF inhibitors |
| **Almeida** | Fungal EVs | EV-mediated immune modulation | EV biogenesis 억제 |
| **Lee** | Calcineurin-Byc1 | Amino acid permease regulation | 진균-특이적 Cn inhibitors |
| **Mota** | N-glycan QC | ERQC → EV biogenesis | UGG1 inhibitors |

### 통합적 관점

**진균 병원성의 다층 시스템**:
```yaml
Level 1 - 유전자 조절 (Bahn):
  - Transcription factors → Drug resistance
  - Rpn4 = Master regulator (Proteasome + Efflux)

Level 2 - 세포 간 통신 (Almeida):
  - EVs → 장거리 신호 전달
  - Virulence factors delivery
  - Immune modulation

Level 3 - 신호 전달 (Lee):
  - Calcineurin pathway → Stress response
  - Novel target: Byc1 (amino acid permease)

Level 4 - 품질 관리 (Mota):
  - ERQC → Protein homeostasis
  - N-glycan QC → EV biogenesis
```

### 공통 테마: **Redundancy & Robustness**
- 여러 TF가 같은 efflux pump 조절
- Multiple stress response pathways
- EV biogenesis의 여러 경로
- → **Single target 억제 = 불충분** → **Combination therapy 필수**

---

## 📚 사전 읽기 (우선순위)

### 필수

1. **Yong-Sun Bahn (2025)** - mBio, "Signaling pathways...C. auris"
2. **Fausto Almeida (2025)** - J Extracellular Biology, "EVs from fungal infection"
3. **Catia Mota (2024)** - bioRxiv, "N-glycan QC...EVs"

### 추천

4. **C. auris Review (2024)** - "Comprehensive Overview of Candida auris"
5. **Calcineurin in fungi (2017)** - Virulence journal

---

## 🎤 Top 5 Questions

1. **[Bahn]** "Rpn4 triple knockout (+ Mrr1 + Upc2) → Pan-azole susceptible? Fitness cost?"
2. **[Almeida]** "C. auris EVs vs. other Candida? Cargo differences?"
3. **[Lee]** "Byc1-PKA mechanistic link? TORC1 involved?"
4. **[Mota]** "UGG1 substrate (no Glc)? ERQC-EV cargo selection?"
5. **[All]** "Combination therapy: Azole + EV biogenesis inhibitor + Calcineurin inhibitor?"

---

## 🤝 네트워킹 우선순위

1. **Yong-Sun Bahn** (연세대) ⭐⭐⭐ - 국내, C. auris 전문가
2. **Fausto Almeida** (Brazil) ⭐⭐⭐ - EV 선구자
3. **Catia Mota** (KBSI) ⭐⭐ - 국내, N-glycan & EV

---

**예상 학습 성과**:
✅ C. auris MDR 메커니즘 (TF networks)
✅ 진균 EVs의 역할 (면역, virulence, 진단)
✅ Calcineurin pathway (새로운 타겟 Byc1)
✅ N-glycan QC-EV link (진균 특이적)
✅ 신규 항진균제 타겟 4+

**진균 연구자에게 필수 세션!** 🍄
