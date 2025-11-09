# 배경 자료: S8 세균 감염 진단 및 치료

**세션**: S8 - Recent Advances in Diagnosis and Treatment of Bacterial Infections
**일시**: 2025년 10월 27일 (월) 13:50-15:50
**장소**: Rm 301+302
**중요도**: ⭐⭐⭐⭐⭐ (98/100점) - **최우선 필수!**

---

## 🎯 세션 개요

이 세션은 **AMR 진단 및 치료의 최신 기술**을 다룹니다. 도심 AMR 감시 연구에 **즉시 적용 가능한 현장 진단 기술**을 배울 수 있는 가장 실용적인 세션입니다.

### 왜 이 세션이 최우선인가?

- 🔬 **현장 진단 (Point-of-Care)**: 실험실 없이 도심 현장에서 AMR 검출
- ⚡ **빠른 검출**: 기존 48-72시간 → 30분-2시간으로 단축
- 🦠 **공기 중 AMR 검출**: 도심 대기 감시에 직접 적용 가능
- 💡 **혁신적 플랫폼**: Fidget spinner, Cell-free system, Graphene FET

---

## 📋 발표별 상세 분석

### 🔹 발표 1 (13:50-14:15)

**연사**: Jeong Wook Lee (이정욱)
**소속**: POSTECH (Pohang University of Science and Technology)
**제목**: Cell-free transcription cascades for rapid RNA detection and SNP discrimination

#### 최근 연구 배경

Lee 교수팀은 **COVID-19 진단을 위한 혁신적인 cell-free RNA 검출 기술 SENSR**을 개발했습니다.

**SENSR (SENsitive Splint-based one-pot isothermal RNA detection)**:
- **2020년 Nature Biomedical Engineering** 게재
- 30-50분 만에 RNA 검출 (RT-PCR 대비 빠름)
- 0.1 attomolar 검출 한계 (초고감도)
- 40개 nasopharyngeal 샘플: 95% PPV, 100% NPV

**핵심 메커니즘**:
```
1. Probe hybridization (표적 RNA 결합)
   ↓
2. SplintR ligase (Ligation)
   ↓
3. T7 RNA polymerase (Transcription cascade)
   ↓
4. Fluorogenic dye binding (Signal amplification)
   ↓
5. Fluorescence detection (30-50분)
```

**특징**:
- **One-pot reaction**: 모든 반응이 한 튜브에서
- **Isothermal**: 일정 온도 (37-42°C) - PCR처럼 thermal cycling 불필요
- **SNP discrimination**: Single nucleotide polymorphism 구별 가능

#### 예상 발표 내용

**1. Cell-free Transcription Cascade란?**

전통적 방법 vs. SENSR:
| 방법 | 시간 | 민감도 | 장비 | SNP 구별 |
|------|------|--------|------|----------|
| RT-qPCR | 2-4시간 | 높음 | Thermal cycler | 가능 (melting curve) |
| LAMP | 1-2시간 | 높음 | Heat block | 어려움 |
| **SENSR** | 30-50분 | 초고감도 | 단순 (형광 리더) | 가능 |

**2. 작동 원리**

**Key Components**:
- **Splint probes**: 표적 RNA 특이적 결합
- **SplintR ligase**: RNA ligase (thermostable)
- **T7 RNA polymerase**: Transcription amplification
- **RNA aptamer + fluorogenic dye**: Signal generation

**Cascade Amplification**:
- Ligation → 1 ligated product
- T7 transcription → 수백~수천 copies RNA
- Each RNA → Fluorescence signal
- **Exponential amplification**

**3. SNP Discrimination**

**중요성**:
- AMR mutation 검출 (e.g., rpoB S531L in rifampin-resistant TB)
- Strain typing
- Virulence gene variants

**메커니즘**:
- Splint probe가 perfect match에만 ligation 허용
- Single mismatch → No ligation → No signal
- **Allele-specific detection**

**4. 세균 감염 진단 응용**

COVID-19 외 응용:
- **Bacterial pathogens**: 16S rRNA detection
- **AMR genes**: mecA, blaKPC, blaNDM
- **Toxin genes**: Shiga toxin (stx1/stx2), Cholera toxin
- **Multiplex detection**: 여러 표적 동시 검출

#### 당신의 연구와의 연결점

**도심 AMR 감시에 적용**:

**1. 현장 RNA 검출**:
- **메타전사체 샘플**: 도심 대기/물/토양에서 RNA 추출
- SENSR로 **AMR gene transcripts** 검출
  - mecA (MRSA)
  - blaNDM, blaKPC (carbapenemase)
  - erm genes (macrolide resistance)
- **Active AMR 검출**: DNA가 아닌 RNA = actively expressed genes

**2. SNP-based AMR detection**:
- **Point mutations** 검출:
  - rpoB mutations (rifampin resistance)
  - gyrA/gyrB (fluoroquinolone resistance)
  - 23S rRNA (macrolide resistance)
- 메타지노믹스로 variant 발견 → SENSR로 현장 검증

**3. Portable platform**:
- **Battery-powered fluorescence reader**
- 도심 현장 (지하철역, 병원, 수처리장)에서 즉시 검사
- 30-50분 → **실시간 AMR 감시 가능**

**4. Multiplex AMR panel**:
```yaml
Urban AMR SENSR Panel:
  Gram-positive:
    - mecA (MRSA)
    - vanA/vanB (VRE)
  Gram-negative:
    - blaNDM (Carbapenemase)
    - blaKPC (Carbapenemase)
    - mcr-1 (Colistin resistance)
  Mycobacteria:
    - rpoB S531L (Rifampin-R TB)
```

#### 필수 배경 지식

**1. Cell-free Systems**
- **정의**: 세포 없이 생화학 반응만 수행
- **장점**:
  - 빠름 (세포 배양 불필요)
  - 조작 용이 (반응 조건 최적화)
  - 안전 (살아있는 병원체 불필요)
- **단점**:
  - 효소 비용
  - 안정성 (cold chain 필요)

