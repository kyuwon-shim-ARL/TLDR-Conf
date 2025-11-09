# [CONFERENCE_ID] - [Conference Full Name]

## Conference Information

**Full Name**: [Full conference name]
**Organization**: [Organizing institution/society]
**Dates**: [Start date] - [End date]
**Location**: [Venue name and city]

## Directory Structure

```
[CONFERENCE_ID]/
├── raw/                    # Original conference materials
│   ├── [filename].pdf          # Conference program
│   ├── [filename].docx         # Abstract book
│   └── [filename].md           # Schedule
│
├── backgrounds/            # Generated session background materials
│   ├── [PREFIX]_S1_[topic].md
│   ├── [PREFIX]_S2_[topic].md
│   └── ...
│
├── plans/                  # Personalized conference plans
│   └── conference_plan_[CONFERENCE_ID].md
│
└── archive/                # Backup and deprecated files
    └── *_backup.md
```

## Statistics

- **Total Background Materials**: [N] files
- **Session Count**: [N] sessions
- **Total Lines**: [N] lines
- **Average Length**: [N] lines per session

### Session Breakdown
| Session | Topic | Talks | Lines | Importance |
|---------|-------|-------|-------|------------|
| S1 | [Topic] | [N] | [N] | [Score]/100 |
| S2 | [Topic] | [N] | [N] | [Score]/100 |

## Sessions Overview

### Session 1: [Title] ([Time])
**Speakers**:
- [Name] ([Institution]) - [Talk title]
- [Name] ([Institution]) - [Talk title]

### Session 2: [Title] ([Time])
**Speakers**:
- [Name] ([Institution]) - [Talk title]
- [Name] ([Institution]) - [Talk title]

## Research Focus Areas

### Scientific Topics
- [Topic 1]
- [Topic 2]
- [Topic 3]

### Technologies Highlighted
- [Technology 1]
- [Technology 2]
- [Technology 3]

### Industrial/Translational
- [Aspect 1]
- [Aspect 2]

## Target Audience

This conference is particularly valuable for:
- [Audience profile 1]
- [Audience profile 2]
- [Audience profile 3]

## Usage

All background materials follow the comprehensive template with 9 sections:
1. 개요 (Overview) with importance score
2. 쉬운말 풀이 (Easy Explanation) - session and individual talks
3. 발표별 상세 분석 (Talk-by-Talk Analysis)
4. 핵심 요약 (10 Key Messages)
5. 사전 읽기 (Pre-reading) with recent research
6. 질문 리스트 (25-35 Questions)
7. 네트워킹 우선순위 (Networking Strategy)
8. 당일 체크리스트 (Day-of Checklist)
9. 학습 성과 (Learning Outcomes)

## Conference Plan

See `plans/conference_plan_[CONFERENCE_ID].md` for:
- Detailed schedule with action items
- Networking strategy (tiered prioritization)
- Pre-conference preparation timeline
- Post-conference follow-up plan
- Success metrics and learning objectives

## Related Configuration

See `.claude/skills/conference-advisor/conferences/[CONFERENCE_ID].yml` for full configuration.

## Setup Instructions

To use this template for a new conference:

1. **Copy this directory**:
   ```bash
   cp -r conferences/_template conferences/[NEW_CONFERENCE_ID]
   ```

2. **Add source materials**:
   ```bash
   # Place PDF, DOCX, or other source files in raw/
   cp /path/to/program.pdf conferences/[NEW_CONFERENCE_ID]/raw/
   ```

3. **Create config file**:
   ```bash
   cp .claude/skills/conference-advisor/conferences/IAMRT2025.yml \
      .claude/skills/conference-advisor/conferences/[NEW_CONFERENCE_ID].yml
   ```

4. **Edit config** (`.claude/skills/conference-advisor/conferences/[NEW_CONFERENCE_ID].yml`):
   ```yaml
   conference:
     id: [NEW_CONFERENCE_ID]
     full_name: "[Full Name]"
     dates:
       start: "YYYY-MM-DD"
       end: "YYYY-MM-DD"

   source_files:
     program: "conferences/[NEW_CONFERENCE_ID]/raw/program.pdf"
     abstract: "conferences/[NEW_CONFERENCE_ID]/raw/abstracts.pdf"

   output:
     prefix: "[PREFIX]_background_"
     directory: "conferences/[NEW_CONFERENCE_ID]/backgrounds"

   research_areas:
     - "[Area 1]"
     - "[Area 2]"
   ```

5. **Run conference-advisor skill**:
   ```
   /conference-advisor
   → Select "3. Other"
   → Specify: [NEW_CONFERENCE_ID]
   ```

6. **Update this README** with actual conference details

## Generated

Materials generated using conference-advisor skill v2.0 with comprehensive background template.

**Quality Standard**: 1000-2000 lines per session, following proven quality benchmarks.
