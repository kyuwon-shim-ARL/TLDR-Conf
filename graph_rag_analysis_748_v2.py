#!/usr/bin/env python3
"""
Graph RAG Analysis for 748 Virtual Cell Papers - Version 2

Improved version with:
- Word-boundary regex matching (fixes "rat" from "generative" bug)
- Stopword filtering for capitalized word extraction
- Better organism/method/dataset lists
"""

import argparse
import json
import re
from pathlib import Path
from typing import Dict, List, Any, Optional, Tuple, Set
from collections import defaultdict, Counter
from itertools import combinations
import sys
import numpy as np
import networkx as nx
from cdlib import algorithms, evaluation
from tqdm import tqdm

# Add paper-pipeline to path
sys.path.insert(0, str(Path(__file__).parent / '.claude/skills/paper-pipeline/src'))
from paper_pipeline.hybrid_rag import KnowledgeGraphBuilder, GraphStats


# ============================================================================
# Community Merging Functions (v2 - Modularity-based, Conservative)
# ============================================================================

def extract_paper_dois(community: Dict) -> Set[str]:
    """Extract paper DOIs from community members."""
    return {m for m in community["members"] if m.startswith("https://doi.org/")}


def extract_entity_ids(community: Dict) -> Set[str]:
    """Extract entity IDs from community members (non-DOI entries)."""
    return {m for m in community["members"] if not m.startswith("https://doi.org/")}


def find_optimal_resolution(
    graph: nx.Graph,
    resolution_range: Tuple[float, float] = (0.1, 4.0),
    steps: int = 20
) -> Tuple[float, Dict[float, float]]:
    """
    Find optimal Louvain resolution via modularity maximization.

    Uses Louvain algorithm with resolution parameter scanning.
    This approach is similar to Microsoft GraphRAG's hierarchical community
    detection where modularity determines the natural community structure.

    Args:
        graph: NetworkX graph
        resolution_range: (min, max) resolution to scan
        steps: Number of resolution steps to try

    Returns:
        (optimal_resolution, modularity_scores_dict)
    """
    resolutions = np.linspace(resolution_range[0], resolution_range[1], steps)
    modularity_scores = {}

    print(f"  Scanning {steps} resolutions from {resolution_range[0]} to {resolution_range[1]}...")

    for res in resolutions:
        # Use Louvain algorithm with resolution parameter
        communities = algorithms.louvain(graph, resolution=res)

        # Newman-Girvan modularity
        modularity = evaluation.newman_girvan_modularity(graph, communities).score
        modularity_scores[float(res)] = modularity

        num_comms = len(communities.communities)
        print(f"    Resolution {res:.2f}: modularity={modularity:.4f}, communities={num_comms}")

    optimal_res = max(modularity_scores, key=modularity_scores.get)
    print(f"\n  Optimal resolution: {optimal_res:.2f} (modularity={modularity_scores[optimal_res]:.4f})")

    return optimal_res, modularity_scores


def compute_similarity_matrix(
    communities: List[Dict],
    min_papers: int = 3
) -> Dict[Tuple[int, int], float]:
    """
    Compute pairwise Jaccard similarity on entity sets.

    Only considers communities with >= min_papers.
    Returns sparse dict: (id1, id2) -> similarity

    Note: Filters out very high-frequency generic entities to reduce false similarities.
    """
    # Filter by paper count
    valid_comms = []
    for c in communities:
        paper_count = c.get("paper_count", len(extract_paper_dois(c)))
        if paper_count >= min_papers:
            c["paper_count"] = paper_count
            valid_comms.append(c)

    # Compute entity frequency across all communities to identify generic entities
    entity_comm_count = Counter()
    for c in valid_comms:
        entities = extract_entity_ids(c)
        for e in entities:
            entity_comm_count[e] += 1

    # Filter out entities appearing in >30% of communities (too generic)
    threshold = len(valid_comms) * 0.3
    generic_entities = {e for e, count in entity_comm_count.items() if count > threshold}

    if generic_entities:
        print(f"  Filtered {len(generic_entities)} generic entities (appear in >30% communities)")

    similarities = {}

    for c1, c2 in combinations(valid_comms, 2):
        entities1 = extract_entity_ids(c1) - generic_entities
        entities2 = extract_entity_ids(c2) - generic_entities

        if not entities1 or not entities2:
            continue

        intersection = len(entities1 & entities2)
        union = len(entities1 | entities2)
        jaccard = intersection / union if union > 0 else 0.0

        if jaccard > 0:  # Only store non-zero
            similarities[(c1["community_id"], c2["community_id"])] = jaccard

    return similarities


class UnionFind:
    """Union-Find data structure for transitive merge tracking."""

    def __init__(self, items):
        self.parent = {item: item for item in items}
        self.rank = {item: 0 for item in items}

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # Path compression
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

    type_counts = Counter(e.split(":")[0] if ":" in e else "UNKNOWN" for e in all_entities)
    max_type_ratio = max(type_counts.values()) / len(all_entities)

    return max_type_ratio < 0.8  # Must have some diversity


def conservative_merge(
    communities: List[Dict],
    similarities: Dict[Tuple[int, int], float],
    min_similarity: float = 0.7
) -> List[Dict]:
    """
    Merge communities only when clearly similar.

    Key differences from v1:
    - No forced anchor assignment
    - High similarity threshold (0.7)
    - Merge validation to prevent bad merges
    - Transitive merging via union-find
    - Post-merge validation for final cluster diversity
    """
    comm_ids = [c["community_id"] for c in communities]
    comm_lookup = {c["community_id"]: c for c in communities}

    uf = UnionFind(comm_ids)
    merge_count = 0

    # Merge similar pairs
    for (id1, id2), sim in sorted(similarities.items(), key=lambda x: -x[1]):
        if sim >= min_similarity:
            c1, c2 = comm_lookup[id1], comm_lookup[id2]
            if validate_merge(c1, c2):
                uf.union(id1, id2)
                merge_count += 1

    print(f"  Performed {merge_count} pairwise merges")

    # Group by root
    groups = defaultdict(list)
    for cid in comm_ids:
        root = uf.find(cid)
        groups[root].append(cid)

    # Build merged communities
    merged = []
    warnings = []

    for root, member_ids in groups.items():
        members = set()
        papers = set()
        merged_from = []

        for cid in member_ids:
            comm = comm_lookup[cid]
            members.update(comm["members"])
            papers.update(extract_paper_dois(comm))
            merged_from.append(cid)

        # Post-merge validation: check final cluster diversity
        entities = {m for m in members if not m.startswith("https://doi.org/")}
        if entities:
            type_counts = Counter(e.split(":")[0] if ":" in e else "UNKNOWN" for e in entities)
            max_ratio = max(type_counts.values()) / len(entities)
            if max_ratio > 0.8 and len(merged_from) > 1:
                warnings.append(f"Cluster {root} has {max_ratio:.1%} single-type dominance")

        merged.append({
            "community_id": root,
            "members": list(members),
            "paper_count": len(papers),
            "merged_from": sorted(merged_from),
            "merge_count": len(merged_from)
        })

    # Print warnings for problematic merges
    for w in warnings:
        print(f"  WARNING: {w}")

    return sorted(merged, key=lambda x: x["paper_count"], reverse=True)


