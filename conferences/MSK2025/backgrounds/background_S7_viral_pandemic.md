# 배경 자료: S7 바이러스 연구 & 팬데믹 대응

**세션**: S7 - Frontiers in Viral Research and Pandemic Response
**일시**: 2025년 10월 27일 (월) 13:50-15:50
**장소**: Convention Hall 1
**Sponsored by**: International Vaccine Institute (IVI)
**Chair**: Jae-Ouk Kim (IVI) & Manki Song (IVI)
**중요도**: ⭐⭐⭐⭐ (80/100점) - **바이러스/백신 연구자 필수!**

---

## 🎯 세션 개요

이 세션은 **바이러스 연구의 최신 동향과 팬데믹 대응 전략**을 다룹니다. IVI (국제백신연구소)가 후원하는 만큼 **백신 개발**에 초점이 맞춰져 있습니다.

### 왜 이 세션이 중요한가?

- 🧬 **AI 백신 개발**: AlphaFold 이후 시대의 structure-based vaccine design
- 🦠 **Host-directed therapy**: 바이러스가 아닌 숙주를 타겟
- 💉 **차세대 플랫폼**: mRNA, nanoparticle, structure-based design
- 🌍 **팬데믹 대비**: 한국의 백신 R&D 전략

### 이 세션의 공통 테마

```
팬데믹 대응 전략
├─ 숙주 타겟 치료 (Host-directed therapy)
├─ 구조 기반 백신 (Structure-based design)
├─ AI 활용 (AlphaFold, RoseTTAFold)
└─ 신속 개발 플랫폼 (Rapid response platforms)
```

---

## 📋 발표별 상세 분석

### 🔹 발표 1 (13:50-14:20)

**연사**: Seungmin Hwang (황승민)
**소속**: Broad Institute of MIT and Harvard, USA
**제목**: Host-directed therapy for respiratory viral infection

#### 최근 연구 배경 (2024-2025)

Hwang 박사는 **2023년 9월 Broad Institute에 합류**했으며, **host-directed therapy (HDT)** 전문가입니다.

**최신 연구 (2025)**:

**PNAS (2025년 3월 accepted)**:
"Shared host genetic landscape of respiratory viral infection"

**핵심 발견**:
- 다양한 **호흡기 바이러스**가 **공통 숙주 유전자**에 의존
- **Broad-spectrum HDT** 가능성
- **STT3A/B** (oligosaccharyltransferase) = 유망한 타겟
  - N-linked glycosylation 담당
  - 바이러스가 감염에 hijack

#### 예상 발표 내용

**1. Host-Directed Therapy (HDT) 개념**

**전통적 항바이러스제**:
```yaml
Target: 바이러스 단백질
  - Polymerase inhibitors (Remdesivir)
  - Protease inhibitors (Paxlovid)
  - Neuraminidase inhibitors (Tamiflu)

문제점:
  - 바이러스 변이 → 내성
  - Virus-specific (narrow spectrum)
  - 개발 시간 오래 걸림
```

**Host-Directed Therapy**:
```yaml
Target: 숙주 세포 단백질 (바이러스가 의존)
  - Endocytosis 억제
  - Glycosylation 차단
  - Immune modulation

장점:
  - 내성 발생 어려움 (숙주 유전자 변이 느림)
  - Broad-spectrum (여러 바이러스에 효과)
  - 재사용 가능 (drug repurposing)

단점:
  - Host toxicity 우려
  - Therapeutic window 좁을 수 있음
```

**2. 호흡기 바이러스의 공통 숙주 의존성**

**주요 호흡기 바이러스**:
- **Influenza A/B**: 계절성 독감, 팬데믹
- **SARS-CoV-2**: COVID-19
- **RSV**: 영유아 폐렴
- **HPIV** (Human parainfluenza): 소아 크룹
- **hMPV** (Human metapneumovirus)

**공통 숙주 경로**:

