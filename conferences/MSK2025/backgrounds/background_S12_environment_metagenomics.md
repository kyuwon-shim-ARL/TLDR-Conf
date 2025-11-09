# 배경 자료: S12 환경 미생물 - Hidden Jewels

**세션**: S12 - Digging Out Hidden Jewels from the Environment
**일시**: 2025년 10월 27일 (월) 16:00-18:00
**장소**: Convention Hall 1
**중요도**: ⭐⭐⭐⭐ (88/100점) - **강력 추천!**

---

## 🎯 세션 개요

이 세션은 **환경 미생물 메타지노믹스의 최신 기법**을 다룹니다. 도심 AMR 감시를 위한 **샘플링 전략, 분석 방법, 대규모 데이터 활용**을 배울 수 있는 핵심 세션입니다.

### 왜 이 세션이 중요한가?

- 🔬 **Single-cell genomics**: 배양 불가 미생물 연구
- 🌍 **대규모 metagenomics**: Continental/global scale 분석
- 🧊 **극한 환경**: Antarctic, deep lake → 도심 "극한" 환경 (지하철, 하수) 유추
- 📊 **Big data**: 대용량 메타지노믹 데이터 처리 기법

---

## 📋 발표별 상세 분석

### 🔹 발표 1 (16:00-16:30) ⭐ **핵심 기법!**

**연사**: Yusuke Okazaki (岡嵜 友輔)
**소속**: Kyoto University, Institute for Chemical Research, Bioinformatics Center
**제목**: Genomic individuality of lake bacteria at the single-cell level reflects their ecological strategies

#### 최근 연구 배경

Okazaki 박사는 **담수 호수 미생물의 single-cell genomics 전문가**입니다.

**핵심 연구**:

1. **Single-cell virus-host pairing (2023)**
   - "Contrasting defense strategies of oligotrophs and copiotrophs revealed by single-cell-resolved virus–host pairing of freshwater bacteria"
   - **Oligotrophs** (빈영양성 세균) vs. **Copiotrophs** (부영양성 세균)의 바이러스 방어 전략

2. **Long-read metagenomics (2022, mSystems)**
   - "Long-Read-Resolved, Ecosystem-Wide Exploration of Nucleotide and Structural Microdiversity of Lake Bacterioplankton Genomes"
   - **Microdiversity** (미세 다양성): Closely related genotypes의 genomic variants
   - **Long-read sequencing** (PacBio, Nanopore) → Complete MAGs

3. **Lake Biwa research**
   - **Lake Biwa**: 일본 최대 담수호 (420 km²)
   - **Deep freshwater ecosystem** model

#### 예상 발표 내용

**1. Single-cell Genomics란?**

**기존 Metagenomics 한계**:
```
Bulk metagenomics
  ↓
Mixed DNA from all cells
  ↓
MAG (Metagenome-Assembled Genome) assembly
  ↓
Problem: Strain mixing, incomplete genomes, loss of microdiversity
```

**Single-cell Genomics**:
```
Single cell isolation (Flow cytometry, Microfluidics)
  ↓
Individual cell lysis
  ↓
WGA (Whole Genome Amplification)
  ↓
Sequencing (Illumina or Nanopore)
  ↓
SAG (Single-cell Amplified Genome)
  ↓
Benefits: Strain-level resolution, complete genomes, linkage of genes
```

**2. Genomic Individuality**

**Microdiversity**:
- **정의**: Within-species genomic variation
- **Types**:
  - **SNPs** (Single Nucleotide Polymorphisms)
  - **Indels** (Insertions/Deletions)
  - **Structural variants** (inversions, duplications)
  - **Gene content variation** (accessory genes)

**Ecological significance**:
- Different genotypes → Different niches
- **Example**: E. coli ST131 (pandemic clone) vs. commensal E. coli
  - Genotype → Virulence, AMR, fitness

**3. Ecological Strategies**

**r vs. K strategists** (Ecology 101):
- **r-strategists** (Copiotrophs):
  - Fast growth
  - High nutrient conditions
  - Boom-bust dynamics
  - **Example**: Proteobacteria (Vibrio, E. coli)

