import networkx as nx

# Define your cities and edges
cities = {
    "Stockholm": {"Uppsala": 1.2, "Gothenburg": 2.5, "Malmo": 3.1, "Vasteras": 1.5},
    "Uppsala": {"Stockholm": 1.2, "Vasteras": 1.8},
    "Gothenburg": {"Stockholm": 2.5, "Malmo": 1.1, "Vasteras": 2.0},
    "Malmo": {"Gothenburg": 1.1, "Stockholm": 3.1},
    "Vasteras": {"Stockholm": 1.5, "Uppsala": 1.8, "Gothenburg": 2.0},
}

def create_graph():
    G = nx.Graph()
    for city, connections in cities.items():
        for neighbor, fuel in connections.items():
            G.add_edge(city, neighbor, weight=fuel)
    return G
