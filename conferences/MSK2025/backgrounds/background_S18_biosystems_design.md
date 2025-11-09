# S18: 생체시스템 설계 및 합성의 발전
**Day 3 (10월 28일) 09:00-11:00, Rm 301+302**
**좌장**: 조병관 (KAIST)

## 📋 세션 개요
지속가능성을 위한 합성생물학 및 대사공학에 초점. 플라스틱 upcycling 및 생분해, polycistronic 유전자 발현 제어, 세균 엔지니어링을 위한 머신러닝, Acetogen을 사용한 C1 gas bioconversion을 다룹니다.

**우선순위 점수**: 73/100 (합성생물학/대사공학에 높음, 기타 중간)

---

## 🎤 발표별 상세 분석

### 1️⃣ 노명현 (한국화학연구원)
**주제**: 플라스틱 지속가능성을 위한 진화 활용: 폐기물 upcycling에서 생분해성 복합재까지

**핵심 연구 방향**:
- 효소적 플라스틱 분해 (PET, PUR 등)
- 개선된 depolymerase를 위한 directed evolution
- 플라스틱 폐기물을 부가가치 제품으로 upcycling
- 생분해성 플라스틱 대안

**왜 중요한가**:
- **플라스틱 폐기물 위기**: 전 세계적 환경 도전
- **순환 경제 접근**: 폐기물에서 자원으로
- **실제 응용을 위한 효소 엔지니어링**
- **지속가능한 재료 개발**

**핵심 개념**:
- **PETase/MHETase**: PET 플라스틱 분해 효소
- **Directed evolution**: 효소 활성, 열안정성 개선
- **Upcycling**: PET 단량체를 고부가가치 화학물질로 전환
- **Biodegradable plastics**: 대안으로서의 PHAs, PLA

**기대 내용**:
- 효소 진화 전략 (random mutagenesis, rational design)
- 개선된 효소의 열안정성 및 활성 (PET Tm ~70°C 극복)
- Upcycling 경로 (TPA → 방향족 화합물)
- 생분해성 플라스틱 생산 (PHA)
- 경제성 분석

---

### 2️⃣ 한용희 (전남대학교)
**주제**: 세균에서 정밀한 polycistronic 유전자 발현 제어를 위한 translational coupling 기반 합성 생체 부품

**핵심 연구 방향**:
- 세균에서의 translational coupling 메커니즘
- 예측 가능한 유전자 발현을 위한 합성생물학 부품
- Polycistronic operon 설계 및 최적화
- 대사 공학에서의 응용

**왜 중요한가**:
- **경로 효소의 정밀한 화학양론적 제어**
- **Plasmid 부담 감소** (더 적은 promoter)
- **설계로부터 예측 가능한 유전자 발현**
- **대사 경로 효율 개선**

**Translational Coupling 기술**:
- **메커니즘**: Upstream 유전자로부터의 ribosome이 downstream 유전자에서 재개시
- **설계 규칙**:
  - Inter-cistronic spacing (5-50 nt)
  - RBS strength
  - Secondary structure 방지
- **응용**: Multi-enzyme pathways, protein complexes
- **장점**: 조율된 발현, 유전 요소 감소

**기대 내용**:
- Translational coupling의 정량적 모델
- 설계 도구 및 검증
- 대사공학 사례 연구
- 다양한 유전적 맥락에서의 robustness

---

### 3️⃣ 신종오 (전남대학교)
**주제**: Machine Learning-Derived Modules로 세균 기능 조절

**핵심 연구 방향**:
- 유전 회로 설계를 위한 머신러닝
- 유전자 발현을 위한 예측 모델
- 데이터 기반 합성생물학 부품 특성화
- 자동화된 design-build-test-learn 사이클

**왜 중요한가**:
- **합성생물학 가속화**: Trial-and-error 감소
- **데이터로부터 설계 규칙 추출**
- **복잡한 회로 설계 가능**
- **합성생물학의 민주화**

**ML 응용**:
- **Promoter 강도 예측**: Sequence → 발현 수준
- **RBS calculator**: Translation initiation rate 예측
- **Circuit behavior**: 유전 회로 동역학 예측
- **최적화**: ML 가이드 directed evolution