**A. Entry (세포 침투)**:
```
Receptor binding
  ↓
Endocytosis (Clathrin/Caveolin-mediated)
  ↓
Endosome acidification
  ↓
Membrane fusion
  ↓
Viral genome release
```

**공통 타겟**:
- **ACE2, TMPRSS2** (SARS-CoV-2)
- **Sialic acid** (Influenza, others)
- **Endosomal acidification** (V-ATPase)

**B. Replication**:
```
Host ribosomes, tRNA
  ↓
ER/Golgi (protein processing)
  ↓
Lipid synthesis
```

**C. Egress (방출)**:
```
Viral assembly
  ↓
Budding (ESCRT pathway)
  ↓
Release
```

**3. STT3A/B: 유망한 Broad-Spectrum Target**

**STT3A/B**:
- **Oligosaccharyltransferase (OST) complex** catalytic subunits
- **N-linked glycosylation** 담당
  - Asn-X-Ser/Thr motif에 glycan 부착
  - ER lumen에서 발생

**바이러스가 N-glycosylation을 hijack하는 이유**:
```yaml
Viral envelope proteins (spike, HA, etc.):
  - N-glycans 많음 (glycan shield)
  - 면역 회피 (antibody epitope 차폐)
  - Protein folding 도움
  - Receptor binding 조절

예시:
  - SARS-CoV-2 Spike: ~22 N-glycans
  - Influenza HA: ~5-11 N-glycans
  - HIV Env: ~30 N-glycans (극단적)
```

**STT3A/B 억제의 효과**:
```
N-glycosylation ↓
  ↓
Viral protein misfolding
  ↓
ER retention, degradation
  ↓
감염성 virion 생산 ↓
```

**장점**:
- **Broad-spectrum**: 거의 모든 enveloped virus 타겟
- **필수 경로**: 바이러스가 우회하기 어려움

**단점**:
- **Host toxicity**: 인간 glycoprotein도 영향
- **Therapeutic window**: 일시적 억제 필요

**4. Genetic Evidence (PNAS 2025)**

**Approach**:
```python
# Genome-wide CRISPR screen
1. Human cell library (각 유전자 knockout)
2. Virus infection (Influenza, SARS-CoV-2, etc.)
3. Survival selection
4. Sequencing (어떤 knockout이 생존?)
5. Common host factors 동정

Result:
  - 수백 개 host genes identified
  - Pathway analysis:
    - Glycosylation (STT3A/B, DDOST, etc.)
    - Endocytosis (AP2, Dynamin)
    - Membrane trafficking (SNAREs)
```

**Shared genes across viruses**:
- **STT3A/B**: Influenza, SARS-CoV-2, RSV 모두 의존
- **TMEM41B**: Flaviviruses, Coronaviruses
- **ATP6V0**: Endosomal acidification

**5. Clinical Perspective**

**기존 HDT 예시**:
- **Chloroquine**: Endosomal pH ↑ (말라리아 약, 재사용)
- **IFN-α/β**: Immune stimulation (HCV 치료)
- **JAK inhibitors**: Cytokine storm 억제 (COVID-19)

**STT3A/B inhibitors 개발**:
- **NGI-1**: STT3 억제제 (연구용)
- **In vivo efficacy**: 동물 모델 테스트 필요
- **Toxicity profiling**: 필수

**Combination therapy**:
```
HDT (STT3i) + Antiviral (Remdesivir)
  ↓
Synergy:
  - 바이러스 복제 ↓↓
  - 내성 발생 ↓
  - 치료 효과 ↑
```

#### 연구와의 연결점

**바이러스학 실험실 관점**:

**1. CRISPR Screen**:
```python
# Genome-wide host factor screen
1. Library: Brunello, GeCKO (human genome-wide)
2. Transduction: Lentiviral sgRNA library
3. Selection: Puromycin
4. Infection: MOI 0.1-1
5. Timepoint: 3-7 days post-infection
6. Sequencing: NGS (sgRNA abundance)
7. Analysis: MAGeCK, BAGEL
```

