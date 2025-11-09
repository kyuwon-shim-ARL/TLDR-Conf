# Conference Materials Repository

This directory contains all conference preparation materials organized by conference. Each conference has its own subdirectory with raw materials, generated backgrounds, and personalized plans.

## Directory Structure

```
conferences/
├── README.md                     # This file
│
├── MSK2025/                      # Korean Society for Microbiology 2025
│   ├── raw/                      # Source materials
│   ├── backgrounds/              # Session backgrounds (31 files)
│   ├── plans/                    # Conference plans
│   ├── archive/                  # Backup files
│   └── README.md
│
├── IAMRT2025/                    # Intl. Workshop on AMR & Antibiotics
│   ├── raw/                      # Source materials
│   ├── backgrounds/              # Session backgrounds (4 files)
│   ├── plans/                    # Conference plans
│   └── README.md
│
└── _template/                    # Template for new conferences
    ├── raw/
    ├── backgrounds/
    ├── plans/
    ├── archive/
    └── README.md                 # Setup instructions
```

## Available Conferences

### MSK2025 - Korean Society for Microbiology Annual Meeting 2025

**Status**: ✅ Complete
**Dates**: October 26-28, 2025
**Location**: 대전 컨벤션센터 (Daejeon, Korea)
**Sessions**: 21 Symposia + 4 Plenary + 2 Award Lectures

**Statistics**:
- 31 background files
- ~46,500 total lines
- Average: 1,500 lines per file

**Focus Areas**:
- Bacterial pathogenesis & AMR
- Microbiome science
- Synthetic biology & biosystems
- One Health & biosafety

**Directory**: `MSK2025/`
[See full details →](MSK2025/README.md)

---

### IAMRT2025 - International Workshop on AMR & Antibiotic Development

**Status**: ✅ Complete
**Date**: October 30, 2025 (Single-day workshop)
**Location**: Sungkyunkwan University (Seoul, Korea)
**Sessions**: 4 sessions, 12 talks

**Statistics**:
- 4 background files
- 6,174 total lines
- Average: 1,544 lines per file

**Focus Areas**:
- Antimicrobial resistance (One Health approach)
- Bacterial pathogenesis (Mtb, P. aeruginosa, S. aureus)
- Host-pathogen interaction (autophagy, organoids)
- Antibiotic development (peptides, natural products, AI/ML)

**Special Note**: Strong bioinformatics component (Tn-seq, scRNA-seq, ML/AI)

**Directory**: `IAMRT2025/`
[See full details →](IAMRT2025/README.md)

---

## Adding a New Conference

Use the `_template/` directory as a starting point:

### Quick Start

```bash
# 1. Copy template
cp -r conferences/_template conferences/[NEW_CONF_ID]

# 2. Add source materials (PDFs, etc.)
cp /path/to/materials/* conferences/[NEW_CONF_ID]/raw/

# 3. Create config file
cp .claude/skills/conference-advisor/conferences/IAMRT2025.yml \
   .claude/skills/conference-advisor/conferences/[NEW_CONF_ID].yml

# 4. Edit config (update paths, conference details)
# 5. Run conference-advisor skill
# 6. Update README with actual details
```

[See detailed instructions →](_template/README.md)

---

## Quality Standards

All conference materials follow the **comprehensive background template** with these guarantees:

### Length Standards
- Multi-talk sessions: **1000-2000 lines**
- Single talks: **700-1000 lines**
- Proven benchmark: MSK2025 S17-S21 (1,487 lines average)

### Content Standards (9 Mandatory Sections)
1. ✅ 개요 (Overview) with importance score
2. ✅ 쉬운말 풀이 (Easy Explanation) - session AND individual talks
3. ✅ 발표별 상세 분석 (Talk-by-Talk Analysis)
4. ✅ 핵심 요약 (10 Key Messages)
5. ✅ 사전 읽기 (Pre-reading) with actual citations
6. ✅ 질문 리스트 (25-35 Questions)
7. ✅ 네트워킹 우선순위 (Networking Strategy with tiers)
8. ✅ 당일 체크리스트 (Day-of Checklist)
9. ✅ 학습 성과 (Learning Outcomes)

### Research Currency
- ✅ WebSearch for 2024-2025 research
- ✅ Speaker's recent publications cited
- ✅ Industry trends (where applicable)

---

## File Naming Conventions

