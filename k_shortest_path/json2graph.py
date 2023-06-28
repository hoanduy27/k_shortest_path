import argparse
import json
from dataclasses import dataclass 
from .mock_data import *
from .utils import dist

def json2graph_mock(data_path, out_graph_path):
    nx.write_gml(mock_graph(), out_graph_path)


def json2graph(data_path, out_graph_path):
    G = nx.Graph()
    # TODO (Khoan): Parse map data in data_path (JSON) to nx.Graph and write to `out_graph_path`
    mock_map_data = json.load(open(data_path), 'r')
    
    # add all nodes in graph
    for node in list(mock_map_data.keys()):
        G.add_node(node)
    
    visited_edge = []
    for loc, info in mock_map_data.items():
        for des in info['reachable_to']:
            if str(loc + des) not in visited_edge:
                weight_edge = dist(info['longtitude'], 
                                info['lattitude'], 
                                mock_map_data[des]['longtitude'],
                                mock_map_data[des]['lattitude'])
                
                G.add_edge(loc, des, weight=weight_edge)
                visited_edge.append(str(loc + des))
                visited_edge.append(str(des + loc))
                
    nx.write_gml(G, out_graph_path)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "data_path",
        type=str,
        help="Path to map data"
    )
    parser.add_argument(
        "out_graph_path",
        type=str,
        help="Path to export graph"
    )
    parser.add_argument(
        "--mock",
        action="store_true",
    )
    args = parser.parse_args()

    if args.mock:
        json2graph_func = json2graph_mock
    else:
        json2graph_func = json2graph
    
    json2graph_func(
        data_path=args.data_path, 
        out_graph_path=args.out_graph_path
    )

if __name__=='__main__':
    main()