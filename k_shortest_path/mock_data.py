import networkx as nx

A = 1
B = 2
C = 3
D = 4

mock_map_data = {
    A:{ 
        "longtitude": 1.0,
        "lattitude": 2.0,
        "street": "LTK",
        "reachable_to": [B, C, D]
    },

    B:{ 
        "longtitude": 2.0,
        "lattitude": 3.0,
        "street": "LTK",
        "reachable_to": [A, C, D]
    },

    C:{ 
        "longtitude": 3.0,
        "lattitude": 4.0,
        "street": "LTK",
        "reachable_to": [A, B, D]
    },

    D:{ 
        "longtitude": 4.0,
        "lattitude": 5.0,
        "street": "LTK",
        "reachable_to": [A, B, C]
    },
}

def mock_graph():
    G = nx.Graph()
    G.add_node(A)
    G.add_node(B)
    G.add_node(C)
    G.add_node(D)
    G.add_edge(A, B, weight= A + B)
    G.add_edge(A, C, weight= A + C)
    G.add_edge(A, D, weight= A + D)
    G.add_edge(B, C, weight= B + C)
    G.add_edge(B, D, weight= B + D)
    G.add_edge(C, D, weight= C + D)

    return G
