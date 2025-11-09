# 배경 자료: S17 인수공통감염병 연구 (One Health)

**세션**: S17 - Emerging Zoonosis Researches for One Health
**일시**: 2025년 10월 28일 (화) 09:00-11:00
**장소**: Convention Hall 1
**Co-organized**: Korea Zoonosis Research Institute (KoZRI), Jeonbuk National University
**Chair**: Jeong Yoon Lee (Jeonbuk National University) & Jun-Gu Kang (Jeonbuk National University)
**중요도**: ⭐⭐⭐⭐⭐ (85/100점) - **One Health 연구자 필수!**

---

## 🎯 세션 개요

이 세션은 **한국의 주요 인수공통감염병 (Zoonosis)**과 **One Health 접근법**을 다룹니다. 전북대 Korea Zoonosis Research Institute 주최로 **국가 차원의 zoonosis 대응 전략**을 제시합니다.

### 왜 이 세션이 중요한가?

- 🦠 **SFTS 백신**: 중증열성혈소판감소증후군 (진드기 매개) - 한국 주요 위협
- 🐷 **ASF 백신**: 아프리카돼지열병 - 한국 양돈 산업 위기
- 💊 **AMR Stewardship**: 양돈 산업에서 항생제 사용 관리
- 🧬 **Flavivirus 플랫폼**: SARS-CoV-2 기술의 확장 적용
- 🔬 **Exosome 면역**: 세포 외 소포체 매개 병원성

### 이 세션의 공통 테마

```
One Health Approach
├─ 인간-동물-환경 통합 감시
├─ 백신 개발 (SFTS, ASF)
├─ AMR 관리 (양돈)
├─ 플랫폼 기술 (Flavivirus, SARS-CoV-2)
└─ 면역 기전 (Exosome signaling)
```

---

## 📋 발표별 상세 분석

### 🔹 발표 1 (09:00-09:25)

**연사**: Jun-Gu Kang (강준구)
**소속**: Jeonbuk National University (전북대학교)
**제목**: Vaccine development of *Bandavirus dabieense* in mouse and dog models

#### 연구 배경

**Bandavirus dabieense** (구명: SFTS virus):
- **SFTS** (Severe Fever with Thrombocytopenia Syndrome): 중증열성혈소판감소증후군
- **2009년 중국 발견**, 2012년 한국 첫 확진
- **진드기 매개** (Haemaphysalis longicornis - 작은소피참진드기)
- **치사율 10-30%** (한국, 일본), 중국은 ~15%

**문제점**:
- **치료제 없음**: 대증 요법만
- **백신 없음**: 개발 중
- **매년 증가**: 기후 변화, 진드기 서식지 확대

#### 예상 발표 내용

**1. SFTS Virus (Bandavirus dabieense)**

**분류**:
- **Family**: Phenuiviridae
- **Genus**: Bandavirus
- **Genome**: Segmented (L, M, S) negative-sense RNA

**구조**:
- **Glycoproteins** (Gn, Gc): Envelope, receptor binding
- **Nucleoprotein** (N): RNA 보호, 면역 타겟
- **Polymerase** (L): RNA replication

**전파 경로**:
```
진드기 (Haemaphysalis longicornis)
  ↓ (물림)
인간/동물 (개, 고양이, 소, 염소)
  ↓ (바이러스 증식)
발열, 혈소판 감소, 백혈구 감소
  ↓
다장기 부전 → 사망 (10-30%)
```

**One Health 관점**:
- **동물**: 반려동물 (개, 고양이) 감염 → 사람 전파?
- **환경**: 진드기 서식지 (산림, 풀밭)
- **인간**: 농업 종사자, 등산객 고위험

**2. 백신 개발 전략**

**A. 불활화 백신 (Inactivated)**:
```python
# Protocol
1. Virus 배양 (Vero cells)
2. β-propiolactone 처리 (inactivation)
3. Adjuvant 혼합 (Alum, AS03, etc.)
4. Mouse/Dog immunization
5. Antibody titers (ELISA, neutralization)
6. Challenge (live virus)
```