- **K-strategists** (Oligotrophs):
  - Slow growth
  - Low nutrient (oligotrophic lakes)
  - Stable populations
  - **Example**: SAR11 (Pelagibacterales), Actinobacteria (acI lineage)

**Okazaki's findings**:
- **Oligotrophs**: Streamlined genomes, fewer defense genes
  - **Viral defense**: "Surrender strategy" (apoptosis?)
- **Copiotrophs**: Larger genomes, diverse defense systems
  - **Viral defense**: CRISPR-Cas, restriction-modification

**4. Single-cell-resolved Virus-Host Pairing**

**Challenge**: 누가 누구를 감염시키나?
- Metagenomics: Virus와 host DNA 섞여 있음
- → Host-virus linkage 불명확

**Solution**:
- **Single-cell approach**: 감염된 세포 분리
- Viral DNA + Host DNA in same cell
- → Direct pairing!

**Findings**:
- Low infection rate (<5% of cells)
- Heterogeneous interactions (specific virus-host pairs)

#### 당신의 연구와의 연결점

**도심 환경 = "Urban Lake"?**

**1. 도심 미생물의 Genomic Individuality**:

**Application**:
```yaml
Urban environments as "lakes":
  Subway air:
    - Oligotrophic (nutrient-poor air)
    - vs. Nutrient-rich surfaces (copiotrophs)

  Wastewater:
    - Copiotrophic (high nutrients)
    - Diverse strains

Single-cell genomics application:
  - AMR strain-level tracking
  - E. coli ST131, ST410 (pandemic clones) detection
  - Genomic individuality = Transmission tracking
```

**2. Microdiversity & AMR**:

**Why it matters**:
- **AMR spread**: Not all E. coli strains are equal
  - ST131 → blaCTX-M-15 (ESBL)
  - ST410 → blaOXA-48
- **Strain-level resolution** needed for:
  - Outbreak source tracking
  - Transmission pathways
  - Intervention targeting

**Metagenomics limitation**:
- Strain mixing in MAGs
- Cannot distinguish ST131 vs. ST410 reliably

**Single-cell genomics advantage**:
- **Individual clone genomes**
- AMR gene + Plasmid linkage
- **Transmission network** reconstruction

**3. Sampling Strategies from Lake Research**:

**Okazaki's Lake Biwa approach** → Urban adaptation:

| Lake Biwa | Urban Environment |
|-----------|-------------------|
| Depth profiling (surface, deep) | Spatial gradient (outdoor → indoor → deep underground) |
| Seasonal sampling | Temporal (daily, seasonal) |
| Oligotrophic zones | Low-nutrient air, treated water |
| Eutrophic zones | Wastewater, food waste |

**4. Long-read Metagenomics**:

**Benefits for urban AMR**:
- **Complete MAGs**: Entire plasmids (AMR gene context)
- **Structural variants**: Large deletions, inversions in AMR bacteria
- **Mobile elements**: Full transposon, integron sequences

**Technology**:
- **PacBio HiFi**: High accuracy long reads
- **ONT (Oxford Nanopore)**: Ultra-long reads (100+ kb)

#### 필수 배경 지식

**1. Single-cell Genomics Workflow**

**Cell isolation**:
- **Flow cytometry (FACS)**: Fluorescence-activated cell sorting
  - Stain with SYBR Green (DNA stain)
  - Sort into 96/384-well plates (1 cell per well)
- **Microfluidics**: Droplet-based (10X Genomics, but for bacteria)

**WGA (Whole Genome Amplification)**:
- **MDA (Multiple Displacement Amplification)**:
  - Phi29 polymerase (high fidelity)
  - Random primers (hexamers)
  - Isothermal (30°C)
  - **Problem**: Amplification bias
- **MALBAC**: Reduced bias (but lower yield)

**Challenges**:
- **Contamination**: Ultra-sensitive (single cell!)
- **Amplification bias**: Some regions over-amplified
- **Chimerism**: Rare (different cells混입)
- **Completeness**: 50-90% genome coverage (vs. 70-95% for MAGs)

