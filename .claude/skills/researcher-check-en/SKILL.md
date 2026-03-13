---
name: researcher-check-en
description: Individual researcher verification and academic profile analysis. Publication/citation verification, h-index, grant history, society activities, mentorship track record (English version) (project)
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

# Researcher Check Skill v1.0 (English)
## Individual Researcher Verification & Academic Profile Analysis

A skill for objectively verifying an individual researcher's academic capabilities and background for collaborative research, advisory appointments, hiring, or academic partnerships.

---

## 🎯 Core Functions

1. **Education/Career Verification**
2. **Publication Analysis** (citations, h-index, key papers)
3. **Grant Funding History**
4. **Society Activities/Leadership**
5. **Mentorship Track Record**
6. **Research Network Analysis**
7. **Red Flags Detection**

---

## 📋 Workflow

### Step 1: Initialization & Information Gathering

**Ask the user:**
```
Starting individual researcher verification.

1. Researcher name (English/native):

2. Affiliated institution (if known):

3. Field/Research area:

4. Do you have related materials? (Optional)
   - CV file path
   - Personal webpage URL
   - Google Scholar profile URL
   - None (web search only)

5. What is the purpose of this verification?
   - Collaborative research partner
   - Advisory/review committee
   - Hiring/recruitment
   - Seminar speaker invitation
   - Thesis committee member
   - Other
```

### Step 2: Education/Career Verification

**WebSearch queries:**
```
- "[name] [field] PhD thesis"
- "[name] curriculum vitae CV"
- "[name] [university] professor"
- "[name] LinkedIn profile"
- "[name] ORCID"
```

**Verification items:**

| Item | Verification Method | Result |
|------|---------------------|--------|
| Bachelor's | University alumni DB, LinkedIn | ✓/✗/? |
| Master's | Thesis database | ✓/✗/? |
| Ph.D. | ProQuest, thesis DB | ✓/✗/? |
| Postdoc | Institution website, paper affiliations | ✓/✗/? |
| Current Position | Faculty page | ✓/✗/? |

### Step 3: Publication Analysis

**Sources:**
- Google Scholar
- PubMed
- Web of Science
- Scopus
- ORCID

**Metrics to collect:**

| Metric | Description | Value |
|--------|-------------|-------|
| **Total Publications** | All published papers | N |
| **First/Corresponding** | Primary contribution papers | N |
| **Total Citations** | Per Google Scholar | N |
| **h-index** | h papers with h+ citations each | N |
| **i10-index** | Papers with 10+ citations | N |
| **Last 5-year Citations** | Research activity indicator | N |

**Top Publications Analysis (Top 5):**

| Rank | Title | Journal | IF | Citations | Role |
|------|-------|---------|-----|-----------|------|
| 1 | ... | ... | ... | ... | First/Corresponding |
| 2 | ... | ... | ... | ... | ... |

**Research Keywords:**
- Key topics extracted from paper titles/abstracts
- Research trend evolution

### Step 4: Grant Funding History

**WebSearch queries:**
```
- "[name] NIH grant"
- "[name] NSF funding"
- "[name] ERC grant"
- "[name] research grant PI"
```

**Information to collect:**

| Grant Title | Period | Amount | Role | Funder |
|-------------|--------|--------|------|--------|
| ... | 20XX-20XX | $XXX | PI/Co-PI | NIH/NSF/ERC |

**Assessment:**
- Total PI funding
- Active grants count
- Large-scale (center-level) experience

### Step 5: Society Activities/Leadership

**Items to investigate:**

| Activity Type | Details |
|---------------|---------|
| **Society Officers** | President, Board member, Committee chair |
| **Journal Roles** | Editor-in-Chief, Associate Editor, Editorial Board |
| **Conference Organization** | Conference chair, Session organizer |
| **Invited Talks** | Keynote, Plenary, Invited lectures |
| **Awards** | Scientific awards, Young investigator awards |

### Step 6: Mentorship Track Record

**Search methods:**
```
- "[name] lab alumni"
- "[name] PhD students graduated"
- "[name] mentorship"
- Lab webpage → Alumni section
```

**Information to collect:**

