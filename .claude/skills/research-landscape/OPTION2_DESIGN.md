# Option 2 Design: Conceptual Framework Auto-Generation

## 목표

논문 landscape를 **문제-해결 계통도**로 자동 재구성하여 연사들을 이 framework에 매핑

### 현재 (Option 1)
```
Session Landscape:
├── Reviews (리뷰 논문들)
├── Anchors (거점 논문들)
├── Trends (최신 동향)
└── Speakers mapped to papers
```

### 목표 (Option 2)
```
Conceptual Framework:
├── 1. 핵심 문제 (Core Problems)
│   ├── 문제 1.1: [자동 추출된 문제 정의]
│   │   ├── 관련 anchor papers
│   │   ├── 주요 논쟁점 (review papers)
│   │   └── 세션 내 연사: A, B
│   └── 문제 1.2: [또 다른 문제]
│       └── ...
│
├── 2. 접근 방식 (Approaches)
│   ├── 방법론 A: [자동 추출]
│   │   ├── 이론적 기초 (anchor papers)
│   │   ├── 최신 발전 (trends)
│   │   └── 세션 내 연사: C, D
│   └── 방법론 B: [실험적 접근]
│       └── ...
│
├── 3. 한계점 & 돌파구 (Limitations & Breakthroughs)
│   └── Emerging concepts → 연사 E
│
└── 4. 미래 방향 (Future Directions)
    └── ...
```

---

## 핵심 도전 과제

### 1. Concept Extraction (개념 추출)
**문제**: 논문 제목/초록에서 핵심 개념을 어떻게 추출할 것인가?

**접근**:
- **Option A (Simple)**: OpenAlex concepts 활용
  - 장점: 이미 분류됨, 빠름
  - 단점: 너무 broad (e.g., "Medicine", "Biology")

- **Option B (Advanced)**: Title/abstract keyword extraction
  - TF-IDF로 중요 키워드 추출
  - 장점: 세밀함
  - 단점: 구현 복잡, NLP 필요

- **Option C (Hybrid)**: OpenAlex concepts + keyword co-occurrence
  - 장점: 균형
  - **추천**: 이 방식 사용

### 2. Hierarchical Classification (계층 분류)
**문제**: 논문을 "문제 / 방법 / 한계" 카테고리로 어떻게 자동 분류?

**접근**:
- **Rule-based heuristics** (title/abstract pattern matching):
  ```python
  if "challenge" in title or "problem" in abstract:
      category = "Problem"
  elif "approach" in title or "method" in abstract:
      category = "Approach"
  elif "limitation" in abstract or "future" in title:
      category = "Limitation"
  ```

- **Concept co-occurrence** (관련 논문끼리 그룹화):
  - Papers with similar concepts → same cluster
  - Cluster의 주요 concept → framework node

- **Citation patterns**:
  - Anchor papers (heavily cited) → Foundational problems
  - Recent trends → Emerging solutions
  - Bridge papers → Cross-cutting approaches

### 3. Framework Structure Generation (계통도 구조 생성)
**문제**: 계층 구조를 어떻게 자동으로 만들 것인가?

**전략**:

#### Level 1: Top-level categories (고정)
```
1. 핵심 문제 (Core Problems)
2. 접근 방식 (Approaches)
3. 한계점 & 돌파구 (Limitations & Breakthroughs)
4. 미래 방향 (Future Directions)
```

#### Level 2: Sub-categories (자동 생성)
- Concept clustering (K-means or hierarchical)
- Top N concepts → sub-categories

#### Level 3: Individual papers
- 각 논문을 가장 관련성 높은 sub-category에 배치

---

## 구현 전략

### Phase 1: MVP (Simple Heuristics)

**Input**: Landscape from Option 1
```python
landscape = {
    'reviews': [...],
    'anchors': [...],
    'recent_trends': [...],
    'trend_clusters': {...}
}
```

**Processing**:
1. Extract top N concepts from all papers (N=10)
2. Classify papers into 4 top-level categories (rule-based)
3. Cluster papers by concept similarity (K-means)
4. Generate framework structure

**Output**: Conceptual framework
```python
framework = {
    'core_problems': [
        {
            'problem': "Granuloma formation mechanisms",
            'concepts': ['granuloma', 'inflammation'],
            'anchor_papers': [...],
            'review_papers': [...],
            'speakers': ['Speaker A', 'Speaker B']
        }
    ],
    'approaches': [...],
    'limitations': [...],
    'future_directions': [...]
}
```

### Phase 2: Enhanced (NLP + ML)

**Additional capabilities**:
- Abstract text analysis (TF-IDF)
- More sophisticated classification (not just rule-based)
- Concept relationship graph (A → B → C)

