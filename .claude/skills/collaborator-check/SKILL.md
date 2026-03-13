---
name: collaborator-check
description: 협업 파트너(회사/연구기관/연구자) 검증 및 Due Diligence 보고서 생성. 창업자 배경검증, 기술평가, 펀딩현황, 경쟁사 분석 등 종합 조사 (한글 버전) (project)
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

# Collaborator Check Skill v1.0
## 협업 파트너 검증 및 Due Diligence 보고서 생성

협업 제안, 파트너십, 투자 검토 시 상대방에 대한 객관적인 배경조사를 수행하고 표준화된 보고서를 생성하는 skill입니다.

---

## 🎯 주요 기능

1. **회사/기관 기본정보 조사**
2. **창업자/핵심인력 배경 검증**
3. **기술 수준 객관적 평가**
4. **펀딩/재무 상태 확인**
5. **경쟁사 비교 분석**
6. **Red Flags 탐지**
7. **종합 Due Diligence 보고서 생성**

---

## 📋 워크플로우

### Step 1: 초기화 및 정보 수집

**사용자에게 질문:**
```
협업 파트너 검증을 시작합니다.

1. 조사 대상은 무엇인가요?
   - 회사/스타트업
   - 연구기관/대학 랩
   - 개인 연구자
   - 기타

2. 조사 대상의 이름/회사명:

3. 관련 자료가 있나요? (선택)
   - PDF 파일 경로
   - 웹사이트 URL
   - 없음 (웹 검색만 진행)

4. 어떤 목적의 협업인가요?
   - 공동연구/학술협력
   - 기술이전/라이선싱
   - 투자/지분참여
   - 프로젝트 위탁/용역
   - 기타
```

### Step 2: 기본정보 조사

**WebSearch 쿼리 실행:**
```
- "[회사명] company profile"
- "[회사명] founding team background"
- "[회사명] Crunchbase OR LinkedIn"
- "[회사명] funding investment"
- "[회사명] technology platform"
```

**수집할 정보:**
| 항목 | 내용 |
|------|------|
| 회사명 | 정식 법인명, 영문명 |
| 설립일 | 연도, 법인등록 여부 |
| 본사 위치 | 국가, 도시 |
| 웹사이트 | 공식 URL |
| 직원 수 | 규모 추정 |
| 사업 분야 | 핵심 기술/서비스 |

### Step 3: 창업자/핵심인력 검증

**각 핵심인력에 대해:**

```
WebSearch 실행:
- "[이름] [전공] PhD dissertation"
- "[이름] Google Scholar citations"
- "[이름] LinkedIn profile"
- "[이름] publications research"
- "[이름] [이전 소속기관]"
```

**검증 항목:**
| 주장 | 검증방법 | 결과 |
|------|----------|------|
| 학력 | 대학 웹사이트, 학위논문 DB | ✓/✗/? |
| 경력 | LinkedIn, 기관 웹사이트 | ✓/✗/? |
| 인용수 | Google Scholar | 실제 숫자 |
| 대표 논문 | PubMed, Google Scholar | 존재 여부 |
| 수상/특허 | 특허청, 학회 웹사이트 | 존재 여부 |

**평가 기준:**
- **검증됨**: 공신력 있는 출처에서 확인
- **미검증**: 확인 불가 (주장만 존재)
- **불일치**: 주장과 실제가 다름 (⚠️ Red Flag)

### Step 4: 기술 수준 평가

**평가 매트릭스:**

| 항목 | 평가 기준 | 점수 |
|------|-----------|------|
| 학술 검증 | Peer-reviewed 논문 수 | 상/중/하 |
| 기술 차별성 | 경쟁사 대비 독창성 | 상/중/하 |
| 시장 타이밍 | 해당 분야 성숙도 | 상/중/하 |
| 실제 구현 | 프로토타입/제품 존재 | 상/중/하 |
| IP 보유 | 특허/영업비밀 | 상/중/하 |

**WebSearch 쿼리:**
```
- "[기술명] peer-reviewed publications"
- "[기술명] patent search"
- "[기술명] competitors comparison"
- "[기술명] market size [연도]"
- "[기술명] vs [경쟁기술] benchmark"
```

### Step 5: 펀딩/재무 상태 조사

**정보원:**
- Crunchbase
- CB Insights
- PitchBook (유료)
- 공시자료 (상장사)
- 뉴스 기사

**수집 정보:**
| 항목 | 내용 |
|------|------|
| 펀딩 단계 | Seed/Series A/B/C... |
| 총 투자유치 | 금액 (공개된 경우) |
| 최근 라운드 | 일시, 금액, 투자자 |
| 투자자 명단 | VC, 엔젤, 전략적 투자자 |
| 기업가치 | 밸류에이션 (추정) |
| 재무상태 | 수익성, 런웨이 |

### Step 6: 경쟁사 분석

**경쟁 환경 매핑:**
```
| 회사/기관 | 접근법 | 자원 규모 | 현황 | 강점 | 약점 |
|-----------|--------|-----------|------|------|------|
| [조사대상] | ... | ... | ... | ... | ... |
| [경쟁사1] | ... | ... | ... | ... | ... |
| [경쟁사2] | ... | ... | ... | ... | ... |
| [경쟁사3] | ... | ... | ... | ... | ... |
```

