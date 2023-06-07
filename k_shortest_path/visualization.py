import os
import argparse
import yaml
import networkx as nx
from typing import List
import matplotlib.pyplot as plt
from mock_data import mock_graph
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
            # vis_dir = os.path.join(self.vis_root_dir, vis_name)
            vis_dir = self.vis_root_dir
            shortest_paths = self.solver(source, dest)
            for idx in range(len(shortest_paths)):
                shortest_path=shortest_paths[idx]
                pos = nx.spring_layout(self.G)
                node_colors = {}
                labels = {}
                for node in self.G.nodes():
                    if node == source:
                        node_colors[node] = 'g'
                        labels[node]= str(node)+'\n(source)'
                    elif node == dest:
                        node_colors[node] = 'y'
                        labels[node]= str(node)+'\n(dest)'
                    else:
                        node_colors[node] = 'b'
                        labels[node]= node
                nx.draw(self.G, pos, with_labels=True, node_color=list(node_colors.values()), labels = labels)
                edge_labels = {(shortest_path[i], shortest_path[i+1]): i+1 for i in range(len(shortest_path)-1)}
                edgelist = [(shortest_path[i], shortest_path[i+1]) for i in range(len(shortest_path)-1)]
                nx.draw_networkx_edges(self.G, pos, edgelist=edgelist, edge_color='r', width=2.0)
                nx.draw_networkx_edge_labels(self.G, pos, edge_labels=edge_labels, font_color='black')
                
                plt.savefig(f'{vis_dir}/{vis_name}--{idx}.pdf')
                plt.clf()
            
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
    # v  = Visualization(
    #     mock_graph(),
    #     2,
    #     [[2,3]],
    #     '/home/binhpham2/master_lectuters/co so toan/k_shortest_path/results'
    # )
    # v.visualize()
