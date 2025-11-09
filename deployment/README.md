# Deployment Directory

이 디렉토리는 **conference-advisor skill**을 팀원들에게 배포하기 위한 패키지를 생성하고 관리합니다.

## 📁 구조

```
deployment/
├── README.md                          # 이 파일
├── create_deployment_package.sh       # 배포 패키지 생성 스크립트
└── packages/                          # 생성된 패키지들
    ├── conference-advisor-skill-minimal.tar.gz    # 최소 패키지 (16K)
    ├── conference-advisor-skill-full.tar.gz       # 전체 패키지 (396K)
    ├── TEAM_DEPLOYMENT_GUIDE.md                   # 팀원 사용 가이드
    └── MANIFEST.md                                # 패키지 설명
```

## 🚀 사용법

### 1. 배포 패키지 생성

```bash
cd deployment
./create_deployment_package.sh
```

이 스크립트는 자동으로:
- ✅ Minimal 패키지 생성 (skill + templates + configs)
- ✅ Full 패키지 생성 (skill + examples)
- ✅ Deployment guide 복사
- ✅ Manifest 생성

### 2. 팀원에게 배포

**방법 A: Git으로 배포 (권장)**
```bash
# 프로젝트 루트로 이동
cd ..

# Skill과 conferences 추가
git add .claude/skills/conference-advisor/
git add conferences/
git add TEAM_DEPLOYMENT_GUIDE.md

# 커밋
git commit -m "Add conference-advisor skill v2.0

- Multi-conference support
- Comprehensive background generation (1000-2000 lines)
- Clean data structure
- See TEAM_DEPLOYMENT_GUIDE.md for usage

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>"

# Push
git push origin master

# 팀원은 git pull만 하면 됨!
```

**방법 B: 파일 전송**
```bash
# 패키지 선택
cd packages/

# 이메일/클라우드/USB로 전송:
# - conference-advisor-skill-minimal.tar.gz (처음 사용자)
# - conference-advisor-skill-full.tar.gz (예시 필요한 사용자)
# - TEAM_DEPLOYMENT_GUIDE.md (필수!)
```

### 3. 팀원 사용 확인

**설치 후 확인**:
```bash
# 팀원의 프로젝트에서
ls .claude/skills/conference-advisor/SKILL.md

# Claude Code에서
/conference-advisor
```

## 📦 패키지 설명

### Minimal Package (16K)

**포함**:
- SKILL.md (필수!)
- Templates (3개)
- Config examples (MSK2025.yml, IAMRT2025.yml)
- _template/ (새 학회 추가용)
- README

**추천 대상**:
- 자신의 학회 데이터만 사용할 팀원
- 깨끗한 시작을 원하는 경우

### Full Package (396K)

**포함**:
- Minimal package 전체
- MSK2025 examples (31 background files)
- IAMRT2025 examples (4 background files)
- Conference READMEs

**추천 대상**:
- 예시를 보고 싶은 팀원
- 품질 기준을 확인하고 싶은 경우
- 학습 목적

## 🎯 팀원에게 전달할 메시지 템플릿

### 이메일 예시

```
제목: [공유] Conference-Advisor Skill - 학회 준비 자동화

안녕하세요,

학회 준비를 자동화하는 Claude Code skill을 만들었습니다!

🎯 기능:
- 학회 세션 분석 및 추천
- 세션별 상세 배경 자료 생성 (1000-2000줄)
- 개인 맞춤 학회 계획 생성
- 네트워킹 전략, 질문 리스트 등 포함

📦 첨부 파일:
1. conference-advisor-skill-minimal.tar.gz - Skill 패키지
2. TEAM_DEPLOYMENT_GUIDE.md - 사용 설명서

🚀 설치 방법:
1. 프로젝트 디렉토리에서 tar -xzf conference-advisor-skill-minimal.tar.gz
2. Claude Code 실행 후 /conference-advisor 입력
3. 끝!

상세 사용법은 TEAM_DEPLOYMENT_GUIDE.md를 참고하세요.

질문 있으시면 언제든 연락주세요!
```

### Slack/Teams 예시

