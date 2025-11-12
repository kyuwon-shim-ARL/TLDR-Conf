# 노션 Import 가이드 | MSK2025 Conference Materials

## 📦 생성된 파일 목록

### 1. 노션용 핵심 파일 (우선 import)
- **`NOTION_sessions_database.csv`** - 세션 데이터베이스 (필터링/정렬 가능)
- **`NOTION_optimized_guide.md`** - 토글 구조 마스터 가이드
- **`QUICK_REFERENCE_mobile.md`** - 모바일 빠른 참조

### 2. 상세 Background 파일 (21개)
- `background_S1.md` ~ `background_S21.md`

---

## 🚀 노션 Import 방법

### Step 1: 세션 데이터베이스 생성

1. **노션에서 새 페이지 생성**
   - 페이지 이름: "MSK2025 세션 데이터베이스"

2. **데이터베이스 Import**
   ```
   페이지 내에서 /table-inline 입력
   → Import 선택
   → NOTION_sessions_database.csv 업로드
   ```

3. **속성(Property) 설정**

   Import 후 다음 속성을 조정하세요:

   | Property | Type | 설정 |
   |----------|------|------|
   | Session | Title | 기본 제목 필드 |
   | Title_KR | Text | - |
   | Title_EN | Text | - |
   | Date | Date | - |
   | Start_Time | Text | (또는 별도 Date로 시간 포함) |
   | End_Time | Text | - |
   | Room | Select | 옵션: Convention Hall 1, Rm 301+302, Rm 304+305, Rm 303, Rm 306 |
   | **Priority** | Number | ⭐ 중요! |
   | Duration | Text | - |
   | **Tags** | Multi-select | ⭐ 중요! 옵션 추가 필요 (아래 참조) |
   | Chair | Text | - |
   | Description | Text | - |

4. **Tags Multi-select 옵션 추가**

   Tags 컬럼 클릭 → Edit property → 다음 옵션 추가:
   ```
   Bacteriology
   Virology
   Mycology
   Microbiome
   Pathogenesis
   Diagnostics
   Therapeutics
   Vaccines
   Pandemic Preparedness
   Structural Biology
   Synthetic Biology
   Industrial
   Environmental
   Agricultural
   Clinical Translation
   Regulation
   ```

5. **뷰(View) 생성**

   데이터베이스 우측 상단 "View" 클릭:

   - **📅 Timeline by Date** (Calendar view)
     - Group by: Date
     - 시간대별 세션 한눈에 보기

   - **⭐ By Priority** (Table view)
     - Sort: Priority (Descending)
     - Filter: Priority ≥ 80
     - 필수 세션만 보기

   - **🏷️ By Research Area** (Board view)
     - Group by: Tags
     - 연구 분야별 카드 보기

   - **📍 By Room** (Table view)
     - Group by: Room
     - 장소별 정리

---

### Step 2: 마스터 가이드 Import

1. **노션에서 새 페이지 생성**
   - 페이지 이름: "MSK2025 마스터 가이드"

2. **마크다운 Import**
   ```
   페이지 설정 (⋯) → Import → Markdown
   → NOTION_optimized_guide.md 선택
   ```

3. **Import 후 수동 조정**

   노션 import 시 일부 서식이 깨질 수 있습니다:
   - [ ] Callout 박스 확인 (`>` 로 시작하는 부분)
   - [ ] 토글 블록 확인 (계층 구조)
   - [ ] 테이블 정렬 확인
   - [ ] 이모지 깨짐 확인

---

### Step 3: Background 파일 Import (선택사항)

**방법 A: 개별 페이지로 Import**
1. 각 세션마다 서브페이지 생성
2. `background_S##.md` 파일을 각각 import

**방법 B: 데이터베이스 연결 (추천)**
1. Step 1의 세션 데이터베이스 사용
2. 각 세션 row 클릭 → 페이지 열기
3. 해당 세션의 `background_S##.md` 내용 복사/붙여넣기
4. 토글 블록으로 구조화:
   ```
   ▼ Overview
   ▼ Speaker 1: [이름]
      - Key Research
      - Why This Matters
   ▼ Speaker 2: [이름]
   ▼ Background Concepts
   ▼ Networking Tips
   ```

---

### Step 4: 모바일 빠른 참조

1. **노션 모바일 앱에서 접근하기 쉽게 설정**

   - 페이지 생성: "MSK2025 현장용"
   - `QUICK_REFERENCE_mobile.md` import
   - ⭐ Favorite 추가 (노션 모바일 앱에서 빠른 접근)

2. **오프라인 접근 설정**

   노션 모바일 앱:
   - 페이지 열기
   - 설정 → "Make available offline" 활성화
   - 학회장에서 인터넷 없이도 접근 가능!

---

## 🎨 노션 최적화 팁

### 1. 데이터베이스 활용법

**필터 조합 예시:**

