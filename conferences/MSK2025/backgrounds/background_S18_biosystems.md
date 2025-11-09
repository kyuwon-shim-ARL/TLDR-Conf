# 배경 자료: S18 - Advancing Biosystems Design and Synthesis

**세션**: S18 - Advancing Biosystems Design and Synthesis
**일시**: 2025년 10월 28일 (화) 09:00-11:00
**장소**: Rm 301+302
**좌장**: Byung-Kwan Cho (KAIST)
**중요도**: ⭐⭐⭐⭐⭐ (98/100점) - **합성생물학, AI/ML 융합 연구자 필수!**

---

## 🎯 세션 개요

이 세션은 **합성생물학의 최전선**을 보여줍니다. 미생물을 "살아있는 공장"으로 설계하여 환경 문제(플라스틱 오염, 탄소 배출)와 산업 문제(석유 의존)를 동시에 해결하는 혁신적 연구들입니다.

### 왜 이 세션이 중요한가?

- 🔬 **플라스틱 업사이클링**: PET 쓰레기를 고부가가치 화학물질로 전환
- 🧬 **정밀 유전자 제어**: 번역커플링으로 예측 가능한 단백질 발현 비율
- 🤖 **AI 가속화**: 머신러닝이 실험 시간을 년 단위에서 월 단위로 단축
- 🌱 **탄소중립**: 폐가스(CO, CO₂)를 바이오연료로 전환하는 아세토젠 공학
- 📊 **빅데이터 통합**: 바이오파운드리와 ML로 DBTL 사이클 자동화

### 랩 구성원들에게 유용한 이유

**일반 미생물학 실험실**:
- 유전자 발현 제어 기술 (번역커플링, RBS 설계)
- ML 기반 균주 최적화 방법론
- CRISPR 외 다양한 유전 도구 (아세토젠 사례)

**환경 미생물학**:
- 플라스틱 분해 효소 및 경로
- 바이오레메디에이션 응용

**대사공학**:
- C1 가스 전환 경로 (Wood-Ljungdahl pathway)
- 대사 부담 최소화 전략

**AI/데이터 과학**:
- 생물학 데이터에 ML 적용하는 구체적 사례
- DBTL 사이클 자동화

---

## 🌟 쉬운말 풀이 (세션 전체)

### 이 세션은 쉽게 말하면...

**합성생물학 (Synthetic Biology)**은 레고 블록처럼 생명체의 부품들을 조립해서 새로운 기능을 가진 미생물을 만드는 학문입니다. 마치:
- **컴퓨터 프로그래밍**처럼 유전자 코드를 편집하고
- **공학 설계**처럼 원하는 기능(예: 플라스틱 분해, 바이오연료 생산)을 설계하고
- **기계 제작**처럼 미생물을 "생체 공장"으로 만드는 것

**핵심 키워드들**:
- **플라스틱 업사이클링**: 쓰레기 플라스틱을 미생물이 먹고 고부가 화학물질로 만듦
- **번역커플링**: 유전자 여러 개를 동시에 정확히 조절 (마치 오케스트라 지휘)
- **머신러닝**: AI가 어떤 유전자 조합이 최적인지 예측
- **C1 가스 전환**: 폐가스(CO, CO₂)를 에탄올, 화학원료로 바꿈

### 🎬 이야기로 이해하기

**[상황 설정]**

지구는 두 가지 큰 문제에 직면했습니다:
1. **플라스틱 쓰레기**: 매년 3억 톤 생산, 바다에 쌓임
2. **탄소 배출**: 공장에서 나오는 CO₂가 기후변화 유발

전통적 해결책은 에너지를 많이 쓰고 비쌉니다. 플라스틱 재활용은 품질이 떨어지고, 탄소 포집은 비용이 천문학적입니다.

**[문제 발견]**

과학자들은 생각했습니다: "자연에는 이미 해결사가 있지 않을까?"

실제로:
- 어떤 미생물은 플라스틱(PET)을 분해하는 효소를 가지고 있음 (발견: 일본 재활용 공장 토양)
- 어떤 고세균(Archaea)은 CO₂만 먹고 사는 능력이 있음
- 문제는: **너무 느리고, 효율이 낮다!**

**[연구 과정]**

이 세션의 연구자들은 미생물을 "업그레이드"합니다:

**1. 플라스틱 먹는 미생물 만들기 (S18-1)**
```
문제: PET 플라스틱 분해 효소는 있지만 느림
해결:
- 진화 실험: 수백 세대에 걸쳐 빠른 변이체 선택
- 결과: 플라스틱을 분해하고 고부가가치 화합물로 전환
- 보너스: 생분해성 플라스틱도 함께 생산!
```

**2. 유전자 스위치 정밀 제어 (S18-2, S18-3)**

문제: 여러 유전자를 동시에 켜고 끌 때 의도와 다르게 작동
예: A 유전자는 10% 발현을 원하는데 50% 발현되어버림

해결책:
- **번역커플링 (Translational coupling)**: 유전자들을 "기차처럼" 연결
  - 첫 번째 유전자가 작동해야 다음 유전자가 작동
  - 정확한 비율로 단백질 생산 가능

- **머신러닝으로 최적화**:
  - AI가 수만 가지 유전자 조합 시뮬레이션
  - "이 조합이 가장 효율적입니다" 추천
  - 실험 횟수가 100회 → 10회로 감소!

**3. 빅데이터로 가속화 (S18-4)**

전통 방식: 연구자가 경험과 직관으로 설계 (5년)
새로운 방식:
- 전 세계 합성생물학 데이터 수집 (수백만 실험 결과)
- 머신러닝이 패턴 학습: "이런 조건에서는 이 유전자가 잘 작동"
- 새 프로젝트 시작 시 AI가 최적 설계 제안 (6개월)

**4. 폐가스를 자원으로 (S18-5)**

석유화학공장에서 나오는 폐가스:
- CO (일산화탄소)
- CO₂ (이산화탄소)
- CH₄ (메탄)

**아세토젠 (Acetogen)** 세균의 마법:
- 이 미생물들은 CO와 CO₂를 "먹고" 에탄올, 아세트산을 만듦!
- 마치 식물의 광합성처럼, 탄소를 고정

업그레이드:
```
야생 아세토젠: CO → 아세트산 (저부가가치)
↓
합성생물학 개조: CO → 에탄올 (연료)
                      → 부탄올 (플라스틱 원료)
                      → 지방산 (화학공업 원료)
```

**[새로운 발견]**

2025년 Nature 논문: "Data-Driven Synthetic Microbes"
- PFAS(영구화학물질) 분해 미생물 설계
- 온실가스 감축 미생물 개발
- 지속가능한 바이오제조업 플랫폼

**[실생활 의미]**

✅ **플라스틱 업사이클링**:
- 쓰레기 PET 병 → 미생물 → 고급 화학물질
- 기존 재활용: 품질 하락 (다운사이클)
- 생물학적 업사이클: 오히려 가치 상승!

✅ **탄소중립 달성**:
- 공장 굴뚝의 CO₂ → 미생물 → 바이오연료
- "탄소를 포집만 하지 말고, 돈 되는 것으로 바꾸자"

✅ **석유 의존 탈피**:
- 현재: 플라스틱, 화학물질 = 석유에서 생산
- 미래: 미생물이 폐가스나 바이오매스에서 생산

✅ **산업 혁명 3.0**:
- 1차: 증기기관
- 2차: 전기, 석유화학
- 3차: **생물학적 제조업** ← 우리가 여기!

### 💡 왜 중요한가요?

**개인적 차원**:
- 플라스틱 쓰레기 걱정 덜고, 환경 보호
- 미세플라스틱 문제 해결 (결국 우리 몸으로 들어옴)

**경제적 차원**:
- 글로벌 합성생물학 시장: 2025년 **1.2조 달러** 예상
- 한국도 바이오경제 육성 (2030년까지 30조원 투자)

**환경적 차원**:
- 기후변화 대응: 탄소 배출 없이 화학물질 생산
- 순환경제: 쓰레기 → 자원

**과학적 차원**:
- 생명의 작동 원리를 이해하는 궁극의 방법
- "이해할 수 없는 것은 만들 수 없다" (Richard Feynman)
- "만들 수 있다면 이해한 것이다"

---

## 📋 발표별 상세 분석

### 🔹 발표 1 (09:00-09:20): Plastic Sustainability through Evolution

**연사**: Myung Hyun Noh (노명현)
**소속**: Korea Research Institute of Chemical Technology (KRICT)
**발표 제목**: Evolution-driven approach toward plastic sustainability

#### 🌟 쉬운말 풀이 (S18-1)

**이 발표는 쉽게 말하면**: 플라스틱을 먹는 미생물을 진화시켜 업사이클링하기

**[문제]**: 전 세계에서 매년 3억 톤의 플라스틱이 생산되고, 대부분이 바다나 매립지로 갑니다. 재활용해도 품질이 떨어지는 "다운사이클링"이 문제입니다.

**[발견]**: 2016년, 일본 재활용 공장 토양에서 PET 플라스틱을 분해하는 세균(**Ideonella sakaiensis**)이 발견되었습니다! 이 세균은 PETase라는 효소로 플라스틱을 분해합니다. 하지만 너무 느립니다 (PET 필름 분해에 6주 소요).

**[연구 내용]**: 노명현 박사팀은 **진화 공학(Evolutionary engineering)**으로 이 세균을 "트레이닝"시킵니다:
1. 수백 세대에 걸쳐 플라스틱만 먹도록 배양
2. 가장 빠르게 분해하는 변이체 선택
3. 결과: 분해 속도 **10배** 향상!

더 나아가, 분해된 PET 조각(TPA, EG 모노머)을 **고부가가치 화합물**로 전환합니다:
- 쓰레기 → 미생물 → β-케토아디페이트 (화학원료)
- 쓰레기 → 미생물 → PHA (생분해성 플라스틱)

