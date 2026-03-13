---
name: collaborator-check-en
description: Collaboration partner (company/institution/researcher) verification and Due Diligence report generation. Founder background verification, technology assessment, funding status, competitor analysis - comprehensive investigation (English version) (project)
allowed-tools:
  - Read
  - Write
  - WebSearch
  - WebFetch
  - Grep
  - Glob
  - Bash
---

> **DEPRECATED**: This skill has been replaced by `academic-investigator`.
> Use `academic-investigator` skill instead for unified researcher/lab/collaborator/conference investigation.
> For conference mode, see `academic-investigator-conference` skill.
> This file will be removed in a future update.

# Collaborator Check Skill v1.0 (English)
## Collaboration Partner Verification & Due Diligence Report Generation

A skill for conducting objective background investigations and generating standardized reports when evaluating collaboration proposals, partnerships, or investment opportunities.

---

## 🎯 Core Functions

1. **Company/Institution Basic Information Research**
2. **Founder/Key Personnel Background Verification**
3. **Objective Technology Level Assessment**
4. **Funding/Financial Status Check**
5. **Competitor Comparison Analysis**
6. **Red Flags Detection**
7. **Comprehensive Due Diligence Report Generation**

---

## 📋 Workflow

### Step 1: Initialization & Information Gathering

**Ask the user:**
```
Starting collaboration partner verification.

1. What type of entity are you investigating?
   - Company/Startup
   - Research institution/University lab
   - Individual researcher
   - Other

2. Name of the entity/company:

3. Do you have related materials? (Optional)
   - PDF file path
   - Website URL
   - None (web search only)

4. What is the purpose of this collaboration?
   - Joint research/Academic collaboration
   - Technology transfer/Licensing
   - Investment/Equity participation
   - Project outsourcing/Contract
   - Other
```

### Step 2: Basic Information Research

**Execute WebSearch queries:**
```
- "[company name] company profile"
- "[company name] founding team background"
- "[company name] Crunchbase OR LinkedIn"
- "[company name] funding investment"
- "[company name] technology platform"
```

**Information to collect:**
| Item | Content |
|------|---------|
| Company Name | Legal name, English name |
| Founded | Year, incorporation status |
| Headquarters | Country, City |
| Website | Official URL |
| Employee Count | Size estimate |
| Business Area | Core technology/service |

### Step 3: Founder/Key Personnel Verification

**For each key person:**

```
Execute WebSearch:
- "[name] [field] PhD dissertation"
- "[name] Google Scholar citations"
- "[name] LinkedIn profile"
- "[name] publications research"
- "[name] [previous institution]"
```

**Verification items:**
| Claim | Verification Method | Result |
|-------|---------------------|--------|
| Education | University website, thesis DB | ✓/✗/? |
| Career | LinkedIn, institution website | ✓/✗/? |
| Citations | Google Scholar | Actual number |
| Key Papers | PubMed, Google Scholar | Existence |
| Awards/Patents | Patent office, society websites | Existence |

**Evaluation criteria:**
- **Verified**: Confirmed from credible sources
- **Unverified**: Cannot confirm (claim only exists)
- **Discrepancy**: Claim differs from reality (⚠️ Red Flag)

### Step 4: Technology Level Assessment

**Evaluation Matrix:**

| Item | Criteria | Score |
|------|----------|-------|
| Academic Validation | Number of peer-reviewed papers | High/Med/Low |
| Technology Differentiation | Uniqueness vs competitors | High/Med/Low |
| Market Timing | Field maturity | High/Med/Low |
| Actual Implementation | Prototype/product existence | High/Med/Low |
| IP Ownership | Patents/trade secrets | High/Med/Low |

**WebSearch queries:**
```
- "[technology name] peer-reviewed publications"
- "[technology name] patent search"
- "[technology name] competitors comparison"
- "[technology name] market size [year]"
- "[technology name] vs [competing tech] benchmark"
```

### Step 5: Funding/Financial Status Research

**Information sources:**
- Crunchbase
- CB Insights
- PitchBook (paid)
- Public filings (public companies)
- News articles

**Information to collect:**
| Item | Content |
|------|---------|
| Funding Stage | Seed/Series A/B/C... |
| Total Raised | Amount (if disclosed) |
| Latest Round | Date, amount, investors |
| Investor List | VCs, angels, strategic investors |
| Valuation | Estimated valuation |
| Financial Health | Profitability, runway |

### Step 6: Competitor Analysis