**2. Microdiversity Analysis**

**SNP calling**:
- Map reads to reference genome
- **Variant calling**: GATK, BCFtools
- **Filter**: Quality score, depth, strand bias

**Types of variation**:
- **Core genome SNPs**: Phylogeny (relatedness)
- **Accessory genome**: Gene presence/absence
  - **Example**: AMR genes (mecA, blaNDM) in some strains, not others

**Ecological interpretation**:
- **High diversity**: Balancing selection, niche partitioning
- **Low diversity**: Recent sweep, clonal expansion

**3. r vs. K Strategies in Microbiology**

| Trait | r-strategists (Copiotrophs) | K-strategists (Oligotrophs) |
|-------|----------------------------|----------------------------|
| **Growth rate** | Fast (μ_max high) | Slow |
| **Genome size** | Large (4-7 Mb) | Small (1-3 Mb, streamlined) |
| **Nutrient affinity** | Low (K_s high) | High (K_s low) |
| **Defense** | Diverse (CRISPR, R-M) | Minimal |
| **Examples** | E. coli, Vibrio, Pseudomonas | SAR11, Prochlorococcus |

**Urban AMR context**:
- **Copiotrophs**: Wastewater, biofilms (high AMR prevalence)
- **Oligotrophs**: Treated water, air (lower AMR?)

**4. Long-read Sequencing**

**Platforms**:
| Platform | Read length | Accuracy | Cost | Throughput |
|----------|-------------|----------|------|------------|
| **PacBio HiFi** | 10-25 kb | 99.9% (HiFi mode) | $$$ | Medium |
| **ONT (Nanopore)** | 10 kb - >100 kb | 95-99% | $$ | High |
| **Illumina** | 150-300 bp | 99.9% | $ | Very High |

**Advantages for metagenomics**:
- **Complete genomes**: MAGs with no gaps
- **Plasmid resolution**: Entire plasmid sequences
  - Crucial for AMR (many resistance genes on plasmids)
- **Repeat resolution**: Mobile elements, rRNA operons

**5. Lake Microbiology Concepts**

**Stratification**:
- **Epilimnion**: Surface (warm, oxygenated)
- **Thermocline**: Temperature gradient
- **Hypolimnion**: Deep (cold, often anoxic)

**Microbial zonation**:
- Oxic → Aerobic bacteria
- Anoxic → Anaerobes (sulfate reducers, methanogens)

**Analogy to urban**:
- **Surface (outdoor air)**: Oxic, UV exposure
- **Subway (deep)**: Reduced light, different microbiome

#### 예상 질문 & 토론 포인트

**당신이 물어볼 질문**:

1. "도심 환경 샘플(예: 지하철 공기, 하수)에 **single-cell genomics**를 적용할 때, 기술적 챌린지는? Cell isolation (FACS)이 복잡한 matrix에서 가능한가요?"

2. "AMR 확산 추적을 위해 **strain-level microdiversity** 분석이 필수인데, long-read metagenomics vs. single-cell genomics 중 어느 접근이 더 효율적일까요?"

3. "Lake Biwa의 **oligotrophic zones**에서 발견한 미생물이 도심의 '영양 빈곤' 환경(예: 처리된 수돗물, 대기)과 유사할 수 있을까요?"

4. "**Viral predation**이 도심 AMR bacteria의 abundance를 조절할 수 있을까요? (Virus-host pairing 관점)"

**토론 예상**:
- **Cost-effectiveness**: Single-cell vs. bulk metagenomics
- **Scalability**: 수백~수천 cells 분석 가능한가?
- **Integration**: Single-cell + metagenomics 통합 전략

**네트워킹**:
- 중간 우선순위 (기법 학습 위주)
- Single-cell 기술 도입 시 자문 가능성

---

### 🔹 발표 2 (16:30-17:00)

**연사**: Sung-Keun Rhee (이성근)
**소속**: Chungbuk National University, Department of Biological Sciences and Biotechnology
**제목**: Utilizing novel methanotrophs to mitigate nitrous oxide emissions in wetland ecosystems