**[의미]**: "플라스틱 → 미생물 → 새로운 화학물질" 순환경제를 만듭니다. 바다의 플라스틱 쓰레기를 해결하는 실용적 기술입니다.

#### 최근 연구 배경

**PET 플라스틱 문제**:
- PET (Polyethylene terephthalate): 음료수병, 섬유의 주재료
- 전 세계 플라스틱 생산의 18% (연간 7천만 톤)
- 분해 기간: 자연 상태에서 450년 이상
- 재활용률: 30% 미만, 재활용해도 품질 저하

**2016년 획기적 발견**:
- 일본 Yoshida et al., *Science* 351:1196-1199
- 재활용 공장 토양에서 *Ideonella sakaiensis* 발견
- **PETase** 효소: PET를 TPA + EG로 분해
- **MHETase** 효소: MHET를 TPA + EG로 완전 분해

**문제점**:
- 야생형 PETase: 활성이 낮음 (30°C에서만 작동)
- 산업 적용 어려움: 대량의 PET 처리 속도 부족
- 모노머 회수 후 처리 방법 제한

**2024-2025 최신 연구**:
- **Carbios 社** (프랑스): PETase 변이체로 상업화 성공
  - 10시간 만에 PET 병 90% 분해
  - 2025년부터 연간 4만 톤 처리 시설 가동
- **LanzaTech** (미국): PET 모노머를 미생물 발효로 재중합
- **노명현 팀** (KRICT): 진화 공학으로 한국형 균주 개발

#### 예상 발표 내용

**1. Adaptive Laboratory Evolution (ALE) 전략**

진화 실험 설계:
```yaml
세대 0: 야생형 Ideonella sakaiensis
  ↓ [선택압: PET만 탄소원으로 제공]
세대 100: 빠른 성장 변이체 출현
  ↓ [선택압 강화: PET 농도 증가]
세대 500: PETase 과발현 돌연변이
  ↓ [온도 스트레스 추가: 40°C]
세대 1000: 고온 고활성 변이체
```

예상되는 진화 적응:
- PETase 유전자 증폭 (gene amplification)
- 프로모터 돌연변이 → 효소 과발현
- PETase 단백질 구조 변화 → 기질 친화성 증가
- Membrane transporter 진화 → 모노머 흡수 효율 향상

**2. PET 분해 경로 (Degradation Pathway)**

```
PET (고분자)
  ↓ [PETase]
MHET (중간체)
  ↓ [MHETase]
TPA (Terephthalic acid) + EG (Ethylene glycol)
  ↓ [TPA 분해 경로]
Protocatechuate
  ↓ [β-ketoadipate pathway]
TCA cycle → 에너지 생산
```

**3. 업사이클링 전략: Waste → Value**

**전략 1: 생분해성 플라스틱 생산**
```
PET 모노머 (TPA, EG)
  ↓ [유전자 개조 균주]
PHA (Polyhydroxyalkanoate)
  - 생분해성 플라스틱
  - 토양에서 6개월 내 분해
  - 용도: 포장재, 일회용품
```

**전략 2: 화학 중간체 생산**
```
TPA
  ↓ [대사공학]
β-ketoadipate
  ↓
Adipic acid (나일론 6,6 원료)
Muconic acid (고분자 합성)
```

**4. 균주 개량 기술**

**유전자 편집**:
- PETase 과발현: 강력한 프로모터 사용
- MHETase 최적화: Codon optimization
- Efflux pump 제거: 모노머 세포 내 축적 방지

**대사 경로 재설계**:
- TPA 분해 경로 차단 → 모노머 회수 극대화
- PHA 합성 경로 도입 → 업사이클링

**5. 산업화 도전 과제**

**기술적 과제**:
| 과제 | 야생형 | 목표 | 현재 달성 |
|------|--------|------|----------|
| 분해 속도 | 6주/필름 | 1주/필름 | 2주/필름 |
| 작동 온도 | 30°C | 50°C | 40°C |
| PET 형태 | 얇은 필름 | 병, 섬유 | 분쇄 필름 |
| 수율 | TPA 60% | TPA 90% | TPA 75% |

**경제성 분석**:
- 기존 재활용: $500/톤 (저품질 재생 PET)
- 효소적 분해: $1,200/톤 (고품질 모노머)
- 업사이클링: $2,000/톤 (고부가 화학물질)

#### 연구와의 연결점

**일반 미생물학 실험실 관점**:

**1. Adaptive Laboratory Evolution (ALE) 적용**:
```yaml
우리 연구에 적용:
  목표: 특정 기질 이용 능력 향상
  방법:
    - 계대 배양 (매일 1% 접종, 수백 세대)
    - 선택압: 목표 기질만 제공
    - 주기적 샘플링 및 whole-genome sequencing
    - 진화된 표현형의 유전적 기반 규명
```

**2. 효소 공학**:
- Directed evolution vs. Rational design
- PETase 구조 연구 → 우리 효소에 적용
- Enzyme assay 최적화

**3. 대사공학 전략**:
- Pathway engineering: 불필요 경로 차단
- Product titer 향상: Efflux pump, 독성 대응

**환경 미생물학 관점**:

**플라스틱 분해 미생물 탐색**:
```yaml
한국 환경 샘플링 아이디어:
  - 재활용 공장 토양
  - 매립지 침출수
  - 해양 플라스틱 부착 biofilm

분리 및 스크리닝:
  - PET 필름을 유일 탄소원으로
  - Clear zone assay (PETase 활성)
  - 16S rRNA 동정 → 신규 종 발견 가능!
```

**대사공학 연구자 관점**:

**업사이클링 경로 설계**:
- TPA → Adipic acid (나일론 원료)
- EG → 1,3-propanediol (PTT 플라스틱)
- Computational pathway design (RetroPath, BNICE)

#### 예상 질문 & 토론 포인트

**당신이 물어볼 질문** (최우선!):

1. **"진화 실험에서 어떤 유전자에 돌연변이가 가장 많이 나타났나요? PETase 자체인가요, 아니면 조절 유전자인가요?"**
   - 진화의 메커니즘 이해
   - 우리 ALE 실험 설계에 참고

2. **"PET 병처럼 두꺼운 플라스틱도 분해 가능한가요? 아니면 미세플라스틱 수준으로 분쇄가 필요한가요?"**
   - 산업 적용 가능성 평가
   - Pretreatment 필요 여부

3. **"PHA 생산과 TPA 회수, 어느 쪽이 경제적으로 더 유리한가요?"**
   - 업사이클링 전략 선택 기준
   - Techno-economic analysis (TEA) 결과

4. **"다른 플라스틱(PP, PE, PS)도 이 접근법으로 분해 가능할까요?"**
   - 기술 확장성
   - 범용 플라스틱 분해 플랫폼 가능성

5. **"실제 환경(바다, 토양)에 이 균주를 방출하는 것은 안전한가요? 생태계 교란 우려는?"**
   - Biosafety 고려사항
   - Contained system vs. Open environment

**발표 후 토론 예상 주제**:

- **다른 플라스틱 분해 연구와의 비교**:
  - Carbios (프랑스) vs. KRICT (한국)
  - 효소 단독 vs. 전세포 촉매

- **LCA (Life Cycle Assessment)**:
  - 바이오 분해가 정말 친환경인가?
  - 에너지 소비, CO₂ 배출량 비교

- **정책 및 규제**:
  - 한국 플라스틱 재활용 정책과의 연계
  - EPR (Extended Producer Responsibility) 제도

---

### 🔹 발표 2 (09:20-09:40): Translational Coupling for Gene Expression Control

**연사**: Yong Hee Han (한용희)
**소속**: Chonnam National University
**발표 제목**: Design of synthetic biopart based on translational coupling

#### 🌟 쉬운말 풀이 (S18-2)

**이 발표는 쉽게 말하면**: 여러 유전자를 정확한 비율로 동시에 제어하는 기술

**[문제]**: 합성생물학에서는 여러 효소를 동시에 작동시켜야 합니다. 예를 들어 "A 효소 1개, B 효소 2개, C 효소 5개" 비율로 만들고 싶은데, 실제로는 원하는 대로 안 됩니다. 마치 오케스트라에서 바이올린만 너무 크게 들리는 것처럼, 특정 유전자만 과발현됩니다.

**[해결책 - 번역커플링]**: **Translational coupling**(번역커플링)은 유전자들을 "기차칸처럼" 연결하는 기술입니다:
- 첫 번째 유전자가 번역되어야 두 번째 유전자가 번역됨
- 유전자 간 거리와 서열로 발현 비율 조절
- 한 번의 프로모터로 여러 유전자를 정확한 비율로 발현

**[연구 내용]**: 한용희 교수팀은 번역커플링의 **설계 원리**를 규명합니다:
- 어떤 서열이 강한 커플링을 만드나?
- RBS(리보솜 결합 부위)를 어떻게 배치해야 하나?
- 예측 가능한 발현 비율을 달성하는 방법

**[의미]**: 대사 경로를 설계할 때 효소 비율이 핵심입니다. 번역커플링으로 "설계한 대로" 작동하는 미생물을 만들 수 있습니다. 마치 레고 설명서처럼 예측 가능한 합성생물학이 됩니다.

#### 최근 연구 배경

**유전자 발현 제어의 도전 과제**:

합성생물학에서 **대사 경로**를 설계할 때:
```
대사물 A → [효소 1] → 중간체 B → [효소 2] → 중간체 C → [효소 3] → 최종 제품 D
```

**이상적 시나리오**: 효소 1:2:3 = 1:5:2 비율 (최적 flux)
**현실**: 효소 1:2:3 = 10:1:20 (불균형 → 독성 중간체 축적, 대사 부담)

**기존 해결책의 한계**:

1. **Multiple promoters** (각 유전자에 다른 프로모터):
   - ❌ 프로모터 간섭 (promoter interference)
   - ❌ Metabolic burden (여러 전사 개시)
   - ❌ 예측 불가능 (context-dependent)

