# Work Plan: Improved Community Merging (v2)

## Context

### Original Request
Community merging improvement to address:
- "잘못 들러붙는것을 피할 수 없다" - False merges from forced anchor assignment
- Need modularity-based resolution selection instead of forced 10 anchors
- Preserve niche/emerging topics instead of forcing everything into anchors

### Research Findings (SOTA Methods)

| Method | Key Insight | Applicable |
|--------|-------------|------------|
| **Microsoft GraphRAG** | Hierarchical Leiden with auto-resolution via modularity | YES - replaces fixed anchor count |
| **t-NEB** | Density-based merge validation, false merge prevention | YES - high threshold validation |
| **GNN Soft Clustering** | Overlapping communities, boundary papers | PARTIAL - preserve boundary papers |

### Problem with v1 Plan
1. **Forced 10 anchors** - Arbitrary, ignores natural cluster structure
2. **Low min_similarity=0.05** - Too aggressive, creates false merges
3. **Orphan bucket** - Lumps unrelated topics together

### Improved Approach (v2)
1. **Auto-resolution**: Use modularity to find optimal Leiden resolution
2. **High threshold**: min_similarity >= 0.7 for merging (strict)
3. **Preserve niche**: Keep communities above paper threshold as "Emerging Topics"
4. **No forced merging**: If similarity < threshold, keep separate

---

## Work Objectives

### Core Objective
Implement modularity-based community detection with conservative merging to achieve 90%+ coverage while minimizing false merges.

### Key Principles
- **Quality over quantity**: Better to have 25 good clusters than 15 forced merges
- **Preserve structure**: Modularity-optimized resolution respects natural boundaries
- **Fail-safe merging**: Only merge when clearly similar (0.7+ Jaccard)
- **Emerging topics**: Small but coherent clusters become "Emerging Topics" category

### Deliverables
1. `find_optimal_resolution()` - Modularity-based resolution finder
2. `calculate_similarity_matrix()` - Pairwise community similarities
3. `conservative_merge()` - High-threshold merging with validation
4. `categorize_communities()` - Major / Emerging / Niche classification
5. Updated CLI with new parameters
6. New output: `level_optimal.json` and `merged_conservative.json`

### Definition of Done
- [ ] Optimal resolution automatically selected via modularity
- [ ] No forced merging below 0.7 similarity threshold
- [ ] Small coherent topics preserved as "Emerging Topics"
- [ ] 90%+ coverage with fewer than 10% false merge rate
- [ ] OVERVIEW.md shows hierarchical structure

---

## Guardrails

### Must Have
- Modularity-based optimal resolution selection
- Similarity threshold >= 0.7 for any merge
- "Emerging Topics" category for small but distinct communities
- Merge validation: check entity type diversity post-merge
- CLI backward compatibility with v1 flags

### Must NOT Have
- Forced anchor count (no `--anchor-count=10`)
- Low similarity threshold (no `min_similarity < 0.5`)
- "Miscellaneous" bucket that lumps unrelated topics
- Breaking changes to existing community detection

---

## Task Flow and Dependencies

```
[T1] Implement optimal resolution finder
         |
         v
[T2] Implement similarity matrix computation
         |
         v
[T3] Implement conservative merge algorithm
         |
         v
[T4] Implement community categorization
         |
         v
[T5] Update CLI and integrate with pipeline
         |
         v
[T6] Generate hierarchical OVERVIEW
         |
         v
[T7] Validate coverage and merge quality
```

---

## Detailed TODOs

### T1: Implement Optimal Resolution Finder
**Location**: `graph_rag_analysis_748_v2.py` (new function)
**Acceptance Criteria**:
- [ ] `find_optimal_resolution(graph, resolution_range=(0.1, 4.0), steps=20) -> float`
- [ ] Compute modularity for each resolution using Leiden
- [ ] Return resolution with maximum modularity
- [ ] Log modularity curve for debugging