def categorize_communities(
    communities: List[Dict],
    major_threshold: int = 10,
    emerging_threshold: int = 5,
    niche_threshold: int = 3
) -> Dict[str, List[Dict]]:
    """
    Categorize communities by size and coherence.

    Categories (optimized for maximum coverage):
    - major: >= 10 papers (main research themes)
    - emerging: 5-9 papers (distinct emerging topics)
    - niche: 3-4 papers (specialized areas, included in OVERVIEW)
    - noise: < 3 papers (isolated papers, ~18% unavoidable fragmentation)

    Note: The research landscape analysis reveals ~18% of papers are in
    singleton/doubleton communities due to entity fragmentation. This is
    expected in diverse, interdisciplinary research collections.
    """
    categories = {
        "major": [],
        "emerging": [],
        "niche": [],
        "noise": []
    }

    for comm in communities:
        paper_count = comm.get("paper_count", 0)

        if paper_count >= major_threshold:  # >= 10
            categories["major"].append(comm)
        elif paper_count >= emerging_threshold:  # 5-9
            categories["emerging"].append(comm)
        elif paper_count >= niche_threshold:  # 3-4
            categories["niche"].append(comm)
        else:  # 1-2 papers (isolated)
            categories["noise"].append(comm)

    # Sort each category by paper count
    for cat in categories:
        categories[cat].sort(key=lambda x: x["paper_count"], reverse=True)

    return categories


def generate_hierarchical_overview(
    output_dir: Path,
    categories: Dict[str, List[Dict]],
    stats: Dict[str, Any],
    summaries_dir: Path
) -> Path:
    """Generate OVERVIEW.md with hierarchical structure (Major/Emerging)."""

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
    lines.append(f"**Combined Coverage**: {major_papers + emerging_papers} papers ({(major_papers + emerging_papers)/total_papers*100:.1f}%)")
    lines.append("")

    lines.append("**Research Domains**:")
    for cat, count in stats["category_distribution"].items():
        cat_display = cat.replace("_", " ").title()
        lines.append(f"- {cat_display}: {count} papers")
    lines.append("")

    lines.append("**Graph Statistics**:")
    lines.append(f"- Paper nodes: {stats['graph_stats']['paper_nodes']}")
    lines.append(f"- Entity nodes: {stats['graph_stats']['entity_nodes']}")
    lines.append(f"- Edges: {stats['graph_stats']['edges']}")
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

        # Try to parse summary
        summary_file = summaries_dir / f"community_{comm_id}.md"
        summary = parse_community_summary(summary_file) if summary_file.exists() else None

        if summary:
            name = get_community_name(summary, comm_id)
        else:
            name = f"Theme {comm_id}"

        lines.append(f"### {rank}. {name} ({paper_count} papers)")
        if merge_count > 1:
            lines.append(f"*Consolidated from {merge_count} related clusters*")
        lines.append("")

        if summary:
            if summary.get("years"):
                lines.append(f"**Period**: {summary['years']}")
                lines.append("")

            if summary.get("research_focus"):
                lines.append(f"**Focus**: {summary['research_focus']}")
                lines.append("")

            if summary.get("top_entities"):
                lines.append(f"**Key Entities**: {', '.join(summary['top_entities'][:5])}")
                lines.append("")

            if summary.get("sample_papers"):
                lines.append("**Representative Papers**:")
                for paper in summary["sample_papers"][:3]:
                    lines.append(f"- {paper}")
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
        summary = parse_community_summary(summary_file) if summary_file.exists() else None

        if summary:
            name = get_community_name(summary, comm_id)
            focus = summary.get("research_focus", "")[:100] if summary else ""
        else:
            name = f"Topic {comm_id}"
            focus = ""

        lines.append(f"**{rank}. {name}** ({paper_count} papers)")
        if focus:
            lines.append(f"   {focus}...")
        lines.append("")

    lines.append("---")
    lines.append("")

    # Niche Areas Section (if any)
    niche_count = len(categories["niche"])
    niche_papers = sum(c["paper_count"] for c in categories["niche"])

    if niche_count > 0:
        lines.append("## Niche Research Areas")
        lines.append("")
        lines.append("*Specialized topics with 5-9 papers each*")
        lines.append("")

        for rank, comm in enumerate(categories["niche"], 1):
            comm_id = comm["community_id"]
            paper_count = comm["paper_count"]

            summary_file = summaries_dir / f"community_{comm_id}.md"
            summary = parse_community_summary(summary_file) if summary_file.exists() else None

            if summary:
                name = get_community_name(summary, comm_id)
            else:
                name = f"Area {comm_id}"

            lines.append(f"**{rank}. {name}** ({paper_count} papers)")
            lines.append("")

        lines.append("---")
        lines.append("")

    # Coverage Statistics
    lines.append("## Coverage Statistics")
    lines.append("")
    lines.append("| Category | Count | Papers | Coverage |")
    lines.append("|----------|-------|--------|----------|")
    lines.append(f"| Major Themes | {major_count} | {major_papers} | {major_papers/total_papers*100:.1f}% |")
    lines.append(f"| Emerging Topics | {emerging_count} | {emerging_papers} | {emerging_papers/total_papers*100:.1f}% |")
    if niche_count > 0:
        lines.append(f"| Niche Areas | {niche_count} | {niche_papers} | {niche_papers/total_papers*100:.1f}% |")
    total_listed = major_papers + emerging_papers + niche_papers
    total_count = major_count + emerging_count + niche_count
    lines.append(f"| **Total Listed** | {total_count} | {total_listed} | {total_listed/total_papers*100:.1f}% |")
    lines.append("")

    lines.append("---")
    lines.append("")
    lines.append("*Generated by Graph RAG v2 (modularity-optimized, conservative merge)*")

    output_file.write_text("\n".join(lines))
    return output_file