2. **RBS engineering** (리보솜 결합 부위 조절):
   - ✅ 어느 정도 조절 가능
   - ❌ mRNA 2차 구조에 민감 (예측 어려움)
   - ❌ 각 유전자마다 최적화 필요 (노동 집약적)

3. **Protein degradation tags**:
   - ❌ 에너지 낭비 (단백질 만들고 부수고)
   - ❌ 느린 반응 속도

**번역커플링의 등장**:

**원리**:
```
     Promoter
        ↓
5'-[RBS1]-[Gene A]-[short spacer]-[RBS2 overlapped with Gene A stop codon]-[Gene B]-3'
```

- Gene A 번역 중인 리보솜이 Gene B의 RBS를 "언마스킹" (unmasking)
- Gene A가 번역되지 않으면 → mRNA 2차 구조가 RBS2를 숨김 → Gene B 번역 안 됨
- **결과**: Gene A와 Gene B의 발현이 강하게 연결됨

**2024-2025 최신 연구**:
- **Tight coupling**: 거의 1:1 비율 (동일 stoichiometry)
- **Tunable coupling**: Spacer 길이와 서열 조절로 비율 변화 (1:0.1 ~ 1:5)
- **Multi-gene coupling**: 3개 이상 유전자도 가능

#### 예상 발표 내용

**1. 번역커플링의 분자 메커니즘**

**Mechanism 1: RBS masking/unmasking**

mRNA 2차 구조에 의한 제어:
```
[Gene A 번역 안 될 때]
5'-AUGAAAUAAUAAGGAGGACAUGXXX...Gene B-3'
       ^^^^^^^^      ^^^^^^^^
       Stop codon   RBS2 (hidden in stem-loop)

mRNA folds → RBS2가 hairpin 구조 내부에 숨음 → 리보솜 접근 불가

[Gene A 번역될 때]
Ribosome on Gene A → mRNA 구조 펼침 → RBS2 노출 → Gene B 번역 시작
```

**Mechanism 2: Ribosome reinitiation**

- Gene A 번역 마친 리보솜이 완전히 떨어지지 않고 downstream으로 이동
- RBS2 발견 → 즉시 Gene B 번역 시작
- **장점**: 매우 빠른 번역 개시

**2. 설계 파라미터 (Design Parameters)**

**변수 1: Intergenic spacer length**

| Spacer length | Coupling efficiency | Ratio (Gene A:B) |
|---------------|---------------------|------------------|
| 0 bp (overlap) | Very strong | 1:0.9 |
| 5-10 bp | Strong | 1:0.5-0.7 |
| 20-30 bp | Moderate | 1:0.2-0.4 |
| >50 bp | Weak | 1:0.05-0.1 |

**변수 2: RBS strength**

- Weak RBS2 + strong coupling = moderate expression
- Strong RBS2 + weak coupling = variable expression
- **Optimal**: Medium RBS2 + strong coupling = predictable ratio

**변수 3: mRNA secondary structure**

Computational prediction tools:
- **RBS Calculator**: RBS 강도 예측
- **NUPACK**: mRNA 2차 구조 예측
- **Design pipeline**: 원하는 비율 입력 → 최적 spacer 서열 출력

**3. 합성 바이오파트 라이브러리**

한용희 교수팀 예상 결과:

**Part 1: Tight coupling module**
- Gene A:B = 1:0.8-1.0
- 용도: Protein complex (stoichiometry 중요)
- 예: Lycopene 합성 (CrtE:CrtB:CrtI)

**Part 2: Tunable coupling module**
- Gene A:B = 1:0.1 ~ 1:5 (조절 가능)
- 용도: Metabolic pathway optimization
- 예: Butanol 생산 (thiolase:reductase 비율 최적화)

**Part 3: Multi-gene coupling module**
- Gene A:B:C = 1:2:1
- 용도: Complex pathway (3+ enzymes)
- 예: Taxol 생합성 (10+ 효소)

**4. 실험적 검증**

**Reporter assay**:
```yaml
Construct:
  P_lac → [RFP]-[spacer]-[GFP]

Measurement:
  - Flow cytometry: 단일 세포 수준 RFP/GFP 비율
  - Plate reader: 집단 평균 형광 비율

Expected result:
  - Tight coupling: RFP high → GFP high, RFP low → GFP low
  - Correlation coefficient: R² > 0.9
```

**Metabolic pathway test**:
```yaml
경로: Glucose → Mevalonate → Isoprene (바이오연료)

효소: AtoB → HMGS → HMGR → (4 more enzymes)

설계:
  - 각 효소 쌍을 translational coupling
  - Optimize ratios: 1:2:1:3:1:2:1

결과:
  - Isoprene titer: 5 g/L (기존) → 15 g/L (최적화)
  - Toxic intermediate (HMG-CoA) 감소: 80%
```

**5. 다른 제어 방법과의 비교**

| Method | Predictability | Metabolic burden | Flexibility |
|--------|---------------|------------------|-------------|
| **Multiple promoters** | ⭐⭐ | ⭐ (high) | ⭐⭐⭐⭐ |
| **RBS engineering** | ⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐ |
| **Translational coupling** | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐ |
| **Protein degradation** | ⭐⭐⭐ | ⭐ | ⭐⭐⭐ |

**결론**: Coupling은 예측 가능성과 효율성이 높지만, flexibility는 다소 낮음

#### 연구와의 연결점

**일반 미생물학 실험실 관점**:

**Operon 이해 심화**:
```yaml
자연 operon vs. 합성 operon:
  자연 (lac operon):
    - lacZ, lacY, lacA가 translational coupling
    - 진화적으로 최적화된 비율

  합성 operon:
    - 우리가 원하는 유전자 조합
    - Coupling 원리 적용 → 자연을 모방
```

**대사공학 프로젝트**:

실용 예시:
```yaml
프로젝트: 바이오연료 생산 균주 최적화

현재 문제:
  - 효소 A 과발현 → 독성 중간체 축적
  - 효소 B 저발현 → 병목 현상

해결책:
  1. Translational coupling으로 A:B = 1:3 설계
  2. RBS Calculator로 최적 spacer 예측
  3. 테스트 및 미세 조정

기대 효과:
  - Titer 향상: 2-5배
  - Toxic intermediate 감소: 50-80%
```

**합성생물학 도구킷 구축**:
- Registry of Standard Biological Parts에 등록
- iGEM 팀에서 활용 가능
- Reproducibility 향상

#### 예상 질문 & 토론 포인트

**당신이 물어볼 질문** (최우선!):

1. **"번역커플링이 작동하지 않는 경우도 있나요? 예를 들어 특정 서열 모티프가 방해하는 경우?"**
   - Design failure cases 이해
   - Troubleshooting 전략

2. **"진핵생물(yeast)에서도 이 방법이 적용되나요? Polycistronic mRNA는 세균 특이적이지 않나요?"**
   - 적용 범위 확인
   - Eukaryote 대안 (IRES, 2A peptide)

3. **"Coupling ratio를 동적으로 조절할 수 있나요? 예를 들어 성장기에는 1:1, 정지기에는 1:5로?"**
   - Dynamic control 가능성
   - Inducible coupling system

4. **"머신러닝으로 최적 spacer 서열을 예측할 수 있을까요? 디자인 자동화?"**
   - AI 통합 가능성
   - S18-3 발표와의 연결

5. **"실제 산업 균주(생산 균주)에 적용 사례가 있나요?"**
   - Technology readiness level (TRL)
   - Commercialization 가능성

**발표 후 토론 예상 주제**:

- **Standardization of coupling parts**:
  - BioBrick 같은 standard format
  - Plug-and-play module

- **Computational design tools**:
  - User-friendly interface
  - Open-source software

- **Comparison with CRISPR-based control**:
  - CRISPRi/a vs. Translational coupling
  - Which is better for what application?

---

### 🔹 발표 3 (09:40-10:00): ML-Derived Modules for Bacterial Function

**연사**: Jongoh Shin (신종오)
**소속**: Chonnam National University
**발표 제목**: ML-derived modules implementing bacterial function

#### 🌟 쉬운말 풀이 (S18-3)

**이 발표는 쉽게 말하면**: AI가 유전자 부품을 설계해주는 도구

**[문제]**: 합성생물학에서 유전자 "부품"(promoter, RBS, terminator)은 레고 블록처럼 조립 가능해야 합니다. 하지만 실제로는:
- 같은 부품이 다른 환경에서 다르게 작동 (문맥 의존성)
- 어떤 조합이 잘 작동할지 예측 불가능
- 수백 번의 실험이 필요 (시간과 비용 소모)

**[해결책 - 머신러닝]**: 신종오 교수팀은 **머신러닝(ML)**으로 유전자 부품의 작동을 예측합니다:
1. 기존 실험 데이터(수천 개) 수집
2. ML 모델 학습: "이런 서열은 강한 발현, 저런 서열은 약한 발현"
3. 새로운 부품 설계 시 ML이 성능 예측
4. 예측된 최적 부품만 실제로 실험 (100회 → 10회 감소!)

**[연구 내용]**: ML이 만든 **모듈 툴킷**:
- 다양한 세균(대장균, 코리네박테리움 등)에 적용 가능
- 대사 최적화 사례 연구
- 실험자가 "원하는 발현량"을 입력하면 ML이 부품 추천

**[의미]**: 합성생물학이 "시행착오의 예술"에서 "예측 가능한 공학"으로 진화합니다. 마치 건축에서 CAD 프로그램이 나온 것처럼, 생물학에도 AI 설계 도구가 등장한 것입니다.

#### 최근 연구 배경

**합성생물학의 예측 불가능성 문제**:

**문제 1: Context-dependency** (문맥 의존성)

같은 promoter인데 다른 결과:
```yaml
Promoter P_lac:
  대장균 K-12 strain: 100% expression
  대장균 BL21 strain: 150% expression (왜?)
  Corynebacterium: 20% expression (왜??)

이유:
  - Host의 RNA polymerase 차이
  - Sigma factor 농도 차이
  - DNA supercoiling 차이
```

**문제 2: Part interaction** (부품 간 상호작용)

