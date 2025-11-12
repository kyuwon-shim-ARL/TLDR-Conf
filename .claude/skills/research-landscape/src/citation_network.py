"""
Citation Network Builder for Research Landscape Analyzer
Constructs citation graphs and calculates network metrics.
"""

import networkx as nx
from typing import List, Dict, Any, Optional, Set
from openalex_client import OpenAlexClient


class CitationNetworkBuilder:
    """
    Builds citation networks from seed papers.

    Constructs directed graphs:
    - Nodes: Papers
    - Edges: Citations (A → B means A cites B)

    Calculates network metrics:
    - PageRank: Overall importance
    - Betweenness centrality: Bridge papers
    - Clustering coefficient: Community structure
    """

    def __init__(self, email: Optional[str] = None):
        """
        Initialize builder.

        Args:
            email: Email for OpenAlex polite pool (recommended)
        """
        self.client = OpenAlexClient(email=email)
        self.graph = None
        self.metrics = {}

    def build_network(
        self,
        seed_papers: List[Dict[str, Any]],
        hops: int = 1,
        max_refs_per_paper: int = 20,
        max_cites_per_paper: int = 50
    ) -> nx.DiGraph:
        """
        Build citation network from seed papers.

        Args:
            seed_papers: List of anchor papers to start from
            hops: Number of hops (1 = direct citations only, 2 = 2-hop)
            max_refs_per_paper: Max references to fetch per paper
            max_cites_per_paper: Max citing papers to fetch per paper

        Returns:
            NetworkX directed graph

        Example:
            builder = CitationNetworkBuilder(email="your@email.com")
            network = builder.build_network(
                seed_papers=anchors,
                hops=1,
                max_refs_per_paper=20,
                max_cites_per_paper=50
            )

            print(f"Nodes: {network.number_of_nodes()}")
            print(f"Edges: {network.number_of_edges()}")
        """
        print(f"\n🕸️  Building citation network...")
        print(f"   Seed papers: {len(seed_papers)}")
        print(f"   Hops: {hops}")

        # Initialize graph
        self.graph = nx.DiGraph()

        # Add seed papers as nodes
        seed_ids = set()
        for paper in seed_papers:
            paper_id = self._extract_id(paper.get('id'))
            if paper_id:
                self.graph.add_node(paper_id, **self._extract_node_data(paper))
                seed_ids.add(paper_id)

        print(f"   Added {len(seed_ids)} seed nodes")

        # Build network hop by hop
        current_layer = seed_ids
        for hop in range(hops):
            print(f"\n   Hop {hop + 1}:")
            next_layer = set()

            # For each paper in current layer
            for paper_id in current_layer:
                # Fetch backward citations (references)
                refs = self._fetch_references(paper_id, max_refs_per_paper)
                for ref_id in refs:
                    if ref_id not in self.graph:
                        # Add new node
                        ref_data = self.client.fetch_work(ref_id)
                        if ref_data:
                            self.graph.add_node(ref_id, **self._extract_node_data(ref_data))
                            next_layer.add(ref_id)
                    # Add edge (paper_id cites ref_id)
                    self.graph.add_edge(paper_id, ref_id, type='cites')

                # Fetch forward citations (citing papers)
                cites = self._fetch_citing_papers(paper_id, max_cites_per_paper)
                for cite_id in cites:
                    if cite_id not in self.graph:
                        # Add new node
                        cite_data = self.client.fetch_work(cite_id)
                        if cite_data:
                            self.graph.add_node(cite_id, **self._extract_node_data(cite_data))
                            next_layer.add(cite_id)
                    # Add edge (cite_id cites paper_id)
                    self.graph.add_edge(cite_id, paper_id, type='cites')

            print(f"      Added {len(next_layer)} new nodes")
            current_layer = next_layer

            if not current_layer:
                break

        print(f"\n   ✅ Network complete:")
        print(f"      Total nodes: {self.graph.number_of_nodes()}")
        print(f"      Total edges: {self.graph.number_of_edges()}")

        return self.graph

    def calculate_metrics(self) -> Dict[str, Any]:
        """
        Calculate network metrics.

        Returns:
            Dict with metrics:
            - pagerank: Dict[node_id -> score]
            - betweenness: Dict[node_id -> score]
            - clustering: Float (average clustering coefficient)
            - diameter: Int (longest shortest path)
            - density: Float (edge density)

        Example:
            metrics = builder.calculate_metrics()
            print(f"Average clustering: {metrics['clustering']:.3f}")

            # Top 5 by PageRank
            top_pr = sorted(metrics['pagerank'].items(),
                           key=lambda x: x[1], reverse=True)[:5]
            for node_id, score in top_pr:
                print(f"{node_id}: {score:.4f}")
        """
        if not self.graph:
            raise ValueError("Build network first using build_network()")

        print(f"\n📊 Calculating network metrics...")

        # PageRank (importance)
        pagerank = nx.pagerank(self.graph, alpha=0.85)
        print(f"   ✓ PageRank calculated")

        # Betweenness centrality (bridges)
        betweenness = nx.betweenness_centrality(self.graph)
        print(f"   ✓ Betweenness calculated")

        # Clustering coefficient (community structure)
        # For directed graph, convert to undirected
        G_undirected = self.graph.to_undirected()
        clustering = nx.average_clustering(G_undirected)
        print(f"   ✓ Clustering calculated: {clustering:.3f}")

        # Network topology metrics
        try:
            # Only works if graph is weakly connected
            if nx.is_weakly_connected(self.graph):
                diameter = nx.diameter(G_undirected)
            else:
                diameter = None
        except:
            diameter = None

        density = nx.density(self.graph)

        self.metrics = {
            'pagerank': pagerank,
            'betweenness': betweenness,
            'clustering': clustering,
            'diameter': diameter,
            'density': density,
            'num_nodes': self.graph.number_of_nodes(),
            'num_edges': self.graph.number_of_edges()
        }

        print(f"   ✅ Metrics complete\n")

        return self.metrics

    def find_bridge_papers(self, top_k: int = 10) -> List[Dict[str, Any]]:
        """
        Find top bridge papers (high betweenness centrality).

        These papers connect different research communities.

        Args:
            top_k: Number of top bridges to return

        Returns:
            List of paper dicts with betweenness scores

        Example:
            bridges = builder.find_bridge_papers(top_k=5)
            for paper in bridges:
                print(f"{paper['title']}: {paper['betweenness']:.4f}")
        """
        if 'betweenness' not in self.metrics:
            self.calculate_metrics()

        # Sort by betweenness
        sorted_nodes = sorted(
            self.metrics['betweenness'].items(),
            key=lambda x: x[1],
            reverse=True
        )[:top_k]

        # Get node data
        bridges = []
        for node_id, score in sorted_nodes:
            node_data = self.graph.nodes[node_id]
            bridges.append({
                'id': node_id,
                'title': node_data.get('title', 'Unknown'),
                'year': node_data.get('publication_year'),
                'citations': node_data.get('cited_by_count', 0),
                'betweenness': score
            })

        return bridges

    def export_graphml(self, output_file: str):
        """
        Export network to GraphML format (for Gephi visualization).

        Args:
            output_file: Path to save GraphML file

        Example:
            builder.export_graphml("network.graphml")
            # Then open in Gephi for visualization
        """
        if not self.graph:
            raise ValueError("Build network first")

        nx.write_graphml(self.graph, output_file)
        print(f"📊 Network exported to: {output_file}")
        print(f"   Open in Gephi for visualization")

    def _extract_id(self, openalex_id: str) -> Optional[str]:
        """Extract clean ID from OpenAlex ID."""
        if not openalex_id:
            return None

        if openalex_id.startswith('http'):
            return openalex_id.split('/')[-1]
        return openalex_id

    def _extract_node_data(self, paper: Dict[str, Any]) -> Dict[str, Any]:
        """Extract relevant node attributes."""
        return {
            'title': paper.get('title', 'Unknown'),
            'publication_year': paper.get('publication_year'),
            'cited_by_count': paper.get('cited_by_count', 0),
            'doi': paper.get('doi'),
        }

    def _fetch_references(
        self,
        paper_id: str,
        limit: int
    ) -> List[str]:
        """Fetch reference IDs for a paper."""
        paper = self.client.fetch_work(paper_id)
        if not paper:
            return []

        refs = paper.get('referenced_works', [])
        # Return IDs (extract from URLs)
        return [self._extract_id(ref) for ref in refs[:limit] if ref]

    def _fetch_citing_papers(
        self,
        paper_id: str,
        limit: int
    ) -> List[str]:
        """Fetch IDs of papers that cite this paper."""
        url = f"{self.client.base_url}/works?filter=cites:{paper_id}&per-page={min(limit, 200)}"

        response = self.client._make_request(url)
        if not response:
            return []

        papers = response.get('results', [])
        return [self._extract_id(p.get('id')) for p in papers[:limit] if p.get('id')]


# Convenience function

def build_citation_network(
    seed_papers: List[Dict[str, Any]],
    hops: int = 1,
    email: Optional[str] = None
) -> nx.DiGraph:
    """
    Quick wrapper to build citation network.

    Args:
        seed_papers: Anchor papers to start from
        hops: Network depth (1 or 2)
        email: Email for polite pool

    Returns:
        NetworkX directed graph

    Example:
        network = build_citation_network(anchors, hops=1)
        print(f"Nodes: {network.number_of_nodes()}")
    """
    builder = CitationNetworkBuilder(email=email)
    return builder.build_network(seed_papers, hops=hops)