**2. T7 RNA Polymerase**
- **유래**: Bacteriophage T7
- **특성**:
  - 매우 빠른 transcription (속도: E. coli RNAP의 5배)
  - T7 promoter 특이성 (고특이성)
  - **In vitro transcription (IVT)의 표준**
- **응용**: mRNA 백신 (Pfizer, Moderna), RNA probe 합성

**3. SplintR Ligase**
- **RNA ligase**: RNA-RNA ligation
- **Thermostable**: 고온에서 안정
- **Splinted ligation**:
  - Splint (guide) RNA가 두 RNA를 정렬
  - Perfect match 필요 → SNP discrimination

**4. Isothermal Amplification Methods**

비교:
| 방법 | 온도 | 시간 | 복잡도 | SNP 구별 |
|------|------|------|--------|----------|
| **LAMP** | 60-65°C | 30-60분 | 중간 | 어려움 |
| **RPA** | 37-42°C | 10-20분 | 낮음 | 어려움 |
| **SENSR** | 37-42°C | 30-50분 | 중간 | **가능** |

**5. Fluorogenic Dyes & RNA Aptamers**
- **RNA aptamer**: RNA that binds specific molecules
- **Malachite green aptamer**: Binds malachite green → 형광 증가
- **Spinach aptamer**: Binds DFHBI → GFP-like fluorescence
- **Signal-to-noise ratio**: Background 낮음 (unbound dye = low fluorescence)

#### 예상 질문 & 토론 포인트

**당신이 물어볼 질문** (우선순위):

1. "**메타전사체 샘플** (도심 대기에서 추출한 총 RNA)에 SENSR를 직접 적용할 수 있나요? Pre-amplification 필요한가요?"

2. "**Multiplex SENSR**로 여러 AMR genes를 동시 검출할 때, 최대 몇 개 타겟까지 가능한가요? (다른 fluorophores 사용?)"

3. "SENSR로 **정량 분석** (qSENSR?)이 가능한가요? AMR gene transcript abundance를 측정하고 싶습니다."

4. "**False positive**를 유발할 수 있는 요인은? 환경 샘플의 inhibitors (humic acid, polysaccharides) 영향?"

5. "Commercial kit 개발 계획이 있나요? **Point-of-care device** 형태로?"

**토론 예상**:
- **CRISPR-based detection (SHERLOCK, DETECTR)** vs. SENSR 비교
- **Lyophilization** (동결건조) 가능성 → Cold chain 없이 보관
- **Cost per test**: RT-PCR 대비 경제성?
- **Sensitivity in complex matrices**: Soil, wastewater, air samples

**네트워킹**:
- POSTECH는 KRIBB, UNIST와 가까움 (포항-울산-대전)
- Collaborative study 제안: "Urban air AMR surveillance with SENSR"

---

### 🔹 발표 2 (14:15-14:40) ⭐ **도심 AMR 감시 핵심!**

**연사**: Eun-Kyung Lim (임은경)
**소속**: KRIBB (Korea Research Institute of Bioscience & Biotechnology)
**제목**: Portable biosensing platforms for onsite detection of airborne antibiotic-resistant bacteria

#### 최근 연구 배경

Lim 박사는 **KRIBB에서 바이오센서 개발**을 주도하고 있으며, **2025년 획기적인 연구**를 발표했습니다.

**핵심 연구: CN-TAR Assay (2025)**

**제목**: "Onsite detection of airborne antibiotic-resistant bacteria via Cas9 nickase-triggered amplification reactions"

**CN-TAR = Cas9 Nickase-Triggered Amplification Reaction**

**성능**:
- **MRSA 검출 한계**: 1.40 copies/μL
- **VRE 검출 한계**: 1.13 copies/μL
- **Turnaround time**: Real-time (등온 반응)
- **Portable**: Isothermal PCR device 통합

**혁신성**:
- **Cas9 nickase**: DNA의 한 가닥만 절단 (double-strand 아님)
- **Rolling Circle Amplification (RCA)**: 지수적 증폭
- **Single-step detection**: 복잡한 workflow 없음
- **공기 샘플 검증**: Actual airborne samples tested!

**Validation**:
- Synthetic nucleic acids ✓
- Cultured bacteria ✓
- **Airborne samples** ✓ ← 실제 환경 검증!
- RT-PCR와 comparable sensitivity

#### 예상 발표 내용

**1. 공기 중 항생제 내성균의 중요성**

**문제**:
- **병원 감염**: 공기 매개 MRSA, VRE 전파
- **지역사회 확산**: 대중교통, 학교, 사무실
- **축산 환경**: MRSA ST398 (livestock-associated)
- **항생제 내성 유전자 전파**: Airborne horizontal gene transfer

**현재 방법의 한계**:
| 방법 | 시간 | 민감도 | 현장 사용 |
|------|------|--------|-----------|
| Culture | 24-72시간 | 중간 | ❌ |
| PCR | 3-5시간 | 높음 | ❌ (장비 필요) |
| qPCR | 2-3시간 | 매우 높음 | ❌ |
| **CN-TAR** | <2시간 | 매우 높음 | ✅ **Portable!** |

**2. CN-TAR Assay 메커니즘**

**Step-by-step**:
```
1. Air sampling
   ↓ (Filter collection)
2. DNA extraction (간단한 lysis)
   ↓
3. Cas9 nickase target recognition
   ↓ (mecA or vanA gene)
4. Single-strand cleavage (nick 생성)
   ↓
5. Rolling Circle Amplification (RCA)
   ↓ (Phi29 polymerase)
6. Real-time fluorescence detection
   ↓
7. Result (30-90분)
```

**핵심 구성요소**:
- **Cas9 nickase (D10A mutant)**:
  - Normal Cas9: Double-strand break
  - **Nickase**: Single-strand nick만
  - → RCA의 starting point
- **Guide RNA (gRNA)**:
  - mecA-specific gRNA (MRSA)
  - vanA-specific gRNA (VRE)
  - **Specificity**: Single nucleotide discrimination
- **Phi29 DNA polymerase**:
  - RCA workhorse
  - High processivity (수만 nucleotides)
  - Strand displacement
- **Circular template**:
  - Rolling circle
  - 지수적 증폭 (exponential)