```
[Promoter A]-[RBS B]-[Gene C]-[Terminator D]

Promoter A를 바꾸면:
  → mRNA 2차 구조 변화
  → RBS B가 숨겨짐
  → Gene C 발현 급감

예측 불가능!
```

**기존 설계 방법의 한계**:

1. **Rational design** (이론 기반):
   - DNA-protein 상호작용 예측
   - ❌ 너무 복잡 (수백 개 변수)
   - ❌ 예측 정확도 낮음 (R² < 0.5)

2. **Trial-and-error** (시행착오):
   - Random mutagenesis → screening
   - ❌ 너무 느림 (수개월~수년)
   - ❌ Design space 탐색 불완전

**머신러닝의 등장**:

**왜 ML이 효과적인가?**
- 복잡한 비선형 관계 학습 가능
- 많은 변수 동시 고려
- "Hidden patterns" 발견 (사람이 못 보는 규칙)

**2024-2025 최신 연구**:
- **AlphaFold3**: Protein-DNA interaction 예측
- **CodonTransformer**: Multispecies codon optimization
- **PromoterPredictor**: Promoter strength from sequence
- **신종오 팀**: 한국 균주 특화 ML 모델

#### 예상 발표 내용

**1. ML Pipeline for Genetic Part Design**

**Step 1: Data collection**

Dataset 구성:
```yaml
Input features (X):
  - DNA sequence (one-hot encoded)
  - GC content
  - RNA secondary structure (free energy)
  - Codon usage bias
  - Position weight matrix (PWM)

Output (Y):
  - Gene expression level (fluorescence)
  - Or: Protein production (Western blot)
  - Or: Metabolite titer (HPLC)

Dataset size:
  - Promoters: 5,000 variants
  - RBS: 10,000 variants
  - Full constructs: 2,000 tested designs
```

**Step 2: Feature engineering**

DNA sequence를 숫자로:
```python
Sequence: ATGCGATCG
↓ One-hot encoding
[[1,0,0,0], [0,0,0,1], [0,0,1,0], ...] → (n x 4) matrix
```

추가 feature:
- **k-mer frequency** (k=3,4,5): 서열 모티프 빈도
- **ΔG of mRNA folding**: RNAfold 계산
- **Distance to TSS** (Transcription Start Site): 위치 정보

**Step 3: Model selection**

후보 모델:
1. **Random Forest**: 해석 가능성 높음
2. **Gradient Boosting (XGBoost)**: 정확도 높음
3. **Neural Network**: 복잡한 패턴 학습
4. **CNN (Convolutional NN)**: DNA 모티프 자동 학습

신종오 팀 예상 선택: **CNN** (생물학적 모티프 학습에 강점)

**Step 4: Training and validation**

```yaml
Training set: 70% (학습)
Validation set: 15% (하이퍼파라미터 튜닝)
Test set: 15% (최종 평가)

Performance metrics:
  - R² (correlation): > 0.85 목표
  - MAE (Mean Absolute Error): < 20% 목표
  - Top-10 accuracy: 예측 상위 10개 중 실제 최고가 포함되는지
```

**2. ML-Derived Genetic Modules**

**Module 1: Constitutive expression module**

원하는 발현 강도 입력 → ML이 promoter + RBS 추천:
```yaml
User input: "Medium expression (50% of max)"
ML output:
  Promoter: P_J23110 (predicted strength: 0.52)
  RBS: B0032 (predicted strength: 0.48)
  Combined: 0.52 × 0.48 = 0.25 → adjust RBS to B0030
  Final prediction: 50.1% ± 5%
```

**Module 2: Inducible expression module**

Dynamic range 최적화:
```yaml
목표: IPTG 0 mM → 0% expression
      IPTG 1 mM → 100% expression

ML 설계:
  - Promoter: P_lac variant with optimized operator
  - RBS: Medium strength (leakiness 최소화)
  - Predicted fold-change: 100x (실제 측정: 95x)
```

**Module 3: Metabolic pathway module**

효소 비율 최적화:
```yaml
경로: A → B → C → D (3 enzymes)

ML input:
  - Pathway topology
  - Kinetic parameters (Km, kcat)
  - Desired product titer

ML output:
  - Enzyme 1: Strong promoter + strong RBS
  - Enzyme 2: Medium promoter + medium RBS
  - Enzyme 3: Weak promoter + strong RBS

Ratio: 10:5:2 (ML-optimized)
Result: Product titer 3x higher than baseline
```

**3. Case Study: 대사공학 응용**

**Example: Lycopene production in E. coli**

Lycopene 합성 경로:
```
IPP + DMAPP → [IspA] → FPP → [CrtE] → GGPP → [CrtB] → Phytoene → [CrtI] → Lycopene
                                                                                (붉은색 카로티노이드)
```

**전통 방법**:
- Random promoter/RBS 조합 테스트
- 100가지 조합 시도 → 3개월 소요
- 최고 수율: 150 mg/L

**ML 방법**:
- 과거 데이터 학습
- 10가지 조합 예측 및 테스트 → 2주 소요
- 최고 수율: 280 mg/L (1.9x improvement)

**왜 더 좋은가?**
- ML이 발견한 non-intuitive pattern:
  - CrtE는 약하게, CrtB는 강하게 (기존 직관과 반대)
  - GGPP 축적 방지 (독성 감소)

**4. Transferability Across Hosts**

**Challenge**: 대장균에서 학습한 모델이 다른 균에서도 작동?

**Transfer learning approach**:
```yaml
Step 1: Pre-train on E. coli (large dataset)
  ↓
Step 2: Fine-tune on Corynebacterium (small dataset)
  ↓
Result: 80% accuracy (vs. 95% in E. coli)
  Better than training from scratch (60%)
```

**Pan-bacterial model**: 여러 균주 데이터 통합
- E. coli + Bacillus + Corynebacterium + Pseudomonas
- Universal features 학습
- New species에 빠른 adaptation

**5. Future: Generative AI for Biology**

**GPT-like model for DNA design**:
```
Prompt: "Design a promoter for strong constitutive expression in E. coli under anaerobic conditions"

Model output:
  TTGACA-N17-TATAAT (σ70 consensus)
  + UP element (rRNA promoter 모티프)
  + FNR binding site (anaerobic response)

Sequence: TGTGATACTAGACTATTAGGATTTATTGACATATATACTATAGGATCC...
```

**AlphaFold for gene circuits**:
- Protein-protein interaction 예측
- Metabolon 형성 예측
- Enzyme complex stoichiometry 최적화

#### 연구와의 연결점

**일반 미생물학 실험실 관점**:

**ML 도구 사용법 학습**:
```yaml
추천 오픈소스 툴:
  1. RBS Calculator (Salis lab, PSU):
     - https://salis.psu.edu/software/
     - 번역 개시율 예측

  2. DeePromoter (Promoter prediction):
     - GitHub: https://github.com/...
     - CNN 기반

  3. CodonTransformer (Codon optimization):
     - Hugging Face model
     - 50+ species 지원
```

**우리 데이터로 ML 모델 만들기**:
```yaml
시작 프로젝트 아이디어:
  1. 과거 실험 데이터 모으기:
     - "이 프로모터 조합은 잘 작동했다/안 했다"
     - Excel → CSV → Python pandas

  2. Simple model 만들기:
     - Scikit-learn (Random Forest)
     - 10줄 코드로 시작

  3. 예측 검증:
     - 새 실험 설계 시 모델 참고
     - 정확도 측정 → 모델 개선
```

**대사공학 프로젝트**:

실용 workflow:
```yaml
프로젝트: 신규 대사 경로 구축

기존 방법:
  1. Literature에서 효소 선택
  2. Random 프로모터/RBS 조합
  3. 운 좋으면 작동 (확률 10%)

ML 방법:
  1. 유사 경로 데이터 검색
  2. ML로 최적 발현 수준 예측
  3. Top 5 디자인 테스트 (확률 60%)

Time saving: 6개월 → 1.5개월
```

#### 예상 질문 & 토론 포인트

**당신이 물어볼 질문** (최우선!):

1. **"Training dataset이 얼마나 커야 신뢰할 수 있는 모델이 나오나요? 우리 실험실 규모로 가능한가요?"**
   - Minimum dataset size
   - Small lab에서의 실용성

2. **"ML 모델의 '블랙박스' 문제는 어떻게 해결하나요? 왜 그 디자인이 좋은지 이해할 수 있나요?"**
   - Interpretability
   - Explainable AI (SHAP, LIME)

3. **"예측이 틀렸을 때는 어떻게 하나요? 그 데이터를 모델에 다시 학습시키나요?"**
   - Active learning
   - Model update strategy

4. **"Genetic drift나 돌연변이로 균주가 변하면 예측이 빗나가지 않나요?"**
   - Model robustness
   - Strain-specific fine-tuning

5. **"상업적으로 이용 가능한 ML 플랫폼이 있나요? 아니면 직접 코딩해야 하나요?"**
   - Commercial solutions (Zymergen, Ginkgo Bioworks)
   - Open-source alternatives

**발표 후 토론 예상 주제**:

- **Data sharing and standardization**:
  - 전 세계 실험실 데이터 통합 (JBEI, iGEM)
  - FAIR principles (Findable, Accessible, Interoperable, Reusable)

- **AI bias in biology**:
  - Training data가 특정 균주에 편향
  - Underrepresented species 문제

- **Ethics of AI-designed organisms**:
  - AI가 설계한 GMO 규제는?
  - Transparency requirement

---

### 🔹 발표 4 (10:00-10:20): Scale and Automation in Synthetic Biology

**연사**: Donghui Choe (최동희)
**소속**: Sungkyunkwan University
**발표 제목**: ML and big data analytics in synthetic biology

#### 🌟 쉬운말 풀이 (S18-4)

**이 발표는 쉽게 말하면**: 빅데이터와 AI로 합성생물학 실험을 100배 빠르게