```
📢 Conference-Advisor Skill 공유합니다!

학회 준비를 10배 빠르게 할 수 있는 Claude Code skill입니다.

✨ 주요 기능:
• 세션 자동 분석 & 추천
• 1000-2000줄 수준의 배경 자료 생성
• 맞춤 학회 계획 (네트워킹 전략 포함)

📥 설치:
Git 사용자: `git pull` (이미 커밋됨)
비Git 사용자: 첨부 파일 다운로드 → 압축 해제

📖 사용법: TEAM_DEPLOYMENT_GUIDE.md 참고

🎓 이미 MSK2025, IAMRT2025에서 검증됨
   (총 35개 세션, 52,674줄 생성)

궁금한 점 있으시면 댓글로!
```

## 🔄 업데이트 프로세스

### Skill 업데이트 시

```bash
# 1. 패키지 재생성
cd deployment
./create_deployment_package.sh

# 2. Git으로 배포
cd ..
git add .claude/skills/conference-advisor/
git commit -m "Update conference-advisor to v2.1"
git push

# 팀원은 git pull만 하면 자동 업데이트!
```

### 버전 관리

```bash
# 태그 생성 (권장)
git tag -a conference-advisor-v2.0 -m "Conference-Advisor Skill v2.0

Features:
- Multi-conference support
- Comprehensive backgrounds (1000-2000 lines)
- Clean data structure"

git push origin conference-advisor-v2.0
```

## 📊 배포 현황 추적

### 체크리스트

배포 시 확인 사항:
- [ ] 패키지 생성 완료 (`./create_deployment_package.sh`)
- [ ] 패키지 테스트 완료 (압축 해제 → SKILL.md 확인)
- [ ] TEAM_DEPLOYMENT_GUIDE.md 최신 버전
- [ ] Git 커밋 (또는 파일 전송)
- [ ] 팀원에게 공지
- [ ] 팀원 설치 확인 (최소 1명)

### 팀원 사용 현황

| 팀원 | 설치일 | 버전 | 사용 학회 | 상태 |
|------|--------|------|-----------|------|
| [이름] | YYYY-MM-DD | v2.0 | [학회명] | ✅ |
| [이름] | YYYY-MM-DD | v2.0 | [학회명] | ✅ |

## 🐛 일반적인 문제

### Q: 팀원이 "skill을 찾을 수 없다"고 합니다

**확인**:
```bash
# 팀원의 프로젝트에서
ls .claude/skills/conference-advisor/SKILL.md
```

**없으면**: 패키지 설치 안 됨
```bash
# 다시 설치
tar -xzf conference-advisor-skill-minimal.tar.gz
```

### Q: 팀원의 프로젝트 구조가 다릅니다

**해결**: Skill은 프로젝트 루트 기준 상대 경로 사용
```bash
# 프로젝트 루트에서 압축 해제해야 함
cd /path/to/project/root
tar -xzf conference-advisor-skill-minimal.tar.gz

# 확인
ls .claude/skills/conference-advisor/SKILL.md
```

### Q: Config 경로가 안 맞습니다

**원인**: Config 파일의 경로는 프로젝트 루트 기준

**해결**: 팀원이 자신의 프로젝트 구조에 맞게 config 수정
```yaml
# 예: 프로젝트 루트가 다른 경우
source_files:
  program: "conferences/NEWCONF2025/raw/program.pdf"  # 항상 루트 기준
```

## 📚 관련 문서

- **Skill 문서**: `../claude/skills/conference-advisor/README.md`
- **팀원 가이드**: `packages/TEAM_DEPLOYMENT_GUIDE.md`
- **패키지 설명**: `packages/MANIFEST.md`
- **전체 데이터**: `../conferences/README.md`

## 🎓 Best Practices

1. **버전 관리**: Git 태그로 버전 추적
2. **테스트**: 배포 전 /tmp에서 설치 테스트
3. **문서화**: 업데이트마다 CHANGELOG 유지
4. **피드백**: 팀원 사용 경험 수집
5. **개선**: 피드백 반영하여 지속 개선

## 📞 지원

문제 발생 시:
1. `TEAM_DEPLOYMENT_GUIDE.md` 트러블슈팅 섹션 확인
2. 기존 예시 참고 (MSK2025, IAMRT2025)
3. 재생성: `./create_deployment_package.sh`

---

**Deployment System Version**: 1.0
**Last Updated**: 2025-11-07
**Skill Version**: 2.0
