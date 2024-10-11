import networkx as nx
import matplotlib.pyplot as plt
exp_cities = {
    "Stockholm": {"Gothenburg": 396, "Malmo": 614, "Uppsala": 71, "Orebro": 203, "Linkoping": 199, "Norrkoping": 160, "Helsingborg": 556},
    "Gothenburg": {"Stockholm": 396, "Malmo": 272, "Vaxjo": 185, "Linkoping": 328, "Uppsala": 466, "Helsingborg": 229, "Karlstad": 252},
    "Malmo": {"Gothenburg": 272, "Stockholm": 614, "Lund": 19, "Uppsala": 674, "Vaxjo": 197, "Helsingborg": 65},
    "Uppsala": {"Stockholm": 71, "Orebro": 160, "Umea": 553, "Norrkoping": 196, "Gothenburg": 466},
    "Linkoping": {"Gothenburg": 328, "Orebro": 118, "Norrkoping": 41, "Stockholm": 199},
    "Orebro": {"Stockholm": 203, "Gothenburg": 252, "Linkoping": 118, "Karlstad": 116},
    "Norrkoping": {"Stockholm": 160, "Linkoping": 41, "Uppsala": 196, "Vasteras": 163},
    "Lund": {"Malmo": 19, "Helsingborg": 67, "Gothenburg": 243},
    "Helsingborg": {"Malmo": 65, "Gothenburg": 229, "Lund": 67, "Stockholm": 556},
    "Vaxjo": {"Gothenburg": 185, "Malmo": 197, "Stockholm": 368, "Karlstad": 308},
    "Karlstad": {"Gothenburg": 252, "Orebro": 116, "Stockholm": 305, "Vaxjo": 308},
    "Umea": {"Uppsala": 553, "Stockholm": 636, "Lulea": 265},
    "Lulea": {"Umea": 265, "Kiruna": 341},
    "Kiruna": {"Lulea": 341, "Umea": 606}
}

def create_graph():
    G = nx.Graph()
    for city, connections in exp_cities.items():
        for neighbor, fuel in connections.items():
            G.add_edge(city, neighbor, weight=fuel)
    return G

'''def plot_graph(G):
    plt.figure(figsize=(12, 10))
    pos = nx.spring_layout(G, seed=42)  # Position nodes using spring layout
    weights = nx.get_edge_attributes(G, 'weight')
    
    # Draw the nodes and edges
    nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=3000, font_size=10, font_weight='bold', edge_color='gray')
    
    # Draw edge labels (weights)
    nx.draw_networkx_edge_labels(G, pos, edge_labels=weights)
    
    plt.title("Swedish Cities and Road Distances")
    plt.show()

# Create and plot the graph
G = create_graph()
plot_graph(G)
'''