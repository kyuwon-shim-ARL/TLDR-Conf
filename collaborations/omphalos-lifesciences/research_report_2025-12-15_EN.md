# Omphalos Lifesciences - Collaboration Due Diligence Report

> **Date:** 2025-12-15
> **Related Meeting:** Paratus Non-Dilutive Funding Project DEV Discussion
> **Source Material:** `data/raw/Project Evaluation Meeting.pdf`

---

## 1. Company Overview

| Item | Details |
|------|---------|
| **Company Name** | Omphalos Lifesciences Inc. |
| **Founded** | 2021 |
| **Headquarters** | Dallas, Texas, USA |
| **Funding Stage** | Series A (amount undisclosed) |
| **Website** | [omphaloslifesci.com](https://omphaloslifesci.com/) |
| **Business Area** | Biology simulation platform, Virtual Cell technology |

---

## 2. Leadership Background Verification

### Daehwan Kim, Ph.D. (Founder, Co-CEO, CTO)

| Item | Claimed | Verification |
|------|---------|--------------|
| **Education** | University of Maryland - CS Ph.D. | **Verified** |
| **Career** | Johns Hopkins Postdoc → UT Southwestern Asst. Professor | **Verified** |
| **Citations** | 66,000+ (per PDF) → **Actual: 69,000+** | **Verified (higher)** |
| **Key Work** | HISAT, HISAT2, TopHat2 development | **Verified** |

**Key Publications (by citations):**
- HISAT2 (Nature Biotechnology, 2019): **7,862 citations**
- HISAT/StringTie/Ballgown (Nature Protocols, 2016): **4,863 citations**

**Assessment:** World-class bioinformatician. HISAT is an industry-standard tool for RNA-seq analysis with high credibility in academia.

---

### Donghoon Lee, Ph.D. (Co-Founder, Co-CEO, CSO)

| Item | Claimed | Verification |
|------|---------|--------------|
| **Education** | University of Toronto - Cell & Systems Biology Ph.D. | **Verified** |
| **Career** | Johns Hopkins Postdoc (Elizabeth Chen Lab) → UT Southwestern Instructor | **Verified** |
| **Research Area** | Cell fusion mechanisms, developmental biology | **Verified** |

**Assessment:** Experimental biologist background. Complementary team composition with computational expert Daehwan Kim.

---

## 3. Core Technology Explained

### L++ (Life Programming Language)

**One-liner:**
> "A programming language for coding biology"

**Simple Analogy:**
```
If C++ is a language for creating computer programs,
L++ is a language for creating virtual cells/organisms
```

**Key Features:**

| Feature | Description |
|---------|-------------|
| Biology Syntax | Express chemical reactions, proteins, genes as code |
| Unit Support | Auto-handles biological units (uM, nM, mg/L) |
| SMILES Support | Input chemical structures directly in code |
| Multi-scale | Model from molecule → cell → tissue → organism level |

**Code Example (PDF page 7):**
```cpp
protein AACT(2 acetyl-CoA -> acetoacetyl-CoA + CoA, k = 1)
// Two acetyl-CoA molecules react to form acetoacetyl-CoA
```

---

### Virtual Cell

**One-liner:**
> "A digital cell that operates inside a computer"

**Why It Matters:**
```
Traditional: Drug → Cell experiment → Animal testing → Clinical (costly/slow)
Future: Drug → Virtual cell simulation → Only validated candidates tested (faster/cheaper)
```

**Omphalos Claims vs Competitors:**

| Organization | Approach | Model Size | Characteristics |
|--------------|----------|------------|-----------------|
| **Omphalos** | Hybrid (rules+AI) | 200K parameters | Efficient, interpretable |
| CZI/NVIDIA | Pure AI | Billions of parameters | Data-dependent |
| Stanford (Karr) | Pure rule-based | - | Slow to build |

---

## 4. Project Analysis: Virtual *A. baumannii*

### Target Pathogen Background

**Acinetobacter baumannii:**
- WHO **"Critical Priority" #1** pathogen
- CDC **"Urgent Threat"** designation
- Major cause of hospital-acquired infections
- **MDR (Multi-Drug Resistant)** strains limiting treatment options

**Why This Pathogen:**
1. Clinical urgency (aligned with BARDA priorities)
2. Rich public data (multi-omics, GEM models available)
3. Similarities to E. coli facilitate model extension

---

### Project Budget Analysis (PDF page 13)

| Item | Amount | Allocation |
|------|--------|------------|
| Pathogen Model Development | $32,000 | 80% |
| Project Management | $2,000 | 5% |
| Data Integration | $2,000 | 5% |
| Validation/Benchmarking | $1,600 | 4% |
| Documentation | $800 | 2% |
| Operational Overhead | $1,600 | 4% |
| **Total** | **$40,000** | 100% |

**Assessment:**
- 96% direct labor → Lean startup operation
- 6 weeks / 3 milestones → Rapid prototyping approach
- $40K is modest but valuable as **non-dilutive funding**

---

## 5. Competitive Landscape

### Key Players in Virtual Cell Space

| Organization | Funding/Resources | Approach | Status |
|--------------|-------------------|----------|--------|
| **CZI + NVIDIA** | Billions USD | Pure AI, massive data | Oct 2025 expanded partnership, VCP platform |
| **DeepMind** | Unlimited | AlphaFold extension | Protein structure focus |
| **Stanford (Covert Lab)** | Academic | Rule-based | First M. genitalium whole-cell model |
| **Omphalos** | Series A + BARDA | Hybrid | E. coli model complete, A. baumannii starting |

**Omphalos Differentiators:**
1. **Efficiency:** 200K vs 20B parameters (100,000x smaller)
2. **Interpretability:** Mechanism-based, not black-box AI
3. **Practicality:** Specialized for pathogen + antibiotic simulation

**Risks:**
- CZI/NVIDIA resource scale is overwhelming
- No peer-reviewed publications on L++/Virtual Cell technology

---

## 6. BARDA/Paratus Program

### Program Overview

| Item | Details |
|------|---------|
| **Operator** | MATTER (Chicago-based healthcare accelerator) |
| **Funding Source** | BARDA (under US HHS) |
| **Purpose** | Digital health solutions for health security threats |
| **Funding Range** | $50,000 ~ $200,000 (general) / up to $2M (TBI) |

### Omphalos Selection (Announced 2025.12.11)

- **Significance:** US government agency technology validation
- **Terms:** Non-dilutive (no equity dilution)
- **Goal:** Q1 2026 prototype deployment

---

## 7. Objective Research Level Assessment

### Strengths

| Item | Rating |
|------|--------|
| Founder Academic Credentials | **High** (HISAT 69K citations, world-class) |
| Technology Differentiation | **Medium-High** (Hybrid approach is novel) |
| Market Timing | **High** (Virtual Cell, AMR both hot topics) |
| Government Validation | **Medium-High** (BARDA selection) |

### Weaknesses/Uncertainties

| Item | Concern |
|------|---------|
| Academic Validation | No peer-reviewed publications on core technology |
| Funding Scale | Series A amount undisclosed, likely small vs competitors |
| Team Size | 2-founder core, scalability unclear |
| E. coli Validation | Limited benchmarks against experimental data |

---

## 8. Questions for Meeting

### Technology
1. Plans for L++ code release (open source)?
2. Experimental validation data for E. coli model?
3. Comparison results against existing GEMs?

### Business
4. Series A funding amount and runway?
5. Current team size and hiring plans?
6. Pharma/research institution partnerships?

### Collaboration
7. What type of collaboration is desired? (Data? Validation? Joint research?)
8. Interest in pathogens beyond A. baumannii?

---

## 9. Key Terms Glossary

| Term | Simple Explanation |
|------|-------------------|
| **Virtual Cell** | A simulation that behaves like a real cell inside a computer |
| **L++** | A new programming language designed for coding biology |
| **Whole-cell model** | A complete model including all genes and reactions in a cell |
| **GEM** | Genome-scale metabolic model; simpler than whole-cell (metabolism only) |
| **MDR** | Multi-Drug Resistant; bacteria resistant to multiple antibiotics |
| **ESKAPE** | Acronym for 6 dangerous hospital-acquired resistant pathogens |
| **Non-dilutive funding** | Funding that doesn't require giving up equity (grants) |
| **In silico** | By computer simulation (vs in vitro=test tube, in vivo=living organism) |

---

## 10. Executive Summary

**Omphalos Lifesciences** is a biotech startup founded in 2021 in Dallas by world-class bioinformatician **Daehwan Kim** (HISAT developer, 69K citations) and experimental biologist **Donghoon Lee**.

Their core technology **L++** is a proprietary programming language for biology simulation, adopting a **hybrid rules+AI approach** that emphasizes efficiency and interpretability, unlike CZI/NVIDIA's pure AI approach.

In December 2025, they were **selected for the BARDA/Paratus program**, gaining US government validation, and have begun developing a whole-cell model of **A. baumannii**, a WHO #1 priority pathogen.

**Caveats:** While founder academic credentials are verified, there are no peer-reviewed publications on L++ or Virtual Cell technology itself, and resource scale is small compared to competitors (CZI/NVIDIA). Verifying actual technology maturity and validation data is important for collaboration decisions.

---

## References

- [Omphalos Lifesciences Official Website](https://omphaloslifesci.com/)
- [BARDA Support Announcement (2025.12.11)](https://omphaloslifesci.com/2025/12/11/omphalos-secures-barda-support-for-pathogen-agnostic-antimicrobial-strategy-simulation/)
- [Daehwan Kim Google Scholar](https://scholar.google.com/citations?user=RotyhxEAAAAJ&hl=en)
- [CZI-NVIDIA Virtual Cell Collaboration](https://chanzuckerberg.com/newsroom/nvidia-partnership-virtual-cell-model/)
- [MATTER Paratus Program](https://matter.health/paratus/)
- [CDC Acinetobacter Information](https://www.cdc.gov/acinetobacter/about/index.html)
- [WHO Priority Pathogens](https://www.who.int/news/item/27-02-2017-who-publishes-list-of-bacteria-for-which-new-antibiotics-are-urgently-needed)
