import os
import argparse
import yaml
import networkx as nx
from typing import List
from k_shortest_path import Solver
class Visualization:
    """
    Visualization
    
    Args
        G: the nx.Graph graph
        k: Number of shortest paths
        pairs: List of tuple of (source, dest) to compute shortest path
        vis_root_dir: Root directory to store the visualization result
    """
    def __init__(
            self, 
            G: nx.Graph, 
            k: int, 
            pairs: List,
            vis_root_dir: str = None
    ):
        self.solver = Solver(G, k)
        self.G = G
        self.k = k
        self.pairs = pairs
        self.vis_root_dir = vis_root_dir

    def visualize(self):
        for pair in self.pairs:
            source, dest = pair
            vis_name = f'{source}--{dest}'
            vis_dir = os.path.join(self.vis_root_dir, vis_name)

            shortest_paths = self.solver(source, dest) 
            print(shortest_paths)
            # TODO (Binh): Visualize and store result to `vis_dir`, 
            # format `vis_dir`/`k`.pdf, where `k` is the k-th shortest path

    @classmethod
    def from_config(cls, graph_path, config_path):
        G = nx.read_gml(graph_path)
        with open(config_path, 'r') as f:
            config_params = yaml.load(f, Loader=yaml.Loader)

        if 'vis_root_dir' not in config_params:
            vis_root_dir = os.path.basename(config_path)
            config_params.update(dict(vis_root_dir=vis_root_dir))

        return cls(G, **config_params)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "graph_path",
        help="Path to the gml graph"
    )
    parser.add_argument(
        "config_path",
        help="Path to the visualization config file"
    )
    args = parser.parse_args()

    viz = Visualization.from_config(
        args.graph_path,
        args.config_path
    )
    viz.visualize()

if __name__ == "__main__":
    main()