**기대 내용**:
- 훈련 데이터셋 및 특징 엔지니어링
- ML 모델 (CNN, Random Forest, Neural networks)
- 실험적 검증 결과
- 설계 도구 및 사용자 인터페이스

---

### 4️⃣ 최동희 (성균관대학교)
**주제**: 머신러닝 및 빅데이터 분석을 통한 합성생물학의 규모 확장

**핵심 연구 방향**:
- 대규모 합성생물학 데이터셋
- 균주 엔지니어링을 위한 빅데이터 분석
- 바이오엔지니어링을 위한 multi-omics 통합
- 대사 공학을 위한 예측 모델

**왜 중요한가**:
- **데이터 기반 균주 개발** (직관을 대체)
- **축적된 지식 활용**
- **상업화 가속화**
- **시스템 수준 이해**

**빅데이터 소스**:
- Public 데이터베이스 (NCBI, KEGG, BioCyc)
- Omics 데이터 (genome, transcriptome, proteome, metabolome)
- Literature mining
- Proprietary 균주 엔지니어링 데이터

**기대 내용**:
- 데이터 통합 및 정규화 전략
- ML 모델 (회귀, 분류, deep learning)
- 예측 성능 벤치마킹
- 실제 균주 개발 사례 연구

---

### 5️⃣ 조병관 (KAIST)
**주제**: 지속가능한 C1 gas bioconversion을 위한 acetogenic 세균의 합성생물학

**핵심 연구 방향**:
- C1 gas 발효를 위한 Acetogens (*Clostridium autoethanogenum* 등)
- CO, CO₂, syngas를 화학물질/연료로 전환
- 비모델 acetogen을 위한 유전 도구
- 산업 규모 C1 bioconversion

**왜 중요한가**:
- **기후 변화 완화**: CO₂ 활용
- **제철소 off-gas 가치화**
- **지속가능한 화학물질 생산**
- **화석 연료 대안**

**Acetogenic Fermentation**:
- **기질**: CO, CO₂ + H₂, syngas (산업 폐가스)
- **생성물**: 에탄올, acetate, 2,3-butanediol 등
- **Wood-Ljungdahl pathway**: CO₂ → Acetyl-CoA
- **도전과제**: 낮은 생산성, 유전적 난제, scale-up

**합성생물학 접근**:
- Acetogens을 위한 CRISPR 도구
- Heterologous pathway 발현
- Systems 대사 공학
- 산업 균주 최적화

**기대 내용**:
- Acetogen 대사의 시스템 분석
- 유전 도구 개발 (transformation, CRISPR)
- Pathway engineering 사례
- Pilot/industrial scale 결과

---

## 🎯 연구 분야별 적합도

| 연구 분야 | 적합도 | 참석 이유 |
|----------|--------|----------|
| **합성생물학** | ★★★★★ | 바이오엔지니어링 및 설계 핵심 초점 |
| **대사공학** | ★★★★★ | 경로 최적화, C1 발효 |
| **머신러닝/AI** | ★★★★☆ | 회로 설계를 위한 ML, 빅데이터 분석 |
| **지속가능성** | ★★★★☆ | 플라스틱 분해, CO₂ 활용 |
| **산업 생명공학** | ★★★★☆ | Scale-up, 상업적 응용 |

---

## 💡 핵심 질문

1. **플라스틱 분해**: 산업 규모 플라스틱 재활용을 위해 필요한 효소 개선은? 경제적 타당성은?

2. **유전자 발현 제어**: Translational coupling이 다양한 유전적 맥락에서 얼마나 예측 가능? 제한사항은?

3. **머신러닝**: 필요한 훈련 데이터의 품질과 양은? Distribution shift를 어떻게 처리?

4. **Acetogens**: 산업 C1 발효의 핵심 bottleneck은? 생산성을 어떻게 개선?

5. **상업적 translation**: 어떤 접근법이 상업화에 가장 가까운가?

---

## 🤝 네트워킹 기회