#### 최근 연구 배경 (2024, Nature Communications)

**획기적 발견**: **Acidophilic methanotrophs can respire N₂O!**

**핵심 내용**:
- Methanotrophs (메탄산화세균): CH₄ → CO₂
- **New capability**: N₂O → N₂ (Denitrification)
- **Dual benefit**: CH₄ 감소 + N₂O 감소 (둘 다 온실가스)

**메커니즘**:
- **N₂O reductase (NosZ)** in methanotrophs
- Anaerobic growth on CH₃OH, H₂, C₂-C₄ compounds (not just CH₄!)
- **Acidic wetlands** (pH 3.7-6.4): High methanotroph activity

**Significance**:
- Wetlands (논, 이탄지) → CH₄ + N₂O 주요 배출원
- **Methanotrophs = Natural mitigation**

#### 예상 발표 내용

**1. Greenhouse gases from wetlands**:
- CH₄ (methane): 28x CO₂ (100-year GWP)
- N₂O (nitrous oxide): 298x CO₂!

**2. Methanotrophs**:
- Type I, Type II (classification)
- **Methylocystis** (acidophilic, common in peatlands)

**3. N₂O respiration**:
- **nosZ gene** encoding N₂O reductase
- Electron acceptor: N₂O → N₂
- **Alternative respiration** (when O₂ low)

**4. Wetland mitigation strategy**:
- Enhance methanotroph populations
- Optimize conditions (pH, nutrients)
- **Dual function**: CH₄ oxidation + N₂O reduction

#### 당신의 연구와의 연결점

**도심 환경 응용 (간접)**:

**1. 도심 wetlands**:
- **Parks, constructed wetlands** (수처리)
- **Storm water retention ponds**
- CH₄, N₂O emissions 우려

**Metagenomics application**:
```yaml
Urban wetland metagenomics:
  Target genes:
    - pmoA (particulate methane monooxygenase)
    - nosZ (N2O reductase)

  Purpose:
    - Methanotroph community profiling
    - N2O mitigation potential assessment
```

**2. Nitrogen cycling & AMR**:

**Linkage** (약함, 하지만 흥미로움):
- **Nitrogen stress**: Affects bacterial metabolism
- Some AMR genes co-localize with nitrogen metabolism genes?
- **Wastewater treatment**: Nitrification/denitrification + AMR genes

**Priority**: 낮음 (AMR과 직접 관련 적음)

---

### 🔹 발표 3 (17:00-17:30)

**연사**: Haiyan Chu (褚海燕)
**소속**: University of Chinese Academy of Sciences, Institute of Soil Science
**제목**: Soil microbial distribution in China and across the globe

#### 연구 배경

Chu 교수는 **토양 미생물 biogeography 권위자**입니다.

**주요 업적**:
- **"China Soil Microbiome"** 특집호 guest editor (2022, FEMS Microbiology Ecology)
- "Soil Microbial Biogeography in a Changing World" (2020, mSystems)
- **Highly cited researcher** (2019)

**연구 분야**:
- Soil microbial ecology
- Microbial biogeography (공간 분포 패턴)
- **Climate change response**: 온난화, 강수 변화 → Microbiome shift

**Large-scale studies**:
- **Eastern China forests**: 58 tree species, 5 mountain forests
- **Tibetan Plateau**: Alpine grassland
- **Changbai Mountain**: Treeline ecotone

#### 예상 발표 내용

**1. Soil microbial biogeography**:

**Drivers of spatial distribution**:
- **Climate**: Temperature, precipitation (MAT, MAP)
- **Soil properties**: pH (strongest predictor!), C:N ratio, nutrients
- **Vegetation**: Plant species, productivity
- **Geography**: Latitude, altitude, distance

**Patterns**:
- **Distance-decay**: Geographic distance ↑ → Community dissimilarity ↑
- **pH gradient**: Acidic (fungi-dominant) vs. Neutral/alkaline (bacteria)

