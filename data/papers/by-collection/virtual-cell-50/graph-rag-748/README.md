# Graph RAG Analysis: 748 Virtual Cell Papers

## Overview

This directory contains a comprehensive Graph RAG (Retrieval-Augmented Generation) analysis of 748 papers related to virtual cell research. The analysis was performed on 2026-02-02.

## Methodology

### 1. Entity Extraction
- **Approach**: Rule-based entity extraction from paper titles
- **Entity Types**: METHOD, ORGANISM, CONCEPT, DATASET
- **Total entities extracted**: 3,823 mentions (1,506 unique entities)

### 2. Knowledge Graph Construction
- **Graph structure**: Bipartite graph connecting papers and entities
- **Nodes**: 2,243 total (748 papers + 1,495 entities)
- **Edges**: 3,823 connections (paper-entity relationships)
- **Implementation**: NetworkX graph using `hybrid_rag.py` module

### 3. Community Detection
- **Algorithm**: Louvain community detection (supports multi-resolution)
- **Resolution levels**: 4 levels (0.5, 1.0, 2.0, 4.0)
- **Total communities detected**: 434 across all levels

### 4. Community Summarization
- **Approach**: Rule-based summaries generated from entity frequencies and paper metadata
- **Output**: 434 markdown summaries organized by resolution level

## File Structure

```
graph-rag-748/
├── README.md                    # This file
├── entities.json                # Extracted entities for all papers
├── knowledge_graph.json         # Complete NetworkX graph export
├── stats.json                   # Overall analysis statistics
├── communities/
│   ├── level_0.5.json          # 159 communities (fine-grained)
│   ├── level_1.0.json          # 68 communities
│   ├── level_2.0.json          # 89 communities
│   └── level_4.0.json          # 118 communities (coarse-grained)
└── summaries/
    ├── level_0.5/               # 159 community summaries
    ├── level_1.0/               # 68 community summaries
    ├── level_2.0/               # 89 community summaries
    └── level_4.0/               # 118 community summaries
```

## Key Statistics

### Dataset
- **Total papers**: 748
- **Categories**:
  - Foundation models: 106 papers
  - Whole cell models: 191 papers
  - Systems biology tools: 209 papers
  - Multi-scale modeling: 96 papers
  - Virtual cell specific: 146 papers

### Entity Extraction
- **Total mentions**: 3,823
- **Unique entities**: 1,506
- **Entity type distribution**:
  - METHOD: 2,873 mentions (1,423 unique)
  - ORGANISM: 470 mentions (21 unique)
  - CONCEPT: 423 mentions (35 unique)
  - DATASET: 57 mentions (16 unique)

### Top 10 Most Frequent Entities
1. cell (171 mentions)
2. rat (126 mentions)
3. network (66 mentions)
4. modeling (59 mentions)
5. single-cell (50 mentions)
6. The (49 mentions)
7. Models (41 mentions)
8. omics (38 mentions)
9. cellular (37 mentions)
10. pathway (35 mentions)

### Community Detection Results

#### Level 0.5 (Fine-grained)
- **Communities**: 159
- **Average size**: 14.1 nodes
- **Size range**: 1-514 nodes
- **Distribution**: 84 small, 72 medium, 1 large, 2 very large

#### Level 1.0
- **Communities**: 68
- **Average size**: 33.0 nodes
- **Size range**: 1-247 nodes
- **Distribution**: 40 small, 10 medium, 12 large, 6 very large

#### Level 2.0
- **Communities**: 89
- **Average size**: 25.2 nodes
- **Size range**: 1-116 nodes
- **Distribution**: 40 small, 34 medium, 14 large, 1 very large

#### Level 4.0 (Coarse-grained)
- **Communities**: 118
- **Average size**: 19.0 nodes
- **Size range**: 1-48 nodes
- **Distribution**: 41 small, 77 medium, 0 large, 0 very large

## Usage Examples

### Loading the Knowledge Graph
```python
import json
import networkx as nx

# Load graph
with open('knowledge_graph.json') as f:
    graph_data = json.load(f)
graph = nx.node_link_graph(graph_data)

# Query paper entities
paper_doi = "https://doi.org/10.1101/2023.04.30.538439"
neighbors = list(graph.neighbors(paper_doi))
print(f"Entities connected to paper: {len(neighbors)}")
```

### Analyzing Communities
```python
import json

# Load communities at resolution 1.0
with open('communities/level_1.0.json') as f:
    communities = json.load(f)

# Find largest community
largest = max(communities, key=lambda c: c['size'])
print(f"Largest community: {largest['size']} members")

# Read its summary
with open(f'summaries/level_1.0/community_{largest["community_id"]}.md') as f:
    summary = f.read()
print(summary)
```

### Entity Analysis
```python
import json
from collections import Counter

# Load entities
with open('entities.json') as f:
    entities_data = json.load(f)

# Find papers mentioning "foundation model"
papers_with_fm = [
    doi for doi, data in entities_data.items()
    if any(e['name'].lower() == 'foundation model' for e in data['entities'])
]
print(f"Papers mentioning 'foundation model': {len(papers_with_fm)}")
```

## Implementation Details

### Scripts
- **Main script**: `graph_rag_analysis_748_simple.py`
- **Dependencies**: `networkx`, `cdlib`, `paper_pipeline.hybrid_rag`

### Entity Extraction Rules
The rule-based extractor uses keyword matching on paper titles:
- **Methods**: ML/DL algorithms, computational techniques, tools, frameworks
- **Organisms**: Species, cell types, biological systems
- **Concepts**: Scientific phenomena, research areas, biological processes
- **Datasets**: Databases, repositories, data sources

Capitalized terms (3+ characters) are also extracted as potential methods or datasets.

### Community Detection Algorithm
- **Louvain algorithm**: Fast, hierarchical community detection
- **Resolution parameter**: Controls granularity (lower = fewer, larger communities)
- **Optimization**: Modularity-based optimization

## Limitations

1. **Entity extraction**: Rule-based approach may miss context-specific entities
2. **Title-only**: Entities extracted only from titles, not abstracts or full text
3. **No relationship extraction**: Only paper-entity connections, no entity-entity relationships
4. **Summary quality**: Automated summaries based on entity frequencies, not semantic understanding

## Future Improvements

1. Use Claude API for semantic entity extraction and relationship identification
2. Include abstract text for richer entity extraction
3. Generate LLM-based community summaries with deeper insights
4. Add temporal analysis of research trends
5. Create interactive visualization of the knowledge graph
6. Implement RAG queries for paper retrieval based on semantic questions

## Related Files

- **Input data**: `../comprehensive_papers.json`
- **Analysis script**: `/home/kyuwon/projects/MSK2025/graph_rag_analysis_748_simple.py`
- **Hybrid RAG module**: `/.claude/skills/paper-pipeline/src/paper_pipeline/hybrid_rag.py`

## Citation

If you use this analysis, please cite:
```
Graph RAG Analysis of 748 Virtual Cell Papers
Generated: 2026-02-02
Method: Louvain community detection with rule-based entity extraction
Repository: MSK2025
```