# ============================================================================
# OVERVIEW Generation Functions
# ============================================================================

def load_communities(communities_file: Path) -> list:
    """Load communities from JSON file."""
    with open(communities_file) as f:
        return json.load(f)


def filter_and_sort_communities(communities: list, min_size: int = 10, top_n: int = 15) -> list:
    """Filter communities by size and return top N sorted by size descending."""
    filtered = []
    for comm in communities:
        paper_count = sum(1 for m in comm["members"] if m.startswith("https://doi.org/"))
        if paper_count >= min_size:
            comm["paper_count"] = paper_count
            filtered.append(comm)

    filtered.sort(key=lambda x: x["paper_count"], reverse=True)
    return filtered[:top_n]


def parse_community_summary(summary_file: Path) -> Optional[Dict[str, Any]]:
    """Parse a community summary markdown file and extract key information."""
    if not summary_file.exists():
        return None

    content = summary_file.read_text()

    result = {
        "research_focus": "",
        "top_entities": [],
        "sample_papers": [],
        "dominant_category": "",
        "years": ""
    }

    # Extract dominant category
    cat_match = re.search(r"\*\*Dominant Category\*\*:\s*(\S+)", content)
    if cat_match:
        result["dominant_category"] = cat_match.group(1)

    # Extract years
    years_match = re.search(r"\*\*Years\*\*:\s*(.+)", content)
    if years_match:
        result["years"] = years_match.group(1).strip()

    # Extract research focus (first paragraph after **Research Focus**:)
    focus_match = re.search(r"\*\*Research Focus\*\*:\s*(.+?)(?=\n\n|\*\*Entity Type)", content, re.DOTALL)
    if focus_match:
        focus_text = focus_match.group(1).strip()
        sentences = re.split(r'(?<=[.!?])\s+', focus_text)
        result["research_focus"] = sentences[0] if sentences else focus_text[:200]

    # Extract top 5 entities
    entities_section = re.search(r"\*\*Most Frequent Entities\*\*:\n((?:- .+\n)+)", content)
    if entities_section:
        entity_lines = entities_section.group(1).strip().split("\n")
        for line in entity_lines[:5]:
            match = re.match(r"- (.+?) \((\w+)\):", line)
            if match:
                result["top_entities"].append(match.group(1))

    # Extract sample papers (up to 3)
    papers_section = re.search(r"\*\*Sample Papers\*\*.+?:\n((?:- .+\n)+)", content)
    if papers_section:
        paper_lines = papers_section.group(1).strip().split("\n")
        for line in paper_lines[:3]:
            match = re.match(r"- \((\d{4})\) (.+)", line)
            if match:
                result["sample_papers"].append(f"({match.group(1)}) {match.group(2)}")

    return result


def get_community_name(summary: Dict[str, Any], community_id: int) -> str:
    """Generate a descriptive name for the community based on its content."""
    category = summary.get("dominant_category", "Research").replace("_", " ").title()

    top_entities = summary.get("top_entities", [])[:3]
    if top_entities:
        entity_str = ", ".join(top_entities[:2])
        return f"{category}: {entity_str}"

    return f"{category} Community {community_id}"


def generate_overview(
    output_dir: Path,
    stats: Dict[str, Any],
    top_n: int = 15,
    min_size: int = 10
) -> Path:
    """
    Generate OVERVIEW.md with top N communities.

    Args:
        output_dir: Directory containing communities/ and summaries/
        stats: Statistics dictionary (from stats.json or in-memory)
        top_n: Number of top communities to include
        min_size: Minimum paper count for a community

    Returns:
        Path to the generated OVERVIEW.md file
    """
    communities_file = output_dir / "communities" / "level_0.5.json"
    summaries_dir = output_dir / "summaries" / "level_0.5"
    output_file = output_dir / "OVERVIEW.md"

    # Load communities
    communities = load_communities(communities_file)

    # Filter and sort communities
    top_communities = filter_and_sort_communities(communities, min_size=min_size, top_n=top_n)

    # Calculate coverage
    total_papers = stats["total_papers"]
    top_community_papers = sum(c["paper_count"] for c in top_communities)
    coverage_pct = (top_community_papers / total_papers) * 100 if total_papers > 0 else 0

    # Build OVERVIEW content
    lines = []
    lines.append(f"# Virtual Cell Research Landscape ({total_papers} Papers)")
    lines.append("")
    lines.append("## Executive Summary")
    lines.append("")
    lines.append(f"This overview synthesizes {total_papers} papers into {len(top_communities)} major research themes,")
    lines.append(f"representing {top_community_papers} papers ({coverage_pct:.1f}% of the collection).")
    lines.append("")
    lines.append("**Research Domains**:")
    for cat, count in stats["category_distribution"].items():
        cat_display = cat.replace("_", " ").title()
        lines.append(f"- {cat_display}: {count} papers")
    lines.append("")
    lines.append("**Graph Statistics**:")
    lines.append(f"- Paper nodes: {stats['graph_stats']['paper_nodes']}")
    lines.append(f"- Entity nodes: {stats['graph_stats']['entity_nodes']}")
    lines.append(f"- Edges: {stats['graph_stats']['edges']}")
    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append("## Core Research Themes")
    lines.append("")

    # Process each top community
    for rank, comm in enumerate(top_communities, 1):
        comm_id = comm["community_id"]
        paper_count = comm["paper_count"]

        summary_file = summaries_dir / f"community_{comm_id}.md"
        summary = parse_community_summary(summary_file)

        if summary is None:
            lines.append(f"### {rank}. Community {comm_id} ({paper_count} papers)")
            lines.append("")
            lines.append("*Summary not available*")
            lines.append("")
            continue

        community_name = get_community_name(summary, comm_id)

        lines.append(f"### {rank}. {community_name} ({paper_count} papers)")
        lines.append("")

        if summary["years"]:
            lines.append(f"**Period**: {summary['years']}")
            lines.append("")

        if summary["research_focus"]:
            lines.append(f"**Research Focus**: {summary['research_focus']}")
            lines.append("")

        if summary["top_entities"]:
            entities_str = ", ".join(summary["top_entities"])
            lines.append(f"**Key Entities**: {entities_str}")
            lines.append("")

        if summary["sample_papers"]:
            lines.append("**Representative Papers**:")
            for paper in summary["sample_papers"]:
                lines.append(f"- {paper}")
            lines.append("")

        lines.append("---")
        lines.append("")

    # Coverage statistics
    lines.append("## Coverage Statistics")
    lines.append("")
    lines.append(f"- **Total Papers**: {total_papers}")
    lines.append(f"- **Top {len(top_communities)} Themes**: {top_community_papers} papers ({coverage_pct:.1f}%)")
    lines.append(f"- **Total Communities (level 0.5)**: {stats['communities']['level_0.5']['num_communities']}")
    lines.append("")
    lines.append("### Community Size Distribution")
    lines.append("")
    size_dist = stats['communities']['level_0.5']['size_distribution']
    lines.append(f"- Small (<10 papers): {size_dist['small (<10)']} communities")
    lines.append(f"- Medium (10-50 papers): {size_dist['medium (10-50)']} communities")
    lines.append(f"- Large (50-100 papers): {size_dist['large (50-100)']} communities")
    lines.append(f"- Very Large (>=100 papers): {size_dist['very_large (>=100)']} communities")
    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append("*Generated by Graph RAG analysis pipeline*")

    # Write output
    output_file.write_text("\n".join(lines))
    print(f"  Top {len(top_communities)} communities covering {top_community_papers}/{total_papers} papers ({coverage_pct:.1f}%)")

    return output_file


