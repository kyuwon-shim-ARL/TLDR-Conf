# Work Plan: Community Merging for 90%+ Coverage

## Context

### Original Request
커뮤니티 병합 로직 구현:
1. 상위 5-10개 대형 커뮤니티를 "앵커"로 설정
2. 나머지 소형 커뮤니티를 가장 유사한 앵커에 병합
3. 유사도 = 공유 엔티티 수
4. 목표: 15-20개 테마로 90%+ 커버리지

### Current State Analysis
- **Total Papers**: 748
- **Current Coverage**: Top-15 = 58.6% (438 papers), Top-37 = 80%, Top-92 = 90%
- **Community Distribution (level_0.5)**:
  - 166 total communities
  - Very Large (>=100 papers): 2 communities
  - Large (50-100 papers): 5 communities
  - Medium (10-50 papers): 36 communities
  - Small (<10 papers): 123 communities

### Key Files
- Main Script: `/home/kyuwon/projects/MSK2025/graph_rag_analysis_748_v2.py`
- Community Data: `/home/kyuwon/projects/MSK2025/data/papers/by-collection/virtual-cell-50/graph-rag-748/communities/level_0.5.json`
- Stats: `/home/kyuwon/projects/MSK2025/data/papers/by-collection/virtual-cell-50/graph-rag-748/stats.json`
- OVERVIEW: `/home/kyuwon/projects/MSK2025/data/papers/by-collection/virtual-cell-50/graph-rag-748/OVERVIEW.md`

### Research Findings
- Community structure: Each community contains `members` list with paper DOIs and entity IDs
- Entity format: `METHOD:name`, `CONCEPT:name`, `ORGANISM:name`, `DATASET:name`
- Largest community has 344 members (papers + entities combined)
- Paper count requires filtering DOI strings (`https://doi.org/...`)
- **Code structure**: `detect_communities()` returns `communities_by_level` dict keyed by resolution floats (e.g., `communities_by_level[0.5]`)

---

## Work Objectives

### Core Objective
Implement anchor-based community merging to consolidate 166 communities into 15-20 thematic clusters while achieving 90%+ paper coverage.

### Deliverables
1. `merge_communities()` function in `graph_rag_analysis_748_v2.py`
2. Updated `generate_overview()` to use merged communities
3. New merged community JSON output file
4. Updated OVERVIEW.md with merged themes

### Definition of Done
- [ ] 15-20 merged communities covering 90%+ of 748 papers
- [ ] Merged community summaries reflect combined themes
- [ ] OVERVIEW.md displays consolidated research landscape
- [ ] No regression in existing functionality

---

## Guardrails