**Implementation Notes**:
```python
import numpy as np
from cdlib import algorithms, evaluation

def find_optimal_resolution(
    graph: nx.Graph,
    resolution_range: tuple = (0.1, 4.0),
    steps: int = 20
) -> tuple[float, dict]:
    """
    Find optimal Leiden resolution via modularity maximization.

    Returns:
        (optimal_resolution, modularity_scores)
    """
    resolutions = np.linspace(resolution_range[0], resolution_range[1], steps)
    modularity_scores = {}

    for res in resolutions:
        communities = algorithms.leiden(graph, resolution=res)
        # Newman-Girvan modularity
        modularity = evaluation.newman_girvan_modularity(graph, communities).score
        modularity_scores[res] = modularity
        print(f"  Resolution {res:.2f}: modularity={modularity:.4f}, communities={len(communities.communities)}")

    optimal_res = max(modularity_scores, key=modularity_scores.get)
    print(f"\n  Optimal resolution: {optimal_res:.2f} (modularity={modularity_scores[optimal_res]:.4f})")

    return optimal_res, modularity_scores
```

**Rationale**: GraphRAG uses similar approach - modularity tells us when communities are "naturally" separated vs artificially split.

---

### T2: Implement Similarity Matrix Computation
**Location**: `graph_rag_analysis_748_v2.py` (new function)
**Acceptance Criteria**:
- [ ] `compute_similarity_matrix(communities) -> Dict[tuple, float]`
- [ ] Use Jaccard similarity on entity sets (not papers)
- [ ] Only compute for pairs where both have >= 3 papers (filter noise)
- [ ] Return sparse dict of (comm_id_1, comm_id_2) -> similarity

**Implementation Notes**:
```python
from itertools import combinations

def compute_similarity_matrix(
    communities: List[Dict],
    min_papers: int = 3
) -> Dict[tuple, float]:
    """
    Compute pairwise Jaccard similarity on entity sets.

    Only considers communities with >= min_papers.
    Returns sparse dict: (id1, id2) -> similarity
    """
    # Filter by paper count
    valid_comms = [c for c in communities if c.get("paper_count", 0) >= min_papers]

    similarities = {}

    for c1, c2 in combinations(valid_comms, 2):
        entities1 = extract_entity_ids(c1)
        entities2 = extract_entity_ids(c2)

        if not entities1 or not entities2:
            continue

        intersection = len(entities1 & entities2)
        union = len(entities1 | entities2)
        jaccard = intersection / union if union > 0 else 0.0

        if jaccard > 0:  # Only store non-zero
            similarities[(c1["community_id"], c2["community_id"])] = jaccard

    return similarities
```

---

### T3: Implement Conservative Merge Algorithm
**Location**: `graph_rag_analysis_748_v2.py` (new function)
**Acceptance Criteria**:
- [ ] `conservative_merge(communities, similarities, min_similarity=0.7) -> List[Dict]`
- [ ] Only merge if similarity >= threshold (0.7 default)
- [ ] Validate merge: entity type diversity check (prevent "everything is METHOD")
- [ ] Use union-find for transitive merging (if A~B and B~C, merge all three)
- [ ] Preserve original community IDs in `merged_from`

**Key Difference from v1**:
- v1: Force all small communities into anchors
- v2: Only merge when clearly similar, keep distinct clusters separate