**Competitive landscape mapping:**
```
| Company/Org | Approach | Resources | Status | Strengths | Weaknesses |
|-------------|----------|-----------|--------|-----------|------------|
| [Subject]   | ...      | ...       | ...    | ...       | ...        |
| [Competitor1] | ...    | ...       | ...    | ...       | ...        |
| [Competitor2] | ...    | ...       | ...    | ...       | ...        |
| [Competitor3] | ...    | ...       | ...    | ...       | ...        |
```

**WebSearch queries:**
```
- "[field] leading companies startups"
- "[field] market landscape [year]"
- "[subject] vs [competitor] comparison"
- "[field] industry report"
```

### Step 7: Red Flags Detection

**Automatic check items:**

| Category | Red Flag | Severity |
|----------|----------|----------|
| **Career** | Unverifiable education/career | 🔴 High |
| **Career** | Frequent job changes (< 1 year) | 🟡 Medium |
| **Technology** | "Innovation" claims without peer-reviewed papers | 🟡 Medium |
| **Technology** | Exaggerated performance claims (no validation data) | 🔴 High |
| **Financial** | Undisclosed funding info (relative to size) | 🟡 Medium |
| **Financial** | Frequent pivots/business model changes | 🟡 Medium |
| **Legal** | Lawsuit/legal dispute history | 🔴 High |
| **Reputation** | Negative news/reviews | 🟡 Medium |
| **Transparency** | Missing team/contact information | 🔴 High |

**WebSearch queries:**
```
- "[company name] lawsuit legal issues"
- "[company name] controversy scandal"
- "[founder name] fraud allegations"
- "[company name] reviews complaints"
- "[company name] former employee reviews"
```

---

## 📝 Report Template

### File Naming Convention
```
collaborations/[company-name]/research_report_[YYYY-MM-DD]_EN.md
```

### Report Structure

```markdown
# [Company/Institution Name] - Collaboration Due Diligence Report

> **Date:** YYYY-MM-DD
> **Related Meeting:** [Meeting title]
> **Source Material:** [Path or URL]

---

## 1. Company Overview
[Basic info in table format]

## 2. Leadership Background Verification
[Detailed verification results for each key person]
- Claim vs Reality comparison table
- Google Scholar citation verification
- Key achievements confirmation

## 3. Core Technology Explained
[Technology explanation accessible to non-experts]
- One-liner summary
- Simple analogy
- How it works
- Differentiators

## 4. Project/Product Analysis
[Specific project/product evaluation]
- Target market
- Budget/timeline
- Expected deliverables

## 5. Competitive Landscape
[Competitor comparison matrix]
- Key players
- Subject's positioning
- Differentiators and risks

## 6. Funding/Financial Status
[Disclosed financial information]
- Funding history
- Investors
- Estimated runway

## 7. Objective Level Assessment
### Strengths
[Table format]

### Weaknesses/Uncertainties
[Table format]

### Red Flags
[Discovered warning signs]

## 8. Questions for Meeting
### Technology
[5-10 questions]

### Business
[5 questions]

### Collaboration
[3-5 questions]

## 9. Key Terms Glossary
[Table format - simple explanations]

## 10. Executive Summary
[3-4 paragraph summary]
- Subject introduction
- Core technology/business
- Verification results
- Collaboration caveats

## References
[Source list - hyperlinks]
```

---

## 🔄 Execution Workflow

### When user invokes
```
1. Collect subject information (interactive)
2. If PDF/URL provided, read first
3. Execute WebSearch in parallel (company, personnel, technology, funding)
4. Synthesize and verify results
5. Check Red Flags
6. Generate report
7. Confirm save location and save
```

### Output
1. **Standard Report**: `research_report_[date]_EN.md` (English)
2. **Korean Report**: Use `collaborator-check` skill for Korean version

---

## ⚙️ Settings

### Language
- **Default**: English
- **Korean version**: Use `collaborator-check` skill

### Save Location
```
[project]/collaborations/[company-name-lowercase-hyphenated]/
```

### Quality Standards
- **Minimum length**: 500+ lines
- **Required sections**: All 10 sections
- **Verification items**: Attempt verification for all claims
- **Source attribution**: Reference links for all information

---

## 🚨 Important Notes

- **ALWAYS** distinguish between claims and verified facts
- **ALWAYS** mark unverifiable information as "Unverified"
- **ALWAYS** include Red Flags section (state "None found" if none)
- **NEVER** write only positive assessment without verification
- **NEVER** include information without sources
- **NEVER** share confidential material contents outside the report

---

## 📊 Success Metrics

✅ 100% verification attempt for key personnel backgrounds
✅ Technology/product explanation in simple terms included
✅ 3+ competitor comparisons
✅ Red Flags checklist completed
✅ 15+ questions for meeting
✅ All sources hyperlinked

---

**Version**: 1.0
**Last Updated**: 2025-12-15
**Author**: MSK2025 Project
