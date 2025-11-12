# 📊 노션에서 포스터 데이터베이스 활용 가이드

**파일**: `POSTER_MECE_notion.csv`
**포스터 수**: 454개 (분류된 포스터)
**최종 업데이트**: 2025-10-26

---

## 🚀 노션 임포트 방법 (단계별)

### Step 1: CSV 다운로드
- 파일: `POSTER_MECE_notion.csv`
- 위치: `/home/kyuwon/projects/MSK2025/`

### Step 2: 노션에서 데이터베이스 생성

1. **노션 페이지 열기**
2. `/table` 입력 → "Table - Full page" 선택
3. 우측 상단 `···` 메뉴 클릭
4. **"Merge with CSV"** 선택
5. `POSTER_MECE_notion.csv` 업로드
6. 컬럼 매핑 확인 후 **Import**

### Step 3: 데이터베이스 설정

**컬럼 타입 변경** (추천):
- `Code`: **Title** (제목으로 설정)
- `Main_Category`: **Select** (단일 선택)
- `Sub_Category`: **Select** (단일 선택)
- `Session`: **Select**
- `Zone`: **Select**
- `Parsing_Status`: **Select**
- `Title`, `Authors`, `Affiliation`: **Text** (기본값)
- `Keywords_Matched`: **Multi-select** (선택사항)

---

## 🎯 노션 데이터베이스 활용법

### 1️⃣ 필터 활용

#### 예시 1: AMR 연구자
```
필터 추가:
- Main_Category = 🦠 항생제 내성 (AMR)
- Session = Session 1 (10/26)
- Sub_Category = Carbapenem-resistant

결과: 카바페넴 내성 포스터 9개
```

#### 예시 2: 마이크로바이옴 - Gut만
```
필터 추가:
- Main_Category = 🧬 마이크로바이옴
- Sub_Category = Gut microbiome

결과: 장내 마이크로바이옴 28개
```

#### 예시 3: Session 1만 보기
```
필터 추가:
- Session = Session 1 (10/26)

결과: 10/26 포스터만 표시
```

### 2️⃣ 정렬 활용

**추천 정렬**:
1. Main_Category (오름차순)
2. Sub_Category (오름차순)
3. Zone (오름차순)

**동선 최적화 정렬**:
1. Session (오름차순)
2. Zone (오름차순)
3. Code (오름차순)

### 3️⃣ 뷰(View) 생성

**추천 뷰 4가지**:

#### View 1: 전체 보기
- 필터: 없음
- 정렬: Main_Category → Sub_Category
- 용도: 전체 포스터 브라우징

#### View 2: Session 1 (10/26 일요일)
- 필터: Session = Session 1 (10/26)
- 정렬: Zone → Code
- 용도: 일요일 포스터 세션 준비

#### View 3: Session 2 (10/27 월요일)
- 필터: Session = Session 2 (10/27)
- 정렬: Zone → Code
- 용도: 월요일 포스터 세션 준비

#### View 4: 내 관심 분야 (예: AMR)
- 필터: Main_Category = 🦠 항생제 내성 (AMR)
- 정렬: Sub_Category → Zone
- 용도: AMR 포스터만 집중

---

## 📋 데이터베이스 컬럼 설명

| 컬럼 | 설명 | 예시 |
|------|------|------|
| **Code** | 포스터 코드 | D001, B045 |
| **Main_Category** | 주 카테고리 (8개) | 🦠 AMR, 🧬 마이크로바이옴 |
| **Sub_Category** | 서브 카테고리 | Gut microbiome, Marine/Ocean |
| **Title** | 포스터 제목 (전체) | Flavobacterium rhizosalinus... |
| **Authors** | 저자 | Kim A, Lee B, and Park C* |
| **Affiliation** | 소속 기관 | Seoul National University |
| **Session** | 세션 날짜/시간 | Session 1 (10/26) |
| **Zone** | 물리적 위치 | Zone 2, Zone 3 |
| **Keywords_Matched** | 매칭된 키워드 | gut, microbiome, diversity |
| **Parsing_Status** | 파싱 성공 여부 | Success / Failed |

---

## 🎨 세분화된 카테고리 구조