**Implementation Notes**:
```python
class UnionFind:
    """Union-Find for transitive merge tracking."""
    def __init__(self, items):
        self.parent = {item: item for item in items}
        self.rank = {item: 0 for item in items}

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px == py:
            return
        if self.rank[px] < self.rank[py]:
            px, py = py, px
        self.parent[py] = px
        if self.rank[px] == self.rank[py]:
            self.rank[px] += 1


def validate_merge(comm1: Dict, comm2: Dict) -> bool:
    """
    Validate that merge doesn't create overly homogeneous cluster.

    Returns False if merged cluster would have >80% of one entity type.
    """
    entities1 = extract_entity_ids(comm1)
    entities2 = extract_entity_ids(comm2)
    all_entities = entities1 | entities2

    if len(all_entities) < 5:
        return True  # Too small to judge

    type_counts = Counter(e.split(":")[0] for e in all_entities)
    max_type_ratio = max(type_counts.values()) / len(all_entities)

    return max_type_ratio < 0.8  # Must have some diversity


def conservative_merge(
    communities: List[Dict],
    similarities: Dict[tuple, float],
    min_similarity: float = 0.7
) -> List[Dict]:
    """
    Merge communities only when clearly similar.

    Key differences from v1:
    - No forced anchor assignment
    - High similarity threshold (0.7)
    - Merge validation to prevent bad merges
    - Transitive merging via union-find
    """
    comm_ids = [c["community_id"] for c in communities]
    comm_lookup = {c["community_id"]: c for c in communities}

    uf = UnionFind(comm_ids)

    # Merge similar pairs
    for (id1, id2), sim in similarities.items():
        if sim >= min_similarity:
            c1, c2 = comm_lookup[id1], comm_lookup[id2]
            if validate_merge(c1, c2):
                uf.union(id1, id2)
                print(f"  Merging {id1} + {id2} (similarity={sim:.3f})")

    # Group by root
    groups = defaultdict(list)
    for cid in comm_ids:
        root = uf.find(cid)
        groups[root].append(cid)

    # Build merged communities
    merged = []
    for root, member_ids in groups.items():
        members = set()
        papers = set()
        merged_from = []

        for cid in member_ids:
            comm = comm_lookup[cid]
            members.update(comm["members"])
            papers.update(extract_paper_dois(comm))
            merged_from.append(cid)

        merged.append({
            "community_id": root,
            "members": list(members),
            "paper_count": len(papers),
            "merged_from": sorted(merged_from),
            "merge_count": len(merged_from)
        })

    return sorted(merged, key=lambda x: x["paper_count"], reverse=True)
```

---

### T4: Implement Community Categorization
**Location**: `graph_rag_analysis_748_v2.py` (new function)
**Acceptance Criteria**:
- [ ] `categorize_communities(communities, thresholds) -> Dict[str, List[Dict]]`
- [ ] Categories:
  - **Major Themes**: >= 30 papers (natural large clusters)
  - **Emerging Topics**: 10-29 papers (distinct but smaller)
  - **Niche Areas**: 3-9 papers (specialized, keep if coherent)
  - **Noise**: < 3 papers (ignore in OVERVIEW)
- [ ] Return categorized dict

**Implementation Notes**:
```python
def categorize_communities(
    communities: List[Dict],
    major_threshold: int = 30,
    emerging_threshold: int = 10,
    niche_threshold: int = 3
) -> Dict[str, List[Dict]]:
    """
    Categorize communities by size and coherence.

    Categories:
    - major: >= 30 papers (main research themes)
    - emerging: 10-29 papers (distinct emerging topics)
    - niche: 3-9 papers (specialized areas)
    - noise: < 3 papers (ignored)
    """
    categories = {
        "major": [],
        "emerging": [],
        "niche": [],
        "noise": []
    }

    for comm in communities:
        paper_count = comm.get("paper_count", 0)

        if paper_count >= major_threshold:
            categories["major"].append(comm)
        elif paper_count >= emerging_threshold:
            categories["emerging"].append(comm)
        elif paper_count >= niche_threshold:
            categories["niche"].append(comm)
        else:
            categories["noise"].append(comm)

    # Sort each category by paper count
    for cat in categories:
        categories[cat].sort(key=lambda x: x["paper_count"], reverse=True)

    return categories
```

**Key Insight**: Instead of forcing everything into 15 themes, we acknowledge that research landscapes have:
- A few major themes (5-8)
- Several emerging areas (10-15)
- Many niche specializations (20+)

This is more accurate than artificial consolidation.

---

### T5: Update CLI and Integrate with Pipeline
**Location**: `graph_rag_analysis_748_v2.py` (modify `parse_args()` and `main()`)
**Acceptance Criteria**:
- [ ] Add `--auto-resolution` flag (use modularity optimization)
- [ ] Add `--merge-threshold` flag (default: 0.7)
- [ ] Add `--preserve-emerging` flag (default: True)
- [ ] Keep v1 flags for backward compatibility but deprecate
- [ ] New step: "Finding optimal resolution" before community detection