### Must Have
- Anchor selection based on paper count (not total member count)
- Entity-based similarity metric (shared entities between communities)
- Preserve original community data (create new merged output, don't overwrite)
- CLI flag to enable/disable merging (backward compatibility)

### Must NOT Have
- Hard-coded anchor community IDs
- Modification to original `level_0.5.json` file
- Breaking changes to existing OVERVIEW generation
- LLM-based summarization (keep rule-based approach)

---

## Task Flow and Dependencies

```
[T1] Implement entity extraction helpers
         |
         v
[T2] Implement anchor selection logic
         |
         v
[T3] Implement similarity calculation
         |
         v
[T4] Implement community merging algorithm
         |
         v
[T5] Integrate with main pipeline
         |
         v
[T6] Update OVERVIEW generation
         |
         v
[T7] Test and validate coverage
```

---

## Detailed TODOs

### T1: Implement Entity Extraction Helpers
**Location**: `graph_rag_analysis_748_v2.py` (new helper functions)
**Acceptance Criteria**:
- [ ] `extract_paper_dois(community) -> Set[str]` - Extract paper DOIs from community members
- [ ] `extract_entity_ids(community) -> Set[str]` - Extract entity IDs (METHOD:x, CONCEPT:x, etc.)
- [ ] Handle both paper DOIs and entity IDs in members list

**Implementation Notes**:
```python
def extract_paper_dois(community: Dict) -> Set[str]:
    """Extract paper DOIs from community members."""
    return {m for m in community["members"] if m.startswith("https://doi.org/")}

def extract_entity_ids(community: Dict) -> Set[str]:
    """Extract entity IDs from community members."""
    return {m for m in community["members"] if not m.startswith("https://doi.org/")}
```

---

### T2: Implement Anchor Selection Logic
**Location**: `graph_rag_analysis_748_v2.py` (new function)
**Acceptance Criteria**:
- [ ] `select_anchor_communities(communities, min_papers=30, max_anchors=10) -> List[Dict]`
- [ ] Sort communities by paper count (descending)
- [ ] Select top N communities with >= min_papers as anchors
- [ ] Return list of anchor communities with their paper counts

**Implementation Notes**:
```python
def select_anchor_communities(
    communities: List[Dict],
    min_papers: int = 30,
    max_anchors: int = 10
) -> List[Dict]:
    """Select large communities as anchors for merging."""
    # Add paper_count to each community
    for comm in communities:
        comm["paper_count"] = len(extract_paper_dois(comm))

    # Sort by paper count descending
    sorted_comms = sorted(communities, key=lambda x: x["paper_count"], reverse=True)

    # Select anchors meeting minimum threshold
    anchors = [c for c in sorted_comms if c["paper_count"] >= min_papers][:max_anchors]
    return anchors
```

---

### T3: Implement Similarity Calculation
**Location**: `graph_rag_analysis_748_v2.py` (new function)
**Acceptance Criteria**:
- [ ] `calculate_entity_similarity(comm1, comm2) -> float` - Jaccard similarity on shared entities
- [ ] Consider only entity nodes (not paper DOIs) for similarity
- [ ] Return 0.0 if no shared entities

**Implementation Notes**:
```python
def calculate_entity_similarity(comm1: Dict, comm2: Dict) -> float:
    """Calculate similarity based on shared entities (Jaccard index)."""
    entities1 = extract_entity_ids(comm1)
    entities2 = extract_entity_ids(comm2)

    if not entities1 or not entities2:
        return 0.0

    intersection = len(entities1 & entities2)
    union = len(entities1 | entities2)

    return intersection / union if union > 0 else 0.0
```

---

### T4: Implement Community Merging Algorithm
**Location**: `graph_rag_analysis_748_v2.py` (new function)
**Acceptance Criteria**:
- [ ] `merge_communities(communities, anchors, min_similarity=0.05) -> List[Dict]`
- [ ] For each non-anchor community, find most similar anchor
- [ ] Merge communities with similarity >= threshold into anchor
- [ ] Track merged community IDs for provenance
- [ ] Handle orphan communities (no similar anchor) - create "Miscellaneous" bucket

**Design Rationale for `min_similarity=0.05`**:
- Lower threshold (0.05) ensures more communities get merged, maximizing coverage
- Jaccard similarity for entity sets tends to be low due to entity diversity
- Orphan communities (below threshold) go to "Miscellaneous" bucket anyway
- Can be tuned via CLI flag if results are too aggressive

**Implementation Notes**:
```python
def merge_communities(
    communities: List[Dict],
    anchors: List[Dict],
    min_similarity: float = 0.05
) -> List[Dict]:
    """Merge small communities into most similar anchors."""
    anchor_ids = {a["community_id"] for a in anchors}

    # Initialize merged results
    merged = {a["community_id"]: {
        "community_id": a["community_id"],
        "members": set(a["members"]),
        "merged_from": [a["community_id"]],
        "paper_count": a["paper_count"]
    } for a in anchors}

    # Track orphans
    orphan_members = set()
    orphan_ids = []

    # Process non-anchor communities
    for comm in communities:
        if comm["community_id"] in anchor_ids:
            continue

        # Find most similar anchor
        best_anchor = None
        best_similarity = 0.0

        for anchor in anchors:
            sim = calculate_entity_similarity(comm, anchor)
            if sim > best_similarity:
                best_similarity = sim
                best_anchor = anchor["community_id"]

        if best_anchor and best_similarity >= min_similarity:
            merged[best_anchor]["members"].update(comm["members"])
            merged[best_anchor]["merged_from"].append(comm["community_id"])
        else:
            orphan_members.update(comm["members"])
            orphan_ids.append(comm["community_id"])

    # Create miscellaneous bucket for orphans if any
    if orphan_members:
        merged["misc"] = {
            "community_id": "misc",
            "members": orphan_members,
            "merged_from": orphan_ids,
            "paper_count": len([m for m in orphan_members if m.startswith("https://doi.org/")])
        }

    # Convert sets back to lists and calculate final paper counts
    result = []
    for mid, m in merged.items():
        m["members"] = list(m["members"])
        m["paper_count"] = len([x for x in m["members"] if x.startswith("https://doi.org/")])
        result.append(m)

    return sorted(result, key=lambda x: x["paper_count"], reverse=True)
```

---

### T5: Integrate with Main Pipeline
**Location**: `graph_rag_analysis_748_v2.py` (modify `parse_args()` and `main()`)
**Acceptance Criteria**:
- [ ] Add `--merge-communities` flag to CLI
- [ ] Add `--anchor-count` flag (default: 10)
- [ ] Add `--min-anchor-papers` flag (default: 30)
- [ ] Add `--min-similarity` flag (default: 0.05)
- [ ] Call merging after community detection completes
- [ ] Save merged communities to `communities/level_0.5_merged.json`
- [ ] Pass `use_merged=True` to `generate_overview()` when `--merge-communities` is used

**Key Data Flow**:
1. Community detection returns `communities_by_level` dict (keyed by resolution floats)
2. Access level 0.5 communities via `communities_by_level[0.5].communities`
3. Convert cdlib community objects to JSON-serializable format first
4. Then run merging logic on the JSON format

**Implementation Notes**:
```python
# In parse_args():
parser.add_argument(
    '--merge-communities', action='store_true',
    help='Merge small communities into anchor communities'
)
parser.add_argument(
    '--anchor-count', type=int, default=10,
    help='Maximum number of anchor communities (default: 10)'
)
parser.add_argument(
    '--min-anchor-papers', type=int, default=30,
    help='Minimum papers for anchor community (default: 30)'
)
parser.add_argument(
    '--min-similarity', type=float, default=0.05,
    help='Minimum Jaccard similarity for merging (default: 0.05)'
)

# In main(), after Step 3 (community detection) and before Step 4:
# communities_by_level is a dict: {0.5: <cdlib_obj>, 1.0: <cdlib_obj>, ...}

if args.merge_communities:
    print("\n[3.5/7] Merging communities...")

    # Load the already-saved level_0.5.json (JSON format)
    level_05_path = OUTPUT_DIR / 'communities' / 'level_0.5.json'
    with open(level_05_path) as f:
        communities_json = json.load(f)

    # Select anchors and merge
    anchors = select_anchor_communities(
        communities_json,
        min_papers=args.min_anchor_papers,
        max_anchors=args.anchor_count
    )
    print(f"  Selected {len(anchors)} anchor communities")

    merged = merge_communities(
        communities_json,
        anchors,
        min_similarity=args.min_similarity
    )
    print(f"  Merged into {len(merged)} communities")

    # Save merged communities
    merged_path = OUTPUT_DIR / 'communities' / 'level_0.5_merged.json'
    with open(merged_path, 'w') as f:
        json.dump(merged, f, indent=2)
    print(f"  Saved to: {merged_path}")

# Later, in Step 7 (OVERVIEW generation):
if args.skip_overview:
    print("\n[7/7] Skipping OVERVIEW.md generation (--skip-overview)")
    overview_path = None
else:
    print("\n[7/7] Generating OVERVIEW.md...")
    overview_path = generate_overview(
        OUTPUT_DIR,
        stats,
        top_n=args.top_n,
        min_size=args.min_size,
        use_merged=args.merge_communities  # <-- Pass flag here
    )
    print(f"  Created: {overview_path}")
```

---

### T6: Update OVERVIEW Generation
**Location**: `graph_rag_analysis_748_v2.py` (modify `generate_overview()`)
**Acceptance Criteria**:
- [ ] Add `use_merged: bool = False` parameter to `generate_overview()`
- [ ] When `use_merged=True`, load `level_0.5_merged.json` instead of `level_0.5.json`
- [ ] Update summary aggregation to handle merged communities
- [ ] Show merged-from community count in overview for merged communities

**Implementation Notes**:
```python
def generate_overview(
    output_dir: Path,
    stats: Dict[str, Any],
    top_n: int = 15,
    min_size: int = 10,
    use_merged: bool = False  # New parameter
) -> Path:
    """
    Generate OVERVIEW.md with top N communities.

    Args:
        output_dir: Directory containing communities/ and summaries/
        stats: Statistics dictionary (from stats.json or in-memory)
        top_n: Number of top communities to include
        min_size: Minimum paper count for a community
        use_merged: If True, use level_0.5_merged.json instead of level_0.5.json
    """
    if use_merged:
        communities_file = output_dir / "communities" / "level_0.5_merged.json"
    else:
        communities_file = output_dir / "communities" / "level_0.5.json"

    summaries_dir = output_dir / "summaries" / "level_0.5"
    output_file = output_dir / "OVERVIEW.md"

    # Load communities
    communities = load_communities(communities_file)

    # ... rest of existing function ...

    # In the community processing loop, add merged info:
    for rank, comm in enumerate(top_communities, 1):
        comm_id = comm["community_id"]
        paper_count = comm["paper_count"]

        # ... existing summary parsing ...

        lines.append(f"### {rank}. {community_name} ({paper_count} papers)")
        lines.append("")

        # Add merged-from info for merged communities
        if "merged_from" in comm and len(comm["merged_from"]) > 1:
            lines.append(f"*(Merged from {len(comm['merged_from'])} original communities)*")
            lines.append("")

        # ... rest of existing processing ...
```

---

### T7: Test and Validate Coverage
**Location**: Command line execution
**Acceptance Criteria**:
- [ ] Run full pipeline with `--merge-communities` flag
- [ ] Verify merged community count is 15-20
- [ ] Verify coverage is 90%+
- [ ] Validate OVERVIEW.md reflects merged themes
- [ ] Compare before/after coverage statistics

**Validation Script**:
```bash
# Run with merging
python graph_rag_analysis_748_v2.py --merge-communities --top-n 20

# Check coverage
python -c "
import json
with open('data/papers/by-collection/virtual-cell-50/graph-rag-748/communities/level_0.5_merged.json') as f:
    merged = json.load(f)
total_papers = 748
covered = sum(c['paper_count'] for c in merged[:20])
print(f'Merged communities: {len(merged)}')
print(f'Top-20 coverage: {covered}/{total_papers} = {covered/total_papers*100:.1f}%')
"
```

---

## Commit Strategy

### Commit 1: Add helper functions
```
feat(graph-rag): Add entity extraction helpers for community merging

- extract_paper_dois(): Filter paper DOIs from community members
- extract_entity_ids(): Filter entity nodes from community members
```

### Commit 2: Implement merging logic
```
feat(graph-rag): Implement anchor-based community merging

- select_anchor_communities(): Select top communities by paper count
- calculate_entity_similarity(): Jaccard similarity on shared entities
- merge_communities(): Merge small communities into anchors
```

### Commit 3: Integrate and update OVERVIEW
```
feat(graph-rag): Integrate community merging into pipeline

- Add --merge-communities, --anchor-count, --min-anchor-papers, --min-similarity CLI flags
- Update generate_overview() to support merged communities via use_merged param
- Save merged communities to level_0.5_merged.json
```

---

## Success Criteria

| Metric | Target | Current |
|--------|--------|---------|
| Merged community count | 15-20 | 166 |
| Top-N coverage | 90%+ | 58.6% (Top-15) |
| Orphan papers | <5% | N/A |
| Pipeline backward compatibility | 100% | N/A |

---

## Risk Mitigation

| Risk | Mitigation |
|------|------------|
| Over-merging (themes too broad) | Tune `min_similarity` threshold via CLI; start with 0.05 |
| Under-coverage (many orphans) | Lower `min_similarity` or increase `anchor_count` |
| Summary quality degradation | Keep per-original-community summaries; aggregate for display |
| Performance on large datasets | Use set operations for O(1) lookups |

---

*Plan created: 2026-02-03*
*Updated: 2026-02-03 (fixed variable names, min_similarity consistency, use_merged integration)*
*Ready for execution via `/oh-my-claudecode:start-work community-merging`*
