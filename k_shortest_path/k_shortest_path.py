from itertools import islice

import networkx as nx
from .mock_data import *


class Solver:
    def __init__(self, G, k):
        self.G = G
        self.k = k

    def __call__(self, source, dest):
        paths = islice(
            nx.shortest_simple_paths(self.G, source, dest),
            self.k
        )
        return list(paths)
