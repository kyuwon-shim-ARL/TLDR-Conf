# Conference-Advisor Skill - 팀 배포 가이드

## 📦 배포 개요

**conference-advisor** skill은 Claude Code의 재사용 가능한 기능으로, 팀원들과 공유할 수 있습니다.

### ✅ 배포 가능한 이유

Claude Code skills는 **프로젝트 기반**으로 작동:
- `.claude/skills/` 디렉토리에 저장
- Git으로 버전 관리
- 팀원이 `git pull`하면 **자동으로 사용 가능**
- 별도 설치/설정 불필요!

---

## 🚀 배포 방법 (2가지 시나리오)

### 시나리오 1: 같은 Git 저장소 사용 (권장)

**배포자 (당신)**:
```bash
# 1단계: Skill과 데이터를 Git에 추가
git add .claude/skills/conference-advisor/
git add conferences/

# 2단계: 커밋
git commit -m "Add conference-advisor skill v2.0 with MSK2025 & IAMRT2025 data

- Multi-conference support (MSK2025, IAMRT2025)
- Comprehensive background generation (1000-2000 lines)
- Clean data structure in conferences/ directory
- Template for adding new conferences

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>"

# 3단계: Push
git push origin master
```

**팀원**:
```bash
# 1단계: Pull
git pull origin master

# 2단계: 바로 사용!
# Claude Code에서 자동으로 인식됨
```

**끝! 팀원은 즉시 다음 명령을 사용할 수 있습니다:**
```
/conference-advisor
```

또는 대화창에서:
```
@conference-advisor 학회 준비 도와줘
```

---

### 시나리오 2: 다른 프로젝트로 이식

**Skill만 복사하는 경우**:

```bash
# 배포자: 배포 패키지 생성
cd /home/kyuwon/projects/MSK2025
tar -czf conference-advisor-skill.tar.gz \
  .claude/skills/conference-advisor/ \
  conferences/_template/

# 팀원: 자신의 프로젝트에 설치
cd /path/to/their/project
tar -xzf conference-advisor-skill.tar.gz

# 확인
ls .claude/skills/conference-advisor/
ls conferences/_template/
```

**팀원이 자신의 학회 추가**:
```bash
# 1. 템플릿 복사
cp -r conferences/_template conferences/THEIR_CONF_2025

# 2. 원본 자료 추가
cp /path/to/materials/* conferences/THEIR_CONF_2025/raw/

# 3. Config 생성
cp .claude/skills/conference-advisor/conferences/IAMRT2025.yml \
   .claude/skills/conference-advisor/conferences/THEIR_CONF_2025.yml

# 4. Config 수정
# (conference ID, 경로 등 업데이트)

# 5. Claude Code에서 실행
/conference-advisor
→ "3. Other" 선택
→ "THEIR_CONF_2025" 입력
```

---

## 📋 배포 패키지에 포함된 내용

### 필수 파일

```
.claude/skills/conference-advisor/
├── SKILL.md                              # ✅ 필수! (YAML frontmatter 포함)
├── comprehensive_background_template.md  # 배경 자료 템플릿
├── conference_plan_template.md           # 학회 계획 템플릿
├── speaker_analysis_template.md          # 연사 분석 템플릿
└── conferences/
    ├── MSK2025.yml                       # 예시 config
    └── IAMRT2025.yml                     # 예시 config
```

### 선택 파일 (참고용)

```
.claude/skills/conference-advisor/
├── README.md                             # Skill 문서
├── background_template.md                # (deprecated, 참고용)
└── conferences/_template/README.md       # 새 학회 추가 가이드
```

### 데이터 (선택 - 예시로 포함 가능)

```
conferences/
├── README.md                             # 전체 인덱스
├── MSK2025/                              # 예시 학회 1
│   ├── raw/
│   ├── backgrounds/ (31개 파일)
│   ├── plans/
│   └── README.md
├── IAMRT2025/                            # 예시 학회 2
│   ├── raw/
│   ├── backgrounds/ (4개 파일)
│   ├── plans/
│   └── README.md
└── _template/                            # 템플릿
    └── README.md
```

**참고**: 팀원이 자신의 학회 데이터를 사용할 경우, `conferences/MSK2025/`와 `conferences/IAMRT2025/`는 **예시**로만 필요합니다.

---

## 🔧 팀원 사용 가이드

### 초기 설정 (한 번만)

**1. Claude Code 버전 확인**:
- Claude Code가 설치되어 있어야 함
- Skills 기능 지원 버전인지 확인

**2. Skill 인식 확인**:
```bash
# Claude Code 실행 후 대화창에서
/conference-advisor

# 또는
@conference-advisor
```

Skill이 로드되면 성공!

### 기본 사용법

**Step 1: Skill 호출**
```
/conference-advisor
```

**Step 2: 학회 선택**
```
Which conference?
1. MSK2025
2. IAMRT2025
3. Other
```

**Step 3: 연구 관심사 입력**
- 주요 연구 분야 (예: AMR, microbiome, bioinformatics)
- 경력 단계 (학생/포닥/교수/산업)
- 학회 목표 (기술 습득/네트워킹/최신 동향)