**3. Portable Isothermal PCR Device**

**특징**:
- **Battery-powered**: 전원 불필요
- **Compact**: Handheld size
- **Real-time monitoring**: Fluorescence detection
- **Temperature control**: 37°C 유지 (등온)

**Workflow**:
```
[Air sampler] → [Filter] → [Lysis] → [CN-TAR device] → [Result]
   (10분)        (5분)      (5분)       (60-90분)        (즉시)
```

**Total time**: ~2시간 (vs. culture 48-72시간)

**4. 검증 결과**

**Airborne sample testing**:
- 병원 환경
- 축산 시설
- 지역사회 (학교, 지하철?)

**Performance**:
- **Specificity**: 100% (non-target bacteria에 반응 없음)
- **Sensitivity**: 1-2 copies/μL (ultra-sensitive)
- **False positives**: Minimal
- **Cross-reactivity**: None

#### 당신의 연구와의 연결점

**도심 AMR 감시의 완벽한 도구!**

**1. 도심 대기 AMR 모니터링**:

**샘플링 전략**:
```yaml
Location Types:
  High-risk:
    - 지하철역 (환기 불량)
    - 병원 (응급실, 중환자실)
    - 요양원
  Medium-risk:
    - 학교, 어린이집
    - 대형 쇼핑몰
    - 사무실 건물
  Baseline:
    - 공원 (outdoor)
    - 주거 지역

Sampling Schedule:
  - Peak hours (출퇴근 시간)
  - Seasonal variation
  - Before/after cleaning
```

**2. CN-TAR Panel for Urban AMR**:

**확장 가능한 타겟**:
```yaml
Current (Lim's study):
  - mecA (MRSA)
  - vanA/vanB (VRE)

Expandable:
  Gram-negative AMR:
    - blaNDM, blaKPC (Carbapenemase)
    - mcr-1 (Colistin)
  Respiratory pathogens:
    - M. tuberculosis (rpoB mutations)
  Toxins:
    - Shiga toxin genes
```

**3. Metagenomics + CN-TAR 통합**:

**Workflow**:
```
Step 1: 메타지노믹스 (주 1회)
  ↓
  - Community profiling
  - AMR gene discovery
  - Novel variants

Step 2: CN-TAR (매일/실시간)
  ↓
  - 주요 AMR genes targeted monitoring
  - Rapid outbreak detection
  - Hotspot identification
```

**Synergy**:
- Metagenomics = Broad discovery
- CN-TAR = Targeted, real-time monitoring

**4. Public Health Application**:

**Alert System**:
```
CN-TAR threshold > X copies/m³
  ↓
  Alert to public health authority
  ↓
  Enhanced cleaning/ventilation
  ↓
  Follow-up sampling (24h later)
  ↓
  Confirm clearance
```

#### 필수 배경 지식

**1. Cas9 Nuclease vs. Nickase**

| Type | Activity | DSB | Application |
|------|----------|-----|-------------|
| **Cas9 (wild-type)** | Endonuclease | Yes (양 가닥 절단) | Gene editing |
| **Cas9 D10A nickase** | Nickase | No (한 가닥만) | **Diagnostics, RCA** |
| **dCas9** | None | No | Transcription regulation |

**Why nickase for diagnostics?**
- Nick = RCA initiation point
- 특이성 높음 (gRNA-dependent)
- Safety (genomic editing risk 없음)

**2. Rolling Circle Amplification (RCA)**

**메커니즘**:
```
Circular template (100-200 nt)
    ↓
Primer annealing (Nick가 primer 역할)
    ↓
Phi29 polymerase extension
    ↓
Strand displacement
    ↓
Continuous synthesis (수천-수만 nt)
    ↓
Long ssDNA product (concatemer)
```

**장점**:
- **Isothermal** (30-37°C)
- **High sensitivity** (single molecule detection)
- **Simple**: Thermal cycling 불필요

**단점**:
- Circular template 제작 필요
- Background 관리

**3. Air Sampling for Bacteria**

**Methods**:
| Method | Principle | Sample Volume | Pros | Cons |
|--------|-----------|---------------|------|------|
| **Impaction** | Air → Agar plate | 100-1000 L | Culture 직접 | Viable only |
| **Filtration** | Air → Filter | 100-10,000 L | **DNA 추출 가능** | Requires extraction |
| **Impingement** | Air → Liquid | 100-1000 L | Gentle (viability) | Volume 제한 |
| **Electrostatic** | Charged particles | 수천 L | High volume | 고가 |

**For CN-TAR**: **Filtration** 최적
- Filter pore size: 0.22-0.45 μm
- Flow rate: 10-30 L/min
- Sampling time: 10-60분
- → 100-1800 L air volume

**4. Antibiotic Resistance Genes in Air**

**Sources**:
- **Human shedding**: Skin, respiratory droplets
- **Fomites resuspension**: Dust, surfaces
- **Wastewater aerosols**: Treatment plants
- **Livestock**: Farms, slaughterhouses

**Persistence**:
- DNA: Days to weeks (in dust)
- Viable bacteria: Hours to days
- **Spores**: Months (Bacillus, Clostridium)

**Factors**:
- Humidity (higher = longer survival)
- UV radiation (shorter survival)
- Temperature
- Airborne particulate matter (PM2.5, PM10)

**5. Portable Diagnostics Criteria**

**ASSURED (WHO)**:
- **Affordable**: <$10 per test
- **Sensitive**: Low detection limit
- **Specific**: No cross-reactivity
- **User-friendly**: Minimal training
- **Rapid & Robust**: <2h, field conditions
- **Equipment-free**: Minimal instrumentation
- **Deliverable**: Accessible to end-users

**CN-TAR**: Meets most criteria!
- Sensitive ✓
- Specific ✓
- Rapid ✓ (2h)
- Robust ✓
- Equipment: Minimal (portable device)
- Cost: TBD

#### 예상 질문 & 토론 포인트

**당신이 물어볼 질문** (최우선!):

1. "**도심 대기 샘플**에서 어떤 air sampling 방법을 사용했나요? Filter type과 sampling volume은?"

