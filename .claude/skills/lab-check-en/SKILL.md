---
name: lab-check-en
description: Research lab/group verification and capability analysis. PI background, research programs, equipment/infrastructure, alumni careers, funding status, collaboration networks (English version) (project)
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

# Lab Check Skill v1.0 (English)
## Research Lab/Group Verification & Capability Analysis

A skill for objectively evaluating a research laboratory's overall capabilities and environment for collaborative research, graduate school applications, postdoc positions, or institutional partnerships.

---

## 🎯 Core Functions

1. **PI (Principal Investigator) Background Verification**
2. **Research Program Analysis** (topics, methodology, strengths)
3. **Lab Member Composition**
4. **Research Equipment/Infrastructure**
5. **Alumni Career Tracking**
6. **Funding/Financial Status**
7. **Collaboration Network**
8. **Lab Culture/Reputation**

---

## 📋 Workflow

### Step 1: Initialization & Information Gathering

**Ask the user:**
```
Starting research lab verification.

1. Lab name or PI name:

2. Host institution/university:

3. Research field:

4. Do you have related materials? (Optional)
   - Lab webpage URL
   - PI CV file
   - None (web search only)

5. What is the purpose of this verification?
   - Collaborative research
   - Considering for graduate school
   - Considering for postdoc position
   - Technology transfer/industry partnership
   - Institutional MOU
   - Other
```

### Step 2: PI Background Verification

**[Apply same process as researcher-check]**

- Education/career verification
- Publication metrics (h-index, citations)
- Grant funding history
- Society leadership

**Additional PI characteristics:**

| Item | Content |
|------|---------|
| Research Style | Theory/Experimental/Computational/Interdisciplinary |
| Mentoring Style | Hands-on / Independent |
| Lab Duration | Founding year, stability |
| Tenure Status | Position stability |

### Step 3: Research Program Analysis

**Items to investigate:**

| Item | Content |
|------|---------|
| **Core Research Topics** | 3-5 main topics |
| **Methodology** | Experimental/Computational/Theoretical/Clinical |
| **Technical Strengths** | Unique techniques, know-how |
| **Differentiators** | vs competing labs |
| **Research Direction** | Current → Future plans |

**Last 5 years research trends:**
- Keyword changes in major papers
- New research directions
- Discontinued research lines

### Step 4: Lab Member Composition

**WebSearch queries:**
```
- "[lab name] members"
- "[PI name] lab team"
- "[lab name] people"
```

**Member matrix:**

| Position | Count | Details |
|----------|-------|---------|
| Professor/PI | 1 | (Add if co-PIs exist) |
| Research Scientist | N | |
| Postdocs | N | |
| PhD Students | N | Year distribution |
| MS Students | N | |
| Undergraduates | N | |
| Research Staff/Technicians | N | |

**Size adequacy assessment:**
- Total members vs funding level
- Student:Postdoc ratio
- Students per PI (mentoring capacity)

### Step 5: Research Equipment/Infrastructure

**Investigation methods:**
- Lab webpage "Equipment" / "Facilities" section
- Institutional shared facilities
- Methods sections in recent papers

**Equipment list:**

| Equipment | Purpose | Owned/Shared | Status |
|-----------|---------|--------------|--------|
| ... | ... | In-house/Shared | New/Old |

**Infrastructure assessment:**

| Item | Status |
|------|--------|
| Lab Space | Area, location |
| Computing | Cluster, GPUs |
| Biological Resources | Cell lines, animal facilities |
| Databases | In-house databases |

### Step 6: Alumni Career Tracking

**WebSearch queries:**
```
- "[lab name] alumni"
- "[PI name] former students"
- "[PI name] PhD graduates"
```

**Alumni career statistics:**

| Career Path | PhD | MS |
|-------------|-----|-----|
| Faculty/Researcher | N% | - |
| Industry (Large corp) | N% | N% |
| Industry (Startup) | N% | N% |
| PhD program | - | N% |
| Postdoc | N% | - |
| Other | N% | N% |

**Notable alumni:**
- Alumni who became prominent faculty
- Alumni who founded startups
- Alumni in executive positions

**Time to degree:**
- Average PhD duration
- Early/delayed graduation rates

### Step 7: Funding/Financial Status

**Items to investigate:**