- **노명현**: 효소 진화, 플라스틱 분해, KRICT 협력
  - *타겟*: 효소 공학자, 플라스틱 재활용 관심자

- **한용희 & 신종오**: 전남대학교 합성생물학 그룹, ML 응용
  - *타겟*: 합성생물학자, ML 응용 연구자

- **최동희**: 빅데이터 분석, SKKU 시스템생물학
  - *타겟*: 생물정보학자, 시스템생물학자

- **조병관**: Acetogen 엔지니어링, KAIST 협력, 산업 파트너십
  - *타겟*: 대사공학자, C1 발효 관심자

---

## 🔬 필수 배경 지식

### 플라스틱 분해 효소
- **PETase**: PET 가수분해 → MHET (mono(2-hydroxyethyl) terephthalate)
- **MHETase**: MHET 가수분해 → TPA + EG (단량체)
- **출처**: *Ideonella sakaiensis*, thermophilic bacteria, fungi
- **엔지니어링**: 열안정성 (PET Tm ~70°C), 활성, 기질 범위
- **응용**: 소비자 폐 PET 재활용, bioaugmentation

### Translational Coupling
- **메커니즘**: Gene A 번역을 완료한 Ribosome이 gene B에서 재개시
- **요구사항**: 짧은 inter-cistronic 거리 (5-50 nt), overlapping stop/start, secondary structure 방지
- **장점**: 화학양론적 발현, RNase로부터 보호, 부담 감소
- **예**: Natural operons (*lac*, *trp*), synthetic pathways

### 합성생물학에서의 머신러닝

| 응용 | 입력 | 출력 | ML 방법 |
|------|------|------|---------|
| **Promoter 설계** | DNA sequence | 발현 강도 | CNN, RF |
| **RBS Calculator** | 5'UTR sequence | Translation rate | Thermodynamic model + ML |
| **Circuit 예측** | Circuit topology + parts | Dynamics | Neural ODE, GNN |
| **Directed Evolution** | Mutation + fitness 데이터 | Next variants | Gaussian process, RL |

### Acetogenic Bacteria
- **정의**: Wood-Ljungdahl (WL) pathway를 사용하여 CO₂/CO 고정하는 세균
- **주요 생물**: *Clostridium autoethanogenum*, *C. ljungdahlii*, *Moorella thermoacetica*
- **에너지 대사**: Chemolithoautotrophic (CO/CO₂/H₂를 에너지 + 탄소로)
- **산업 응용**: LanzaTech (CO에서 에탄올), BASF (화학물질)
- **도전과제**: 느린 성장, 낮은 제품 역가, O₂ 민감성, 유전 도구

### C1 Gas Fermentation
- **C1 가스**: CO, CO₂, CH₄ (단일 탄소 화합물)
- **출처**: 제철소 off-gas, syngas, CO₂ 포집
- **장점**: 폐가스 사용, 식품과 경쟁 않음 (vs. 당 발효)
- **생성물**: 연료 (에탄올, 부탄올), 화학물질 (acetate, lactate, acetone)
- **경제성**: 가스 비용/가용성, 제품 가치, 생산성에 의존

---

## 🚦 의사결정 가이드

**참석 추천**:
- 합성생물학 및 대사공학
- 머신러닝 응용
- 지속가능한 생명공학 (플라스틱, CO₂)
- 산업 생명공학 및 scale-up

**다른 세션 고려**:
- S1, S4, S5 - 병원균 생물학 우선
- S2, S9, S10, S11 - 마이크로바이옴 연구 우선
- S7, S16, S20 - 임상 응용 우선

---

## ⏰ 시간대 충돌 (Day 3 오전, 09:00-11:00)

**동시 진행 세션**:
- S17 (Zoonosis and One Health) - Convention Hall 1
- S19 (Biosafety Management) - Rm 304+305

**선택 기준**:
- **S18 선택**: 합성생물학, 대사공학, 지속가능성 우선
- **S17 선택**: 인수공통감염병, One Health, 백신 개발 우선
- **S19 선택**: 생물안전 규제, LMO 준수 우선 (틈새 주제)