**Implementation Notes**:
```python
# In parse_args():
parser.add_argument(
    '--auto-resolution', action='store_true',
    help='Use modularity to find optimal Leiden resolution (recommended)'
)
parser.add_argument(
    '--merge-threshold', type=float, default=0.7,
    help='Minimum Jaccard similarity for merging (default: 0.7, higher = stricter)'
)
parser.add_argument(
    '--preserve-emerging', action='store_true', default=True,
    help='Preserve emerging topics instead of forcing into major themes'
)

# Deprecation warnings for v1 flags
parser.add_argument(
    '--merge-communities', action='store_true',
    help='[DEPRECATED] Use --auto-resolution instead'
)
parser.add_argument(
    '--min-similarity', type=float, default=None,
    help='[DEPRECATED] Use --merge-threshold instead'
)


# In main():
if args.auto_resolution:
    print("\n[2.5/7] Finding optimal resolution...")
    optimal_res, modularity_scores = find_optimal_resolution(kg.graph)

    # Use optimal resolution for community detection
    resolutions = [optimal_res]  # Single optimal resolution

    # Save modularity curve
    mod_path = OUTPUT_DIR / 'modularity_curve.json'
    with open(mod_path, 'w') as f:
        json.dump({str(k): v for k, v in modularity_scores.items()}, f, indent=2)
else:
    resolutions = [0.5, 1.0, 2.0, 4.0]  # Default multi-resolution

# Step 3: Detect communities with chosen resolutions
print("\n[3/7] Detecting communities...")
communities_by_level = analyzer.detect_communities(kg.graph, resolutions=resolutions)

# Step 3.5: Conservative merge (if enabled)
if args.auto_resolution or args.merge_communities:
    print("\n[3.5/7] Conservative community merging...")

    # Get communities at optimal (or 0.5) resolution
    target_res = optimal_res if args.auto_resolution else 0.5
    level_path = OUTPUT_DIR / 'communities' / f'level_{target_res}.json'
    with open(level_path) as f:
        communities_json = json.load(f)

    # Add paper counts
    for comm in communities_json:
        comm["paper_count"] = len(extract_paper_dois(comm))

    # Compute similarities
    print("  Computing similarity matrix...")
    similarities = compute_similarity_matrix(communities_json)

    # Merge conservatively
    threshold = args.merge_threshold or 0.7
    print(f"  Merging with threshold={threshold}...")
    merged = conservative_merge(communities_json, similarities, min_similarity=threshold)

    # Categorize
    categories = categorize_communities(merged)
    print(f"  Categories: {len(categories['major'])} major, {len(categories['emerging'])} emerging, {len(categories['niche'])} niche")

    # Save outputs
    merged_path = OUTPUT_DIR / 'communities' / 'merged_conservative.json'
    with open(merged_path, 'w') as f:
        json.dump({
            "metadata": {
                "resolution": target_res,
                "merge_threshold": threshold,
                "total_communities": len(merged)
            },
            "communities": merged,
            "categories": {k: [c["community_id"] for c in v] for k, v in categories.items()}
        }, f, indent=2)

    # Calculate coverage
    total_papers = 748
    major_coverage = sum(c["paper_count"] for c in categories["major"])
    emerging_coverage = sum(c["paper_count"] for c in categories["emerging"])
    total_coverage = major_coverage + emerging_coverage

    print(f"\n  Coverage stats:")
    print(f"    Major themes ({len(categories['major'])}): {major_coverage} papers ({major_coverage/total_papers*100:.1f}%)")
    print(f"    Emerging topics ({len(categories['emerging'])}): {emerging_coverage} papers ({emerging_coverage/total_papers*100:.1f}%)")
    print(f"    Combined: {total_coverage} papers ({total_coverage/total_papers*100:.1f}%)")
```

---

### T6: Generate Hierarchical OVERVIEW
**Location**: `graph_rag_analysis_748_v2.py` (new function)
**Acceptance Criteria**:
- [ ] `generate_hierarchical_overview(output_dir, categories, stats) -> Path`
- [ ] Separate sections for Major Themes, Emerging Topics
- [ ] Show merge count for consolidated clusters
- [ ] Coverage statistics per category