**2. HDT Validation**:
```yaml
In vitro:
  - Dose-response (IC50)
  - Cytotoxicity (CC50)
  - Selectivity index (SI = CC50/IC50)
  - Viral titer reduction (plaque assay, qPCR)

In vivo:
  - Mouse models (K18-hACE2, BALB/c)
  - Viral load (lung, blood)
  - Pathology (H&E staining)
  - Survival
```

**3. Drug Repurposing**:
- FDA-approved drugs screen
- Off-target effects
- Clinical trials 빠름

#### 필수 배경 지식

**1. N-Linked Glycosylation**
```
Asn-X-Ser/Thr motif (X ≠ Pro)
  ↓
Dolichol-PP-GlcNAc2Man9Glc3 (precursor)
  ↓
OST (STT3A/B) transfer
  ↓
Glycan attached to Asn
  ↓
Glucosidase trimming
  ↓
Calnexin/Calreticulin (folding)
```

**2. Viral Glycan Shield**
- **High-density glycans**: Antibody 접근 차단
- **Evolution**: Glycan site 증가 (immune escape)
- **Vaccine design**: Glycan 고려 필수

**3. Therapeutic Window**
- **Narrow window**: Host 필수 vs. 바이러스 의존
- **Transient inhibition**: 급성 감염 시 단기 사용

#### 예상 질문 & 토론 포인트

**질문**:
1. "**STT3A vs. STT3B** 중 어느 것이 더 중요한 타겟? Redundancy?"
2. "**장기 투여 시 host toxicity**는? 만성 바이러스 감염에 사용 가능?"
3. "**바이러스 변이**로 N-glycosylation 회피 가능? 내성 메커니즘?"
4. "**다른 HDT targets** (TMEM41B 등)와 combination?"
5. "**임상 시험** 계획? Phase I 시작?"

---

### 🔹 발표 2 (14:20-14:50)

**연사**: Jae-Hyun Park (박재현)
**소속**: Sungkyunkwan University School of Medicine
**제목**: Structural insight into HBV receptor NTCP and virus binding

#### 연구 배경

**HBV (Hepatitis B Virus)**:
- 만성 간염, 간경화, 간암 원인
- 전 세계 2억 9천만 명 감염
- **NTCP** (Na⁺-taurocholate co-transporting polypeptide) = 수용체

**NTCP**:
- **담즙산 수송체**: 간세포 표면
- **HBV entry**: Pre-S1 domain 결합

#### 예상 내용

**1. NTCP 구조 (Cryo-EM)**
- **10 transmembrane domains**
- **Na⁺ binding site**
- **Bile acid binding pocket**

**2. HBV-NTCP 상호작용**
- **Pre-S1 (2-48 aa)**: Viral attachment site
- **Myristoylation**: N-terminal lipid modification (필수)
- **Binding interface**: NTCP extracellular loops

**3. Entry Inhibitors**
- **Myrcludex B**: NTCP-HBV 결합 차단
  - HDV (Hepatitis D) 승인
  - HBV Phase III

**4. 구조 기반 약물 설계**
- **Small molecules**: NTCP binding pocket
- **Peptide inhibitors**: Pre-S1 mimics

---

### 🔹 발표 3 (14:50-15:20) ⭐ **핵심!**

**연사**: Minkyung Baek (백민경)
**소속**: Seoul National University (서울대학교), Department of Biological Sciences
**제목**: Transforming vaccine development with AI: Recent trends and structure-based strategies

#### 최근 연구 배경 (2024-2025)

Baek 교수는 **2025년 APEC ASPIRE Prize 수상자** (한국인 최초!)이며, **AI 단백질 구조 예측** 전문가입니다.

**핵심 업적**:
- **RoseTTAFold** co-developer (David Baker lab)
  - AlphaFold competitor
  - 2021년 Science 발표
- **2025년 LG AI Research 협력**: 차세대 단백질 구조 예측 AI 개발

**백신 개발 관련**:
- **Structure-based vaccine design**
- **Epitope prediction**
- **Protein stability optimization**