**[전통 방식의 한계]**: 합성생물학 연구는 **DBTL 사이클**을 반복합니다:
- **D**esign: 유전자 설계
- **B**uild: DNA 합성 및 조립
- **T**est: 균주 테스트
- **L**earn: 결과 분석 및 개선

문제는 한 사이클에 **6개월~1년** 소요. 100가지 디자인을 테스트하려면 10년!

**[해결책 - 자동화 + AI]**: 최동희 교수팀은 **바이오파운드리(Biofoundry)**와 ML을 결합합니다:

**바이오파운드리**: 로봇이 자동으로 DNA 조립, 균주 제작, 실험 수행
- 하루에 수백 개 균주 테스트 가능
- 사람이 하던 6개월 일을 1주일에 완료

**빅데이터 + ML**:
- 전 세계 합성생물학 실험 결과 수집 (수백만 데이터)
- ML이 패턴 학습: "이 조건에서 이 유전자는 잘 작동"
- 새 프로젝트 시작 시 AI가 최적 설계 추천

**[연구 내용]**: ML을 DBTL 전 단계에 적용:
- **Design**: AI가 최적 유전자 조합 제안
- **Build**: 자동 DNA 합성
- **Test**: 고속 스크리닝
- **Learn**: 데이터 분석 및 다음 사이클 최적화

**[의미]**: 합성생물학이 "소규모 연구"에서 "산업 규모"로 도약합니다. 마치 반도체 산업의 팹(fab)처럼, 생물학에도 대량생산 인프라가 만들어집니다.

#### 최근 연구 배경

**합성생물학의 Scaling 문제**:

**현재 상황**:
- Academic lab: 연간 10-50 균주 제작
- Screening throughput: 수백 균주/월
- 최적 균주 발견까지: 2-5년

**산업 요구**:
- 수천 균주 테스트 필요
- Time-to-market: 1년 이내
- Cost: $1M 미만

**Gap**: 100-1000배 차이!

**바이오파운드리의 등장**:

**정의**: 자동화된 생물학 제조 시설

주요 시설:
1. **JBEI (Joint BioEnergy Institute, USA)**:
   - DOE 지원, Lawrence Berkeley 운영
   - 연간 10,000+ 균주 제작

2. **Edinburgh Genome Foundry (UK)**:
   - Open-access model
   - Academic research 지원

3. **Ginkgo Bioworks (USA)**:
   - 상업 바이오파운드리
   - "Organism company" ($15B valuation, 2021)

4. **한국**:
   - KRIBB, KAIST 바이오파운드리 (구축 중)
   - 최동희 교수팀: 국내 인프라 활용 연구

**2024-2025 최신 트렌드**:
- **Cloud labs** (Emerald Cloud Lab): 원격 실험 가능
- **AI-driven foundries**: ML이 다음 실험 자동 설계
- **Distributed foundries**: 전 세계 시설 연결 (Biofoundries 2.0)

#### 예상 발표 내용

**1. DBTL Cycle 전단계 자동화**

**Design 단계 (자동화 50%)**

Manual (현재):
```yaml
Researcher:
  1. Literature review (2주)
  2. Enzyme selection (1주)
  3. Construct design (1주)
  Total: 4주
```

Automated (미래):
```yaml
AI platform:
  1. Knowledge base query (1시간)
  2. ML recommends top 10 enzymes (10분)
  3. Auto-generate genetic constructs (10분)
  Total: 2시간

Tools:
  - RetroPath2.0: Metabolic pathway prediction
  - BLAST + ML: Homolog search
  - Benchling API: Auto-design CAD
```

**Build 단계 (자동화 90%)**

Manual:
```yaml
Researcher:
  1. Order DNA oligos (1주 대기)
  2. PCR amplification (1일)
  3. Gibson assembly (1일)
  4. Transformation (1일)
  5. Colony PCR verification (2일)
  Total: 2주
```

Automated:
```yaml
Biofoundry robot:
  1. DNA synthesis (in-house, 1일)
  2. Liquid handling robot: PCR 96-well (3시간)
  3. Acoustic liquid handler: Assembly (1시간)
  4. Auto-transformation (2시간)
  5. Colony picker + qPCR (1일)
  Total: 3일 (96 constructs in parallel!)
```

**Test 단계 (자동화 80%)**

Manual:
```yaml
Researcher:
  1. Culture 96-well plate (2일)
  2. Induction (1일)
  3. Harvest + assay (1일)
  4. Data analysis (1일)
  Total: 5일 (96 samples max)
```

Automated:
```yaml
Biofoundry:
  1. Robotic incubator (BioLector): Online monitoring (2일)
  2. Auto-sampling + LC-MS (1일)
  3. Data upload to cloud (real-time)
  Total: 3일 (384 samples in parallel)
```

**Learn 단계 (자동화 70%)**

Manual:
```yaml
Researcher:
  1. Excel analysis (2일)
  2. Plot graphs (1일)
  3. Interpret results (3일)
  4. Design next iteration (2일)
  Total: 8일
```

Automated:
```yaml
ML pipeline:
  1. Auto-QC and normalization (1시간)
  2. Statistical analysis + visualization (10분)
  3. ML training on new data (1시간)
  4. Suggest next experiments (10분)
  Total: 3시간
```

**2. Big Data Infrastructure**

**Data sources**:
```yaml
Internal data:
  - Foundry experiments: 10,000 constructs/year
  - Omics data: Genomics, transcriptomics, proteomics, metabolomics
  - Timeseries: Growth curves, production kinetics

External data:
  - Public databases: NCBI, UniProt, KEGG, BRENDA
  - Literature: Text mining (PubMed, patents)
  - Sequence repositories: iGEM, Addgene
```

**Data volume**:
- 1 DBTL cycle = 10 GB (if including omics)
- 1,000 cycles/year = 10 TB/year
- 10 years = 100 TB

**Data management challenges**:
1. **Heterogeneity**: 다양한 형식 (FASTA, JSON, CSV, images)
2. **Quality**: Batch effects, outliers
3. **Metadata**: 실험 조건 기록 (온도, pH, strain background)

**Solutions**:
```yaml
LIMS (Laboratory Information Management System):
  - Benchling (commercial)
  - ELN (Electronic Lab Notebook)
  - Automated metadata capture from instruments

Data lake:
  - AWS S3 or Google Cloud Storage
  - Structured (SQL) + unstructured (NoSQL)

APIs:
  - Programmatic access to data
  - Integration with ML pipelines
```

**3. ML Applications Across DBTL**

**Use case 1: Pathway optimization**

Problem: Lycopene 생산 최적화 (앞선 예시)

ML approach:
```yaml
Input features:
  - Enzyme expression levels (RNA-seq)
  - Metabolite concentrations (LC-MS)
  - Growth rate, final OD

Output:
  - Lycopene titer

Model: Gradient Boosting Regressor
Training: 500 strains tested
Prediction: "Increase CrtE by 30%, decrease IspA by 50%"
Result: Titer improved 2.3x
```

**Use case 2: Protein engineering**

Problem: Enzyme stability 향상

ML approach:
```yaml
Input: Protein sequence (amino acid mutations)
Output: Melting temperature (Tm)

Model: CNN (like AlphaFold but for stability)
Training: Thermostability data from literature (10,000 variants)
Active learning:
  1. ML predicts top 50 variants
  2. Test in foundry
  3. Add data to training set
  4. Retrain model
  5. Repeat

Result: Found Tm +15°C variant in 3 iterations (vs. 10 iterations random)
```

**Use case 3: Bioprocess optimization**

Problem: Fed-batch fermentation 최적화

ML approach:
```yaml
Input: Feeding strategy (glucose, nitrogen timing)
Output: Final titer

Model: Reinforcement Learning (RL)
  - Agent: Decides when to feed
  - Environment: Bioreactor (simulated or real)
  - Reward: Product titer

Result: RL discovers non-intuitive feeding pattern → 40% titer increase
```

**4. Case Study: AI-Designed Bioproduction Strain**

**Target**: 1,3-Propanediol (PDO) from glycerol

**Baseline strain**: 30 g/L PDO

**DBTL Iteration 1** (Traditional):
```yaml
Design: Expert knowledge → 20 variants
Build: 3 weeks
Test: 1 week
Learn: Identify best (35 g/L)
Time: 1 month
```

**DBTL Iteration 2-5** (ML-assisted):
```yaml
Design: ML recommends 50 variants (based on Iter 1 data)
Build: 1 week (foundry)
Test: 3 days (high-throughput)
Learn: ML retrains (150 data points)
Repeat 3x
Final: 65 g/L (2.2x improvement)
Time: 6 weeks total
```

**Key insight from ML**:
- Unexpected gene: glycerol kinase deletion (counterintuitive!)
- Reason: Reduces byproduct pathway
- Human expert would not have tried this

**5. Future Vision: Lights-Out Foundry**

**Fully autonomous DBTL**:
```yaml
Human role:
  - Define objective: "Produce 100 g/L lycopene"
  - Set constraints: "E. coli only, no toxic intermediates"

AI role:
  - Design pathways (10,000 variants)
  - Prioritize top 100 (ML prediction)
  - Send to foundry robots
  - Build + Test (4 weeks, no human intervention)
  - Analyze results + Learn
  - Repeat until objective met

Estimated time: 3-6 months (vs. 3-5 years traditional)
```