**Implementation Notes**:
```python
def generate_hierarchical_overview(
    output_dir: Path,
    categories: Dict[str, List[Dict]],
    stats: Dict[str, Any],
    summaries_dir: Path
) -> Path:
    """Generate OVERVIEW.md with hierarchical structure."""

    output_file = output_dir / "OVERVIEW.md"
    total_papers = stats["total_papers"]

    lines = []
    lines.append(f"# Virtual Cell Research Landscape ({total_papers} Papers)")
    lines.append("")
    lines.append("## Executive Summary")
    lines.append("")

    major_count = len(categories["major"])
    emerging_count = len(categories["emerging"])
    major_papers = sum(c["paper_count"] for c in categories["major"])
    emerging_papers = sum(c["paper_count"] for c in categories["emerging"])

    lines.append(f"This landscape identifies **{major_count} major research themes** covering {major_papers} papers ({major_papers/total_papers*100:.1f}%),")
    lines.append(f"plus **{emerging_count} emerging topics** covering {emerging_papers} papers ({emerging_papers/total_papers*100:.1f}%).")
    lines.append("")
    lines.append("---")
    lines.append("")

    # Major Themes Section
    lines.append("## Major Research Themes")
    lines.append("")

    for rank, comm in enumerate(categories["major"], 1):
        comm_id = comm["community_id"]
        paper_count = comm["paper_count"]
        merge_count = comm.get("merge_count", 1)

        # Parse summary
        summary_file = summaries_dir / f"community_{comm_id}.md"
        summary = parse_community_summary(summary_file) if summary_file.exists() else {}

        name = get_community_name(summary, comm_id) if summary else f"Theme {comm_id}"

        lines.append(f"### {rank}. {name} ({paper_count} papers)")
        if merge_count > 1:
            lines.append(f"*Consolidated from {merge_count} related clusters*")
        lines.append("")

        if summary.get("research_focus"):
            lines.append(f"**Focus**: {summary['research_focus']}")
            lines.append("")
        if summary.get("top_entities"):
            lines.append(f"**Key Entities**: {', '.join(summary['top_entities'][:5])}")
            lines.append("")

        lines.append("---")
        lines.append("")

    # Emerging Topics Section
    lines.append("## Emerging Topics")
    lines.append("")
    lines.append("*Distinct research areas with 10-29 papers each*")
    lines.append("")

    for rank, comm in enumerate(categories["emerging"], 1):
        comm_id = comm["community_id"]
        paper_count = comm["paper_count"]

        summary_file = summaries_dir / f"community_{comm_id}.md"
        summary = parse_community_summary(summary_file) if summary_file.exists() else {}

        name = get_community_name(summary, comm_id) if summary else f"Topic {comm_id}"
        focus = summary.get("research_focus", "")[:100] if summary else ""

        lines.append(f"**{rank}. {name}** ({paper_count} papers)")
        if focus:
            lines.append(f"   {focus}...")
        lines.append("")

    lines.append("---")
    lines.append("")
    lines.append("## Coverage Statistics")
    lines.append("")
    lines.append(f"| Category | Count | Papers | Coverage |")
    lines.append(f"|----------|-------|--------|----------|")
    lines.append(f"| Major Themes | {major_count} | {major_papers} | {major_papers/total_papers*100:.1f}% |")
    lines.append(f"| Emerging Topics | {emerging_count} | {emerging_papers} | {emerging_papers/total_papers*100:.1f}% |")
    lines.append(f"| **Total** | {major_count + emerging_count} | {major_papers + emerging_papers} | {(major_papers + emerging_papers)/total_papers*100:.1f}% |")
    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append("*Generated by Graph RAG v2 (modularity-optimized, conservative merge)*")

    output_file.write_text("\n".join(lines))
    return output_file
```

---

### T7: Validate Coverage and Merge Quality
**Location**: Command line validation
**Acceptance Criteria**:
- [ ] Coverage >= 90% with Major + Emerging
- [ ] False merge rate < 10% (manual spot check)
- [ ] No "catch-all" buckets with unrelated topics
- [ ] Entity diversity preserved in merged clusters