**WebSearch 쿼리:**
```
- "[분야] leading companies startups"
- "[분야] market landscape [연도]"
- "[조사대상] vs [경쟁사] comparison"
- "[분야] industry report"
```

### Step 7: Red Flags 탐지

**자동 체크 항목:**

| 카테고리 | Red Flag | 심각도 |
|----------|----------|--------|
| **경력** | 검증 불가능한 학력/경력 | 🔴 높음 |
| **경력** | 빈번한 직장 이동 (< 1년) | 🟡 중간 |
| **기술** | Peer-reviewed 논문 없이 "혁신" 주장 | 🟡 중간 |
| **기술** | 과장된 성능 주장 (검증 데이터 없음) | 🔴 높음 |
| **재무** | 펀딩 정보 비공개 (규모 대비) | 🟡 중간 |
| **재무** | 빈번한 피봇/사업모델 변경 | 🟡 중간 |
| **법적** | 소송/법적 분쟁 이력 | 🔴 높음 |
| **평판** | 부정적 뉴스/리뷰 | 🟡 중간 |
| **투명성** | 팀/연락처 정보 부재 | 🔴 높음 |

**WebSearch 쿼리:**
```
- "[회사명] lawsuit legal issues"
- "[회사명] controversy scandal"
- "[창업자명] fraud allegations"
- "[회사명] reviews complaints"
- "[회사명] former employee reviews"
```

---

## 📝 보고서 템플릿

### 파일명 규칙
```
collaborations/[회사명]/research_report_[YYYY-MM-DD].md
```

### 보고서 구조

```markdown
# [회사/기관명] 협업 미팅 사전 조사 보고서

> **작성일:** YYYY-MM-DD
> **관련 미팅:** [미팅 제목]
> **원본 자료:** [경로 또는 URL]

---

## 1. 회사 개요
[표 형식 기본정보]

## 2. 경영진 배경 검증
[각 핵심인력별 상세 검증 결과]
- 주장 vs 실제 비교표
- Google Scholar 인용수 검증
- 주요 업적 확인

## 3. 핵심 기술 - 쉬운말 풀이
[비전문가도 이해할 수 있는 기술 설명]
- 한 줄 요약
- 쉬운 비유
- 작동 원리
- 차별점

## 4. 프로젝트/제품 분석
[구체적인 프로젝트/제품 평가]
- 타겟 시장
- 예산/일정
- 예상 결과물

## 5. 경쟁 환경 분석
[경쟁사 비교 매트릭스]
- 주요 플레이어
- 조사대상의 포지셔닝
- 차별점 및 리스크

## 6. 펀딩/재무 상태
[공개된 재무 정보]
- 펀딩 이력
- 투자자
- 추정 런웨이

## 7. 객관적 수준 평가
### 강점
[표 형식]

### 약점/불확실성
[표 형식]

### Red Flags
[발견된 위험 신호]

## 8. 미팅 시 확인할 질문
### 기술 관련
[5-10개 질문]

### 비즈니스 관련
[5개 질문]

### 협업 관련
[3-5개 질문]

## 9. 핵심 용어 정리
[표 형식 - 쉬운 설명]

## 10. 요약 (Executive Summary)
[3-4 문단 요약]
- 조사 대상 소개
- 핵심 기술/사업
- 검증 결과
- 협업 시 주의점

## References
[출처 목록 - 하이퍼링크]
```

---

## 🔄 실행 워크플로우

### 사용자 호출 시
```
1. 조사 대상 정보 수집 (대화형)
2. PDF/URL 제공 시 먼저 읽기
3. WebSearch 병렬 실행 (회사, 인력, 기술, 펀딩)
4. 결과 종합 및 검증
5. Red Flags 체크
6. 보고서 생성
7. 파일 저장 위치 확인 후 저장
```

### 출력물
1. **표준 보고서**: `research_report_[날짜].md` (한글)
2. **영문 보고서**: `research_report_[날짜]_EN.md` (선택)

---

## ⚙️ 설정

### 언어
- **기본**: 한글
- **영문 버전**: `collaborator-check-en` skill 사용

### 저장 위치
```
[프로젝트]/collaborations/[회사명-소문자-하이픈]/
```

### 품질 기준
- **최소 분량**: 500줄 이상
- **필수 섹션**: 10개 전체
- **검증 항목**: 모든 주장에 대해 검증 시도
- **출처 명시**: 모든 정보에 Reference 링크

---

## 🚨 주의사항

- **ALWAYS** 주장과 실제를 구분하여 명시
- **ALWAYS** 검증 불가능한 정보는 "미검증"으로 표시
- **ALWAYS** Red Flags 섹션 포함 (없으면 "없음"으로 명시)
- **NEVER** 검증 없이 긍정적 평가만 작성
- **NEVER** 출처 없는 정보 포함
- **NEVER** 대외비 자료 내용을 보고서 외부에 공유

---

## 📊 성공 지표

✅ 핵심인력 배경 100% 검증 시도
✅ 기술/제품 쉬운말 풀이 포함
✅ 경쟁사 3개 이상 비교
✅ Red Flags 체크리스트 완료
✅ 미팅용 질문 15개 이상
✅ 모든 출처 하이퍼링크 포함

---

**Version**: 1.0
**Last Updated**: 2025-12-15
**Author**: MSK2025 Project