2. "CN-TAR를 **multiplex** (mecA + vanA + blaNDM 동시 검출)로 확장할 수 있나요? 여러 gRNA를 한 반응에?"

3. "**Portable device의 비용**은 얼마나 되나요? 그리고 per-test reagent cost는? (Public health surveillance budget 고려)"

4. "**Quantitative** CN-TAR가 가능한가요? Airborne AMR bacteria의 **농도** (CFU/m³ 또는 copies/m³)를 정량하고 싶습니다."

5. "환경 샘플의 **inhibitors** (dust, PM2.5, humic substances) 영향은 어떻게 극복했나요?"

6. "**Real-world deployment** 경험이 있나요? 병원이나 public space에서 pilot study?"

**Collaboration 제안**:
"저는 **도심 메타지노믹스 AMR 감시**를 하고 있습니다. CN-TAR를 서울 지하철/병원에 적용하는 collaborative study에 관심 있으신가요?"

**토론 예상**:
- **CRISPR diagnostics** 다른 플랫폼과 비교:
  - SHERLOCK (Cas13)
  - DETECTR (Cas12)
  - **CN-TAR (Cas9n + RCA)** ← Unique!
- **Commercial development**: Startup? Licensing?
- **Regulatory approval**: In vitro diagnostic (IVD) 인증?
- **Data integration**: CN-TAR + metagenomics + epidemiology

**네트워킹 전략**:
- ⭐⭐⭐ **최우선 네트워킹 대상!**
- 발표 직후 질문 (air sampling method)
- Coffee break/Poster session: "Collaborative study 제안서 보내드리고 싶습니다"
- Follow-up email (3일 내): Specific proposal with preliminary data
- KRIBB 방문 제안: "Lab tour & research discussion"

---

### 🔹 발표 3 (14:40-15:05) ⭐ **혁신적 플랫폼!**

**연사**: Yoon-Kyoung Cho (조윤경)
**소속**: UNIST (Ulsan National Institute of Science and Technology), Department of Biomedical Engineering
**제목**: Fidget spinner platforms for rapid bacterial detection

#### 최근 연구 배경

Cho 교수는 **놀라운 아이디어로 세계적 주목**을 받았습니다: **장난감 피젯 스피너를 진단 도구로 변환!**

**최신 연구: Plasmonic Fidget Spinner (2025)**

**제목**: "Nanoplasmonic SERS on fidget spinner for digital bacterial identification"
**게재**: Microsystems & Nanoengineering (2025년 3월 3일)

**P-FS = Plasmonic Fidget Spinner**

**구성**:
- Fidget spinner (손으로 회전)
- Nitrocellulose membrane (박테리아 여과)
- **Nanoplasmonic-enhanced matrix** (metallic features)
- **SERS (Surface-Enhanced Raman Spectroscopy)**

**성능**:
- **검출 시간**: 수 분 (culture 대비 수백 배 빠름)
- **균 종 구별**: E. coli vs. S. aureus (vibrational fingerprints)
- **실제 샘플**: Urine (UTI 진단)
- **전기 불필요**: Hand-powered! (자원 제한 지역에 이상적)

**이전 연구 (2020, Nature Biomedical Engineering)**:
- "A fidget spinner for the point-of-care diagnosis of urinary tract infection"
- UTI 진단 (E. coli in urine)
- 70분 → 진단 완료
- Sensitivity/specificity > 90%

#### 예상 발표 내용

**1. Fidget Spinner의 진단 활용 - 왜?**

**기존 진단의 문제**:
- **Culture**: 24-72시간
- **PCR**: 고가 장비, 전기 필요
- **Flow cytometry**: 더 고가, 전문가 필요

**자원 제한 환경 (LMICs - Low/Middle Income Countries)**:
- 전기 불안정
- 원심분리기 없음
- Refrigeration 없음

**Fidget Spinner 장점**:
- **Centrifugal force** (회전력으로 separation)
- **No electricity**
- **Portable**: Pocket-size
- **Cheap**: ~$1-5 (vs. centrifuge $1000+)
- **User-friendly**: 교육 최소

**2. 작동 원리**

**Version 1 (2020): UTI Diagnosis**

```
Sample (Urine)
  ↓
Add to spinner chamber
  ↓
Spin (1-2분, hand-powered)
  ↓ (Centrifugal force)
Bacteria pellet (bottom)
  ↓
Add lysis buffer + DNA binding beads
  ↓
Spin again
  ↓
DNA captured on beads
  ↓
Wash (spin)
  ↓
LAMP amplification (isothermal)
  ↓
Fluorescence detection (70분 total)
```

**Version 2 (2025): Plasmonic Fidget Spinner (P-FS)**

**Core Innovation**: **SERS (Surface-Enhanced Raman Spectroscopy)**

```
Sample (Urine, Blood, Environmental)
  ↓
Pass through spinner (회전하며 filtration)
  ↓
Bacteria captured on nanoplasmonic membrane
  ↓ (Nitrocellulose + metallic nanostructures)
Raman spectroscopy
  ↓ (Laser excitation)
Vibrational fingerprint acquisition
  ↓
Machine learning classification
  ↓
Species identification (수 분)
```

**3. SERS (Surface-Enhanced Raman Spectroscopy)**

**Raman Spectroscopy 기본**:
- **원리**: 분자의 vibrational modes 측정
- Laser → 샘플 → Inelastic scattering
- **Fingerprint**: 각 분자/균종마다 unique spectrum

**SERS Enhancement**:
- **Metallic nanostructures** (Au, Ag nanoparticles)
- Localized surface plasmon resonance (LSPR)
- **Enhancement factor**: 10⁶-10⁸ ×
- → Single molecule detection 가능

**Bacterial SERS**:
- **Cell wall components**: Peptidoglycan, teichoic acids
- **Proteins**: Surface proteins
- **Lipids**: Membrane lipids
- **DNA/RNA** (if lysed)