### 🌍 생태 및 환경 (129개)
- **Marine/Ocean** (55개) - 해양, 바다, 연안
- **Soil** (25개) - 토양, 근권
- **Freshwater** (16개) - 담수, 호수, 강
- **Extreme environments** (4개) - 극한 환경, 온천, 극지
- **Others** (29개) - 기타

### 🧬 마이크로바이옴 (72개)
- **Gut microbiome** (28개) - 장내 마이크로바이옴
- **Oral microbiome** (8개) - 구강 마이크로바이옴
- **Skin microbiome** (5개) - 피부 마이크로바이옴
- **Disease-associated** (5개) - 질환 관련
- **Others** (26개) - 기타

### 🏭 응용 미생물 (49개)
- **Industrial production** (22개) - 산업 생산, 효소, 바이오연료
- **Fermentation/Food** (14개) - 발효, 김치, 유산균
- **Bioremediation** (7개) - 환경 정화, 분해
- **Diagnostics** (5개) - 진단, 센서
- **Others** (1개) - 기타

### 🦠 항생제 내성 (AMR) (48개)
- **Others** (20개) - 일반 내성
- **Novel strategies** (13개) - 신규 전략 (파지, 펩타이드)
- **Carbapenem-resistant** (9개) - 카바페넴 내성
- **Resistance mechanisms** (4개) - 내성 메커니즘
- **MRSA/VRE** (2개) - 특정 균주

### 기타 카테고리
- 🔬 병원성 메커니즘 (31개) - 서브카테고리 없음
- 🧪 유전 및 대사 (48개) - 서브카테고리 없음
- 📊 분류 및 신종 (45개) - 서브카테고리 없음
- 🔧 방법론 및 기타 (32개) - 서브카테고리 없음

---

## 💡 실전 활용 시나리오

### 시나리오 1: "AMR 연구하는데 카바페넴 내성만 보고 싶어"

**노션에서**:
1. 필터 추가: Main_Category = 🦠 AMR
2. 필터 추가: Sub_Category = Carbapenem-resistant
3. 결과: 9개 포스터
4. Zone별로 정렬해서 동선 계획

**장점**: PDF에서 "carbapenem" 검색하면 50개 나오는데, 여기선 정말 핵심 9개만!

### 시나리오 2: "해양 미생물 연구자"

**노션에서**:
1. 필터: Main_Category = 🌍 생태 및 환경
2. 필터: Sub_Category = Marine/Ocean
3. 결과: 55개 포스터
4. Session별로 정렬
5. 10-15개 선정

**장점**: 55개를 Session 1/2로 나눠서 계획 가능

### 시나리오 3: "장내 마이크로바이옴 + 질환"

**노션에서**:
1. View 복제
2. 필터: Main_Category = 🧬 마이크로바이옴
3. 필터: Sub_Category = Gut microbiome OR Disease-associated
4. 결과: 33개 (28 + 5)
5. Keywords_Matched 확인해서 관심 키워드 찾기

**장점**: 다중 서브카테고리 필터 가능!

### 시나리오 4: "Session 1 당일 아침 최종 점검"

**노션에서**:
1. 필터: Session = Session 1 (10/26)
2. 정렬: Zone → Code
3. 내가 체크한 포스터만 보기 (체크박스 속성 추가)
4. 프린트하거나 모바일에서 확인

**장점**: 동선 순서대로 정렬되어 효율적!

---

## 🔥 노션 고급 팁

### Tip 1: 체크박스 컬럼 추가
- 컬럼 추가: "방문 예정" (Checkbox)
- 관심 포스터에 체크
- 필터: "방문 예정 = Checked"
- 나만의 맞춤 리스트!

### Tip 2: 메모 컬럼 추가
- 컬럼 추가: "내 메모" (Text)
- 왜 이 포스터가 관심있는지 메모
- 현장에서 질문할 내용 미리 작성

### Tip 3: 우선순위 추가
- 컬럼 추가: "우선순위" (Select)
- 옵션: ⭐⭐⭐ High, ⭐⭐ Medium, ⭐ Low
- 정렬: 우선순위 → Zone

