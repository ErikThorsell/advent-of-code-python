from typing import List, Tuple

import networkx as nx


def create_dag(edges: List[Tuple[str, str]]) -> nx.DiGraph:
    graph = nx.DiGraph()
    graph.add_edges_from(edges)
    return graph
