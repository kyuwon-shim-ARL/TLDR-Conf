# Due Diligence Skills Suite

협업 파트너, 개인 연구자, 연구실 검증을 위한 skill 세트입니다.

---

## 사용 가능한 Skills

### 1. 회사/기관 검증

| Skill | 언어 | 용도 |
|-------|------|------|
| `collaborator-check` | 한글 | 회사, 스타트업, 연구기관 검증 |
| `collaborator-check-en` | English | Company, startup, institution verification |

**적합한 상황:**
- 스타트업과의 협업 제안 검토
- 기업 파트너십 검토
- 투자/지분참여 검토
- 기술이전 대상 평가

---

### 2. 개인 연구자 검증

| Skill | 언어 | 용도 |
|-------|------|------|
| `researcher-check` | 한글 | 개인 연구자 학술 역량 검증 |
| `researcher-check-en` | English | Individual researcher verification |

**적합한 상황:**
- 공동연구자 선정
- 자문위원/심사위원 위촉
- 연사 초청
- 채용/초빙 검토

**검증 항목:**
- 학력/경력 진위
- h-index, 인용수
- 연구비 수주 이력
- 제자 배출 현황
- Retraction 이력

---

### 3. 연구실(랩) 검증

| Skill | 언어 | 용도 |
|-------|------|------|
| `lab-check` | 한글 | 연구실 종합 역량 분석 |
| `lab-check-en` | English | Research lab capability analysis |

**적합한 상황:**
- 대학원 진학 고려
- 포닥 지원 고려
- 랩간 공동연구
- 기관간 MOU

**검증 항목:**
- PI 배경 + 랩 구성원
- 연구 프로그램/장비
- 졸업생 진로
- 연구비/재정 현황
- 랩 문화/평판

---

## 출력 파일 구조

```
[프로젝트]/collaborations/
├── [회사명]/                           # 회사/기관
│   ├── research_report_YYYY-MM-DD.md      # 한글
│   └── research_report_YYYY-MM-DD_EN.md   # 영문
│
├── researchers/                         # 개인 연구자
│   ├── [이름]_profile_YYYY-MM-DD.md       # 한글
│   └── [이름]_profile_YYYY-MM-DD_EN.md    # 영문
│
└── labs/                                # 연구실
    ├── [PI명]_lab_YYYY-MM-DD.md           # 한글
    └── [PI명]_lab_YYYY-MM-DD_EN.md        # 영문
```

---

## 빠른 사용 예시

### 회사 검증
```
"Omphalos 회사 뒷조사 해줘"
→ collaborator-check 실행
```

### 연구자 검증
```
"Daehwan Kim 교수 프로필 분석해줘"
→ researcher-check 실행
```

### 랩 검증
```
"Kim Lab 연구실 분석해줘"
→ lab-check 실행
```

---

## 공통 검증 원칙

1. **교차 검증**: 여러 소스에서 확인
2. **출처 명시**: 모든 정보에 Reference
3. **Red Flags**: 위험 신호 명시적 표시
4. **주장 vs 사실**: 검증 상태 구분 표시

---

## Skill 위치

```
.claude/skills/
├── collaborator-check/      # 회사 - 한글
├── collaborator-check-en/   # 회사 - 영문
├── researcher-check/        # 연구자 - 한글
├── researcher-check-en/     # 연구자 - 영문
├── lab-check/               # 랩 - 한글
└── lab-check-en/            # 랩 - 영문
```

---

**Version**: 1.0
**Created**: 2025-12-15
**Total Skills**: 6개 (3종류 x 2언어)