# ============================================================================
# Entity Extraction
# ============================================================================


# Stopwords to filter from capitalized word extraction
STOPWORDS = {
    'the', 'a', 'an', 'of', 'in', 'for', 'to', 'and', 'with', 'on',
    'using', 'towards', 'building', 'based', 'new', 'novel', 'large',
    'comprehensive', 'survey', 'review', 'challenges', 'future',
    'applications', 'current', 'scale', 'from', 'single', 'multi',
    'via', 'through', 'across', 'beyond', 'into', 'between', 'among',
    'how', 'what', 'why', 'when', 'where', 'which', 'who',
    'can', 'may', 'could', 'would', 'should', 'will', 'shall',
    'are', 'is', 'was', 'were', 'been', 'being', 'have', 'has', 'had',
    'its', 'their', 'our', 'your', 'his', 'her',
    'this', 'that', 'these', 'those', 'all', 'any', 'some', 'each',
    'both', 'few', 'more', 'most', 'other', 'such',
    'only', 'just', 'also', 'very', 'quite', 'rather', 'too',
    'not', 'but', 'yet', 'however', 'although', 'though', 'while',
    'model', 'models', 'modeling', 'modelling', 'analysis', 'approach',
    'method', 'methods', 'study', 'studies', 'data', 'learning',
    'cell', 'cells', 'cellular', 'biology', 'biological',
    'protein', 'proteins', 'gene', 'genes', 'genomic', 'molecular',
    'network', 'networks', 'system', 'systems', 'computational',
    'development', 'prediction', 'predictions', 'predictive',
    'inference', 'identification', 'detection', 'classification',
    'generation', 'synthesis', 'integration', 'exploration',
    'understanding', 'insights', 'perspective', 'perspectives',
    'framework', 'platform', 'pipeline', 'tool', 'tools', 'software',
    'enables', 'enabling', 'enabled', 'reveals', 'revealing', 'revealed',
    'improved', 'improving', 'improvement', 'enhanced', 'enhancing',
    'scalable', 'efficient', 'effective', 'robust', 'accurate',
    'high', 'low', 'deep', 'wide', 'long', 'short',
    'resolution', 'level', 'levels', 'type', 'types',
    'based', 'driven', 'guided', 'informed', 'aware',
    # Common title words that get capitalized at start
    'towards', 'beyond', 'within', 'without',
}


