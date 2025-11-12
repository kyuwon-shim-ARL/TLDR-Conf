"""
Conceptual Framework Builder for Research Landscape Analyzer

Automatically generates problem-solution hierarchical frameworks from paper landscapes.

Strategy:
- Extract key concepts from papers
- Classify papers into: Problems / Approaches / Limitations / Future
- Cluster papers by concept similarity
- Generate hierarchical framework structure
- Map speakers to framework positions
"""

from typing import List, Dict, Any, Optional, Tuple
from collections import Counter


class ConceptualFrameworkBuilder:
    """
    Build hierarchical problem-solution frameworks from research landscapes.

    Transforms flat paper lists into structured conceptual frameworks:
    1. Core Problems
    2. Approaches
    3. Limitations & Breakthroughs
    4. Future Directions
    """

    def __init__(self):
        """Initialize framework builder."""
        # Generic concepts to filter out
        self.generic_concepts = {
            'Medicine', 'Biology', 'Chemistry', 'Physics',
            'Genetics', 'Biochemistry', 'Science', 'Research',
            'Study', 'Analysis', 'Investigation'
        }

        # Keyword patterns for classification
        self.classification_keywords = {
            'problem': [
                'challenge', 'problem', 'difficulty', 'issue', 'obstacle',
                'barrier', 'impediment', 'complication', 'pathogen', 'disease'
            ],
            'approach': [
                'approach', 'method', 'technique', 'strategy', 'therapy',
                'treatment', 'intervention', 'tool', 'system', 'mechanism',
                'pathway', 'process', 'development'
            ],
            'limitation': [
                'limitation', 'drawback', 'weakness', 'challenge',
                'gap', 'unknown', 'unclear', 'debate', 'controversy'
            ],
            'future': [
                'future', 'perspective', 'outlook', 'emerging', 'novel',
                'new', 'next-generation', 'promising', 'potential'
            ]
        }

    def build_framework(
        self,
        landscape: Dict[str, Any],
        speakers: Optional[List[Dict[str, Any]]] = None,
        num_subcategories: int = 3
    ) -> Dict[str, Any]:
        """
        Build conceptual framework from landscape.

        Args:
            landscape: Landscape data from TopicAnalyzer
            speakers: Optional speaker information
            num_subcategories: Number of sub-categories per top-level category

        Returns:
            Hierarchical framework structure
        """
        print("\n🔬 Building conceptual framework...")

        # Step 1: Collect all papers
        all_papers = self._collect_all_papers(landscape)
        print(f"   Total papers: {len(all_papers)}")

        # Step 2: Extract key concepts
        key_concepts = self._extract_key_concepts(all_papers, top_k=15)
        print(f"   Key concepts extracted: {len(key_concepts)}")

        # Step 3: Classify papers into categories
        classified = self._classify_papers(all_papers, landscape)
        print(f"   Papers classified:")
        for cat, papers in classified.items():
            print(f"      {cat}: {len(papers)} papers")

        # Step 4: Cluster within each category
        framework = {
            'topic': landscape['topic'],
            'key_concepts': key_concepts,
            'core_problems': [],
            'approaches': [],
            'limitations': [],
            'future_directions': []
        }

        for category, papers in classified.items():
            if not papers:
                continue

            # Generate sub-categories for this category
            num_clusters = min(num_subcategories, max(1, (len(papers) + 2) // 3))
            subcategories = self._generate_subcategories(papers, num_clusters)

            # Add to framework
            if category == 'problem':
                framework_key = 'core_problems'
            elif category == 'approach':
                framework_key = 'approaches'
            elif category == 'limitation':
                framework_key = 'limitations'
            elif category == 'future':
                framework_key = 'future_directions'

            framework[framework_key] = subcategories

        # Step 5: Map speakers (if provided)
        if speakers:
            self._map_speakers_to_framework(framework, speakers)

        print(f"   ✅ Framework generated")
        print(f"      Core problems: {len(framework['core_problems'])}")
        print(f"      Approaches: {len(framework['approaches'])}")
        print(f"      Limitations: {len(framework['limitations'])}")
        print(f"      Future directions: {len(framework['future_directions'])}")

        return framework

    def _collect_all_papers(self, landscape: Dict[str, Any]) -> List[Dict[str, Any]]:
        """Collect all papers from landscape."""
        papers = []

        # Reviews
        if 'reviews' in landscape:
            for paper in landscape['reviews']:
                paper['source_type'] = 'review'
                papers.append(paper)

        # Anchors
        if 'anchors' in landscape:
            for paper in landscape['anchors']:
                paper['source_type'] = 'anchor'
                papers.append(paper)

        # Recent trends
        if 'recent_trends' in landscape and landscape['recent_trends']:
            for paper in landscape['recent_trends']:
                paper['source_type'] = 'trend'
                papers.append(paper)

        return papers

    def _extract_key_concepts(
        self,
        papers: List[Dict[str, Any]],
        top_k: int = 15
    ) -> List[str]:
        """
        Extract top K concepts from papers.

        Uses OpenAlex concepts + filtering.
        """
        concept_counts = Counter()

        for paper in papers:
            concepts = paper.get('concepts', [])
            for concept in concepts:
                name = concept.get('display_name', '')
                score = concept.get('score', 0)

                # Skip generic concepts
                if name in self.generic_concepts:
                    continue

                # Weight by score
                concept_counts[name] += score

        # Get top K
        top_concepts = [c for c, _ in concept_counts.most_common(top_k)]

        return top_concepts

    def _classify_papers(
        self,
        papers: List[Dict[str, Any]],
        landscape: Dict[str, Any]
    ) -> Dict[str, List[Dict[str, Any]]]:
        """
        Classify papers into 4 categories: problem/approach/limitation/future.

        Uses heuristic-based classification.
        """
        classified = {
            'problem': [],
            'approach': [],
            'limitation': [],
            'future': []
        }

        for paper in papers:
            category = self._classify_single_paper(paper, landscape)
            classified[category].append(paper)

        return classified

    def _classify_single_paper(
        self,
        paper: Dict[str, Any],
        landscape: Dict[str, Any]
    ) -> str:
        """
        Classify single paper into category.

        Heuristics:
        - Title/abstract keyword matching
        - Paper type (review, anchor, trend)
        - Publication year
        """
        title = paper.get('title', '').lower()

        # Score each category
        scores = {
            'problem': 0,
            'approach': 0,
            'limitation': 0,
            'future': 0
        }

        # Keyword matching
        for category, keywords in self.classification_keywords.items():
            for keyword in keywords:
                if keyword in title:
                    scores[category] += 1

        # Heuristics based on paper type
        source_type = paper.get('source_type', '')

        if source_type == 'anchor':
            # Foundational papers usually define problems
            scores['problem'] += 2

        elif source_type == 'review':
            # Reviews often discuss approaches and limitations
            scores['approach'] += 1
            scores['limitation'] += 1

        elif source_type == 'trend':
            # Recent papers often propose new approaches or future directions
            scores['approach'] += 1
            scores['future'] += 2

        # Year-based heuristic
        year = paper.get('publication_year')
        if year and year >= 2023:
            # Very recent → likely future direction or new approach
            scores['future'] += 1
            scores['approach'] += 1

        # Return category with highest score (ties broken by order)
        max_score = max(scores.values())
        if max_score == 0:
            # Default: approach (most papers propose methods)
            return 'approach'

        return max(scores, key=scores.get)

    def _generate_subcategories(
        self,
        papers: List[Dict[str, Any]],
        num_clusters: int = 3
    ) -> List[Dict[str, Any]]:
        """
        Generate sub-categories by clustering papers.

        Uses concept-based clustering (simplified K-means).
        """
        if len(papers) == 0:
            return []

        if len(papers) <= 2:
            # Too few papers, just create one subcategory
            concept_name = self._get_primary_concept(papers)
            return [{
                'name': concept_name,
                'papers': papers,
                'speakers': []
            }]

        # Build concept vectors
        all_concepts = set()
        for paper in papers:
            for concept in paper.get('concepts', []):
                all_concepts.add(concept['display_name'])

        concept_list = list(all_concepts)

        # Create binary vectors
        vectors = []
        for paper in papers:
            paper_concepts = {c['display_name'] for c in paper.get('concepts', [])}
            vector = [1 if c in paper_concepts else 0 for c in concept_list]
            vectors.append(vector)

        # Simple clustering (assign to cluster based on first concept match)
        # This is a simplified version; real K-means would be better
        clusters = self._simple_cluster(papers, vectors, num_clusters)

        # Name each cluster
        subcategories = []
        for cluster_id, cluster_papers in clusters.items():
            concept_name = self._get_primary_concept(cluster_papers)

            subcategories.append({
                'name': concept_name,
                'papers': cluster_papers,
                'speakers': []
            })

        return subcategories

    def _simple_cluster(
        self,
        papers: List[Dict[str, Any]],
        vectors: List[List[int]],
        num_clusters: int
    ) -> Dict[int, List[Dict[str, Any]]]:
        """
        Simple clustering (assign papers to clusters based on primary concept).

        This is a simplified version. For production, use sklearn KMeans.
        """
        # Extract primary concepts
        primary_concepts = []
        for paper in papers:
            concepts = paper.get('concepts', [])
            if concepts:
                # Get concept with highest score (excluding generic)
                valid_concepts = [c for c in concepts
                                if c['display_name'] not in self.generic_concepts]
                if valid_concepts:
                    primary = valid_concepts[0]['display_name']
                    primary_concepts.append(primary)
                else:
                    primary_concepts.append('Other')
            else:
                primary_concepts.append('Other')

        # Count concept frequencies
        concept_counts = Counter(primary_concepts)

        # Top N concepts become cluster names
        top_concepts = [c for c, _ in concept_counts.most_common(num_clusters)]

        # Assign papers to clusters
        clusters = {i: [] for i in range(len(top_concepts))}

        for i, paper in enumerate(papers):
            primary = primary_concepts[i]

            # Find matching cluster
            if primary in top_concepts:
                cluster_id = top_concepts.index(primary)
            else:
                # Assign to cluster with fewest papers (balance)
                cluster_id = min(clusters, key=lambda k: len(clusters[k]))

            clusters[cluster_id].append(paper)

        # Remove empty clusters
        clusters = {k: v for k, v in clusters.items() if v}

        return clusters

    def _get_primary_concept(self, papers: List[Dict[str, Any]]) -> str:
        """Get primary concept for a group of papers."""
        concept_counts = Counter()

        for paper in papers:
            for concept in paper.get('concepts', []):
                name = concept['display_name']
                if name not in self.generic_concepts:
                    concept_counts[name] += 1

        if concept_counts:
            return concept_counts.most_common(1)[0][0]
        else:
            return "Unspecified"

    def _map_speakers_to_framework(
        self,
        framework: Dict[str, Any],
        speakers: List[Dict[str, Any]]
    ):
        """
        Map speakers to framework positions.

        Matches speaker research areas with framework subcategories.
        """
        for speaker in speakers:
            speaker_name = speaker.get('name', 'Unknown')
            research_areas = speaker.get('research_areas', [])

            # Find best matching subcategory
            best_match = None
            best_score = 0

            for category_name in ['core_problems', 'approaches', 'limitations', 'future_directions']:
                for subcategory in framework[category_name]:
                    # Calculate overlap score
                    score = self._calculate_match_score(
                        research_areas,
                        subcategory['name'],
                        subcategory['papers']
                    )

                    if score > best_score:
                        best_score = score
                        best_match = subcategory

            # Add speaker to best matching subcategory
            if best_match:
                best_match['speakers'].append(speaker_name)

    def _calculate_match_score(
        self,
        research_areas: List[str],
        subcategory_name: str,
        papers: List[Dict[str, Any]]
    ) -> float:
        """Calculate match score between speaker and subcategory."""
        score = 0.0

        # Check if any research area appears in subcategory name
        for area in research_areas:
            if area.lower() in subcategory_name.lower():
                score += 2.0

        # Check concept overlap with papers
        subcategory_concepts = set()
        for paper in papers:
            for concept in paper.get('concepts', []):
                subcategory_concepts.add(concept['display_name'].lower())

        for area in research_areas:
            if area.lower() in subcategory_concepts:
                score += 1.0

        return score

    def format_framework_markdown(
        self,
        framework: Dict[str, Any]
    ) -> str:
        """
        Format framework as markdown document.

        Args:
            framework: Conceptual framework structure

        Returns:
            Markdown string
        """
        md = f"## 🔬 개념적 Research Framework: {framework['topic']}\n\n"
        md += "*자동 생성된 문제-해결 계통도*\n\n"

        # Key concepts overview
        md += "### 🔑 핵심 개념 (Key Concepts)\n\n"
        for i, concept in enumerate(framework['key_concepts'][:10], 1):
            md += f"{i}. {concept}\n"
        md += "\n---\n\n"

        # 1. Core Problems
        md += "### 1. 핵심 문제 (Core Problems)\n\n"
        md = self._format_category(md, framework['core_problems'], "문제")

        # 2. Approaches
        md += "### 2. 접근 방식 (Approaches)\n\n"
        md = self._format_category(md, framework['approaches'], "방법론")

        # 3. Limitations
        md += "### 3. 한계점 & 돌파구 (Limitations & Breakthroughs)\n\n"
        md = self._format_category(md, framework['limitations'], "한계")

        # 4. Future Directions
        md += "### 4. 미래 방향 (Future Directions)\n\n"
        md = self._format_category(md, framework['future_directions'], "방향")

        md += "---\n\n"
        md += "*Generated by Conceptual Framework Builder v1.0*\n"

        return md

    def _format_category(
        self,
        md: str,
        subcategories: List[Dict[str, Any]],
        category_type: str
    ) -> str:
        """Format a single category section."""
        if not subcategories:
            md += f"*No {category_type} identified in analysis.*\n\n"
            return md

        for i, subcat in enumerate(subcategories, 1):
            name = subcat['name']
            papers = subcat['papers']
            speakers = subcat.get('speakers', [])

            md += f"#### {i}.{i} {name}\n\n"

            # Papers
            md += f"**관련 논문** ({len(papers)} papers):\n\n"
            for paper in papers[:3]:  # Show top 3
                title = paper.get('title', 'Unknown')[:80]
                year = paper.get('publication_year', 'N/A')
                citations = paper.get('cited_by_count', 0)
                md += f"- \"{title}...\" ({year}, {citations:,} citations)\n"

            if len(papers) > 3:
                md += f"- *...and {len(papers) - 3} more papers*\n"

            md += "\n"

            # Speakers
            if speakers:
                md += f"**세션 내 연사**: {', '.join(speakers)}\n\n"

            md += "---\n\n"

        return md


# Convenience function

def build_conceptual_framework(
    landscape: Dict[str, Any],
    speakers: Optional[List[Dict[str, Any]]] = None,
    output_file: Optional[str] = None
) -> Dict[str, Any]:
    """
    Quick wrapper to build conceptual framework.

    Args:
        landscape: Landscape data from TopicAnalyzer
        speakers: Optional speaker information
        output_file: Optional file to save markdown

    Returns:
        Framework structure

    Example:
        landscape = analyzer.analyze("mycobacterial pathogenesis")
        framework = build_conceptual_framework(landscape)
    """
    builder = ConceptualFrameworkBuilder()
    framework = builder.build_framework(landscape, speakers=speakers)

    if output_file:
        md = builder.format_framework_markdown(framework)
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(md)
        print(f"📄 Framework saved to: {output_file}")

    return framework