---

## 알고리즘 상세

### Algorithm 1: Concept Extraction

```python
def extract_key_concepts(papers, top_k=10):
    """
    Extract top K concepts from paper collection.

    Uses OpenAlex concepts + co-occurrence analysis.
    """
    # Step 1: Count concept frequencies
    concept_counts = Counter()
    for paper in papers:
        for concept in paper['concepts']:
            concept_counts[concept['display_name']] += concept['score']

    # Step 2: Get top K
    top_concepts = [c for c, _ in concept_counts.most_common(top_k)]

    # Step 3: Filter out too generic (optional)
    generic = ['Medicine', 'Biology', 'Chemistry']
    top_concepts = [c for c in top_concepts if c not in generic]

    return top_concepts
```

### Algorithm 2: Paper Classification

```python
def classify_paper(paper):
    """
    Classify paper into: Problem / Approach / Limitation / Future.

    Uses title + abstract heuristics.
    """
    title = paper.get('title', '').lower()
    abstract = paper.get('abstract', '').lower() if 'abstract' in paper else ''

    # Heuristic rules
    problem_keywords = ['challenge', 'problem', 'difficulty', 'issue']
    approach_keywords = ['approach', 'method', 'technique', 'strategy', 'therapy']
    limitation_keywords = ['limitation', 'drawback', 'weakness']
    future_keywords = ['future', 'perspective', 'outlook', 'emerging']

    # Score each category
    scores = {
        'problem': sum(kw in title or kw in abstract for kw in problem_keywords),
        'approach': sum(kw in title or kw in abstract for kw in approach_keywords),
        'limitation': sum(kw in title or kw in abstract for kw in limitation_keywords),
        'future': sum(kw in title or kw in abstract for kw in future_keywords)
    }

    # Default based on paper type
    if paper in anchors:  # Foundational → Problem definition
        scores['problem'] += 2
    elif paper in recent_trends:  # Recent → Approach or Future
        scores['approach'] += 1
        scores['future'] += 1

    # Return category with highest score
    return max(scores, key=scores.get)
```

### Algorithm 3: Concept Clustering

```python
def cluster_papers_by_concepts(papers, num_clusters=5):
    """
    Cluster papers using concept similarity.

    Uses Jaccard similarity on concepts.
    """
    # Build concept vectors for each paper
    all_concepts = set()
    for paper in papers:
        all_concepts.update(c['display_name'] for c in paper['concepts'])

    concept_list = list(all_concepts)

    # Create binary vectors (paper has concept or not)
    vectors = []
    for paper in papers:
        paper_concepts = {c['display_name'] for c in paper['concepts']}
        vector = [1 if c in paper_concepts else 0 for c in concept_list]
        vectors.append(vector)

    # K-means clustering
    from sklearn.cluster import KMeans
    kmeans = KMeans(n_clusters=num_clusters, random_state=42)
    labels = kmeans.fit_predict(vectors)

    # Group papers by cluster
    clusters = {}
    for i, label in enumerate(labels):
        if label not in clusters:
            clusters[label] = []
        clusters[label].append(papers[i])

    # Name each cluster by top concepts
    cluster_names = {}
    for label, cluster_papers in clusters.items():
        concept_counts = Counter()
        for paper in cluster_papers:
            for concept in paper['concepts']:
                concept_counts[concept['display_name']] += 1

        # Top 2 concepts as cluster name
        top_2 = [c for c, _ in concept_counts.most_common(2)]
        cluster_names[label] = ' & '.join(top_2)

    return clusters, cluster_names
```

### Algorithm 4: Framework Generation

```python
def generate_conceptual_framework(landscape, speakers=None):
    """
    Generate problem-solution framework from landscape.
    """
    framework = {
        'core_problems': [],
        'approaches': [],
        'limitations': [],
        'future_directions': []
    }

    all_papers = landscape['reviews'] + landscape['anchors'] + landscape.get('recent_trends', [])

    # Step 1: Extract key concepts
    key_concepts = extract_key_concepts(all_papers, top_k=10)

    # Step 2: Classify each paper
    classified = {
        'problem': [],
        'approach': [],
        'limitation': [],
        'future': []
    }

    for paper in all_papers:
        category = classify_paper(paper)
        classified[category].append(paper)

    # Step 3: Cluster within each category
    for category, papers in classified.items():
        if not papers:
            continue

        if len(papers) >= 3:  # Only cluster if enough papers
            clusters, names = cluster_papers_by_concepts(papers, num_clusters=min(3, len(papers)//2))

            for label, cluster_papers in clusters.items():
                node = {
                    'name': names[label],
                    'papers': cluster_papers,
                    'speakers': []  # Will be filled if speaker mapping provided
                }
                framework[category + 's'].append(node)
        else:
            # Too few papers, just group all
            node = {
                'name': key_concepts[0] if key_concepts else category.title(),
                'papers': papers,
                'speakers': []
            }
            framework[category + 's'].append(node)

    # Step 4: Map speakers (if provided)
    if speakers:
        for speaker in speakers:
            # Find best matching node based on speaker's research areas
            # (implementation omitted for brevity)
            pass

    return framework
```