**B. Subunit 백신**:
- **Gn/Gc glycoproteins**: Receptor binding, neutralizing Ab target
- **Nucleoprotein (N)**: T-cell response

**C. mRNA 백신** (최신):
- **LNP-mRNA (Gn, Gc, N)**
- COVID-19 플랫폼 응용
- 빠른 개발 가능

**3. Mouse Model**

**IFNAR-/- mice** (Interferon receptor knockout):
- **Wild-type**: SFTS virus resistant (interferon 반응)
- **IFNAR-/-**: Susceptible, 인간 질병 재현
  - 발열, 혈소판 감소, 다장기 손상

**Vaccine efficacy testing**:
```yaml
Groups:
  1. Mock (PBS)
  2. Vaccine (prime-boost, 2-3 weeks)

Challenge:
  - SFTS virus inoculation (10^4-10^6 PFU)
  - Monitor: Weight loss, survival, viral load

Endpoints:
  - Survival rate (%)
  - Viral titer (blood, organs) - qRT-PCR
  - Pathology (H&E, IHC)
```

**4. Dog Model** ⭐

**왜 개?**
- **Natural host**: 개도 SFTS 걸림 (야외 진드기)
- **사람과 유사**: 증상, 면역 반응
- **Zoonotic transmission**: 개 → 사람 전파 보고

**Dog vaccination**:
```yaml
Protocol:
  - Healthy dogs (Beagle)
  - Vaccine IM (2-3 doses)
  - Antibody monitoring (weeks 0, 2, 4, 8)

Safety:
  - Adverse events (injection site, 발열)
  - Blood chemistry (간, 신장)

Efficacy:
  - Neutralizing antibody titer
  - T-cell response (IFN-γ ELISPOT)
  - Challenge (experimental or field trial)
```

**5. 예상 결과**

**Mouse**:
- **Survival**: 0% (Mock) vs. 80-100% (Vaccine)
- **Viral load**: 10⁶ → 10² copies/mL
- **Antibody**: Neutralizing titer >1:320

**Dog**:
- **Seroconversion**: 100%
- **Neutralizing Ab**: Detectable at week 2, peak week 4
- **Safety**: Well-tolerated

#### 연구와의 연결점

**One Health 실험실 관점**:

**1. Zoonotic Virus Research**:
- **Biosafety**: BSL-3 facility 필요
- **Animal models**: 윤리 승인, 시설
- **Field surveillance**: 진드기, 동물, 사람 샘플링

**2. Vaccine Development Pipeline**:
```
1. Antigen selection (Gn/Gc/N)
2. Expression system (mammalian, E. coli)
3. Adjuvant screening
4. Immunogenicity (small animals)
5. Efficacy (challenge model)
6. Safety (toxicology)
7. GMP production
8. Clinical trials (Phase I/II/III)
```

**3. Serological Assays**:
| Assay | Purpose |
|-------|---------|
| **ELISA** | Antibody quantification |
| **Neutralization (PRNT)** | Functional antibody |
| **ELISPOT (IFN-γ)** | T-cell response |
| **Flow cytometry** | Cell subsets (CD4/CD8) |

#### 필수 배경 지식

**1. Bunyavirales (Phenuiviridae)**
- **Segmented genome**: L, M, S
- **Ambisense**: S segment codes both strands
- **Vector-borne**: 진드기, 모기

**2. IFNAR-/- Mouse**
- **Type I IFN**: IFN-α/β
- **Receptor**: IFNAR1/IFNAR2
- **Knockout**: Viral infection susceptible
- **Use**: Vaccine/drug testing

**3. Neutralizing Antibodies**
- **PRNT** (Plaque Reduction Neutralization Test)
- **Titer**: 50% reduction (PRNT50), 90% (PRNT90)
- **Correlate of protection**: >1:40-80

#### 예상 질문