| Category | Count | Current Positions |
|----------|-------|-------------------|
| PhD Graduates | N | Faculty N, Industry N, Postdoc N |
| MS Graduates | N | PhD program N, Industry N |
| Postdocs Trained | N | Faculty N, Industry N |

**Mentee Success Stories:**
- Mentees who became prominent researchers
- Mentees who founded startups
- Award-winning mentees

### Step 7: Research Network Analysis

**Co-author Network:**
- Key collaborators (by frequency)
- International collaboration status
- Industry partnerships

**Research Group Affiliations:**
- Consortium/center participation
- Society committee involvement

### Step 8: Red Flags Detection

| Category | Red Flag | Severity |
|----------|----------|----------|
| **Education** | Unverifiable degree | 🔴 High |
| **Publications** | Multiple predatory journal papers | 🔴 High |
| **Publications** | Excessive self-citation (>30%) | 🟡 Medium |
| **Publications** | No papers in last 5 years | 🟡 Medium |
| **Ethics** | Retraction history | 🔴 High |
| **Ethics** | Research misconduct record | 🔴 High |
| **Career** | Frequent position changes (<2 years) | 🟡 Medium |
| **Funding** | No PI grants (for senior researcher) | 🟡 Medium |

**WebSearch queries:**
```
- "[name] retraction"
- "[name] research misconduct"
- "[name] plagiarism"
- "Retraction Watch [name]"
```

---

## 📝 Report Template

### File Naming Convention
```
collaborations/researchers/[name]_profile_[YYYY-MM-DD]_EN.md
```

### Report Structure

```markdown
# [Researcher Name] Academic Profile Analysis Report

> **Date:** YYYY-MM-DD
> **Affiliation:** [Institution]
> **Field:** [Research area]
> **Purpose:** [Verification purpose]

---

## 1. Basic Information
[Table with name, position, field, contact]

## 2. Education/Career Verification
### Education
[Verification results table]

### Career History
[Chronological + verification status]

## 3. Publication Analysis
### Metrics
[h-index, citations table]

### Top Publications (Top 5-10)
[Paper list + impact analysis]

### Research Evolution
[Topic changes over time]

## 4. Grant Funding History
[Grant list table]

## 5. Society Activities/Leadership
[Activity list]

## 6. Mentorship Track Record
[Graduate statistics + success stories]

## 7. Research Network
### Key Collaborators
[By frequency]

### International Collaborations
[By country/institution]

## 8. Objective Assessment

### Strengths
[Table]

### Weaknesses/Limitations
[Table]

### Red Flags
[Findings or "None found"]

## 9. Collaboration Considerations
- Benefits of collaborating with this researcher
- Points to be cautious about
- Recommended collaboration format

## 10. Questions for Meeting
### Research
[5-10 questions]

### Collaboration
[3-5 questions]

## 11. Executive Summary
[3-4 paragraphs]

## References
[Source list]
```

---

## 📊 Evaluation Criteria

### Research Capability Grades

| Grade | h-index | Total Citations | First/Corresponding | Grants |
|-------|---------|-----------------|---------------------|--------|
| **S** (World-class) | 50+ | 10,000+ | 50+ | Multiple large grants |
| **A** (Excellent) | 30-49 | 3,000-10,000 | 30-49 | Multiple medium grants |
| **B** (Good) | 15-29 | 1,000-3,000 | 15-29 | Small grants |
| **C** (Average) | 5-14 | 100-1,000 | 5-14 | Limited |
| **D** (Early-career) | <5 | <100 | <5 | None |

*Field-specific variations apply (Life sciences vs Engineering vs Humanities)*

---

## ⚙️ Settings

### Language
- **Default**: English
- **Korean version**: Use `researcher-check` skill

### Save Location
```
[project]/collaborations/researchers/
```

---

## 🚨 Important Notes

- **ALWAYS** cross-verify with Google Scholar and official institution pages
- **ALWAYS** check Retraction Watch
- **ALWAYS** note field-specific h-index standards
- **NEVER** evaluate based on single metric
- **NEVER** quote CV content without verification

---

**Version**: 1.0
**Last Updated**: 2025-12-15
