# Conference Advisor Skill

## 📖 Overview

학회 준비를 위한 종합 지원 시스템입니다. 세션 분석, 맞춤 추천, 그리고 **1000-2000줄 수준의 초고퀄리티 배경 자료**를 자동 생성합니다.

## ✨ Version 2.0 Features

### 🆕 New in v2.0
- **다중 학회 지원**: MSK2025, IAMRT2025, 그리고 확장 가능
- **종합 템플릿**: 1000-2000줄 수준 (S1/S17-S21 표준)
- **구성 기반**: 각 학회별 config 파일로 관리
- **세션 + 발표 쉬운말 풀이**: 양쪽 모두 제공

### ✅ Proven Quality
기존 MSK2025 작업 결과:
- `background_S17_zoonosis.md`: **1,547줄**
- `background_S18_biosystems.md`: **2,174줄**
- `background_S20_epidemic.md`: **1,492줄**
- `background_AL_microbiome.md`: **1,799줄**

→ 동일한 퀄리티를 모든 학회에 적용!

## 🚀 Quick Start

### 1. 기본 사용법

```bash
# Claude Code에서 skill 호출
/conference-advisor
```

또는 대화창에서:
```
@conference-advisor 학회 준비 도와줘
```

### 2. Skill이 물어볼 내용

**Step 1: 학회 선택**
```
Which conference?
1. MSK2025
2. IAMRT2025
3. Other
```

**Step 2: 연구 관심사**
- 주요 연구 분야
- 경력 단계 (학생/포닥/교수/산업)
- 학회 목표 (기술 습득/네트워킹/최신 동향)

**Step 3: 세션 선택**
- AI가 추천한 10-15개 세션 중 선택
- 시간 충돌 확인 및 대안 제시

### 3. 결과물

**개인 맞춤 학회 계획**:
- `conference_plan_MSK2025.md`
- 일자별 스케줄
- 네트워킹 전략

**세션별 종합 배경 자료** (각 1000-2000줄):
- `background_S17_zoonosis.md`
- `background_S18_biosystems.md`
- `IAMRT_background_S01_[topic].md`
- 등등...

## 📁 File Structure

```
.claude/skills/conference-advisor/
├── SKILL.md                              # Main skill (v2.0)
├── SKILL_v2.md                          # Backup/reference
├── README.md                            # This file
├── comprehensive_background_template.md  # NEW: 200+ line template
├── background_template.md               # OLD: Simple template (deprecated)
├── conference_plan_template.md
├── speaker_analysis_template.md
└── conferences/                         # Conference configs
    ├── MSK2025.yml
    └── IAMRT2025.yml

Project root/
├── raw/
│   ├── MSK2025-ebook.pdf
│   ├── time_table.md
│   ├── symposia.md
│   └── IAMRT2025/
│       ├── 2025_IAMRT_abstract.pdf
│       └── 2025_IAMRT_program.docx
│
├── background_S17_zoonosis.md           # MSK2025 outputs
├── background_S18_biosystems.md
├── ...
│
└── IAMRT2025_backgrounds/               # IAMRT2025 outputs
    ├── IAMRT_background_S01_[topic].md
    └── ...
```

## 🎯 Background Document Quality Standards

### ✅ Must Have (모든 배경 자료에 필수)

**1. 분량**:
- 멀티 발표 세션: **최소 1000줄**
- 단독 강연: **최소 700줄**
- 목표: **1000-2000줄** (S17-S21 수준)

**2. 구조** (9개 필수 섹션):
```
✓ 🎯 개요 (중요도 점수 포함)
✓ 🌟 쉬운말 풀이 (세션 전체) - 500+ 줄
✓ 📋 발표별 상세 분석 (각 발표마다 쉬운말 풀이)
✓ 🧠 핵심 요약 (10가지 메시지)
✓ 📚 사전 읽기 (실제 논문 인용)
✓ 🎤 질문 리스트 (25-35개)
✓ 🤝 네트워킹 우선순위 (구체적 전략)
✓ ⚡ 당일 체크리스트
✓ 📊 학습 성과
```

**3. 쉬운말 풀이 퀄리티**:
```
✓ 세션 레벨 + 개별 발표 레벨 (양쪽 모두!)
✓ 구체적 예시와 비유
✓ 이야기 형식 (3-7개 챕터)
✓ 최소 500줄 이상
```

**4. 질문 리스트**:
```
✓ 25-35개 구체적 질문
✓ 과학적 (10-15개)
✓ 기술적 (5-10개)
✓ 응용/산업 (5개)
✓ 진로/교육 (3-5개)
✓ 철학적 (2-3개)
```

**5. 최신성**:
```
✓ WebSearch로 2024-2025 최신 연구 포함
✓ 연사의 최근 논문 인용
✓ 산업 동향 (해당 시)
```

### ❌ Avoid (피해야 할 것)

```
✗ Generic placeholders: [TODO], [FILL IN]
✗ 섹션 생략
✗ 쉬운말 풀이가 세션만 있고 개별 발표 없음
✗ 1000줄 미만 (멀티 발표 세션의 경우)
✗ 질문이 10개 미만
✗ 논문 인용 없음
✗ 구체적이지 않은 네트워킹 조언
```

## 🔧 Adding a New Conference

### Step 1: 자료 준비
```bash
mkdir -p raw/[CONFERENCE_ID]
# PDF, DOCX 등을 raw/[CONFERENCE_ID]/에 복사
```