**2. China-specific findings**:

**Diversity hotspots**:
- **Subtropical forests** (Yunnan, Sichuan): High diversity
- **Tibetan Plateau**: Unique cold-adapted microbiome

**Human impacts**:
- **Agricultural intensification**: Simplified microbiome
- **Urbanization**: Soil degradation

**3. Global comparisons**:

**Databases**:
- **Earth Microbiome Project (EMP)**
- **Global Soil Microbiome Atlas**

**Findings**:
- Soil microbial diversity > Ocean, freshwater
- **Rare biosphere**: Low-abundance taxa = high functional diversity

**4. Climate change implications**:

**Responses**:
- **Warming**: Accelerated C cycling (CO₂ release)
- **Precipitation shifts**: Drought → Fungal dominance

#### 당신의 연구와의 연결점

**도심 토양 AMR 감시**:

**1. Urban soil as unique biome**:

**Characteristics**:
- **Compaction**: Reduced aeration
- **Pollution**: Heavy metals, PAHs
- **Nutrient enrichment**: Dog waste, fertilizer
- **pH variability**: Acid rain, lime

**Biogeography approach**:
```yaml
Urban soil AMR mapping:
  Sampling:
    - Parks (20+ sites)
    - Playgrounds
    - Street trees
    - Construction sites

  Analysis:
    - Distance-decay of AMR genes
    - pH correlation with AMR abundance
    - Hotspot identification
```

**2. Drivers of urban AMR distribution**:

**Hypotheses** (from biogeography):
- **pH**: Acidic soils → Lower AMR? (Needs testing)
- **Distance to hospitals**: Hospital proximity → Higher AMR?
- **Land use**: Residential vs. commercial vs. industrial
- **Vegetation**: Green spaces vs. bare soil

**3. Rare biosphere & AMR**:

**Concept**:
- **Abundant bacteria**: Core microbiome
- **Rare bacteria**: "Seed bank" (dormant, infrequent)

**AMR relevance**:
- Rare AMR bacteria → Can bloom during antibiotic exposure
- **Early detection**: Metagenomics finds rare AMR before clinical emergence

#### 필수 배경 지식

**1. Biogeography**

**Macroecology principles**:
- **Species-area relationship**: Larger area → More species
- **Distance-decay**: β-diversity increases with distance
- **Environmental filtering**: Abiotic factors select for adapted species

**Microbial biogeography** (Baas Becking 1934):
- **"Everything is everywhere, but the environment selects"**
- Microbes disperse globally (wind, water, animals)
- **Local adaptation**: Environment determines who thrives

**2. Soil pH Effects**

**Why pH is the strongest predictor**:
- **Direct**: Enzyme activity, nutrient solubility
- **Indirect**: Affects plant growth, organic matter

**Microbial responses**:
- **Acidic (pH <5.5)**: Fungi, Acidobacteria
- **Neutral (pH 6-7)**: Proteobacteria, Actinobacteria, Firmicutes
- **Alkaline (pH >8)**: Specialized alkaliphiles

**3. Climate Change & Microbiome**

**Warming effects**:
- **Increased activity**: Enzyme kinetics ↑
- **Shifts**: Cold-adapted → Warm-adapted taxa
- **C release**: Accelerated decomposition

**Precipitation effects**:
- **Drought**: Water stress, fungal advantage (better drought tolerance)
- **Flooding**: Anoxic conditions, anaerobes ↑

**Feedbacks**:
- Microbiome shifts → Alter C, N cycling → Amplify or dampen climate change

---

### 🔹 발표 4 (17:30-17:45) [Short talk]

**연사**: Hanbyul Lee (이한별)
**소속**: Korea Polar Research Institute (KOPRI)
**제목**: Lifting the ice lid: Unveiling hidden microbial worlds in Antarctic lakes and glaciers

#### 연구 배경

Lee 박사는 **극한 환경 미생물 전문가** (Antarctic lakes, subglacial ecosystems)