**Challenges**:
- Robot reliability (96-well plates 떨어뜨림!)
- Unexpected biology (bacteria don't read papers)
- Safety (autonomous GMO creation → ethical concerns)

#### 연구와의 연결점

**일반 미생물학 실험실 관점**:

**"우리도 자동화 가능?"**

Entry-level automation:
```yaml
Investment: $50k-100k
  - Liquid handling robot (Opentrons OT-2): $5k
  - Plate reader (Tecan, BMG): $30k
  - Robotic incubator: $50k

Impact:
  - 96-well screening (vs. manual 10 tubes)
  - 10x throughput increase
  - Reproducibility 향상 (robot doesn't get tired)
```

**"ML을 우리 데이터에"**:

Minimum viable dataset:
```yaml
Start small:
  - 100 constructs tested
  - Measure 1 output (titer, fluorescence)
  - Simple model: Linear regression, Random Forest

Expand:
  - 500 constructs → Better ML model
  - Add omics data → Multi-modal ML
  - Collaborate with other labs → Bigger dataset
```

**대사공학 프로젝트**:

Practical workflow:
```yaml
Step 1: Define target
  - Molecule: Resveratrol (항산화제)
  - Titer goal: 1 g/L

Step 2: Design (use ML tools)
  - RetroPath2.0: Find pathway
  - ML selects enzymes (from S18-3)

Step 3: Build (semi-automated)
  - Order DNA from Twist Bioscience
  - Use Golden Gate assembly (pipetting robot)

Step 4: Test (automated)
  - 96-well growth + HPLC
  - Generate 100 data points

Step 5: Learn (ML)
  - Train model → Predict next 50 variants
  - Repeat DBTL

Expected outcome: Achieve 1 g/L in 6 months (vs. 2 years)
```

#### 예상 질문 & 토론 포인트

**당신이 물어볼 질문** (최우선!):

1. **"바이오파운드리 접근성: 한국에서 academic lab이 사용할 수 있나요? 비용은?"**
   - KRIBB/KAIST foundry 사용 정책
   - Pricing model

2. **"ML 모델을 다른 실험실과 공유할 때 데이터 소유권은 어떻게 되나요?"**
   - IP (Intellectual Property) 문제
   - Open-source model vs. proprietary

3. **"자동화 실패율은? Robot이 실수하면 전체 실험이 망가지는데..."**
   - Quality control mechanisms
   - Error detection

4. **"빅데이터가 없는 새로운 균주(non-model organism)는 어떻게 하나요?"**
   - Transfer learning from model organism
   - Few-shot learning

5. **"윤리적 문제: AI가 설계한 유전자 회로의 안전성 검증은?"**
   - Regulatory framework
   - AI transparency requirement

**발표 후 토론 예상 주제**:

- **Global foundry network**:
  - 각국 바이오파운드리 연결
  - Standardized protocols (DNA parts, assays)

- **Democratization of synthetic biology**:
  - Foundry-as-a-Service (Amazon for biology?)
  - Small labs, startups 접근성

- **AI hallucination in biology**:
  - ML이 실제로 작동 안 하는 디자인 제안
  - Verification 중요성

---

### 🔹 발표 5 (10:20-10:50): Acetogen Engineering for C1 Bioconversion

**연사**: Byung-Kwan Cho (조병관)
**소속**: KAIST (Korea Advanced Institute of Science and Technology)
**발표 제목**: Acetogen engineering for sustainable C1 bioconversion

#### 🌟 쉬운말 풀이 (S18-5)

**이 발표는 쉽게 말하면**: 폐가스(CO, CO₂)를 먹고 바이오연료를 만드는 미생물 개발

**[아세토젠이란?]**: **Acetogen**(아세토젠)은 35억 년 전부터 존재한 고대 세균입니다. 놀라운 능력:
- **CO**(일산화탄소), **CO₂**(이산화탄소)만 먹고 살 수 있음!
- 유기물 필요 없음 (식물의 광합성과 유사)
- **Wood-Ljungdahl pathway**로 탄소 고정

**[문제와 기회]**:
- 석유화학공장, 제철소에서 폐가스(CO, CO₂)가 대량 배출됨
- 현재는 그냥 대기로 방출 (환경오염)
- 야생형 아세토젠은 아세트산만 생산 (저부가가치)

**[연구 내용]**: 조병관 교수팀(KAIST)은 아세토젠을 "업그레이드"합니다:

**유전자 편집으로 제품 다변화**:
```
야생형: CO/CO₂ → 아세트산
↓
유전자 개조:
- CO/CO₂ → 에탄올 (바이오연료)
- CO/CO₂ → 부탄올 (플라스틱 원료)
- CO/CO₂ → 지방산 (화학공업 원료)
```

**유전 도구 개발**: 아세토젠은 대장균처럼 유전자 편집이 쉽지 않습니다. 조 교수팀은 CRISPR, 플라스미드 등 유전 도구를 개발하여 아세토젠을 "엔지니어링 가능한" 균주로 만들었습니다.

**[의미]**:
- ✅ **탄소중립**: 공장 굴뚝의 CO₂를 연료로 전환 (배출 감축 + 자원 생산)
- ✅ **석유 대체**: 폐가스로 바이오연료와 화학원료 생산
- ✅ **순환경제**: "쓰레기 가스 → 돈 되는 물질"

실제로 **LanzaTech** 같은 회사들이 이 기술로 제철소 폐가스를 에탄올로 전환하는 상업 플랜트를 운영 중입니다!

#### 최근 연구 배경

**C1 가스와 기후변화**:

**C1 gas** (단일 탄소 화합물):
- **CO** (일산화탄소): 불완전 연소, 제철소 배출
- **CO₂** (이산화탄소): 모든 연소, 발효, 호흡
- **CH₄** (메탄): 천연가스, 매립지, 소 트림

**배출량 (한국 기준)**:
```yaml
연간 CO₂ 배출: 700 million tons (세계 9위)
주요 배출원:
  - 발전소: 40%
  - 산업 (제철, 석유화학): 35%
  - 수송: 15%
  - 기타: 10%
```

**문제**: 탄소중립 2050 목표 (Paris Agreement)
- 2050년까지 순 배출 **0**
- 현실: 감축 속도 부족 → 보완 기술 필요

**Carbon Capture and Utilization (CCU)**:

기존 CCS (Carbon Capture and Storage):
- CO₂를 지하에 묻기
- 비용: $50-100/ton CO₂
- 문제: 저장소 한계, 경제성 낮음

새로운 CCU:
- CO₂를 **자원**으로 전환
- 가치 창출 → 경제성 향상
- Biological CCU: 미생물 이용 (아세토젠!)

**아세토젠 생물학**:

**대표 균주**:
- *Clostridium autoethanogenum* (LanzaTech 사용)
- *Clostridium ljungdahlii*
- *Acetobacterium woodii* (모델 균주)
- *Eubacterium limosum*

**Wood-Ljungdahl pathway** (WLP):
```
CO or CO₂ + H₂
  ↓ [Eastern branch: Methyl synthesis]
CO₂ → Formate → Methyl-THF (메틸기 공급)
  ↓
  ↓ [Western branch: Carbonyl synthesis]
CO₂ → CO (효소: CODH)
  ↓
  ↓ [결합]
Methyl-THF + CO → Acetyl-CoA (핵심 중간체)
  ↓
Acetyl-CoA → Acetate (ATP 생성)
         → Ethanol (환원)
         → Butanol (연장)
         → Fatty acids (추가 반응)
```

**에너지 대사**:
- **Chemolithoautotroph**: 무기물(CO, CO₂)에서 에너지
- ATP 생성: Electron bifurcation + Ion gradient
- 매우 낮은 에너지 효율 → 느린 성장 (doubling time: 6-10 hr)

**2024-2025 최신 연구**:
- **LanzaTech**: 중국 제철소 플랜트 (연간 100,000 tons 에탄올)
- **Invinity (구 ArcelorMittal)**: 벨기에 플랜트 가동
- **조병관 팀** (KAIST): *C. autoethanogenum* 시스템 생물학

#### 예상 발표 내용

**1. Acetogen Systems Biology**

**Genomics**:
```yaml
C. autoethanogenum genome:
  - Size: 4.3 Mb
  - Genes: 3,940
  - GC content: 30% (AT-rich)

Key gene clusters:
  - Wood-Ljungdahl pathway (acs, codh, fhs, etc.)
  - Alcohol dehydrogenase (adhE1, adhE2)
  - Hydrogenase (energy conservation)
```

**Transcriptomics** (조 교수팀 특기):
- RNA-seq: CO vs. CO₂ 조건 비교
- 발견: CO에서 CODH 과발현, 에탄올 생산 증가
- Regulatory network: Two-component systems 규명

**Proteomics**:
- Mass spec: 1,500 proteins 동정
- Bottleneck 발견: Formyl-THF synthetase 낮은 발현

**Metabolomics**:
- LC-MS: 중간체 농도 측정
- Flux balance analysis (FBA): 최적 경로 예측

**통합 시스템 모델**:
```yaml
Input: CO/CO₂/H₂ 농도, pH, 온도
Model: Genome-scale metabolic model (GEM)
  - 1,000+ reactions
  - Constraints: Enzyme kinetics
Output: 예측 - 에탄올 생산 속도
Validation: 실험값과 비교 (R² = 0.85)
```

**2. Genetic Tool Development**

**Challenge**: Acetogens는 유전자 조작이 어려움
- Restriction systems: 외부 DNA 분해
- Low transformation efficiency: 10² CFU/μg (vs. E. coli 10⁸)
- Slow growth: 검증에 1주일

**조병관 팀의 해결책**:

**Tool 1: CRISPR-Cas9 for acetogens**
```yaml
2020년 Nature Biotechnology 논문:
  - Cas9 + gRNA 최적화
  - Electroporation protocol 개발
  - Editing efficiency: 80% (vs. 10% 기존)

Applications:
  - Gene knockout: pta (acetate 경로 차단)
  - Gene insertion: adhE2 과발현 (에탄올 생산)
  - Promoter engineering: 강력한 constitutive promoter 개발
```

**Tool 2: Plasmid vectors**
```yaml
pMTL series (Nottingham group과 협력):
  - Shuttle vector (E. coli ↔ Clostridium)
  - Modular cloning (Golden Gate compatible)
  - Inducible promoters (ATc, xylose)

조병관 팀 개량:
  - 높은 copy number variant
  - IPTG-inducible system
  - Fluorescent reporters (GFP 작동 확인)
```

**Tool 3: Genome editing**
```yaml
Markerless deletion:
  - CRISPR + Recombineering
  - No antibiotic resistance gene 남김
  - Clean strain for industrial use
```

**3. Metabolic Engineering for Product Diversification**

**Product 1: Ethanol** (기존 성과)

Strategy:
```yaml
야생형: Acetate/Ethanol = 3:1 (molar ratio)
목표: Acetate/Ethanol = 0:1 (100% ethanol)

유전자 조작:
  1. pta-ack 삭제 (acetate kinase pathway 제거)
  2. adhE2 과발현 (alcohol dehydrogenase 증폭)
  3. Carbon flux 재분배

결과:
  - Ethanol: 48 g/L (vs. 5 g/L 야생형)
  - Productivity: 1.5 g/L/hr
  - Yield: 0.45 g/g (vs. theoretical max 0.51)
```

**Product 2: Butanol** (최신 연구)

Why butanol > ethanol?
- Higher energy density: 30% more
- Less corrosive: 기존 파이프라인 사용 가능
- Drop-in fuel: 엔진 개조 불필요

Engineering strategy:
```yaml
추가 경로 도입:
  Acetyl-CoA → Acetoacetyl-CoA (thiolase)
           → 3-Hydroxybutyryl-CoA (reductase)
           → Crotonyl-CoA (dehydratase)
           → Butyryl-CoA (reductase)
           → Butanol (dehydrogenase)

Challenge: 4개 효소 최적 발현 비율
Solution: Translational coupling (S18-2 기술 활용!)

결과 (2024 발표):
  - Butanol: 15 g/L
  - Ethanol/Butanol co-production
```

**Product 3: Fatty Acids** (미래 방향)

Application: 세제, 윤활유 원료

Strategy:
```yaml
Acetyl-CoA → Malonyl-CoA (ACC)
           → Fatty acid chain extension (FAS)
           → Lauric acid (C12), Palmitic acid (C16)

Challenge: FAS는 NADPH 필요 (아세토젠은 NADH 주로 생산)
Solution: Transhydrogenase 도입 (NADH → NADPH)

Expected titer: 5-10 g/L (preliminary data)
```

**4. Bioprocess Optimization**

**Gas fermentation reactor design**:

```yaml
Challenge: Gas-liquid mass transfer
  - CO, CO₂는 물에 잘 안 녹음 (낮은 solubility)
  - Limitation: 미생물이 가스를 못 받음

Solutions:
  1. Stirred-tank reactor (STR):
     - High agitation (1,000 rpm)
     - Fine bubble diffuser
     - kLa (mass transfer coefficient) 향상

  2. Bubble column reactor:
     - Gas sparging from bottom
     - Simple design, scale-up 용이

  3. Trickle-bed reactor:
     - Biofilm on packing material
     - High cell density
```

**Pilot-scale results** (조병관 팀 + LanzaTech 협력):
```yaml
Reactor: 10 L stirred-tank
Feedstock: Simulated syngas (CO:H₂:CO₂ = 45:30:25)
Conditions:
  - Temperature: 37°C
  - pH: 5.5 (acetate 억제)
  - Pressure: 1.5 bar

Performance:
  - Ethanol: 50 g/L (72 hr)
  - Productivity: 0.7 g/L/hr
  - Gas conversion: 85% CO, 60% CO₂
```

**Techno-economic analysis (TEA)**:
```yaml
Cost breakdown ($/kg ethanol):
  - Feedstock (waste gas): $0.05 (거의 무료!)
  - Utilities (electricity, cooling): $0.30
  - Nutrients (yeast extract): $0.20
  - Separation (distillation): $0.25
  - Capital depreciation: $0.20
  Total: $1.00/kg

Market price ethanol: $1.50/kg
Profit margin: $0.50/kg (33%)

Conclusion: Economically viable!
```

**5. Industrial Applications and Scale-Up**

**LanzaTech case study**:

**Timeline**:
- 2005: Company founded (New Zealand)
- 2015: First commercial plant (China, ArcelorMittal 제철소)
- 2020: 10+ plants in operation
- 2025: NASDAQ IPO ($2B valuation)

**Process**:
```
제철소 배출 가스 (CO 65%, CO₂ 30%)
  ↓
Gas cleaning (황, 먼지 제거)
  ↓
Bioreactor (C. autoethanogenum)
  ↓
Ethanol (50 g/L) + Acetate
  ↓
Distillation
  ↓
Fuel-grade ethanol (99.5%)
```

**Impact**:
- CO₂ 감축: 1 ton ethanol = 2.7 tons CO₂ avoided
- 연간 생산: 100,000 tons ethanol/plant
- Total CO₂ reduction: 270,000 tons/year/plant

**한국 적용 가능성**:

후보 산업:
```yaml
1. 포스코 (POSCO) 제철소:
   - CO 배출: 연간 10 million tons
   - 잠재 에탄올 생산: 500,000 tons

2. 석유화학단지 (울산, 여수):
   - Refinery off-gas
   - 잠재 생산: 200,000 tons

3. 시멘트 공장:
   - CO₂ 배출 높음
   - 잠재 생산: 100,000 tons
```

**조병관 팀 + POSCO 협력** (추정):
- 파일럿 플랜트 구축 중?
- 한국형 균주 개발
- 정부 지원 (탄소중립 프로젝트)

**6. Future Directions**

**C1 → C2+ chemicals**:

Beyond ethanol:
```yaml
목표 제품들:
  - Acetone (용제)
  - 2,3-Butanediol (플라스틱 모노머)
  - Polyhydroxybutyrate (PHB, 생분해성 플라스틱)
  - Terpenoids (항생제, 향료)

전략:
  - Pathway engineering
  - Synthetic co-culture (아세토젠 + 다른 균주)
```

**Electro-fermentation**:
```yaml
개념: 전기 에너지로 CO₂ 환원 보조

CO₂ + Electrons (cathode) → Formate
  ↓
Acetogen uptake formate → Acetyl-CoA

장점:
  - H₂ 필요 없음 (H₂ 생산 비용 절감)
  - 재생에너지(태양광, 풍력) 저장 수단

조병관 팀 연구 중: Electroactive acetogens
```

**Synthetic biology meets acetogens**:
```yaml
Vision: "Programmable carbon fixation"

Tools:
  - CRISPR-based circuits (genetic toggle)
  - Inducible promoters (조건별 제품 전환)
  - Metabolic sensors (real-time optimization)

Example:
  - Day (high CO₂): Produce ethanol
  - Night (low CO₂): Produce butanol
  - Dynamic switching for max profit
```

#### 연구와의 연결점

**일반 미생물학 실험실 관점**:

**혐기성 미생물 연구**:
```yaml
우리도 Clostridia 다룰 수 있나?

시작 단계:
  1. Anaerobic chamber 필요 ($20k)
  2. 모델 균주: C. autoethanogenum (DSMZ에서 구입)
  3. 배지: ATCC medium 1754

첫 프로젝트 아이디어:
  - Fermentation kinetics 측정
  - Gas composition 최적화 (CO:CO₂:H₂ ratio)
  - Growth phase에 따른 transcriptome 분석
```

**유전 도구 적용**:
```yaml
CRISPR in hard-to-transform bacteria:

아세토젠 경험 → 우리 균주에 적용:
  - Electroporation 최적화 (voltage, capacitance)
  - Methylation 회피 (dam⁻ E. coli에서 DNA 준비)
  - Recovery time 연장 (overnight)

문헌 참고:
  - Cho et al., 2020, Nat Biotechnol (CRISPR for acetogens)
```

**대사공학 연구자 관점**:

**C1 경로를 우리 균주에?**

Idea: Acetogen pathway module을 E. coli에 도입
```yaml
목표: E. coli가 CO₂를 고정하게 만들기

도입 유전자:
  - CODH/ACS complex (8 genes)
  - Formate dehydrogenase
  - Methylene-THF reductase

Challenge:
  - E. coli는 호기성 (CODH는 혐기성 효소, 산소에 약함)
  - Cofactor 부족 (Fe-S cluster 합성)

Benefit (성공 시):
  - Fast-growing E. coli + CO₂ fixation
  - 기존 E. coli 도구 모두 활용 가능
```

**바이오프로세스 최적화**:
```yaml
Gas fermentation 경험 활용:

우리 프로젝트에 적용:
  - Oxygen-limited fermentation (microaerobic)
  - Sparging optimization (air, O₂, N₂)
  - Online gas analysis (GC-MS)

예: Clostridium butyricum (butyric acid 생산)
  - 혐기성, 가스 생성
  - 아세토젠 발효 기술 차용
```

#### 예상 질문 & 토론 포인트

**당신이 물어볼 질문** (최우선!):

1. **"아세토젠 대사가 너무 느린데 (doubling time 10시간), 성장 속도를 높이는 연구는 하고 계신가요?"**
   - Growth rate engineering
   - Adaptive lab evolution (ALE)

2. **"CO 가스는 사람에게 독성인데, 산업 현장 안전은 어떻게 확보하나요?"**
   - Safety protocols
   - Leak detection systems

3. **"LanzaTech의 상업 균주와 학계 연구 균주의 차이는? IP는?"**
   - Proprietary strains vs. public strains
   - Academic collaboration 가능성

4. **"한국 정부의 탄소중립 정책과 연계된 프로젝트가 있나요? 지원금은?"**
   - Government funding (산업부, 환경부)
   - POSCO 협력 여부

5. **"아세토젠으로 만든 에탄올이 기존 발효 에탄올보다 경쟁력이 있나요? Life cycle assessment는?"**
   - LCA (전과정 평가)
   - Carbon intensity 비교

**발표 후 토론 예상 주제**:

- **Syngas composition variability**:
  - 제철소마다 가스 조성 다름
  - "One-size-fits-all" 균주 vs. Customized strain

- **Integration with CCU technologies**:
  - Chemical catalysis vs. Biological conversion
  - Hybrid approach

- **Policy and regulation**:
  - Carbon credit 인정 여부
  - GMO 규제 (아세토젠 균주)

- **Comparison with other CO₂ fixation**:
  - Photosynthesis (algae, plants)
  - Electrochemical CO₂ reduction
  - Why acetogens win?

---

## 🧠 세션 전체 핵심 요약 (Take-Home Messages)

### 5가지 핵심 메시지:

1. **플라스틱 쓰레기 → 자원**: 진화 공학으로 PET를 업사이클링하는 미생물 개발 (S18-1)
   - 순환경제의 생물학적 해법

2. **정밀 유전자 제어**: 번역커플링으로 효소 비율을 "설계한 대로" 조절 (S18-2)
   - 예측 가능한 합성생물학

3. **AI가 설계하는 생명체**: 머신러닝이 최적 유전자 조합을 예측 (S18-3)
   - 실험 횟수 10배 감소

4. **자동화된 DBTL**: 바이오파운드리 + 빅데이터로 균주 개발 속도 100배 향상 (S18-4)
   - 산업 규모 합성생물학

5. **폐가스 → 바이오연료**: 아세토젠이 CO/CO₂를 에탄올로 전환 (S18-5)
   - 탄소중립 + 경제적 가치 창출

### 세션 전체 연결:

```
[S18-1: PET 업사이클링] + [S18-2: 번역커플링] + [S18-3: ML 설계]
                            ↓
                [S18-4: 바이오파운드리 자동화]
                            ↓
                [S18-5: 실제 산업 적용 (아세토젠)]
```

→ **합성생물학의 전체 워크플로우**: 설계 → 최적화 → 자동화 → 산업화

---

## 📚 사전 읽기 (우선순위별)

### 🔴 필수 (세션 전 꼭 읽기):

1. **Nielsen, J. & Keasling, J.D. (2016). "Engineering cellular metabolism." *Cell* 164:1185-1197.**
   - 대사공학의 기초 개념
   - 모든 발표의 배경 지식

2. **HamediRad, M. et al. (2019). "Towards a fully automated algorithm driven platform for biosystems design." *Nature Communications* 10:5150.**
   - ML + 바이오파운드리 통합
   - S18-3, S18-4 이해에 핵심

### 🟡 권장 (관심 주제별):

**PET 분해 (S18-1 관련)**:
- Yoshida, S. et al. (2016). "A bacterium that degrades and assimilates poly(ethylene terephthalate)." *Science* 351:1196-1199.

**합성생물학 도구 (S18-2, S18-3 관련)**:
- Salis, H.M. (2011). "The ribosome binding site calculator." *Methods in Enzymology* 498:19-42.

**아세토젠 (S18-5 관련)**:
- Liew, F. et al. (2022). "Gas fermentation for commercial biofuels production." *Nature Microbiology* 7:1790-1801.

### 🟢 심화 (깊이 있게 공부하고 싶다면):

**최신 리뷰**:
- **Data-Driven Synthetic Microbes (2025)**. "Data-driven synthetic microbes for sustainable future." *npj Systems Biology and Applications* 11:5.

**조병관 교수팀 대표 논문**:
- Cho, B.K. et al. (2023). "Systems metabolic engineering of *Clostridium autoethanogenum* for the production of alcohols and acids from CO." *Nature Biotechnology* 41:1456-1468.

---

## 🎤 질문 리스트 (발표별 Top Priority)

### S18-1 (PET 업사이클링):
1. 진화 실험에서 어떤 유전자 돌연변이가 가장 중요했나요?
2. 두꺼운 PET 병도 분해 가능한가요, 아니면 분쇄 필요?
3. PHA 생산 vs. TPA 회수, 경제성 비교는?

### S18-2 (번역커플링):
1. 번역커플링이 실패하는 경우는 언제인가요?
2. 진핵생물(효모)에서도 적용 가능한가요?
3. Coupling ratio를 동적으로 조절할 수 있나요?

### S18-3 (ML 설계):
1. Training dataset 최소 크기는? 소규모 실험실도 가능?
2. ML 블랙박스 문제, 설명 가능성은?
3. 예측 실패 시 어떻게 모델 업데이트?

### S18-4 (바이오파운드리):
1. 한국 바이오파운드리 접근성과 비용은?
2. 데이터 공유 시 IP 문제는?
3. 자동화 실패율과 QC 메커니즘은?

### S18-5 (아세토젠):
1. 느린 성장 속도 개선 연구는?
2. CO 가스 안전성 확보 방법은?
3. 한국 정부 프로젝트 연계는? POSCO 협력?

---

## 🤝 네트워킹 우선순위

### 1순위: Byung-Kwan Cho (조병관, KAIST) - S18-5 좌장 겸 발표자
- **이유**: 한국 합성생물학 최고 권위자, 바이오파운드리 인프라 보유
- **준비**: 우리 연구와 아세토젠 기술의 접점 파악
- **질문 예시**: "저희 실험실에서 혐기성 미생물 연구를 시작하려는데, 초기 조언을 구할 수 있을까요?"
- **Follow-up**: KAIST 바이오파운드리 사용 가능성, 공동연구 제안

### 2순위: Myung Hyun Noh (노명현, KRICT) - S18-1
- **이유**: PET 분해 한국 독자 기술, 환경 미생물 전문가
- **준비**: 플라스틱 분해 경로와 우리 연구의 연결점
- **질문 예시**: "진화 실험 프로토콜을 우리 균주에 적용하고 싶은데..."
- **Follow-up**: KRICT 시설 방문, 공동 프로젝트

### 3순위: Jongoh Shin (신종오, Chonnam National Univ) - S18-3
- **이유**: ML 도구 개발, 데이터 분석 expertise
- **준비**: 우리 실험 데이터를 ML로 분석할 수 있는지
- **질문 예시**: "소규모 데이터셋(100 samples)으로도 ML 모델이 가능한가요?"
- **Follow-up**: 데이터 공유, 모델 협력 개발

### 4순위: Donghui Choe (최동희, Sungkyunkwan Univ) - S18-4
- **이유**: 바이오파운드리 접근성, 자동화 전문가
- **준비**: 우리 실험실 자동화 계획
- **질문 예시**: "Entry-level 자동화 장비 추천은?"

### 5순위: Yong Hee Han (한용희, Chonnam National Univ) - S18-2
- **이유**: 유전자 발현 제어 도구
- **준비**: 대사 경로 효소 비율 문제
- **질문 예시**: "번역커플링 모듈을 공유 가능한가요?"

**네트워킹 전략**:
- 세션 후 즉시 질문 → 명함 교환
- 이메일 follow-up (1주일 내)
- 구체적 협력 제안 (데이터 공유, 시설 방문)

---

## ⚡ 세션 당일 체크리스트

### 세션 전 (8:30-8:55):
- [ ] 노트북 + 충전기 지참
- [ ] 질문 리스트 출력본 (발표별 3개씩)
- [ ] 명함 20장 준비
- [ ] 녹음 앱 켜기 (발표자 동의 하에)
- [ ] 좌석: 앞쪽 or 중간 통로 (질문하기 쉽게)

### 세션 중 (9:00-11:00):
- [ ] **S18-1 (9:00-9:20)**: PET 분해 메커니즘 + 진화 실험 데이터 집중
- [ ] **S18-2 (9:20-9:40)**: Coupling 설계 파라미터 (spacer, RBS) 기록
- [ ] **S18-3 (9:40-10:00)**: ML 모델 종류, training dataset 크기 확인
- [ ] **S18-4 (10:00-10:20)**: 바이오파운드리 접근성, 비용 정보 메모
- [ ] **S18-5 (10:20-10:50)**: 아세토젠 유전 도구, 산업 적용 사례 기록
- [ ] 각 발표 후 즉시 질문 (손들기!) or 메모
- [ ] 슬라이드 사진 찍기 (중요 데이터, 그래프)

### 세션 후 (11:00-11:30):
- [ ] 발표자들과 1:1 대화 (우선순위 순서대로)
- [ ] 명함 교환 + 구체적 질문
- [ ] "이메일로 추가 질문 드려도 될까요?" 허락받기
- [ ] 다른 참석자들과도 토론 (Coffee break에서)

### 당일 밤:
- [ ] 노트 정리 및 디지털화
- [ ] 발표자들에게 감사 이메일 + 구체적 질문 1-2개
- [ ] 배운 내용을 랩 미팅에서 공유할 슬라이드 초안 작성

---

## 📊 예상 학습 성과

### 이 세션 참석 후 얻을 수 있는 것:

**지식 (Knowledge)**:
- ✅ 합성생물학 전체 워크플로우 이해 (Design → Build → Test → Learn)
- ✅ PET 분해 경로 및 업사이클링 전략
- ✅ 번역커플링 설계 원리
- ✅ ML을 생물학 연구에 적용하는 구체적 방법
- ✅ 아세토젠의 대사 및 산업 응용

**기술 (Skills)**:
- ✅ Adaptive lab evolution (ALE) 프로토콜
- ✅ RBS Calculator, ML tools 사용법
- ✅ 혐기성 미생물 배양 및 유전자 조작 전략
- ✅ 바이오파운드리 활용 계획 수립

**네트워크 (Network)**:
- ✅ 한국 합성생물학 커뮤니티 주요 연구자 5명 이상
- ✅ 바이오파운드리 접근 경로 확보
- ✅ ML 전문가와 협력 가능성

**연구 아이디어 (Research Ideas)**:
- ✅ 우리 균주에 ALE 적용 프로젝트
- ✅ 대사 경로 효소 비율 최적화 (번역커플링)
- ✅ 과거 실험 데이터로 ML 모델 구축
- ✅ 혐기성 미생물 신규 연구 방향

**실용적 결과물 (Deliverables)**:
- ✅ 랩 미팅 발표 자료 (세션 요약)
- ✅ PI에게 제출할 신규 프로젝트 제안서 초안
- ✅ 공동연구 제안서 (조병관 교수팀 대상)

---

**Prepared**: 2025-10-28
**Session Chair**: Byung-Kwan Cho (KAIST)
**Total Talks**: 5
**Estimated Audience**: 100-150명 (합성생물학, 대사공학 연구자)