| Item | Content |
|------|---------|
| Current Grants | Title, period, amount |
| Major Funders | Government/Industry/Foundation |
| Annual Budget | Estimated |
| Financial Stability | Long-term grants |

**Industry Partnerships:**
- Corporate sponsorships
- Contract research
- Technology licensing

### Step 8: Collaboration Network

**Domestic Collaborations:**

| Institution | Field | Type |
|-------------|-------|------|
| ... | ... | Joint research/Equipment sharing/Personnel exchange |

**International Collaborations:**

| Country | Institution | PI | Content |
|---------|-------------|-----|---------|
| ... | ... | ... | ... |

**Industry Partners:**
- Company list
- Collaboration types

### Step 9: Lab Culture/Reputation

**Investigation methods:**
```
- "[lab name] review"
- "[PI name] mentor"
- Glassdoor / RateMyProfessors
- Graduate student communities
```

**Evaluation items:**

| Item | Content |
|------|---------|
| Meeting Frequency | Weekly/individual |
| Work Hours | Flexible/mandatory |
| Vacation Policy | Official/unofficial |
| Graduation Support | Job/career help |
| Lab Atmosphere | Competitive/collaborative |

**Red Flags:**

| Flag | Severity |
|------|----------|
| Multiple negative alumni reviews | 🔴 High |
| High dropout rate | 🔴 High |
| Graduation delay pattern | 🟡 Medium |
| Frequent PI absence | 🟡 Medium |
| Financial instability signs | 🟡 Medium |

---

## 📝 Report Template

### File Naming Convention
```
collaborations/labs/[PI_name]_lab_[YYYY-MM-DD]_EN.md
```

### Report Structure

```markdown
# [Lab Name / PI Lab] Research Lab Capability Analysis Report

> **Date:** YYYY-MM-DD
> **Institution:** [Name]
> **PI:** [Name]
> **Purpose:** [Verification purpose]

---

## 1. Lab Overview
| Item | Content |
|------|---------|
| Lab Name | |
| PI | |
| Institution | |
| Founded | |
| Website | |
| Research Field | |

## 2. PI Profile
[Detailed analysis at researcher-check level]

## 3. Research Program
### Core Topics
### Methodology/Techniques
### Differentiators

## 4. Member Composition
[Headcount by position]
[Key member introductions]

## 5. Research Infrastructure
### Major Equipment
### Facilities/Space
### Computing Resources

## 6. Alumni Careers
[Statistics + success stories]

## 7. Funding/Finances
[Current grant list]
[Financial stability assessment]

## 8. Collaboration Network
### Domestic
### International
### Industry

## 9. Lab Culture/Reputation
[Investigation results]
[Red flags if any]

## 10. Objective Assessment

### Strengths
| Item | Rating |
|------|--------|

### Weaknesses/Risks
| Item | Concerns |
|------|----------|

## 11. Collaboration/Application Considerations
- Benefits of joining/collaborating with this lab
- Points to be cautious about
- Recommended approach

## 12. Question List
### For PI Interview
[5-10 questions]

### For Lab Member Interview
[5 questions]

## 13. Executive Summary
[3-4 paragraphs]

## References
[Source list]
```

---

## 📊 Lab Evaluation Criteria

### Overall Grade

| Grade | PI Capability | Funding | Alumni Careers | Infrastructure |
|-------|---------------|---------|----------------|----------------|
| **S** | h-index 40+ | $1M+/yr | Many faculty | State-of-art |
| **A** | h-index 25+ | $500K+/yr | Top companies | Excellent |
| **B** | h-index 15+ | $200K+/yr | Good | Adequate |
| **C** | h-index 10+ | $100K+/yr | Average | Basic |
| **D** | h-index <10 | Unstable | Unclear | Insufficient |

---

## ⚙️ Settings

### Language
- **Default**: English
- **Korean version**: Use `lab-check` skill

### Save Location
```
[project]/collaborations/labs/
```

---

## 🚨 Important Notes

- **ALWAYS** evaluate PI and lab separately (excellent PI ≠ excellent lab)
- **ALWAYS** verify actual alumni career paths
- **ALWAYS** collect current member/alumni opinions when possible
- **NEVER** judge based on webpage info alone
- **NEVER** evaluate entire lab by single metric (paper count, etc.)

---

**Version**: 1.0
**Last Updated**: 2025-12-15