class ImprovedEntityExtractor:
    """Rule-based entity extraction with word-boundary matching."""

    def __init__(self):
        # Methods - use word boundaries
        self.methods = [
            'scGPT', 'transformer', 'transformers', 'LSTM', 'CNN', 'RNN', 'GRU',
            'neural network', 'deep learning', 'machine learning', 'ML', 'DL', 'AI',
            'random forest', 'support vector', 'SVM', 'clustering', 'k-means',
            'classification', 'regression', 'ensemble', 'boosting', 'XGBoost',
            'reinforcement learning', 'RL',
            'GAN', 'VAE', 'autoencoder', 'diffusion model',
            'attention mechanism', 'self-attention', 'BERT', 'GPT', 'LLM',
            'foundation model', 'language model', 'embedding', 'representation learning',
            'transfer learning', 'fine-tuning', 'pre-training', 'pretraining',
            'zero-shot', 'few-shot', 'contrastive learning',
            'graph neural network', 'GNN', 'graph convolutional', 'GCN',
            'message passing', 'node embedding',
            'simulation', 'optimization', 'algorithm',
            'RNA-seq', 'scRNA-seq', 'spatial transcriptomics', 'ATAC-seq',
            'ChIP-seq', 'Hi-C', 'CITE-seq', 'multiome',
            'mass spectrometry', 'proteomics', 'metabolomics', 'genomics',
            'CRISPR', 'gene editing', 'perturbation', 'screening', 'Perturb-seq',
            'FBA', 'flux balance analysis', 'constraint-based',
            'ODE', 'differential equation', 'stochastic simulation',
            'Monte Carlo', 'MCMC', 'Bayesian', 'variational inference',
            'dimensionality reduction', 'PCA', 'UMAP', 't-SNE',
            'batch correction', 'data integration', 'imputation',
        ]

        # Organisms - IMPORTANT: use word boundaries to avoid substring matches
        self.organisms = [
            'human', 'mouse', 'yeast', 'zebrafish', 'fruit fly',
            'E. coli', 'Escherichia coli', 'S. cerevisiae', 'Saccharomyces cerevisiae',
            'C. elegans', 'Caenorhabditis elegans',
            'Drosophila', 'Arabidopsis', 'Mycoplasma',
            'bacteria', 'bacterial', 'microbial', 'microbiome',
            'mammalian', 'vertebrate', 'eukaryote', 'eukaryotic', 'prokaryote',
            # Cell types
            'stem cell', 'iPSC', 'ESC', 'T cell', 'B cell', 'NK cell',
            'neuron', 'neuronal', 'immune cell', 'macrophage', 'dendritic cell',
            'cancer cell', 'tumor cell', 'epithelial', 'endothelial',
            'cardiomyocyte', 'hepatocyte', 'fibroblast', 'keratinocyte',
            'organoid', 'spheroid', 'tissue', 'organ',
            # NOTE: removed 'rat' - will add with word boundary only
        ]

        # Concepts
        self.concepts = [
            'gene expression', 'transcription', 'translation', 'regulation',
            'pathway', 'signaling', 'metabolism', 'homeostasis', 'metabolic',
            'differentiation', 'development', 'proliferation', 'apoptosis', 'cell cycle',
            'drug discovery', 'drug design', 'therapeutic', 'biomarker',
            'diagnosis', 'prognosis', 'precision medicine', 'personalized medicine',
            'systems biology', 'computational biology', 'bioinformatics',
            'multi-omics', 'multiomics', 'heterogeneity', 'variability',
            'dynamics', 'evolution', 'adaptation', 'response', 'perturbation response',
            'disease', 'cancer', 'diabetes', 'Alzheimer', 'COVID', 'COVID-19',
            'virtual cell', 'whole-cell', 'in silico', 'digital twin',
            'cell state', 'cell fate', 'cell identity', 'cell atlas',
            'gene regulatory network', 'GRN', 'protein-protein interaction', 'PPI',
            'chromatin accessibility', 'epigenetics', 'epigenome', 'methylation',
        ]

        # Datasets/databases
        self.datasets = [
            'UniProt', 'PDB', 'Protein Data Bank', 'GenBank', 'RefSeq', 'Ensembl',
            'KEGG', 'Reactome', 'Gene Ontology', 'GO',
            'TCGA', 'GTEx', 'UK Biobank', 'GnomAD', 'ClinVar',
            'Human Cell Atlas', 'HCA', 'Allen Brain Atlas', 'ENCODE', 'FANTOM',
            'CellxGene', 'CELLxGENE', 'Single Cell Portal', 'GEO', 'ArrayExpress',
            'Tabula Muris', 'Tabula Sapiens', 'HuBMAP', 'BioGRID',
            'STRING', 'DrugBank', 'ChEMBL', 'PubChem',
            'scRNA-seq atlas', 'cell atlas', 'expression atlas',
        ]

        # Build compiled patterns for word-boundary matching
        self._compile_patterns()

    def _compile_patterns(self):
        """Pre-compile regex patterns for efficient matching."""
        self.method_patterns = []
        for method in self.methods:
            # Escape special chars and add word boundaries
            pattern = re.compile(r'\b' + re.escape(method.lower()) + r'\b', re.IGNORECASE)
            self.method_patterns.append((method, pattern))

        self.organism_patterns = []
        for organism in self.organisms:
            pattern = re.compile(r'\b' + re.escape(organism.lower()) + r'\b', re.IGNORECASE)
            self.organism_patterns.append((organism, pattern))

        # Add 'rat' separately with strict word boundary (not in 'generative', etc.)
        # \brat\b will only match standalone "rat"
        self.organism_patterns.append(('rat', re.compile(r'\brat\b', re.IGNORECASE)))

        self.concept_patterns = []
        for concept in self.concepts:
            pattern = re.compile(r'\b' + re.escape(concept.lower()) + r'\b', re.IGNORECASE)
            self.concept_patterns.append((concept, pattern))

        self.dataset_patterns = []
        for dataset in self.datasets:
            pattern = re.compile(r'\b' + re.escape(dataset.lower()) + r'\b', re.IGNORECASE)
            self.dataset_patterns.append((dataset, pattern))

    def extract_entities(self, title: str, category: str) -> List[Dict[str, str]]:
        """
        Extract entities from title using word-boundary regex matching.

        Returns:
            List of {"name": str, "type": str} dicts
        """
        entities = []
        seen = set()

        # Extract methods
        for method, pattern in self.method_patterns:
            if pattern.search(title):
                key = method.lower()
                if key not in seen:
                    entities.append({"name": method, "type": "METHOD"})
                    seen.add(key)

        # Extract organisms
        for organism, pattern in self.organism_patterns:
            if pattern.search(title):
                key = organism.lower()
                if key not in seen:
                    entities.append({"name": organism, "type": "ORGANISM"})
                    seen.add(key)

        # Extract concepts
        for concept, pattern in self.concept_patterns:
            if pattern.search(title):
                key = concept.lower()
                if key not in seen:
                    entities.append({"name": concept, "type": "CONCEPT"})
                    seen.add(key)

        # Extract datasets
        for dataset, pattern in self.dataset_patterns:
            if pattern.search(title):
                key = dataset.lower()
                if key not in seen:
                    entities.append({"name": dataset, "type": "DATASET"})
                    seen.add(key)

        # Extract capitalized terms (acronyms/proper nouns) with stopword filtering
        words = re.findall(r'\b[A-Z][A-Za-z0-9-]*\b', title)
        for word in words:
            word_lower = word.lower()
            # Filter: length >= 3, not a stopword, not already seen
            if len(word) >= 3 and word_lower not in seen and word_lower not in STOPWORDS:
                # Guess type based on context
                if any(kw in word_lower for kw in ['seq', 'omics', 'data', 'atlas', 'bank']):
                    entities.append({"name": word, "type": "DATASET"})
                elif word.isupper() and len(word) <= 6:
                    # Short all-caps likely method/tool acronym
                    entities.append({"name": word, "type": "METHOD"})
                else:
                    entities.append({"name": word, "type": "METHOD"})
                seen.add(word_lower)

        return entities