---

## 출력 형식

### Markdown Output Example

```markdown
## 🔬 개념적 Research Framework: Mycobacterial Pathogenesis

*자동 생성된 문제-해결 계통도*

### 1. 핵심 문제 (Core Problems)

#### 1.1 Granuloma Formation & Immune Evasion

**문제 정의**: How do mycobacteria establish persistent infections through granuloma manipulation?

**거점 논문** (이론적 기초):
1. "Histopathologic review of granulomatous inflammation" (2017, 323 cites)
2. "Neutrophils in granulomas" (2019, 109 cites)

**주요 논쟁점** (리뷰 논문):
- Balance between containment and pathology
- Role of neutrophils vs macrophages

**세션 내 연사**:
- **Speaker A (Neutrophil Role)**: Addresses neutrophil function in granuloma maintenance
  - Related to: Anchor paper #2
  - Position: Investigates cellular mechanisms

#### 1.2 Drug Resistance Mechanisms

**문제 정의**: Mechanisms of antibiotic resistance and persistence

**거점 논문**:
1. "Oxidative phosphorylation as drug target" (2017, 120 cites)

**세션 내 연사**:
- **Speaker C (Drug Targets)**: Novel targets for overcoming resistance
  - Related to: Trend cluster "Mycobacterium abscessus"

---

### 2. 접근 방식 (Approaches)

#### 2.1 Host-Directed Therapy

**방법론**: Modulating host immune response rather than targeting pathogen

**이론적 기초**:
- "Host-directed therapies for TB" (2015, 113 cites)

**최신 발전** (2023-2025):
- Immunomodulation approaches (18 papers)
- Autophagy induction (12 papers)

**세션 내 연사**:
- **Speaker B (Host-Directed Therapy)**: Novel immunomodulation strategies
  - Related to: 4 anchor papers, 3 review papers
  - Position: Advancing therapeutic approach

---

### 3. 한계점 & 돌파구 (Limitations & Breakthroughs)

#### 3.1 Emerging Concepts

**새로운 방향들**:
- Internal medicine approaches: 🆕 NEW
- Chemistry-based interventions: 🆕 NEW (not in foundational papers)

---

### 4. 미래 방향 (Future Directions)

[Extracted from recent trends + emerging concepts]
```

---

## 구현 계획

### Week 1: MVP
- [ ] `concept_framework_builder.py` 기본 구현
- [ ] Simple heuristic classification
- [ ] Concept extraction (OpenAlex concepts)
- [ ] Basic clustering (K-means)
- [ ] Framework generation
- [ ] Markdown output

### Week 2: Enhancement
- [ ] Abstract text analysis (if available)
- [ ] Better classification (beyond heuristics)
- [ ] Speaker mapping integration
- [ ] Visualization (optional: network graph)

### Week 3: Testing & Refinement
- [ ] Test on multiple session topics
- [ ] Refine classification rules
- [ ] Optimize clustering parameters
- [ ] Documentation

---

## 성공 지표

1. **Concept Extraction Quality**
   - Top 10 concepts should be meaningful (not too generic)
   - Manual validation: >70% relevance

2. **Classification Accuracy**
   - Papers classified into correct category
   - Manual validation: >60% accuracy (heuristic-based)

3. **Framework Usefulness**
   - Provides clear problem-solution structure
   - Helps understand session organization
   - User survey: >4/5 stars

4. **Speaker Mapping**
   - Speakers correctly positioned in framework
   - Mapping makes sense to domain experts

---

## 한계점 (인정)

1. **No ground truth**: 정답이 없음 (unsupervised)
2. **Heuristic-dependent**: Rule-based → 도메인마다 다를 수 있음
3. **Concept granularity**: OpenAlex concepts가 너무 broad할 수 있음
4. **Abstract availability**: OpenAlex에 abstract가 없는 경우 많음

**완화 전략**:
- 여러 heuristic 조합
- User feedback 기반 refinement
- Conference-specific tuning

---

**Version**: Design v1.0
**Status**: Ready for implementation
**Estimated Time**: 2-3 weeks for MVP + testing