**Species discrimination**:
| Bacteria | Characteristic Raman Peaks |
|----------|----------------------------|
| **E. coli** | 1380 cm⁻¹ (DNA), 730 cm⁻¹ (adenine) |
| **S. aureus** | 1450 cm⁻¹ (CH₂ bend), 1003 cm⁻¹ (phenylalanine) |
| **P. aeruginosa** | 1600 cm⁻¹ (amide I), pyocyanin peaks |

**4. Nanoplasmonic-Enhanced Matrix**

**Fabrication**:
- Nitrocellulose membrane (porous)
- Metal deposition (Au or Ag nanoparticles)
- Optimized spacing for "hot spots"

**Function**:
- **Filtration**: Bacteria captured
- **SERS enhancement**: Plasmonic hot spots
- **Integration**: Fidget spinner에 장착

**5. Machine Learning Classification**

**Workflow**:
```
SERS spectrum (수백-수천 data points)
  ↓
Preprocessing (baseline correction, normalization)
  ↓
Feature extraction (Peak positions, intensities)
  ↓
ML model (SVM, Random Forest, CNN)
  ↓
Species prediction (E. coli, S. aureus, etc.)
```

**Training**:
- Reference strain spectra (ATCC strains)
- Clinical isolates
- **Accuracy**: >95% (2-3 species)

#### 당신의 연구와의 연결점

**도심 환경 AMR 감시에 혁명적!**

**1. Portable Environmental Monitoring**:

**Use Cases**:
```yaml
Urban Water Monitoring:
  - 지하철 공기
  - 병원 환기구
  - 하수 처리장 유출수
  - 공공 화장실 수도꼭지

Sample Processing:
  1. Collect sample (water, air filter rinse)
  2. Spin on P-FS (1-2분)
  3. SERS measurement (5-10분)
  4. Species ID + AMR prediction
```

**2. SERS-based AMR Detection**:

**가능성**:
- **Phenotypic resistance**: Cell wall changes in resistant strains
  - MRSA vs. MSSA (mecA → altered PBP2a → cell wall structure)
  - VRE vs. VSE (vancomycin → D-Ala-D-Lac)
- **SERS signatures**:
  - Resistant strains: Distinct Raman peaks
  - ML training on resistant vs. susceptible

**Challenge**:
- Genotypic (AMR genes) detection harder with SERS
- → Combine with CN-TAR or SENSR for gene detection

**3. Rapid Species ID for Metagenomics Validation**:

**Workflow**:
```
Metagenomics (Week 1):
  - Community analysis
  - "High E. coli abundance in Site A"
  ↓
P-FS Validation (Week 2):
  - On-site sampling at Site A
  - Fidget spinner + SERS
  - "Confirmed: E. coli dominant"
  ↓
Targeted intervention
```

**4. Resource-Limited Settings**:

**도심 지역도 "자원 제한" 될 수 있음**:
- 야외 모니터링 (공원, 강변)
- 이동식 검사 (Mobile testing van)
- 긴급 상황 (정전, 재난)

**P-FS 장점**:
- No electricity
- Minimal training
- Results in <30분

#### 필수 배경 지식

**1. Centrifugal Microfluidics**

**원리**:
- **Centrifugal force**: F = mω²r
  - m = mass
  - ω = angular velocity
  - r = radius

**Fidget spinner**:
- Rotation speed: 3,000-6,000 RPM (손으로)
- → Centrifugal force sufficient for:
  - Cell pelleting
  - Plasma separation (blood)
  - Bead-based DNA extraction

**Microfluidic design**:
- **Channels**: Sample flow paths
- **Chambers**: Reaction zones, waste
- **Valves**: Passive (burst valves, siphon valves)

**2. Surface-Enhanced Raman Spectroscopy (SERS)**

**Physics**:
- **Raman scattering**: Inelastic photon scattering
  - Stokes shift: λ_scattered > λ_incident
  - Anti-Stokes: λ_scattered < λ_incident

**Enhancement mechanisms**:
1. **Electromagnetic (EM)**:
   - Surface plasmons on metal nanoparticles
   - Local electric field ↑↑
   - Enhancement: 10⁴-10⁸
2. **Chemical (Charge transfer)**:
   - Molecule-metal electron transfer
   - Enhancement: 10-100

**SERS substrates**:
- **Colloidal nanoparticles**: Au, Ag
- **Nanostructured surfaces**: Arrays, roughened
- **"Hot spots"**: Gaps between nanoparticles (1-10 nm)
  - Enhancement max at hot spots

**3. Raman Spectroscopy for Bacteria**

**Advantages**:
- **Label-free**: No staining
- **Non-destructive**: Live cells 가능
- **Fingerprint**: Unique spectrum per species
- **Fast**: 수 초-분 (spectrum acquisition)

**Challenges**:
- **Weak signal**: Raman scattering 효율 낮음 (→ SERS 필요)
- **Fluorescence interference**: 일부 bacteria
- **Standardization**: Spectrum variability (growth conditions)

**Typical bacterial Raman peaks**:
| Wavenumber (cm⁻¹) | Assignment |
|-------------------|------------|
| 730 | Adenine |
| 785 | DNA/RNA bases |
| 1003 | Phenylalanine |
| 1250-1350 | Amide III (protein) |
| 1450 | CH₂ bending (lipids) |
| 1655 | Amide I (protein) |

**4. Machine Learning for Spectral Classification**

**Pipeline**:
```
Raw SERS spectra
  ↓
Preprocessing:
  - Baseline correction (polynomial fitting)
  - Normalization (total area, peak intensity)
  - Smoothing (Savitzky-Golay filter)
  ↓
Feature extraction:
  - Peak picking
  - Principal Component Analysis (PCA)
  - Peak intensity ratios
  ↓
Classification:
  - Support Vector Machine (SVM)
  - Random Forest
  - Convolutional Neural Network (CNN) for raw spectra
  ↓
Species prediction + confidence score
```

**Training data**:
- Reference strains: 10-100 spectra each
- Clinical isolates: Expand diversity
- Cross-validation: 5-10 fold

**Performance metrics**:
- Accuracy, Precision, Recall
- Confusion matrix (misclassifications)

**5. Point-of-Care Diagnostics for Bacteria**

