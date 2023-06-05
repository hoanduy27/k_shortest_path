import argparse
from dataclasses import dataclass 
from .mock_data import *

def json2graph_mock(data_path, out_graph_path):
    nx.write_gml(mock_graph(), out_graph_path)

def json2graph(data_path, out_graph_path):
    G = nx.Graph()
    # TODO (Khoan):

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