### Tip 4: 보드 뷰 활용
- 뷰 추가: Board (칸반)
- Group by: Sub_Category
- 서브카테고리별로 카드처럼 보기
- 드래그앤드롭으로 우선순위 조정

### Tip 5: 타임라인 뷰
- 뷰 추가: Timeline
- 세션 시간을 타임라인으로 시각화
- 시간대별 계획 수립

---

## 📱 모바일 활용

### 노션 모바일 앱에서
1. 동일한 데이터베이스 접근
2. 필터/정렬 그대로 적용
3. 현장에서 체크박스 체크
4. 메모 실시간 추가
5. 오프라인에서도 접근 가능 (사전 로드 필요)

---

## 🎯 학회 전 준비 체크리스트

### 3일 전
- [ ] CSV를 노션에 임포트
- [ ] Main_Category, Sub_Category 컬럼 타입 설정
- [ ] "방문 예정", "우선순위", "내 메모" 컬럼 추가
- [ ] 관심 분야 필터 뷰 생성 (2-3개)

### 2일 전
- [ ] 관심 포스터 30-40개 체크
- [ ] Sub_Category 필터로 세부 분야 확인
- [ ] 우선순위 설정 (High 10개, Medium 15개)
- [ ] 각 포스터에 메모 추가 (왜 관심있는지)

### 1일 전
- [ ] Session 1/2 뷰로 날짜별 계획
- [ ] Zone 순서대로 정렬
- [ ] 최종 10-15개로 압축
- [ ] 질문 리스트 작성

### 당일 아침
- [ ] 모바일 노션 앱 확인
- [ ] 오프라인 접근 테스트
- [ ] 우선순위 Top 10 재확인

### 포스터 세션 중
- [ ] 방문한 포스터 체크박스 해제
- [ ] 인상 깊었던 포스터에 메모 추가
- [ ] 명함 교환한 포스터 표시

---

## 🌟 노션 vs PDF 비교

| 기능 | PDF 검색 | 노션 데이터베이스 |
|------|---------|-----------------|
| 키워드 검색 | ✅ 가능 | ✅ 더 강력 |
| 필터링 | ❌ 불가 | ✅ 다중 필터 |
| 정렬 | ❌ 불가 | ✅ 자유로운 정렬 |
| 서브카테고리 | ❌ 없음 | ✅ 4개 세분화 |
| 체크리스트 | ❌ 불가 | ✅ 체크박스 |
| 메모 | ❌ 어려움 | ✅ 컬럼 추가 |
| 우선순위 | ❌ 불가 | ✅ 우선순위 설정 |
| 모바일 | ⚠️ 불편 | ✅ 노션 앱 |
| 협업 | ❌ 불가 | ✅ 공유/협업 |
| 시각화 | ❌ 없음 | ✅ 보드/타임라인 |

---

## ❓ FAQ

### Q1: CSV 임포트 시 한글이 깨져요
**A**: UTF-8 with BOM 인코딩 사용. 이미 적용되어 있습니다. 여전히 문제시 구글 시트에서 열어서 노션으로 복사.

### Q2: 파싱 실패 포스터는 어떻게 확인하나요?
**A**: Parsing_Status = Failed 필터. 해당 포스터는 PDF에서 코드로 직접 검색.

### Q3: 서브카테고리가 "Others"인 것들은?
**A**: 키워드로 세부 분류 안 된 포스터. 제목 보고 수동 분류 가능.

### Q4: 내가 체크한 포스터만 CSV로 다시 내보낼 수 있나요?
**A**: 노션에서 필터 적용 후 우측 상단 `···` → Export → CSV

### Q5: 동료와 공유하고 싶어요
**A**: 노션 페이지 Share 버튼 → 링크 공유 or 특정 사용자 초대

---

## 🎉 결론

**노션 데이터베이스를 활용하면**:
- 426개 → 필터로 10-15개로 압축
- 서브카테고리로 정밀 탐색
- 체크리스트로 진행 상황 관리
- 모바일에서 현장 활용
- PDF보다 **10배 효율적**

---

**생성일**: 2025-10-26
**파일**: POSTER_MECE_notion.csv
**포스터 수**: 454개
**주 카테고리**: 8개
**서브카테고리**: 4개 카테고리 세분화

**Happy Conference! 🎊**