#### 예상 발표 내용

**1. AI Protein Structure Prediction 혁명**

**AlphaFold2 (2020)**:
```yaml
Impact:
  - 단백질 구조 예측 정확도 90%+
  - 원자 수준 resolution
  - 200 million+ structures (AlphaFold DB)

Limitations:
  - Single chain 위주
  - 동적 구조 (conformational changes) 약함
  - Membrane proteins 어려움
```

**RoseTTAFold (Baek et al. 2021)**:
```yaml
Features:
  - 3-track architecture (1D, 2D, 3D)
  - Protein-protein complexes 가능
  - Speed: AlphaFold보다 빠름

Applications:
  - Antibody-antigen docking
  - Multi-subunit complexes
  - Protein design (역방향)
```

**차세대 모델 (2024-2025)**:
- **AlphaFold3**: Multi-chain, ligands, DNA/RNA
- **RoseTTAFold All-Atom**: Small molecules, ions
- **ESMFold**: Language model-based (Meta)

**2. Structure-Based Vaccine Design**

**전통적 방법**:
```
Pathogen isolation
  ↓
Whole organism (killed/attenuated)
  or Subunit (purified protein)
  ↓
Trial & error
  ↓
10-15년 개발 기간
```

**AI-driven approach**:
```
Pathogen genome
  ↓
AI structure prediction (AlphaFold)
  ↓
Epitope identification (B/T cell epitopes)
  ↓
Antigen design (stabilized, optimized)
  ↓
In silico validation
  ↓
Rapid prototyping (mRNA, nanoparticle)
  ↓
2-3년
```

**3. Epitope Prediction with AI**

**B-cell epitopes**:
- **Surface accessibility**: Exposed loops, termini
- **Antigenicity**: Antibody binding propensity
- **Conservation**: Sequence variability 낮음

**AI tools**:
```python
# B-cell epitope prediction
1. Structure prediction (AlphaFold)
2. Surface area calculation (SASA)
3. Antigenicity scoring (ML models)
4. Conservation analysis (MSA)
5. Ranking top epitopes
```

**T-cell epitopes**:
- **MHC binding**: HLA-A, HLA-B, HLA-DR
- **Peptide presentation**: 8-11mer (Class I), 13-25mer (Class II)

**AI tools**:
- **NetMHCpan**: Deep learning MHC binding
- **AlphaFold-Multimer**: Peptide-MHC complex

**4. Antigen Stabilization (구조 기반)**

**문제**: Viral surface proteins 불안정
- **Pre-fusion** (감염 전) ↔ **Post-fusion** (감염 후)
- 백신은 pre-fusion conformation 필요 (중화 항체 타겟)

**예시: RSV F protein**:
```
Native F protein:
  - Metastable (pre-fusion)
  - Fusion 후 post-fusion (안정)
  - 백신 항원으로 부적합

Stabilized F protein (DS-Cav1):
  - Structure-based design (Jason McLellan)
  - Disulfide bond, proline substitutions
  - Pre-fusion locked
  - → mRNA vaccine (Moderna, Pfizer)
```

**AI 활용**:
```
AlphaFold prediction
  ↓
Conformational analysis (MD simulations)
  ↓
Mutation design (stability ↑)
  ↓
In silico screening
  ↓
Experimental validation
```

**5. Nanoparticle Vaccine Platforms**

**Ferritin, I53-50 등**:
- **Self-assembling**: 24-60 subunits
- **Antigen display**: Surface에 epitopes 제시
- **Multivalent**: B-cell activation ↑

**AI design**:
```yaml
Process:
  1. Antigen selection (epitope)
  2. Scaffold design (nanoparticle core)
  3. Linker optimization (flexibility)
  4. AlphaFold validation
  5. Cryo-EM structure determination

Example:
  - Mosaic nanoparticle (multiple virus strains)
  - Pan-coronavirus vaccine
```

**6. COVID-19 백신 개발 사례**