**Requirements**:
| Criteria | Target | P-FS |
|----------|--------|------|
| **Time** | <1 hour | ✅ 10-30분 |
| **Cost** | <$10 | ✅ ~$5 (estimated) |
| **Sensitivity** | 10³-10⁵ CFU/mL | ✅ (SERS ultra-sensitive) |
| **Specificity** | >95% | ✅ (ML-based) |
| **Equipment** | Portable | ✅ Hand-powered |
| **Electricity** | Optional | ✅ None! |

#### 예상 질문 & 토론 포인트

**당신이 물어볼 질문** (우선순위):

1. "**SERS signature로 AMR 예측**이 가능한가요? 예를 들어 MRSA vs. MSSA를 SERS spectrum으로 구별? (mecA 발현 → PBP2a → cell wall change)"

2. "P-FS를 **환경 샘플** (air filter rinse, wastewater)에 적용했을 때, 복잡한 matrix (다양한 species mixture)에서도 species ID가 가능한가요?"

3. "**Portable Raman spectrometer**의 비용과 크기는? Field deployment를 위한 현실적인 옵션이 있나요?"

4. "SERS + ML 모델을 **새로운 species/strains**에 확장하려면? Transfer learning? 도심 환경 균주로 retraining?"

5. "**Quantification**이 가능한가요? Bacterial load (CFU/mL) estimation?"

**Collaboration 제안**:
"저는 도심 AMR 감시를 위해 메타지노믹스를 사용하는데, **P-FS로 빠른 species validation**을 하고 싶습니다. UNIST-서울 collaborative study 가능할까요?"

**토론 예상**:
- **SERS-based AMR phenotyping**: Realistic?
  - Metabolic byproducts (e.g., β-lactamase activity?)
  - Cell surface changes
- **Smartphone integration**: Portable Raman + smartphone camera?
- **Commercial pathway**: FDA approval for clinical use?
- **Field robustness**: Temperature, humidity effects on SERS?

**네트워킹 전략**:
- ⭐⭐⭐ **매우 혁신적 → 네트워킹 필수!**
- 발표 후 질문 (Environmental sample application)
- UNIST 가까움 (울산) → Lab visit 제안
- Potential collaboration: "Urban microbiome monitoring with P-FS"

---

### 🔹 발표 4 (15:05-15:30)

**연사**: Moo-seung Lee (이무승)
**소속**: KRIBB, Infectious Disease Research Center
**제목**: Diagnosis and treatment of enterohaemorrhagic *Escherichia coli* shiga toxin-mediated hemolytic uremic syndrome

#### 최근 연구 배경

Lee 박사는 **Shiga toxin과 HUS (hemolytic uremic syndrome) 전문가**입니다.

**최신 연구: Graphene FET Biosensor (2025)**

**제목**: "An ultrasensitive diagnostic system for minuscule level of hemolytic uremic syndrome"

**Graphene-based Field-Effect Transistor (FET) Biosensor**:
- **검출 한계**: Femtogram (fg) level (10⁻¹⁵ g)
- **Specificity**: 매우 높음
- **Label-free**: Fluorophore 불필요
- **Real-time**: Electrical signal 직접 측정

**이전 연구 (2018, 2021)**:
- "Experimental in vivo models of bacterial Shiga toxin-associated HUS" (Review)
- "Inhibition of O-GlcNAcylation protects from Shiga toxin-mediated cell injury"

#### 예상 발표 내용

**1. Shiga Toxin & HUS**

**Enterohemorrhagic E. coli (EHEC)**:
- **Serotypes**: O157:H7 (most common), O104:H4, O26, O111
- **Transmission**: Contaminated food (beef, vegetables), water
- **Symptoms**:
  - Bloody diarrhea (hemorrhagic colitis)
  - Abdominal cramps
  - → HUS (5-10% of cases, especially children)

**HUS (Hemolytic Uremic Syndrome)**:
- **Triad**:
  1. **Hemolytic anemia**: RBC lysis
  2. **Thrombocytopenia**: Platelet 감소
  3. **Acute renal failure**: Kidney damage
- **Mortality**: 3-5% (higher in children <5세)
- **Long-term**: Chronic kidney disease (25-30%)

**Shiga Toxin (Stx)**:
- **Types**: Stx1, Stx2 (Stx2 more severe)
- **Structure**:
  - A subunit (enzymatic, RNA N-glycosidase)
  - B subunit (pentamer, binds Gb3 receptor)
- **Mechanism**:
  - Binds Gb3 on endothelial cells (kidney, brain, colon)
  - Internalized → Retrograde transport to ER
  - A subunit → 28S rRNA cleavage → Ribosome inactivation
  - → Protein synthesis ↓ → Cell death

**2. Current Diagnostics**

**Problems**:
- **Culture**: 24-72시간
- **Toxin detection (ELISA)**: 4-8시간, moderate sensitivity
- **PCR (stx genes)**: 3-5시간, requires equipment
- **Early diagnosis critical**: HUS prevention (no antibiotics - toxin release ↑)

**3. Graphene FET Biosensor**

**Field-Effect Transistor (FET)**:
- **Semiconductor device**: Current modulation by electric field
- **Graphene**: Single-layer carbon (2D material)
  - High electron mobility
  - Large surface area
  - Biocompatible

**Biosensor Design**:
```
Graphene channel (FET)
  ↓
Functionalized with anti-Stx antibody
  ↓
Sample applied (serum, stool filtrate)
  ↓
Stx binds antibody
  ↓
Surface charge change
  ↓
Channel conductance change
  ↓
Electrical signal (real-time)
```

**Performance**:
- **Sensitivity**: fg/mL (vs. ELISA ng/mL)
- **Speed**: 수 분
- **Specificity**: Anti-Stx antibody-dependent

**4. Treatment Strategies**

**Current (supportive)**:
- **Hydration**: IV fluids
- **Dialysis**: Acute renal failure
- **Blood transfusion**: Severe anemia
- **⚠️ No antibiotics**: Toxin release 증가