### Step 2: Config 파일 생성
```bash
cp .claude/skills/conference-advisor/conferences/IAMRT2025.yml \
   .claude/skills/conference-advisor/conferences/[NEW_CONFERENCE].yml
```

### Step 3: Config 수정
```yaml
conference:
  id: NEWCONF2025
  full_name: "..."
  dates:
    start: "2025-XX-XX"
    end: "2025-XX-XX"

source_files:
  abstract: "raw/NEWCONF2025/abstracts.pdf"
  program: "raw/NEWCONF2025/program.docx"

output:
  prefix: "NEWCONF_background_"
  directory: "NEWCONF2025_backgrounds"

research_areas:
  - "Area 1"
  - "Area 2"
  # ...
```

### Step 4: Skill 호출
```
/conference-advisor
→ Select "3. Other"
→ Specify: NEWCONF2025
```

**끝!** 자동으로 작동합니다.

## 📊 Example Outputs

### MSK2025 Examples (Already Generated)

**S17 - Emerging Zoonosis** (1,547 lines):
- 5개 발표 × 개별 쉬운말 풀이
- 28개 구체적 질문
- 네트워킹 전략 (3 tiers)
- 당일 체크리스트 (30+ items)

**AL - Microbiome Science** (1,799 lines):
- 7개 챕터 스토리 (쉬운말 풀이)
- KoBioLabs 파이프라인 상세 분석
- 28개 질문 (과학/산업/진로)
- 투자자 질문 포함

### IAMRT2025 Examples (To Be Generated)

동일한 포맷으로:
```
IAMRT_background_S01_single_cell.md  (1000-1500 lines)
IAMRT_background_K01_keynote.md      (700-1000 lines)
IAMRT_background_W01_workshop.md     (800-1200 lines)
```

## 🎓 Best Practices

### For Users

**학회 4주 전**:
1. Skill 실행하여 세션 추천 받기
2. 관심 세션 선택 (8-12개)
3. 배경 자료 생성 요청

**학회 2주 전**:
4. 각 배경 자료 1차 읽기
5. 질문 리스트 검토 및 개인화

**학회 1주 전**:
6. 사전 읽기 논문 다운로드
7. 네트워킹 타겟 명확화
8. Elevator pitch 준비

**학회 D-1**:
9. 체크리스트 최종 확인
10. 명함/노트북 준비

**학회 당일**:
11. 체크리스트 따라가기
12. 실시간 메모

**학회 후 1주일**:
13. Follow-up 이메일 (템플릿 사용)
14. 논문 읽기
15. 학습 성과 자가 평가

### For Skill Developers

**템플릿 수정 시**:
- `comprehensive_background_template.md` 수정
- 실제 output (S17-S21)과 일관성 유지
- 새 섹션 추가 시 SKILL.md도 업데이트

**새 학회 추가 시**:
- YAML config만 생성하면 됨
- SKILL.md 코드 수정 불필요

**퀄리티 검증**:
```bash
# 라인 수 체크
wc -l background_*.md

# 필수 섹션 체크
grep "^## " background_S17_zoonosis.md

# 쉬운말 풀이 개수 확인
grep "쉬운말 풀이" background_S17_zoonosis.md
```

## 🐛 Troubleshooting

### Issue: 생성된 파일이 너무 짧음 (< 500 lines)

**원인**: Skill이 old template 사용
**해결**:
```bash
# SKILL.md 확인
grep "comprehensive_background_template" .claude/skills/conference-advisor/SKILL.md

# 없으면 SKILL_v2.md로 교체
cp .claude/skills/conference-advisor/SKILL_v2.md \
   .claude/skills/conference-advisor/SKILL.md
```

### Issue: 쉬운말 풀이가 세션만 있고 개별 발표가 없음

**지시 사항**:
```
Skill에게 명시적으로:
"각 발표마다 별도의 🌟 쉬운말 풀이를 만들어주세요.
S17-S21 예시처럼 개별 발표마다 [SESSION_ID]-[N] 형식으로."
```

### Issue: PDF에서 정보 추출 실패

**대안**:
1. PDF를 텍스트로 변환: `pdftotext file.pdf file.txt`
2. Skill에게 txt 파일 경로 제공
3. 또는 수동으로 주요 정보 복사

### Issue: WebSearch로 최신 정보를 못 찾음

**확인**:
```
Skill이 WebSearch를 실제로 호출했는지 확인
→ 없으면 명시적으로 요청:
"[주제]에 대해 2024-2025 최신 논문을 WebSearch로 찾아주세요"
```

## 📚 References

### Template Evolution
- v1.0: `background_template.md` (101 lines) - **Deprecated**
- v2.0: `comprehensive_background_template.md` (200+ lines) - **Current**

### Proven Examples
- MSK2025 S1, S17-S21, PL4, AL
- 총 10,413 lines across 7 files
- 평균 1,487 lines per file

### Related Skills
- None yet (first comprehensive conference skill)

## 🤝 Contributing

새로운 학회 추가 시:
1. Config YAML 작성
2. 테스트 실행
3. Example output 생성
4. README 업데이트 (이 파일)

## 📞 Support

Issues/Questions:
- Claude Code conversation
- Check existing MSK2025 outputs for reference

---

**Version**: 2.0
**Last Updated**: 2025-10-31
**Quality Standard**: MSK2025 S1/S17-S21/PL4/AL (1000-2000 lines)