**Step 4: 세션 선택**
- AI가 추천한 10-15개 세션 중 선택
- 시간 충돌 확인

**Step 5: 자료 생성**
- 세션별 배경 자료 (1000-2000줄)
- 종합 학회 계획

### 결과물

**생성되는 파일**:
```
conferences/[CONFERENCE_ID]/
├── backgrounds/
│   ├── [PREFIX]_S1_[topic].md  (1000-2000줄)
│   ├── [PREFIX]_S2_[topic].md
│   └── ...
└── plans/
    └── conference_plan_[ID].md
```

**각 배경 자료 포함 내용** (9개 필수 섹션):
1. 개요 (중요도 점수)
2. 쉬운말 풀이 (세션 + 개별 발표)
3. 발표별 상세 분석
4. 핵심 요약 (10가지 메시지)
5. 사전 읽기 (논문 인용)
6. 질문 리스트 (25-35개)
7. 네트워킹 전략
8. 당일 체크리스트
9. 학습 성과

---

## 🎯 새 학회 추가 방법

팀원이 자신의 학회를 추가하는 방법:

### 빠른 시작

```bash
# 1. 템플릿 복사
cp -r conferences/_template conferences/NEWCONF2025

# 2. 원본 자료 추가
cp /path/to/program.pdf conferences/NEWCONF2025/raw/
cp /path/to/abstracts.pdf conferences/NEWCONF2025/raw/

# 3. Config 생성
cp .claude/skills/conference-advisor/conferences/IAMRT2025.yml \
   .claude/skills/conference-advisor/conferences/NEWCONF2025.yml
```

### Config 수정 (`NEWCONF2025.yml`)

```yaml
conference:
  id: NEWCONF2025
  full_name: "New Conference 2025"
  organization: "Conference Society"
  dates:
    start: "2025-06-01"
    end: "2025-06-03"
  location: "Seoul, Korea"

source_files:
  program: "conferences/NEWCONF2025/raw/program.pdf"
  abstract: "conferences/NEWCONF2025/raw/abstracts.pdf"

output:
  prefix: "NEWCONF_background_"
  suffix: ".md"
  directory: "conferences/NEWCONF2025/backgrounds"

research_areas:
  - "Area 1"
  - "Area 2"
  - "Area 3"

session_types:
  - id: "S"
    name: "Symposium"
    format: "multiple_talks"
  - id: "K"
    name: "Keynote"
    format: "single_talk"

template:
  type: "comprehensive"
  sections:
    - "개요 (Overview)"
    - "쉬운말 풀이 (Easy Explanation)"
    - "발표별 상세 분석 (Talk-by-Talk Analysis)"
    - "핵심 요약 (Summary)"
    - "사전 읽기 (Pre-reading)"
    - "질문 리스트 (Questions)"
    - "네트워킹 (Networking)"
    - "체크리스트 (Checklist)"
    - "학습 성과 (Learning Outcomes)"

language:
  primary: "ko"
  secondary: "en"
```

### Skill 실행

```
/conference-advisor
→ "3. Other" 선택
→ "NEWCONF2025" 입력
→ 연구 관심사 입력
→ 세션 선택
→ 자료 생성!
```

**10분이면 끝!**

---

## 📊 품질 기준

팀원이 생성하는 모든 자료는 동일한 품질 기준을 따릅니다:

### 분량
- 멀티 발표 세션: **최소 1000줄**
- 단독 강연: **최소 700줄**
- 목표: **1000-2000줄** (검증된 품질)

### 구조
- ✅ 9개 필수 섹션 모두 포함
- ✅ 세션 + 개별 발표 쉬운말 풀이
- ✅ 25-35개 구체적 질문
- ✅ 실제 논문 인용 (2024-2025 연구)
- ✅ 단계별 네트워킹 전략
- ✅ 당일 체크리스트

### 최신성
- ✅ WebSearch로 최신 연구 포함
- ✅ 연사의 최근 논문 인용
- ✅ 산업 동향 (해당 시)

---

## 🔍 트러블슈팅

### Q1: Skill이 인식되지 않아요

**확인**:
```bash
ls .claude/skills/conference-advisor/SKILL.md
```

**없으면**:
```bash
git pull origin master
# 또는
tar -xzf conference-advisor-skill.tar.gz
```

### Q2: 생성된 파일이 너무 짧아요 (< 500 lines)

**원인**: Old template 사용

**해결**:
```bash
grep "comprehensive_background_template" \
  .claude/skills/conference-advisor/SKILL.md

# 없으면 SKILL.md가 오래된 버전
# 최신 버전 다시 받기
```

### Q3: 쉬운말 풀이가 세션만 있어요

**해결**:
Skill에게 명시적으로 요청:
```
"각 발표마다 별도의 🌟 쉬운말 풀이를 만들어주세요.
MSK2025 S17-S21 예시처럼 개별 발표마다 생성해주세요."
```

### Q4: PDF에서 정보 추출이 안 돼요