**Validation Commands**:
```bash
# Run with auto-resolution
python graph_rag_analysis_748_v2.py --auto-resolution --merge-threshold 0.7

# Check coverage
python -c "
import json
with open('data/papers/by-collection/virtual-cell-50/graph-rag-748/communities/merged_conservative.json') as f:
    data = json.load(f)

categories = data['categories']
communities = {c['community_id']: c for c in data['communities']}

major_papers = sum(communities[cid]['paper_count'] for cid in categories['major'])
emerging_papers = sum(communities[cid]['paper_count'] for cid in categories['emerging'])

print(f'Major themes: {len(categories[\"major\"])} clusters, {major_papers} papers')
print(f'Emerging topics: {len(categories[\"emerging\"])} clusters, {emerging_papers} papers')
print(f'Total coverage: {(major_papers + emerging_papers) / 748 * 100:.1f}%')
"

# Validate entity diversity in largest merged cluster
python -c "
import json
from collections import Counter

with open('data/papers/by-collection/virtual-cell-50/graph-rag-748/communities/merged_conservative.json') as f:
    data = json.load(f)

largest = data['communities'][0]  # Sorted by size
entities = [m for m in largest['members'] if not m.startswith('https://doi.org/')]
types = Counter(e.split(':')[0] for e in entities)

print(f'Largest cluster: {largest[\"paper_count\"]} papers, {len(entities)} entities')
print(f'Entity type distribution: {dict(types)}')
max_ratio = max(types.values()) / len(entities)
print(f'Max type ratio: {max_ratio:.1%} (should be < 80%)')
"
```

---

## Commit Strategy

### Commit 1: Add modularity-based resolution finder
```
feat(graph-rag): Add modularity-based optimal resolution finder

- find_optimal_resolution(): Scan resolution range, pick max modularity
- Saves modularity_curve.json for analysis
- GraphRAG-style approach to hierarchical community detection
```

### Commit 2: Implement conservative merge with validation
```
feat(graph-rag): Implement conservative community merging (v2)

- compute_similarity_matrix(): Pairwise Jaccard on entity sets
- conservative_merge(): High threshold (0.7), validation checks
- UnionFind for transitive merge tracking
- validate_merge(): Prevent homogeneous clusters
```

### Commit 3: Add community categorization
```
feat(graph-rag): Add community categorization (Major/Emerging/Niche)

- categorize_communities(): Size-based classification
- Major >= 30 papers, Emerging 10-29, Niche 3-9
- Preserves research landscape structure
```

### Commit 4: Integrate and generate hierarchical OVERVIEW
```
feat(graph-rag): Integrate v2 merging with hierarchical OVERVIEW

- Add --auto-resolution, --merge-threshold, --preserve-emerging flags
- generate_hierarchical_overview(): Separate Major/Emerging sections
- Save merged_conservative.json with metadata
```

---

## Success Criteria

| Metric | Target | v1 Problem |
|--------|--------|------------|
| Major + Emerging coverage | >= 90% | 58.6% |
| False merge rate | < 10% | Unknown (forced merges) |
| Entity type diversity | < 80% single type | Not validated |
| "Miscellaneous" bucket | 0 papers | Catch-all for orphans |
| Natural cluster count | Data-driven | Forced to 10 |

---

## Comparison: v1 vs v2

| Aspect | v1 (Current Plan) | v2 (This Plan) |
|--------|-------------------|----------------|
| Resolution | Fixed multi-level | Auto-optimized via modularity |
| Anchor selection | Top-10 by size | Data-driven (no forced count) |
| Merge threshold | 0.05 (too low) | 0.7 (strict) |
| Orphan handling | "Miscellaneous" bucket | Keep as "Emerging" if coherent |
| Validation | None | Entity diversity check |
| Output structure | Flat list | Hierarchical (Major/Emerging/Niche) |

---

## Risk Mitigation

| Risk | Mitigation |
|------|------------|
| Under-merging (too many clusters) | Lower threshold to 0.5 if needed |
| Optimal resolution too extreme | Constrain range to (0.3, 2.0) |
| Slow on large graphs | Cache similarity matrix; skip if exists |
| Category thresholds suboptimal | Make thresholds CLI configurable |

---

*Plan created: 2026-02-03*
*Version: 2.0 (replaces community-merging.md)*
*Key improvement: Modularity-based + high threshold = no forced false merges*

---

PLAN_READY: .omc/plans/community-merging-v2.md