**연구**:
- **Lake Bonney** (McMurdo Dry Valleys, Antarctica)
- **Mercer Subglacial Lake** (2025): 1,374 single-cell genomes from water & sediments
- **Metabolic versatility**: "What allows them to survive" under the ice

#### 예상 발표 내용 (15분 짧은 발표)

**1. Antarctic extreme environments**:
- Permanent ice cover (Lake Untersee, Lake Bonney)
- Subglacial lakes (under ice sheet)
- Temperature: -2 to 4°C
- Darkness (no photosynthesis under ice)

**2. Microbial adaptations**:
- **Psychrophiles**: Cold-adapted
- **Oligotrophs**: Nutrient-limited
- **Metabolic flexibility**: Multiple energy sources

**3. Subglacial Lake Mercer**:
- 1,374 SAGs (single-cell amplified genomes)
- **Genetic isolation**: Cut off from surface for millennia
- **Metabolic complexity**: Diverse pathways (H₂, Fe, S cycling)

#### 연결점 (간접):

**도심 "극한" 환경**:
- Deep underground (subway tunnels, sewers)
- Darkness, low nutrients
- Oligotrophic adapted microbes?

**Survival strategies**:
- AMR bacteria in nutrient-poor treated water?

**Priority**: 낮음 (흥미롭지만 연구 직결 아님)

---

### 🔹 발표 5 (17:45-18:00) [Short talk]

**연사**: Hongjae Park (박홍재)
**소속**: Inha University, Jang-Cheon Cho Lab
**제목**: A continental-scale gene and genome catalogue for freshwater ecosystems

#### 연구 배경

Park 박사는 **대규모 담수 미생물 genomics** 전문가

**최근 연구 (2024, Microbiome)**:
- **170 high-quality genomes** of freshwater picocyanobacteria
- **33 symbiont genomes** (Pseudomonas, Mesorhizobium, Acidovorax, Hydrogenophaga)
- **Central Europe** lakes (Czech Republic)

**Continental-scale catalogue**:
- Inspired by **Garner et al. (2023, Nature Microbiology)**:
  - **6.5 million km²** of lake-rich landscape (Canada, Scandinavia)
  - **Massive metagenomics dataset**
  - Gene catalogue: 수백만 unique genes

#### 예상 발표 내용 (15분)

**1. Why continental-scale?**:
- **Biogeography**: Spatial patterns across 1000s km
- **Gene diversity**: Rare genes discovered (low-abundance taxa)
- **Climate gradients**: Boreal, temperate, subtropical

**2. Gene catalogue construction**:
- **Metagenomics**: 100s of lakes sampled
- **Assembly**: Co-assembly or individual assemblies
- **Gene prediction**: Prodigal, GeneMark
- **Clustering**: CD-HIT (99% identity → gene clusters)
- **Functional annotation**: KEGG, COG, CAZy

**3. Findings**:
- **Core genes**: Shared across lakes (central metabolism)
- **Accessory genes**: Lake-specific (adaptation)
- **Rare genes**: Novel functions

**4. Freshwater picocyanobacteria**:
- **Synechococcus**, **Cyanobium**
- Photosynthesis + N₂ fixation (some)
- **Symbionts**: Co-occurring heterotrophs (cross-feeding)

#### 연결점:

**도심 수계 유전자 카탈로그**:

**Concept**:
```yaml
Urban Water Gene Catalogue:
  Scope:
    - Tap water (across city districts)
    - Rivers (upstream → downstream)
    - Wastewater (influent, effluent)

  Purpose:
    - AMR gene inventory
    - Source tracking (wastewater → river)
    - Functional diversity assessment
```

**Advantage**:
- **Reference database**: Metagenomics QC (contamination check)
- **Baseline**: Pre-intervention vs. post-intervention

**Priority**: 중간 (Big data 관점에서 유용)

---

## 🧠 세션 전체 핵심 요약

### S12의 핵심 메시지

**"환경 메타지노믹스 = Scale + Resolution"**