### Background Files
- **MSK2025**: `background_[TYPE][N]_[topic].md`
  - Examples: `background_S1_bacterial_pathogenesis.md`, `background_PL4_outer_membrane.md`
- **IAMRT2025**: `IAMRT_background_S[N]_[topic].md`
  - Examples: `IAMRT_background_S1_antimicrobial_resistance.md`
- **Custom**: Follow the `prefix` in conference config YAML

### Plan Files
- Format: `conference_plan_[CONFERENCE_ID].md`
- Examples: `conference_plan_MSK2025.md`, `conference_plan_IAMRT2025.md`

### Archive Files
- Format: `[original_name]_backup.md`
- Automatically moved to `archive/` subdirectory

---

## Statistics Summary

| Conference | Sessions | Background Files | Total Lines | Avg Lines/File | Status |
|------------|----------|------------------|-------------|----------------|--------|
| MSK2025 | 27 | 31 | ~46,500 | 1,500 | ✅ Complete |
| IAMRT2025 | 4 | 4 | 6,174 | 1,544 | ✅ Complete |
| **Total** | **31** | **35** | **~52,674** | **1,505** | |

---

## Related Tools

### Conference-Advisor Skill (v2.0)
**Location**: `.claude/skills/conference-advisor/`

**Features**:
- Multi-conference support via YAML configs
- Comprehensive background generation (1000-2000 lines)
- Personalized conference planning
- Session recommendations based on research interests
- Networking strategy generation

**Usage**:
```
/conference-advisor
→ Select conference
→ Provide research interests
→ Choose sessions
→ Generate materials
```

### Configuration Files
**Location**: `.claude/skills/conference-advisor/conferences/`

- `MSK2025.yml` - Korean Society for Microbiology config
- `IAMRT2025.yml` - IAMRT workshop config
- `[YOUR_CONFERENCE].yml` - Add new configs here

---

## Best Practices

### For Conference Preparation

**4 Weeks Before**:
1. Run conference-advisor skill
2. Get session recommendations
3. Select 8-12 target sessions
4. Generate background materials

**2 Weeks Before**:
5. Read all backgrounds (first pass)
6. Review question lists
7. Customize questions based on your research

**1 Week Before**:
8. Download pre-reading papers
9. Identify networking targets
10. Prepare elevator pitch

**Day Before**:
11. Review checklists
12. Prepare materials (business cards, notebook)

**Conference Day**:
13. Follow session checklists
14. Take notes during talks
15. Ask prepared questions
16. Network during breaks

**After Conference**:
17. Send follow-up emails (within 1 week)
18. Read cited papers
19. Self-assess learning outcomes
20. Update research directions

### For Repository Management

**When adding materials**:
- Use consistent naming conventions
- Update conference README
- Archive backup files separately
- Keep raw materials in `raw/` subdirectory

**When archiving**:
- Move outdated materials to `archive/`
- Never delete backup files
- Document major changes in README

---

## System Requirements

### For Skill Execution
- Claude Code with conference-advisor skill v2.0
- WebSearch access (for latest research)
- PDF reading capability (for source materials)

### For Config Files
- YAML format
- Relative paths from project root
- See `_template/README.md` for full spec

---

## Troubleshooting

### Issue: Generated files too short (< 500 lines)
**Solution**: Ensure using `comprehensive_background_template.md` (not old `background_template.md`)

### Issue: Missing individual talk explanations
**Solution**: Explicitly request: "각 발표마다 별도의 쉬운말 풀이를 만들어주세요"

### Issue: PDF extraction fails
**Solution**: Convert to text first: `pdftotext file.pdf file.txt`

### Issue: WebSearch not finding recent research
**Solution**: Verify WebSearch was actually called; manually request if needed

---

## Version History

### v2.0 (Current)
- ✅ Multi-conference support via configs
- ✅ Comprehensive backgrounds (1000-2000 lines)
- ✅ Standardized directory structure
- ✅ Template for new conferences
- ✅ Per-conference READMEs

### v1.0 (Legacy)
- Single conference (MSK2025)
- Files scattered in project root
- Simple background template (~100 lines)

---

## Contributing

When adding a new conference:
1. Follow the template structure
2. Create proper YAML config
3. Generate materials using skill
4. Update this index README
5. Verify quality standards met

---

**Maintained by**: conference-advisor skill v2.0
**Last Updated**: November 2025
**Quality Benchmark**: MSK2025 S1/S17-S21/PL4/AL (1000-2000 lines standard)