1. "**사람 임상 시험** 계획? Phase I 시작 시기?"
2. "**Dog-to-human transmission** 증거? 백신으로 차단 가능?"
3. "**Cross-protection**: 다른 Bandavirus (Heartland virus, etc.)에도 효과?"
4. "**Mass production**: GMP facility, capacity?"
5. "**Adjuvant selection**: Alum vs. AS03 vs. CpG? 최적은?"

---

### 🔹 발표 2 (09:25-09:50)

**연사**: Jung Hyang Sur (서정향)
**소속**: Komipharm International Co., Ltd. (기업)
**제목**: Safety and protective efficacy of the live attenuated ASFV-G-ΔI177L/ΔLVR vaccine in pregnant sows and growing pigs

#### 연구 배경

**ASF (African Swine Fever)**: 아프리카돼지열병
- **2019년 한국 발생**, 이후 지속 발생
- **치사율 100%** (급성형)
- **백신 없음** (상용화된 것)
- **경제적 손실**: 수천억 원

**ASFV-G-ΔI177L/ΔLVR**:
- **Live attenuated vaccine**: 약독화 생백신
- **Deletion**: I177L (면역 억제), LVR (virulence region)

#### 예상 내용

**1. ASF Virus**:
- **Large DNA virus** (~190 kb)
- **복잡한 genome**: 150-200 ORFs
- **Immune evasion**: 다양한 면역 억제 유전자

**2. Vaccine Strategy**:
```
ASFV Georgia 2007 (virulent)
  ↓
I177L deletion (면역 억제 제거)
  ↓
LVR deletion (virulence 감소)
  ↓
ASFV-G-ΔI177L/ΔLVR (attenuated)
```

**3. Safety in Pregnant Sows**:
- **Critical**: 임신돈 안전성 (유산, 기형 우려)
- **Results**: No abortion, healthy piglets

**4. Efficacy in Growing Pigs**:
- **Protection**: 100% survival vs. virulent challenge
- **Antibody**: Long-term (>6 months)

**5. Challenges**:
- **DIVA** (Differentiating Infected from Vaccinated Animals): 필요
- **Reversion**: 약독화 바이러스의 독성 복귀 가능성
- **Scale-up**: 대량 생산

---

### 🔹 발표 3 (09:50-10:15)

**연사**: Kwang-Won Seo (서광원)
**소속**: Chungbuk National University (충북대학교)
**제목**: Development of antimicrobial stewardship model in swine production for reducing zoonosis

#### 예상 내용

**1. Antimicrobial Use in Swine**:
```yaml
Korea:
  - Antibiotics use (tons/year): High
  - Purpose: Growth promotion, disease prevention

Problems:
  - AMR emergence (E. coli, Salmonella, MRSA)
  - Environmental contamination (manure, water)
  - Zoonotic transmission (farm → human)
```

**2. Antimicrobial Stewardship**:
```
Principles:
  1. Surveillance (AMR monitoring)
  2. Prescription guidelines (veterinary oversight)
  3. Alternatives (probiotics, vaccines, hygiene)
  4. Education (farmers)

Implementation:
  - Farm-level interventions
  - Regional coordination
  - Policy (ban on growth promoters)
```

**3. Model Development**:
- **Data collection**: Antibiotic use, AMR prevalence
- **Intervention**: Reduce use by 30-50%
- **Outcomes**: AMR ↓, productivity maintained

**4. Zoonosis Reduction**:
- **Human colonization**: Farmer MRSA carriage ↓
- **Foodborne**: Pork AMR bacteria ↓

---

### 🔹 발표 4 (09:50-10:15)

**연사**: Jun-Gyu Park (박준규)
**소속**: Chonnam National University (전남대학교)
**제목**: Application of reverse genetics technology in SARS-CoV-2 vaccine development and its extension to flavivirus platforms

#### 예상 내용

**1. Reverse Genetics**:
```
Viral genome (cDNA/BAC)
  ↓
Transfection into cells
  ↓
Recombinant virus rescue
  ↓
Attenuation mutations
  ↓
Live attenuated vaccine candidate
```

**2. SARS-CoV-2 Applications**:
- **Codon deoptimization**: Virus 약독화
- **Deletion mutants**: nsp1, ORF3a, ORF7a 제거