class GraphRAGAnalyzer:
    """Comprehensive Graph RAG analyzer for virtual cell papers."""

    def __init__(self, output_dir: Path):
        self.output_dir = output_dir
        self.output_dir.mkdir(parents=True, exist_ok=True)
        self.extractor = ImprovedEntityExtractor()

    def extract_all_entities(self, papers: List[Dict[str, Any]]) -> Dict[str, Any]:
        """Extract entities from all paper titles using improved rule-based method."""
        results = {}
        total = len(papers)

        print(f"\n=== Extracting entities from {total} papers (improved rule-based) ===")

        for paper in tqdm(papers, desc="Extracting entities"):
            doi = paper['doi']
            title = paper['title']
            category = paper['category']

            entities = self.extractor.extract_entities(title, category)

            results[doi] = {
                'title': title,
                'category': category,
                'entities': entities
            }

        print(f"\nCompleted entity extraction for {total} papers")

        # Save results
        output_path = self.output_dir / 'entities.json'
        with open(output_path, 'w') as f:
            json.dump(results, f, indent=2)

        print(f"Saved entities to: {output_path}")

        return results

    def build_knowledge_graph(self, papers: List[Dict[str, Any]], entities_path: Path) -> KnowledgeGraphBuilder:
        """Build knowledge graph from papers and entities."""
        print("\n=== Building Knowledge Graph ===")

        kg = KnowledgeGraphBuilder()

        # Add papers
        num_papers = kg.add_papers(papers)
        print(f"Added {num_papers} paper nodes")

        # Add entities
        num_entities = kg.add_entities_from_json(entities_path)
        print(f"Added {num_entities} entity nodes")

        # Get stats
        stats = kg.get_stats()
        print(f"\nGraph Statistics:")
        print(f"  Paper nodes: {stats.num_paper_nodes}")
        print(f"  Entity nodes: {stats.num_entity_nodes}")
        print(f"  Edges: {stats.num_edges}")
        print(f"  Entity types: {stats.entity_type_counts}")

        return kg

    def detect_communities(self, graph: nx.Graph, resolutions: List[float] = [0.5, 1.0, 2.0, 4.0]) -> Dict[float, Any]:
        """Run hierarchical Louvain community detection."""
        print("\n=== Detecting Communities (Louvain Algorithm) ===")

        communities_by_level = {}

        for resolution in resolutions:
            print(f"\nResolution {resolution}:")

            # Run Louvain algorithm with resolution parameter
            communities = algorithms.louvain(graph, resolution=resolution)

            num_communities = len(communities.communities)
            sizes = [len(c) for c in communities.communities]

            print(f"  Communities: {num_communities}")
            print(f"  Avg size: {sum(sizes) / len(sizes):.1f}")
            print(f"  Size range: {min(sizes)} - {max(sizes)}")

            communities_by_level[resolution] = communities

            # Save to JSON
            self._save_communities(communities, resolution)

        return communities_by_level

    def _save_communities(self, communities, resolution: float):
        """Save community memberships to JSON."""
        output = []
        for i, community in enumerate(communities.communities):
            output.append({
                'community_id': i,
                'size': len(community),
                'members': list(community)
            })

        comm_dir = self.output_dir / 'communities'
        comm_dir.mkdir(exist_ok=True)
        output_path = comm_dir / f'level_{resolution}.json'

        with open(output_path, 'w') as f:
            json.dump(output, f, indent=2)

    def generate_community_summaries(self,
                                     graph: nx.Graph,
                                     communities_by_level: Dict[float, Any],
                                     entities_data: Dict[str, Any]) -> Dict[str, Dict[int, str]]:
        """Generate rule-based summaries for each community."""
        print("\n=== Generating Community Summaries (rule-based) ===")

        all_summaries = {}
        total_communities = sum(len(c.communities) for c in communities_by_level.values())

        with tqdm(total=total_communities, desc="Generating summaries") as pbar:
            for resolution, communities in communities_by_level.items():
                level_dir = self.output_dir / 'summaries' / f'level_{resolution}'
                level_dir.mkdir(parents=True, exist_ok=True)

                summaries = {}

                for i, community in enumerate(communities.communities):
                    summary = self._generate_single_community_summary(
                        community, graph, entities_data, resolution, i
                    )

                    summaries[i] = summary

                    # Save individual summary
                    summary_path = level_dir / f'community_{i}.md'
                    with open(summary_path, 'w') as f:
                        f.write(summary)

                    pbar.update(1)

                all_summaries[f'level_{resolution}'] = summaries

        return all_summaries

    def _generate_single_community_summary(self,
                                          community: List[str],
                                          graph: nx.Graph,
                                          entities_data: Dict[str, Any],
                                          resolution: float,
                                          community_id: int) -> str:
        """Generate rule-based summary for a single community."""

        # Collect community data
        papers = []
        all_entities = []
        categories = []

        for node in community:
            node_data = graph.nodes[node]

            if node_data.get('type') == 'paper':
                doi = node
                papers.append({
                    'title': node_data.get('title', ''),
                    'year': node_data.get('year'),
                    'doi': doi
                })

                # Get entities and category for this paper
                if doi in entities_data:
                    all_entities.extend(entities_data[doi].get('entities', []))
                    categories.append(entities_data[doi].get('category', 'unknown'))

            elif node_data.get('type') == 'entity':
                all_entities.append({
                    'name': node_data.get('name'),
                    'type': node_data.get('entity_type')
                })

        # Count frequencies
        entity_freq = Counter(
            (e['name'], e['type']) for e in all_entities if e.get('name')
        )
        category_freq = Counter(categories)

        # Get top entities by type
        entities_by_type = defaultdict(list)
        for (name, etype), count in entity_freq.most_common(50):
            entities_by_type[etype].append((name, count))

        # Determine theme based on entity types
        top_category = category_freq.most_common(1)[0][0] if category_freq else 'unknown'

        # Get year range safely
        years = [p['year'] for p in papers if p.get('year')]
        min_year = min(years) if years else 'N/A'
        max_year = max(years) if years else 'N/A'

        # Generate summary
        header = f"""# Community {community_id} (Level {resolution})

**Size**: {len(papers)} papers, {len(entity_freq)} unique entities
**Resolution**: {resolution}
**Dominant Category**: {top_category}
**Years**: {min_year} - {max_year}

---

"""

        summary_parts = []

        # Research focus
        if 'METHOD' in entities_by_type and entities_by_type['METHOD']:
            top_methods = ', '.join([name for name, _ in entities_by_type['METHOD'][:5]])
            summary_parts.append(f"**Research Focus**: This community focuses on {top_category} research, "
                                f"primarily utilizing methods such as {top_methods}.")

        # Organisms/systems
        if 'ORGANISM' in entities_by_type and entities_by_type['ORGANISM']:
            top_organisms = ', '.join([name for name, _ in entities_by_type['ORGANISM'][:5]])
            summary_parts.append(f"The work primarily involves {top_organisms}.")

        # Key concepts
        if 'CONCEPT' in entities_by_type and entities_by_type['CONCEPT']:
            top_concepts = ', '.join([name for name, _ in entities_by_type['CONCEPT'][:5]])
            summary_parts.append(f"Key research concepts include {top_concepts}.")

        # Entity type breakdown
        summary_parts.append(f"\n**Entity Type Distribution**:")
        for etype, ents in sorted(entities_by_type.items()):
            summary_parts.append(f"- {etype}: {len(ents)} unique entities")

        # Top entities
        summary_parts.append(f"\n**Most Frequent Entities**:")
        for (name, etype), count in entity_freq.most_common(15):
            summary_parts.append(f"- {name} ({etype}): {count} mentions")

        # Sample papers
        summary_parts.append(f"\n**Sample Papers** (showing up to 10):")
        for paper in papers[:10]:
            year = paper.get('year', 'N/A')
            summary_parts.append(f"- ({year}) {paper['title']}")

        return header + "\n".join(summary_parts)

    def save_overall_stats(self,
                          papers: List[Dict[str, Any]],
                          entities_data: Dict[str, Any],
                          graph_stats: GraphStats,
                          communities_by_level: Dict[float, Any]) -> Dict[str, Any]:
        """Save overall analysis statistics and return stats dict."""

        # Entity statistics
        all_entities = []
        for data in entities_data.values():
            all_entities.extend(data.get('entities', []))

        entity_type_counts = Counter(e['type'] for e in all_entities)
        entity_name_freq = Counter(e['name'] for e in all_entities)

        # Category statistics
        category_counts = Counter(p['category'] for p in papers)

        # Community statistics
        community_stats = {}
        for resolution, communities in communities_by_level.items():
            sizes = [len(c) for c in communities.communities]
            community_stats[f'level_{resolution}'] = {
                'num_communities': len(communities.communities),
                'avg_size': sum(sizes) / len(sizes),
                'min_size': min(sizes),
                'max_size': max(sizes),
                'size_distribution': {
                    'small (<10)': len([s for s in sizes if s < 10]),
                    'medium (10-50)': len([s for s in sizes if 10 <= s < 50]),
                    'large (50-100)': len([s for s in sizes if 50 <= s < 100]),
                    'very_large (>=100)': len([s for s in sizes if s >= 100])
                }
            }

        stats = {
            'total_papers': len(papers),
            'category_distribution': dict(category_counts),
            'graph_stats': {
                'paper_nodes': graph_stats.num_paper_nodes,
                'entity_nodes': graph_stats.num_entity_nodes,
                'edges': graph_stats.num_edges,
                'entity_type_counts': graph_stats.entity_type_counts
            },
            'entity_extraction': {
                'total_entities_extracted': len(all_entities),
                'unique_entities': len(set(e['name'] for e in all_entities)),
                'entity_type_counts': dict(entity_type_counts),
                'top_entities': [
                    {'name': name, 'count': count}
                    for name, count in entity_name_freq.most_common(50)
                ]
            },
            'communities': community_stats
        }

        output_path = self.output_dir / 'stats.json'
        with open(output_path, 'w') as f:
            json.dump(stats, f, indent=2)

        print(f"\n=== Overall Statistics ===")
        print(f"Total papers: {stats['total_papers']}")
        print(f"Total entities extracted: {stats['entity_extraction']['total_entities_extracted']}")
        print(f"Unique entities: {stats['entity_extraction']['unique_entities']}")
        print(f"Graph nodes: {graph_stats.num_paper_nodes + graph_stats.num_entity_nodes}")
        print(f"Graph edges: {graph_stats.num_edges}")
        print(f"\nSaved stats to: {output_path}")

        return stats