| Speaker | Scale | Resolution | Key Method |
|---------|-------|------------|------------|
| **Okazaki** | Single-cell | Strain-level | Single-cell genomics, Long-read |
| **Rhee** | Wetland ecosystem | Functional gene (nosZ) | Gene-targeted metagenomics |
| **Chu** | Continental (China, Global) | Community (OTU/ASV) | Large-scale biogeography |
| **Lee H** | Extreme (Antarctic) | Single-cell (SAG) | Subglacial sampling |
| **Park** | Continental (Freshwater) | Gene catalogue | Metagenome assembly, annotation |

### 도심 AMR 감시 적용

**통합 전략**:

```yaml
Tier 1 - Broad Scale (Urban gene catalogue):
  - 100+ sites across city
  - AMR gene inventory
  - Biogeography patterns

Tier 2 - Medium Scale (Community analysis):
  - District-level sampling
  - Diversity, composition
  - Driver analysis (pH, land use)

Tier 3 - High Resolution (Strain-level):
  - Hotspot investigation
  - Single-cell genomics
  - AMR clone tracking (ST131, ST410)
```

### Metagenomics Methods Comparison

| Method | Pros | Cons | AMR Application |
|--------|------|------|-----------------|
| **Bulk metagenomics** | High throughput, cost-effective | Strain mixing, incomplete MAGs | Community AMR profiling |
| **Single-cell genomics** | Strain-level, complete genomes | Low throughput, expensive | Clone tracking, plasmid linkage |
| **Long-read sequencing** | Complete MAGs, plasmid resolution | High cost | AMR gene context, mobile elements |

---

## 📚 사전 읽기

### 필수

1. **Okazaki** - "Long-Read-Resolved, Ecosystem-Wide Exploration..." (2022, mSystems)
2. **Rhee** - "Nitrous oxide respiration in acidophilic methanotrophs" (2024, Nature Communications)

### 추천

3. **Chu** - "Soil Microbial Biogeography in a Changing World" (2020, mSystems)
4. **Single-cell genomics review** - 기법 이해

---

## 🎤 질문 리스트

### Priority Questions

1. **[Okazaki]** "도심 환경에 single-cell genomics 적용 시 technical challenges? AMR strain tracking 가능한가요?"

2. **[Chu]** "Urban soil AMR biogeography 연구를 위한 sampling strategy 제안? pH 외 주요 drivers?"

3. **[Park]** "Urban water gene catalogue 구축 시 권장 샘플 수와 bioinformatics pipeline?"

### Backup

4. **[Rhee]** "도심 constructed wetlands에서 methanotroph-based mitigation?"

5. **[Lee H]** "도심 지하 (subway deep tunnels) = 'urban subglacial'? Oligotroph 유사성?"

---

## 🤝 네트워킹 우선순위

### 1위: Yusuke Okazaki (Kyoto) ⭐⭐

**Why**: Single-cell genomics expertise

**Strategy**:
- Long-read + single-cell integration for urban AMR
- Technical consultation

### 2위: Hongjae Park (Inha) ⭐⭐

**Why**: 국내 연구자, freshwater genomics

**Strategy**:
- Urban water gene catalogue collaboration
- Inha University 가까움 (인천)

### 3위: Haiyan Chu (CAS) ⭐

**Why**: Biogeography methods

**Strategy**:
- Urban soil AMR biogeography 자문

---

## ⚡ 세션 당일 체크리스트

### 사전
- [ ] Okazaki, Rhee 논문 읽기
- [ ] Single-cell genomics, biogeography 개념 정리

### 당일
- [ ] 16:00 Convention Hall 1 도착 (15:50)
- [ ] 명함 준비
- [ ] Okazaki, Park 발표 집중

### 직후
- [ ] Okazaki, Park와 대화
- [ ] Single-cell 기술 도입 논의
- [ ] Gene catalogue collaboration 제안

---

**예상 학습 성과**:
✅ Single-cell genomics 기법 학습
✅ 대규모 환경 메타지노믹스 전략 습득
✅ Biogeography 관점의 AMR 공간 분포 이해
✅ 국내외 환경 미생물 연구자 네트워킹

**핵심 Takeaway**: "Scale matters! Single-cell → Continental"