**3. Flavivirus Extension**:
- **Platform**: JEV (Japanese Encephalitis Virus)
  - SA14-14-2 (live attenuated strain)
- **Chimeric viruses**: JEV backbone + other flavivirus E protein
  - Dengue, Zika, West Nile 백신

**4. Advantages**:
- **Rapid**: Genome editing → 2-4 weeks
- **Precise**: Specific mutations
- **Scalable**: Cell culture production

---

### 🔹 발표 5 (10:40-11:05)

**연사**: Do-Kyun Kim (김도균)
**소속**: Jeonbuk National University (전북대학교)
**제목**: Exosome-mediated signaling in mast cell-driven immune pathologies

#### 예상 내용

**1. Mast Cells**:
- **Allergic responses**: IgE-mediated degranulation
- **Innate immunity**: Pattern recognition
- **Exosome release**: Inflammatory signals

**2. Exosome Cargo**:
- **Cytokines**: IL-4, IL-13, TNF-α
- **Proteases**: Tryptase, chymase
- **miRNA**: Immune regulation

**3. Zoonosis Connection**:
- **Parasitic infections**: Helminth, protozoa
- **Tick-borne diseases**: SFTS, Lyme
- **Mast cell activation** → Exosome release → Pathology

**4. Therapeutic Targets**:
- **Exosome biogenesis inhibitors**
- **Mast cell stabilizers**

---

## 🧠 세션 전체 핵심 요약

### S17의 핵심 메시지

**"One Health는 인간-동물-환경의 통합 접근이다"**

| 발표 | 주제 | One Health 측면 |
|------|------|----------------|
| **Kang** | SFTS 백신 | 진드기-동물-사람 |
| **Sur** | ASF 백신 | 돼지-산업-식량안보 |
| **Seo** | AMR stewardship | 농장-환경-사람 |
| **Park** | Flavivirus 플랫폼 | 모기-동물-사람 |
| **Kim** | Exosome 면역 | 기생충-면역-질병 |

### 통합 관점

```yaml
One Health Triangle:
  Human Health:
    - SFTS 환자 치료
    - Zoonotic AMR 감염

  Animal Health:
    - 가축 백신 (ASF, SFTS)
    - 항생제 사용 관리

  Environmental Health:
    - 진드기/모기 서식지 관리
    - 항생제 환경 오염 감소

Intersection:
  - Integrated surveillance
  - Vaccine development
  - AMR control
  - Climate adaptation
```

---

## 📚 사전 읽기

### 필수
1. **SFTS Virus Review (2024)**: Pathogenesis and vaccine development
2. **ASF Vaccine (2024)**: Live attenuated vaccines
3. **AMR in Livestock (2024)**: Stewardship programs

### 추천
4. **One Health Framework (WHO, 2023)**
5. **Reverse Genetics (2023)**: Flavivirus platforms

---

## 🎤 Top 5 Questions

1. **[Kang]** "SFTS 백신 사람 임상 시험 계획? Phase I 시작?"
2. **[Sur]** "ASF 백신 DIVA strategy? 야생 감염 vs. 백신 구별?"
3. **[Seo]** "AMR Stewardship 경제성? 농가 수용성?"
4. **[Park]** "JEV 플랫폼으로 pan-flavivirus vaccine 가능?"
5. **[Kim]** "Exosome inhibitors as anti-allergic therapy?"

---

## 🤝 네트워킹 우선순위

1. **Jun-Gu Kang** (전북대) ⭐⭐⭐ - 국내, SFTS 전문가
2. **Kwang-Won Seo** (충북대) ⭐⭐ - AMR stewardship
3. **Jun-Gyu Park** (전남대) ⭐⭐ - Reverse genetics

---

**예상 학습 성과**:
✅ SFTS, ASF 백신 최신 연구
✅ AMR stewardship 전략
✅ Flavivirus 플랫폼 기술
✅ One Health 통합 접근법

**One Health 연구자/수의학 필수!** 🐾