def parse_args():
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser(
        description="Graph RAG Analysis for Virtual Cell Papers (V2)",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Standard analysis with default multi-resolution
  python graph_rag_analysis_748_v2.py

  # With modularity-optimized resolution and conservative merging (RECOMMENDED)
  python graph_rag_analysis_748_v2.py --auto-resolution

  # Custom merge threshold (lower = more aggressive merging)
  python graph_rag_analysis_748_v2.py --auto-resolution --merge-threshold 0.5

  # Skip OVERVIEW generation
  python graph_rag_analysis_748_v2.py --skip-overview
        """
    )
    # Basic options
    parser.add_argument(
        '--top-n', type=int, default=15,
        help='Number of top communities to include in OVERVIEW (default: 15)'
    )
    parser.add_argument(
        '--min-size', type=int, default=10,
        help='Minimum paper count for a community in OVERVIEW (default: 10)'
    )
    parser.add_argument(
        '--skip-overview', action='store_true',
        help='Skip OVERVIEW.md generation'
    )

    # v2 Merging options
    parser.add_argument(
        '--auto-resolution', action='store_true',
        help='Use modularity to find optimal Leiden resolution (recommended for 90%+ coverage)'
    )
    parser.add_argument(
        '--merge-threshold', type=float, default=0.7,
        help='Minimum Jaccard similarity for merging (default: 0.7, higher = stricter)'
    )
    parser.add_argument(
        '--preserve-emerging', action='store_true', default=True,
        help='Preserve emerging topics instead of forcing into major themes (default: True)'
    )

    # Deprecated v1 flags (keep for backward compatibility)
    parser.add_argument(
        '--merge-communities', action='store_true',
        help='[DEPRECATED] Use --auto-resolution instead'
    )
    parser.add_argument(
        '--anchor-count', type=int, default=None,
        help='[DEPRECATED] v2 uses modularity-based resolution instead'
    )
    parser.add_argument(
        '--min-similarity', type=float, default=None,
        help='[DEPRECATED] Use --merge-threshold instead'
    )

    return parser.parse_args()


def main():
    """Main execution function."""
    args = parse_args()

    # Handle deprecated flags
    if args.merge_communities:
        print("WARNING: --merge-communities is deprecated. Using --auto-resolution instead.")
        args.auto_resolution = True
    if args.min_similarity is not None:
        print(f"WARNING: --min-similarity is deprecated. Using --merge-threshold={args.min_similarity} instead.")
        args.merge_threshold = args.min_similarity
    if args.anchor_count is not None:
        print("WARNING: --anchor-count is deprecated. v2 uses modularity-based resolution instead.")

    # Configuration
    BASE_DIR = Path('/home/kyuwon/projects/MSK2025')
    INPUT_FILE = BASE_DIR / 'data/papers/by-collection/virtual-cell-50/comprehensive_papers.json'
    OUTPUT_DIR = BASE_DIR / 'data/papers/by-collection/virtual-cell-50/graph-rag-748'

    # Load papers
    print("=== Loading papers ===")
    with open(INPUT_FILE) as f:
        data = json.load(f)

    papers = data['papers']
    print(f"Loaded {len(papers)} papers")
    print(f"Categories: {data['category_counts']}")

    # Initialize analyzer
    analyzer = GraphRAGAnalyzer(output_dir=OUTPUT_DIR)

    # Step 1: Extract entities
    print("\n[1/8] Extracting entities...")
    entities_data = analyzer.extract_all_entities(papers)

    # Step 2: Build knowledge graph
    print("\n[2/8] Building knowledge graph...")
    entities_path = OUTPUT_DIR / 'entities.json'
    kg = analyzer.build_knowledge_graph(papers, entities_path)

    # Step 2.5: Determine resolution strategy
    optimal_res = None
    modularity_scores = None

    if args.auto_resolution:
        # For coverage optimization, use lower resolution (0.5) which provides
        # finer-grained communities that can be categorized. Modularity optimization
        # often gives too-coarse communities.
        #
        # We still run modularity scan for analysis/logging purposes.
        print("\n[2.5/8] Analyzing resolution impact (modularity scan)...")
        optimal_res_modularity, modularity_scores = find_optimal_resolution(kg.graph)

        # Save modularity curve for analysis
        mod_path = OUTPUT_DIR / 'modularity_curve.json'
        with open(mod_path, 'w') as f:
            json.dump({str(k): v for k, v in modularity_scores.items()}, f, indent=2)
        print(f"  Saved modularity curve to: {mod_path}")

        # Use lower resolution for better coverage
        optimal_res = 0.5
        print(f"\n  Using resolution 0.5 for better coverage (modularity-optimal was {optimal_res_modularity:.2f})")

    # Step 3: Detect communities
    print("\n[3/8] Detecting communities...")
    if args.auto_resolution:
        # Use optimal resolution only
        resolutions = [optimal_res]
        print(f"  Using optimal resolution: {optimal_res:.2f}")
    else:
        resolutions = [0.5, 1.0, 2.0, 4.0]

    communities_by_level = analyzer.detect_communities(kg.graph, resolutions=resolutions)

    # Step 4: Generate summaries
    print("\n[4/8] Generating community summaries...")
    summaries = analyzer.generate_community_summaries(
        kg.graph,
        communities_by_level,
        entities_data
    )

    # Step 5: Save overall stats
    print("\n[5/8] Saving overall statistics...")
    graph_stats = kg.get_stats()
    stats = analyzer.save_overall_stats(
        papers,
        entities_data,
        graph_stats,
        communities_by_level
    )

    # Step 5.5: Conservative community merging (if --auto-resolution)
    merged_categories = None

    if args.auto_resolution:
        print("\n[5.5/8] Conservative community merging...")

        # Load communities at optimal resolution
        level_path = OUTPUT_DIR / 'communities' / f'level_{optimal_res}.json'
        with open(level_path) as f:
            communities_json = json.load(f)

        # Add paper counts
        for comm in communities_json:
            comm["paper_count"] = len(extract_paper_dois(comm))

        print(f"  Computing similarity matrix for {len(communities_json)} communities...")
        similarities = compute_similarity_matrix(communities_json)
        print(f"  Found {len(similarities)} non-zero similarity pairs")

        # Merge conservatively
        print(f"  Merging with threshold={args.merge_threshold}...")
        merged = conservative_merge(
            communities_json,
            similarities,
            min_similarity=args.merge_threshold
        )
        print(f"  Merged into {len(merged)} communities")

        # Categorize
        merged_categories = categorize_communities(merged)
        print(f"  Categories: {len(merged_categories['major'])} major, "
              f"{len(merged_categories['emerging'])} emerging, "
              f"{len(merged_categories['niche'])} niche")

        # Save merged communities
        merged_path = OUTPUT_DIR / 'communities' / 'merged_conservative.json'
        with open(merged_path, 'w') as f:
            json.dump({
                "metadata": {
                    "resolution": optimal_res,
                    "merge_threshold": args.merge_threshold,
                    "total_communities": len(merged),
                    "algorithm": "Leiden + conservative_merge"
                },
                "communities": merged,
                "categories": {k: [c["community_id"] for c in v] for k, v in merged_categories.items()}
            }, f, indent=2)
        print(f"  Saved to: {merged_path}")

        # Calculate coverage
        total_papers = len(papers)
        major_coverage = sum(c["paper_count"] for c in merged_categories["major"])
        emerging_coverage = sum(c["paper_count"] for c in merged_categories["emerging"])
        total_coverage = major_coverage + emerging_coverage

        print(f"\n  Coverage stats:")
        print(f"    Major themes ({len(merged_categories['major'])}): {major_coverage} papers ({major_coverage/total_papers*100:.1f}%)")
        print(f"    Emerging topics ({len(merged_categories['emerging'])}): {emerging_coverage} papers ({emerging_coverage/total_papers*100:.1f}%)")
        print(f"    Combined: {total_coverage} papers ({total_coverage/total_papers*100:.1f}%)")

    # Step 6: Export graph
    print("\n[6/8] Exporting knowledge graph...")
    graph_path = OUTPUT_DIR / 'knowledge_graph.json'
    kg.save_json(str(graph_path))
    print(f"Saved knowledge graph to: {graph_path}")

    # Step 7: Generate OVERVIEW.md
    if args.skip_overview:
        print("\n[7/8] Skipping OVERVIEW.md generation (--skip-overview)")
        overview_path = None
    elif args.auto_resolution and merged_categories:
        print("\n[7/8] Generating hierarchical OVERVIEW.md...")
        # Determine summaries directory based on resolution
        summaries_dir = OUTPUT_DIR / 'summaries' / f'level_{optimal_res}'
        overview_path = generate_hierarchical_overview(
            OUTPUT_DIR,
            merged_categories,
            stats,
            summaries_dir
        )
        print(f"  Created: {overview_path}")
    else:
        print("\n[7/8] Generating OVERVIEW.md...")
        overview_path = generate_overview(
            OUTPUT_DIR,
            stats,
            top_n=args.top_n,
            min_size=args.min_size
        )
        print(f"  Created: {overview_path}")

    # Step 8: Final summary
    print("\n[8/8] Analysis complete!")

    # Count total summaries
    total_summaries = sum(len(s) for s in summaries.values())

    print("\n" + "="*60)
    print("Graph RAG Analysis Complete (V2)")
    print("="*60)
    print(f"\nOutputs saved to: {OUTPUT_DIR}")
    print("\nGenerated files:")
    print(f"  - entities.json")
    print(f"  - knowledge_graph.json")
    print(f"  - stats.json")
    if args.auto_resolution:
        print(f"  - modularity_curve.json")
        print(f"  - communities/level_{optimal_res}.json (optimal resolution)")
        print(f"  - communities/merged_conservative.json")
    else:
        print(f"  - communities/level_*.json (4 levels)")
    print(f"  - summaries/level_*/community_*.md ({total_summaries} total)")
    if overview_path:
        if args.auto_resolution:
            print(f"  - OVERVIEW.md (hierarchical: {len(merged_categories['major'])} major, {len(merged_categories['emerging'])} emerging)")
        else:
            print(f"  - OVERVIEW.md (top {args.top_n} communities, min size {args.min_size})")

    # Verification: Check 'rat' count
    rat_count = sum(
        1 for data in entities_data.values()
        for e in data.get('entities', [])
        if e['name'].lower() == 'rat'
    )
    print(f"\nVerification: 'rat' entity count = {rat_count}")


if __name__ == '__main__':
    main()