- **내 필수 세션만 보기**
  ```
  Priority ≥ 80
  AND Tags contains "Bacteriology"
  ```

- **Day 2 오전 세션만**
  ```
  Date = 2025-10-27
  AND Start_Time = "09:00"
  ```

- **장소별 정렬**
  ```
  Group by: Room
  Sort by: Start_Time
  ```

### 2. 토글 활용 (마스터 가이드)

Import 후 긴 내용을 토글로 접으면 훨씬 깔끔:

```
▼ Day 1: Oct 26
  ▼ 13:30-15:30
    ▼ S1: Bacterial Pathogenesis
       [상세 내용...]
    ▼ S2: Diet-Microbiome
       [상세 내용...]
```

### 3. Callout으로 중요 정보 강조

```
💡 Quick Pick
선택 기준 설명...

⚠️ 주의사항
기업 발표 많음 등...

✨ 최우선 세션
꼭 들어야 할 세션
```

### 4. 링크 연결

데이터베이스와 마스터 가이드를 연결:

- 마스터 가이드에서 세션 언급 시 → 데이터베이스 row에 링크
- 세션 데이터베이스 각 row → background 페이지에 링크

---

## 📱 모바일 사용 최적화

### 노션 앱 설정

1. **Favorite 설정**
   - "MSK2025 현장용" 페이지
   - "세션 데이터베이스" (Priority ≥ 80 필터 뷰)

2. **위젯 추가 (iOS/Android)**
   - 홈 화면에 노션 위젯
   - "MSK2025 현장용" 선택
   - 학회장에서 빠른 접근

3. **오프라인 모드**
   - 모든 페이지를 미리 열어서 캐시
   - "Make available offline" 설정

---

## 🔄 Import 문제 해결

### 문제 1: CSV 한글 깨짐
**해결**:
- Excel에서 열지 말고 직접 노션에 import
- 또는 CSV를 UTF-8로 저장 확인

### 문제 2: 마크다운 테이블 깨짐
**해결**:
- Import 후 테이블 부분 수동 재구성
- 또는 `/table` 명령어로 새로 생성 후 복사/붙여넣기

### 문제 3: 토글 구조 안 보임
**해결**:
- Import 후 수동으로 토글 블록 생성
- 내용 선택 → 드래그로 토글 블록 안으로 이동

### 문제 4: 이모지가 네모로 표시됨
**해결**:
- 노션에서 기본 이모지로 교체
- 또는 그대로 두어도 내용 이해에는 문제 없음

---

## ✅ Import 완료 체크리스트

- [ ] 세션 데이터베이스 CSV import 완료
- [ ] Priority 컬럼이 Number 타입으로 설정됨
- [ ] Tags 컬럼이 Multi-select로 설정됨
- [ ] 4가지 뷰 생성 완료 (Timeline, Priority, Tags, Room)
- [ ] 마스터 가이드 import 완료
- [ ] Callout 박스 정상 표시 확인
- [ ] 모바일 빠른 참조 import 완료
- [ ] Favorite 설정 완료
- [ ] 오프라인 모드 활성화
- [ ] (선택) Background 파일 연결 완료

---

## 💡 활용 시나리오

### 학회 전 (Before Conference)
1. **데이터베이스 "By Priority" 뷰** 확인
2. Priority ≥ 80 세션의 background 읽기
3. 네트워킹 타겟 연사 체크
4. 일정 충돌 시 마스터 가이드 의사결정 트리 참조

### 학회 중 (During Conference)
1. **모바일 "현장용 빠른 참조"** 활용
2. 실시간 세션 선택 시 Priority 점수 확인
3. 시간대별 섹션으로 빠른 의사결정

### 학회 후 (After Conference)
1. 놓친 세션 데이터베이스에서 필터링
2. Background 파일로 보충 학습
3. 발표자 연락처 정리 (데이터베이스에 컬럼 추가)

---

## 🎯 추가 커스터마이징

### 유용한 속성 추가 제안

데이터베이스에 다음 컬럼 추가 가능:

| 속성 이름 | Type | 용도 |
|----------|------|------|
| Attended | Checkbox | 실제 참석 여부 체크 |
| Notes | Text | 현장 메모 |
| Rating | Select | 참석 후 평가 (⭐⭐⭐⭐⭐) |
| Contacts | Text | 만난 연사/참석자 |
| Follow-up | Checkbox | 후속 연락 필요 여부 |
| Slides_Link | URL | 발표 자료 링크 |

### 템플릿 버튼 만들기

"Add Session Notes" 버튼 생성:
```
Template:
---
✅ Attended: [ ]
⭐ Rating:

📝 Key Takeaways:
-
-

🤝 People Met:
-

📧 Follow-up Actions:
-
---
```

---

**이제 노션에서 MSK2025 학회를 완벽하게 준비하고 관리할 수 있습니다!** 🎉

문제가 있으면 이 가이드를 참조하거나, 노션 커뮤니티에서 도움을 받으세요.
