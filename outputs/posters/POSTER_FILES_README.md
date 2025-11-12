# 📂 포스터 자료 파일 구조 (최종 업데이트: 2025-10-26)

## 🌟 추천 사용 파일 (단 1개!)

### ✅ **POSTER_MECE_classification.md** ← 이것만 보세요! (v2 - 개선판)

**특징**:
- 478개 포스터를 8개 주제로 MECE 분류
- **파싱 성공률 87.9%** (420개) - v1 대비 +115개 향상
- 파싱 실패 11.5% (55개) 명확히 표시
- Session/Zone 정보로 동선 최적화
- 매칭 키워드로 관련성 즉시 확인
- 한눈에 스캔 가능한 테이블 형식

**분류 체계**:
1. 🦠 항생제 내성 (AMR) - 48개
2. 🔬 병원성 메커니즘 - 31개
3. 🧬 마이크로바이옴 - 72개
4. 🧪 유전 및 대사 - 48개
5. 🏭 응용 미생물 - 49개
6. 🌍 생태 및 환경 - 129개
7. 📊 분류 및 신종 - 45개
8. 🔧 방법론 및 기타 - 32개

**데이터 품질**:
- ✅ 정상 제목: 420개 (87.9%)
- ⚠️ 파싱 실패: 55개 (11.5%) - "⚠️ 제목 미파싱" 표시, PDF 직접 확인 필요

---

## 📋 참고 자료 (선택)

### POSTER_HOW_TO_USE.md
- 포스터 세션 전반적인 사용 방법
- 카테고리별 설명
- 실전 팁과 체크리스트

### POSTER_SMART_GUIDE.md
- SESSION_POSTER_connections 및 TOPIC_TOP10_recommendations 사용 가이드
- 두 가지 접근법 비교

---

## ⚠️ 더 이상 사용하지 않는 파일들 (Deprecated)

아래 파일들은 초기 버전으로, **이제 사용하지 않습니다**:

### ❌ 카테고리별 상세 파일 (8개)
- `POSTER_Category_A_Systematics.md`
- `POSTER_Category_B_Ecology.md`
- `POSTER_Category_C_Applied.md`
- `POSTER_Category_D_Pathogenesis.md`
- `POSTER_Category_E_Physiology.md`
- `POSTER_Category_F_Genetics.md`
- `POSTER_Category_G_Biotechnology.md`
- `POSTER_Category_H_Others.md`

**문제점**: 제목/저자/소속 파싱 오류율 47.4%, PDF 검색과 차별성 없음

### ❌ 검색 인덱스
- `POSTER_searchable_index.md`

**문제점**: PDF 직접 검색과 동일, 우선순위 정보 없음

### ❌ 점수 기반 추천
- `TOPIC_TOP10_recommendations.md`
- `topic_top_posters.json`

**문제점**: 키워드 가중치 주관적, 점수 산출 기준 불명확

### ❌ 세션-포스터 연결
- `SESSION_POSTER_connections.md`
- `session_poster_connections.json`

**문제점**: 유용하지만 파싱 품질 문제로 신뢰도 낮음

### ❌ 기타 자료
- `POSTER_database_overview.md` - 통계 정보 (참고용)
- `POSTER_navigation_guide.md` - 전략 가이드 (참고용)
- `parsed_posters.json` - 원본 파싱 데이터 (내부 사용)

---

## 🔄 변경 이력

### Version 3.1 (2025-10-26) - 현재 버전
**추가**:
- ✅ `POSTER_MECE_classification.md` (v2) - 개선된 파싱 적용
- ✅ `parsed_posters_v3.json` - 개선된 파싱 데이터

**개선점**:
- **파싱 로직 대폭 개선**: 71.6% → 87.9% (+16.3%p)
- 실패율 60% 감소: 28.4% → 11.5%
- 제목/저자 구분 정확도 향상
- "sp. nov." 제목과 저자 구분 개선
- 파싱 실패 케이스 명확히 표시 ("⚠️ 제목 미파싱")

### Version 3.0 (2025-10-26)
**추가**:
- ✅ `POSTER_MECE_classification.md` - MECE 기반 주제별 분류

**개선점**:
- 복잡한 파싱 제거 → 간단한 키워드 매칭
- 주관적 점수 제거 → 매칭 키워드 표시
- 14개 파일 → 1개 파일로 통합
- PDF 검색 대비 실질적 가치 추가

### Version 2.0 (2025-10-25) - Deprecated
**추가**:
- `SESSION_POSTER_connections.md`
- `TOPIC_TOP10_recommendations.md`

**문제**:
- 점수 산출 기준 불명확
- 파싱 품질 낮음 (47.4% 오류)

### Version 1.0 (2025-10-24) - Deprecated
**추가**:
- 8개 카테고리 파일
- 검색 인덱스

**문제**:
- PDF 검색과 차별성 없음
- 우선순위 정보 없음

---

## 💡 권장 워크플로우

### Step 1: 학회 3일 전
```bash
✅ POSTER_MECE_classification.md 열기
✅ 관심 주제 2-3개 선택
✅ 각 주제에서 10-15개 포스터 확인
✅ Session/Zone 확인 및 동선 계획
```

### Step 2: 학회 당일 아침
```bash
✅ 선정한 포스터 코드 리스트 출력
✅ 우선순위 Top 10 표시
✅ 명함 준비
```

### Step 3: 포스터 세션 중
```bash
✅ 우선순위 포스터부터 방문
✅ 각 포스터 5-10분 할애
✅ 명함 교환 및 네트워킹
```

---

## 🎯 파일 선택 가이드

### "AMR 연구하는데 어떤 포스터 봐야 해?"
→ **POSTER_MECE_classification.md** 열고 "🦠 항생제 내성 (AMR)" 섹션 확인

### "마이크로바이옴 관련 포스터 추천해줘"
→ **POSTER_MECE_classification.md** 열고 "🧬 마이크로바이옴" 섹션 확인

### "Session 1에서 볼 포스터 정리하고 싶어"
→ **POSTER_MECE_classification.md**에서 "Session 1 (10/26)" 필터링

### "전반적인 포스터 세션 전략이 궁금해"
→ **POSTER_HOW_TO_USE.md** 참고

### "PDF에서 직접 검색하고 싶어"
→ MSK2025-ebook.pdf 열고 Ctrl+F (하지만 우선순위 정보 없음)

---

## 📊 요약 비교

| 항목 | PDF 직접 검색 | 기존 파일들 (v1-v2) | **MECE 가이드 (v3)** |
|------|--------------|---------------------|---------------------|
| 우선순위 | ❌ 없음 | ⚠️ 주관적 점수 | ✅ 매칭 키워드 |
| 분류 체계 | ❌ 없음 | ⚠️ 카테고리만 | ✅ MECE 주제별 |
| Session/Zone | ⚠️ 별도 확인 필요 | ✅ 포함 | ✅ 포함 |
| 파싱 품질 | ✅ 완벽 (원본) | ❌ 47.4% 오류 | ✅ N/A (키워드만) |
| 파일 수 | 1개 (PDF) | 14개 | **1개** |
| 실용성 | ⚠️ 보통 | ❌ 낮음 | ✅ 높음 |

---

**결론**: **POSTER_MECE_classification.md 하나면 충분합니다!**

**작성일**: 2025-10-26
**작성자**: Conference Advisor (MSK2025 준비팀)