**Emerging therapies** (Lee's research):
- **O-GlcNAcylation inhibitors**:
  - O-GlcNAc transferase (OGT) inhibition
  - Protects cells from Stx toxicity (2021 publication)
- **Toxin neutralizers**:
  - Anti-Stx antibodies (monoclonal)
  - Gb3 analogs (decoy receptors)
- **Ribosome protection**:
  - Inhibit retrograde transport

#### 당신의 연구와의 연결점

**도심 AMR 감시와의 연결 (간접)**:

**1. EHEC in Urban Environment**:

**Sources**:
- **Food contamination**: Restaurants, markets
- **Water**: Runoff, sewage overflow
- **Contact**: Petting zoos, farms

**Surveillance**:
- Metagenomics에서 **stx genes** 검출
  - stx1, stx2 variants
- **eae gene** (intimin, adhesion)
- Serotyping markers

**2. Graphene FET Technology Transfer**:

**AMR gene detection**:
- Functionalize graphene with **AMR gene-specific probes**
  - mecA, blaNDM, mcr-1
- Direct electrical detection (no amplification)
- **Ultra-sensitive** environmental monitoring

**Potential**:
```yaml
Urban Water AMR Biosensor (Graphene FET):
  Target genes:
    - mecA (MRSA)
    - blaNDM (Carbapenemase)
    - stx2 (EHEC virulence)

  Workflow:
    1. Water sample (100 mL)
    2. Filtration & DNA extraction
    3. Apply to Graphene FET array
    4. Real-time electrical readout (10-30분)
```

**3. Integration with Metagenomics**:

**Discovery → Validation**:
```
Metagenomics: "stx2 detected in river sample"
  ↓
Graphene FET: On-site confirmation (30분)
  ↓
Public health alert
```

#### 필수 배경 지식

**1. Shiga Toxin Mechanism**

**Detailed pathway**:
```
EHEC colonizes colon
  ↓
Stx1/Stx2 released
  ↓
Absorbed into bloodstream
  ↓
Binds Gb3 (globotriaosylceramide) on endothelial cells
  ↓ (Kidney glomeruli, brain)
Receptor-mediated endocytosis
  ↓
Retrograde transport (endosome → Golgi → ER)
  ↓
A subunit translocates to cytosol
  ↓
Cleaves adenine-4324 in 28S rRNA
  ↓
60S ribosomal subunit inactivation
  ↓
Protein synthesis STOP
  ↓
Cell death (apoptosis/necrosis)
  ↓
Endothelial damage → Microthrombi
  ↓
HUS (hemolysis + thrombocytopenia + renal failure)
```

**2. Gb3 Receptor**

**Structure**: Glycosphingolipid
- Ceramide (lipid anchor)
- Glucose-Galactose-Galactose (sugar headgroup)

**Distribution**:
- **High**: Kidney (glomerular endothelium), Brain, Colon
- **Low**: Most other tissues
- → Explains HUS tropism

**B subunit binding**:
- Pentameric B subunit
- Each B binds Gb3
- High avidity (multivalent binding)

**3. Graphene Electronics**

**Graphene properties**:
- **2D material**: Single atomic layer carbon
- **Zero bandgap**: Semi-metal
- **High mobility**: Electrons move fast
- **Ambipolar**: Both electrons and holes as carriers

**FET principle**:
```
Source ----[Graphene channel]---- Drain
              ↑
            Gate (electrolyte)
```

**Sensing**:
- Target binds to graphene surface
- Surface potential changes
- → Gate effect
- → Channel conductance (G = I/V) changes
- → Electrical signal

**Advantages**:
- **Label-free**: No fluorophores, enzymes
- **Real-time**: Immediate electrical response
- **Sensitive**: Single molecule detection possible
- **Portable**: Small device

**4. Biosensor Functionalization**

**Surface chemistry**:
```
Graphene
  ↓
Pyrene-based linker (π-π stacking)
  ↓
Carboxyl groups (-COOH)
  ↓
EDC/NHS coupling
  ↓
Anti-Stx antibody (covalent attachment)
```

**Specificity**:
- Antibody selectivity
- Non-specific binding minimization (BSA blocking)

**5. O-GlcNAcylation**

**Post-translational modification**:
- O-linked β-N-acetylglucosamine (O-GlcNAc)
- Added to Ser/Thr residues (like phosphorylation)
- **OGT (O-GlcNAc transferase)**: Add O-GlcNAc
- **OGA (O-GlcNAcase)**: Remove

**Role in Shiga toxin response**:
- Lee's finding: **OGT inhibition protects cells**
- Mechanism: Unknown (ongoing research)
- Hypothesis: Affects retrograde transport or ribosome?

#### 예상 질문 & 토론 포인트

**당신이 물어볼 질문**:

1. "Graphene FET 기술을 **AMR genes** (mecA, blaNDM) 검출에 적용할 수 있을까요? Antibody 대신 DNA probe 사용?"

2. "**Environmental samples** (강물, 하수)에서 Stx 또는 EHEC를 Graphene FET로 검출한 경험이 있나요?"

3. "**Multiplexing**이 가능한가요? 하나의 chip에 여러 graphene channels (각각 다른 antibody)?"

4. "OGT inhibitors의 **in vivo efficacy**는? Animal model에서 HUS prevention?"

**토론 예상**:
- **Graphene FET commercialization**: Cost, manufacturing?
- **Regulatory hurdles**: Biosensor approval for clinical use?
- **EHEC outbreak response**: Rapid on-site testing

**네트워킹**:
- 중간 우선순위 (기술은 흥미롭지만, 연구 focus가 약간 다름)
- Graphene FET 기술 협력 가능성 탐색

---

### 🔹 발표 5 (15:30-15:50)

**연사**: Namil Lee (이남일)
**소속**: KAIST
**제목**: Unlocking the full potential of *Streptomyces* by synergizing systems and synthetic biology

#### 연구 배경

**Streptomyces**:
- **"Antibiotic factory"**: 자연계 항생제의 50-60% 생산
- **Secondary metabolites**: Streptomycin, tetracycline, erythromycin, etc.
- **Synthetic biology target**: Pathway engineering for novel antibiotics

#### 예상 발표 내용 (간략)

**1. Streptomyces as antibiotic source**
- Natural product biosynthesis
- BGCs (Biosynthetic Gene Clusters)

**2. Systems biology approach**:
- Genome-scale metabolic models
- Transcriptomics, proteomics
- Pathway prediction

**3. Synthetic biology tools**:
- CRISPR-Cas9 editing
- Heterologous expression
- Pathway optimization

**4. Novel antibiotic discovery**:
- Silent BGC activation
- Hybrid antibiotics

#### 연결점 (간접):

**AMR 관점**:
- **New antibiotics from Streptomyces** → AMR 대응
- 도심 토양 Streptomyces metagenomics → Novel BGC discovery

**Priority**: 낮음 (S4, S8 focus 후 여유 있으면)

---

## 🧠 세션 전체 핵심 요약

### S8의 핵심 메시지

**"AMR 진단은 빠르고, 현장에서, 저렴하게!"**

| Technology | Speed | Portability | AMR Application |
|------------|-------|-------------|-----------------|
| **SENSR** (Lee) | 30-50분 | Moderate (fluorescence reader) | AMR gene RNA detection |
| **CN-TAR** (Lim) | <2시간 | ✅ Portable isothermal device | **Airborne MRSA/VRE** ⭐ |
| **P-FS** (Cho) | 10-30분 | ✅✅ Hand-powered! | Species ID, AMR phenotype? |
| **Graphene FET** (Lee M) | <30분 | ✅ Small device | Toxin/Gene detection |

### 도심 AMR 감시 통합 전략

```yaml
Tier 1 - Broad Surveillance (Weekly-Monthly):
  - Metagenomics: Community profiling, AMR gene discovery

Tier 2 - Targeted Monitoring (Daily):
  - CN-TAR: Airborne MRSA/VRE at hotspots
  - P-FS: Species confirmation

Tier 3 - Rapid Validation (On-demand):
  - SENSR: RNA-based active AMR detection
  - Graphene FET: Ultra-sensitive confirmation
```

### Metagenomics Markers from S8

```yaml
Detection Targets:
  Cell-free RNA (SENSR):
    - mecA transcripts (active MRSA)
    - carbapenemase mRNA (blaNDM, blaKPC)

  DNA (CN-TAR):
    - mecA gene (MRSA)
    - vanA/vanB (VRE)
    - Expandable to blaNDM, mcr-1

  SERS Phenotype (P-FS):
    - Species: E. coli, S. aureus, P. aeruginosa
    - Potential AMR signatures (cell wall changes)

  Toxins/Proteins (Graphene FET):
    - Shiga toxin
    - Adaptable to AMR proteins?
```

---

## 📚 사전 읽기 (우선순위)

### 필수

1. **Eun-Kyung Lim (2025)** - "Onsite detection of airborne antibiotic-resistant bacteria via Cas9 nickase-triggered amplification reactions"
   - 최신! 꼭 읽기

2. **Yoon-Kyoung Cho (2025)** - "Nanoplasmonic SERS on fidget spinner for digital bacterial identification" (Microsystems & Nanoengineering)

3. **Jeong Wook Lee (2020)** - SENSR technology (Nature Biomedical Engineering)

### 추천

4. **RCA (Rolling Circle Amplification) Review** - 메커니즘 이해

5. **SERS for bacteria** - Raman spectroscopy 기초

---

## 🎤 질문 리스트 (Top Priority)

### Must Ask!

1. **[Lim]** "CN-TAR를 도심 대기 샘플에 적용할 때 air sampling 방법과 multiplex expansion 가능성은?"

2. **[Cho]** "P-FS SERS로 AMR phenotype (MRSA vs. MSSA) 구별이 가능한가요? 환경 샘플 적용 경험은?"

3. **[Lee J]** "SENSR를 metatranscriptomic 샘플에 적용 시 pre-amplification 필요 여부와 multiplex 한계는?"

### Backup

4. **[Lee M]** "Graphene FET를 AMR gene detection으로 확장 가능한가요?"

5. **[Lee N]** "도심 토양 Streptomyces에서 novel BGC discovery?"

---

## 🤝 네트워킹 우선순위

### 1위: Eun-Kyung Lim (KRIBB) ⭐⭐⭐

**Why**: Airborne AMR detection = 연구 직결!

**Strategy**:
- 발표 직후 질문
- Collaborative study 제안 (Seoul subway CN-TAR monitoring)
- KRIBB 방문 약속

### 2위: Yoon-Kyoung Cho (UNIST) ⭐⭐⭐

**Why**: P-FS 혁신적, portable

**Strategy**:
- Environmental sample application 논의
- SERS-based AMR phenotyping 가능성
- UNIST lab visit

### 3위: Jeong Wook Lee (POSTECH) ⭐⭐

**Why**: SENSR metatranscriptomics 응용

**Strategy**:
- RNA-based active AMR monitoring
- Technical consultation

---

## ⚡ 세션 당일 체크리스트

### 사전 (전날)
- [ ] Lim (2025), Cho (2025) 논문 읽기
- [ ] CN-TAR, P-FS, SENSR 메커니즘 정리
- [ ] 질문 리스트 final check

### 당일 (10/27 오후)
- [ ] 점심 후 Rm 301+302 미리 도착 (13:40)
- [ ] 앞자리 선점
- [ ] 명함 10장 준비
- [ ] 노트 + 볼펜

### 세션 중
- [ ] 각 발표 핵심 포인트 메모
- [ ] 특히 Lim, Cho 발표 집중
- [ ] Slide 사진 (허용시)

### 직후
- [ ] Lim, Cho와 직접 대화
- [ ] Collaborative study 제안
- [ ] 명함 교환 + 뒷면 메모
- [ ] Poster session 약속

---

**예상 학습 성과**:
✅ 4가지 혁신 진단 기술 습득 (SENSR, CN-TAR, P-FS, Graphene FET)
✅ 도심 AMR 감시 즉시 적용 가능한 플랫폼 파악
✅ KRIBB, UNIST 연구자와 collaboration 기회
✅ Portable diagnostics의 미래 비전

**핵심 Takeaway**: "실험실에서 현장으로!" → Point-of-care AMR detection 시대