**Spike protein structure** (Cryo-EM, 2020):
- **Pre-fusion stabilization**: 2P mutations (K986P, V987P)
  - Moderna, Pfizer/BioNTech mRNA vaccines
  - Structure-based design 성공!

**Omicron variant** (2021):
- **AlphaFold2 prediction**: Spike mutations
- **Epitope mapping**: Antibody escape
- **Booster design**: 신속한 변이 대응

**7. Universal Vaccine Strategies**

**목표**: 모든 변이/계절형에 효과

**Approaches**:
- **Conserved epitopes**: Stem region (Influenza HA)
- **Mosaic antigens**: 여러 strain 혼합
- **Computationally optimized breadth (COB)**: AI로 최적 조합

**AI 역할**:
```python
# Universal epitope discovery
1. 수천 개 viral sequences alignment
2. Conservation analysis
3. AlphaFold structure prediction (all variants)
4. Epitope accessibility check
5. Immunogenicity scoring
6. Top candidates selection
```

#### 연구와의 연결점

**백신학 실험실 관점**:

**1. AlphaFold/RoseTTAFold 활용**:
```python
# Practical workflow
1. Target protein sequence (FASTA)
2. AlphaFold/RoseTTAFold prediction
3. pLDDT (confidence) 확인
4. PyMOL visualization
5. Epitope mapping (manual or tools)
6. Mutation design (stabilization, affinity ↑)
7. Experimental validation (binding assays)
```

**2. Epitope Mapping Tools**:
| Tool | Function | Input |
|------|----------|-------|
| **BepiPred3.0** | B-cell epitope | Sequence + Structure |
| **NetMHCpan** | MHC-I/II binding | Peptide sequence |
| **IEDB** | Epitope database | Pathogen name |
| **DiscoTope** | Discontinuous epitopes | Structure (PDB) |

**3. 구조 검증**:
- **Cryo-EM**: 고해상도 (~3 Å)
- **X-ray crystallography**: 원자 수준
- **SAXS**: Solution structure
- **HDX-MS**: Conformational dynamics

#### 필수 배경 지식

**1. AlphaFold Architecture**
```
Input: Multiple Sequence Alignment (MSA)
  ↓
Evoformer blocks (attention mechanisms)
  ↓
Structure module
  ↓
Output: 3D coordinates + pLDDT (confidence)
```

**2. Protein Stability**
- **Thermostability**: Tm (melting temperature)
- **Mutations**: Disulfide bonds, Pro substitutions
- **Folding energy**: ΔG (Rosetta, FoldX)

**3. Immunogen vs. Antigen**
- **Antigen**: 항체가 인식하는 molecule
- **Immunogen**: 면역 반응 유발하는 antigen
- → **Adjuvants** 필요 (면역 증강)

**4. mRNA Vaccine**
- **Mechanism**: mRNA → 세포 내 번역 → 항원 생산 → 면역 반응
- **Advantages**: 빠른 개발, 변이 대응
- **Challenges**: Stability (LNP), 부작용

#### 예상 질문 & 토론 포인트

**질문**:
1. "**AlphaFold3 vs. RoseTTAFold All-Atom** 비교? 백신 설계에 어느 것이 더 유용?"
2. "**한국형 차세대 단백질 AI** (LG 협력)의 특징? 백신 개발 특화?"
3. "**Epitope drift** (변이로 epitope 변화)를 AI로 예측 가능? Predictive modeling?"
4. "**Pan-coronavirus vaccine** 개발 현황? AI 설계 성공 사례?"
5. "**규제 측면**: AI 설계 백신의 FDA/MFDS 승인 경로? 검증 요구사항?"

---

### 🔹 발표 4 (15:20-15:50)

**연사**: Kee-Jong Hong (홍기종)
**소속**: Gachon University (가천대학교)
**제목**: Emerging viruses and pandemic preparedness: Vaccine R&D strategy for the pandemic responsiveness in Korea

#### 예상 내용