**대안 1**: 텍스트로 변환
```bash
pdftotext program.pdf program.txt
```

**대안 2**: 수동으로 주요 정보 복사
```markdown
# conferences/[ID]/raw/manual_extract.md
Session 1: Title
- Speaker 1: Name (Institution) - Talk title
- Speaker 2: ...
```

### Q5: Config 경로가 안 맞아요

**확인**:
```yaml
# Config의 경로는 **프로젝트 루트 기준**
source_files:
  program: "conferences/NEWCONF2025/raw/program.pdf"  # ✅ 절대 경로
  # NOT: "raw/program.pdf"  # ❌

output:
  directory: "conferences/NEWCONF2025/backgrounds"  # ✅
  # NOT: "backgrounds"  # ❌
```

---

## 🤝 팀원 기여 가이드

팀원이 새로운 학회를 추가한 후:

### 1. 로컬 테스트
```bash
# 자료 생성 확인
ls conferences/[NEW_CONF]/backgrounds/

# 라인 수 확인
wc -l conferences/[NEW_CONF]/backgrounds/*.md

# 필수 섹션 확인
grep "^## " conferences/[NEW_CONF]/backgrounds/*.md
```

### 2. (선택) 저장소에 기여
```bash
# Config만 공유 (팀에 유용한 경우)
git add .claude/skills/conference-advisor/conferences/[NEW_CONF].yml
git add conferences/[NEW_CONF]/README.md

git commit -m "Add [NEW_CONF] configuration"
git push origin master
```

**주의**:
- 개인 학회 자료 (`backgrounds/`, `plans/`)는 **공유하지 않아도 됨**
- Config만 공유하면 다른 팀원도 동일한 학회 사용 가능

### 3. 전체 인덱스 업데이트
```bash
# conferences/README.md에 새 학회 추가
```

---

## 📚 추가 리소스

### 문서
- **Skill 설명**: `.claude/skills/conference-advisor/README.md`
- **전체 인덱스**: `conferences/README.md`
- **새 학회 가이드**: `conferences/_template/README.md`

### 예시
- **MSK2025**: `conferences/MSK2025/` (31개 배경 자료, 총 46,500줄)
- **IAMRT2025**: `conferences/IAMRT2025/` (4개 배경 자료, 총 6,174줄)

### Config 예시
- `.claude/skills/conference-advisor/conferences/MSK2025.yml`
- `.claude/skills/conference-advisor/conferences/IAMRT2025.yml`

---

## 🎓 Best Practices

### 학회 4주 전
1. Skill 실행 (`/conference-advisor`)
2. 세션 추천 받기
3. 관심 세션 8-12개 선택
4. 배경 자료 생성 요청

### 학회 2주 전
5. 배경 자료 1차 읽기
6. 질문 리스트 검토 및 개인화

### 학회 1주 전
7. 사전 읽기 논문 다운로드
8. 네트워킹 타겟 명확화
9. Elevator pitch 준비

### 학회 D-1
10. 체크리스트 최종 확인
11. 명함/노트북 준비

### 학회 당일
12. 체크리스트 따라가기
13. 실시간 메모

### 학회 후 1주일
14. Follow-up 이메일 (템플릿 사용)
15. 논문 읽기
16. 학습 성과 자가 평가

---

## 💡 FAQ

### Q: 다른 분야 학회도 가능한가요?

**A**: 가능합니다! 현재는 microbiology/life sciences에 최적화되어 있지만:
- Config만 수정하면 어떤 학회든 가능
- 템플릿은 범용적 (9개 섹션)
- 연구 분야만 `research_areas`에 명시

예: 컴퓨터공학 학회
```yaml
research_areas:
  - "Machine Learning"
  - "Computer Vision"
  - "NLP"
```

### Q: 여러 사람이 동시에 사용 가능한가요?

**A**: 가능합니다!
- 각자 자신의 `conferences/[ID]/` 디렉토리 사용
- Git 충돌 없음 (다른 파일)
- Config도 독립적 (다른 YAML 파일)

### Q: 생성된 자료를 수정해도 되나요?

**A**: 당연합니다!
- 생성 후 자유롭게 편집 가능
- 개인 메모 추가 권장
- 질문 리스트 개인화 권장

### Q: Skill을 업데이트하려면?

**A**:
```bash
# 배포자가 업데이트
git add .claude/skills/conference-advisor/
git commit -m "Update conference-advisor to v2.1"
git push

# 팀원
git pull origin master
# 자동으로 최신 버전 사용!
```

---

## 📞 지원

문제가 생기면:
1. 이 가이드의 트러블슈팅 섹션 확인
2. 기존 예시 (MSK2025, IAMRT2025) 참고
3. `.claude/skills/conference-advisor/README.md` 참고
4. Claude Code 대화창에서 직접 질문

---

**Version**: 2.0
**Last Updated**: 2025-11-07
**Skill Author**: [Your Name/Team]
**Tested With**: Claude Code (2025 version)

**Quality Guarantee**: 모든 팀원이 동일한 고품질 학회 준비 자료를 생성할 수 있습니다! 🎉