**1. 한국의 Emerging Viruses**
- **SFTS** (Severe Fever with Thrombocytopenia Syndrome): 진드기 매개
- **HFRS** (Hemorrhagic Fever with Renal Syndrome): 한타바이러스
- **AI** (Avian Influenza): H5N1, H5N6

**2. Pandemic Preparedness Framework**
```yaml
Surveillance:
  - 조기 감지 시스템
  - Genomic surveillance (변이 추적)

R&D Platform:
  - mRNA, nanoparticle, vectored vaccines
  - Rapid prototyping (100일 목표)

Manufacturing:
  - Domestic capacity (SK bioscience, 등)
  - Fill & finish

Distribution:
  - Cold chain
  - Equity
```

**3. 한국 백신 R&D 전략**
- **Platform diversification**
- **Public-private partnership**
- **International collaboration** (IVI, CEPI)

**4. Regulatory Readiness**
- **Fast-track approval**
- **EUA** (Emergency Use Authorization)

---

## 🧠 세션 전체 핵심 요약

### S7의 핵심 메시지

**"AI와 구조생물학이 백신 개발을 혁신하고 있다"**

| 발표 | 주제 | 혁신 요소 |
|------|------|----------|
| **Hwang** | Host-directed therapy | Broad-spectrum (STT3A/B) |
| **Park** | HBV receptor 구조 | Structure-based inhibitors |
| **Baek** | AI 백신 설계 | AlphaFold, RoseTTAFold |
| **Hong** | 팬데믹 대비 | 신속 플랫폼, 국가 전략 |

### 통합 관점

**백신 개발의 패러다임 전환**:
```
1. Target Identification (Baek - AI)
   ↓
2. Structure Determination (Park - Cryo-EM)
   ↓
3. Antigen Design (Baek - Structure-based)
   ↓
4. Platform Selection (Hong - mRNA, nanoparticle)
   ↓
5. Clinical Development (IVI - Trials)
```

**Host + Virus 통합 접근**:
- **Virus**: 구조 기반 항원 설계
- **Host**: HDT로 감염 억제
- **Synergy**: 조합 요법

---

## 📚 사전 읽기

### 필수
1. **Seungmin Hwang (2025)** - PNAS, "Shared host genetic landscape"
2. **Minkyung Baek (2021)** - Science, "Accurate prediction of protein structures...RoseTTAFold"
3. **AlphaFold2 (2021)** - Nature, "Highly accurate protein structure prediction"

### 추천
4. **RSV vaccine (2023)** - N Engl J Med, "mRNA-1345 vaccine"
5. **COVID-19 vaccine design** - Nature, "Structure-based design of prefusion-stabilized SARS-CoV-2 spikes"

---

## 🎤 Top 5 Questions

1. **[Hwang]** "STT3A/B inhibitor 개발 현황? Clinical trials?"
2. **[Baek]** "AlphaFold3 vs. RoseTTAFold? 백신 설계 차별점?"
3. **[Baek]** "Pan-coronavirus vaccine AI 설계? Success cases?"
4. **[Hong]** "한국 mRNA 백신 플랫폼? Domestic capability?"
5. **[All]** "AI + HDT combination: Rapidly deployable broad-spectrum platform?"

---

## 🤝 네트워킹 우선순위

1. **Minkyung Baek** (서울대) ⭐⭐⭐ - 국내, AI 전문가, ASPIRE Prize
2. **Seungmin Hwang** (Broad) ⭐⭐⭐ - HDT 선구자
3. **Jae-Hyun Park** (성균관대) ⭐⭐ - 국내, 구조생물학
4. **Kee-Jong Hong** (가천대) ⭐⭐ - 국내, 정책/전략

---

**예상 학습 성과**:
✅ AI 백신 설계 최신 동향 (AlphaFold, RoseTTAFold)
✅ Host-directed therapy 전략 (STT3A/B)
✅ Structure-based vaccine design 방법론
✅ 한국 팬데믹 대응 체계

**바이러스/백신 연구자 필수!** 💉
