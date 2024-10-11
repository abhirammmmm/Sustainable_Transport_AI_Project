from flask import Flask, render_template, request
import networkx as nx
from matplotlib import pyplot as plt
from Data.expanded_data import create_graph
import matplotlib
matplotlib.use('Agg')  # Use a non-interactive backend

app = Flask(__name__)

# Create the graph using the data from expanded_data.py
G = create_graph()

@app.route('/')
def index():
    # Pass the list of cities from the graph to the HTML template
    cities = list(G.nodes)
    return render_template('index.html', cities=cities)

@app.route('/optimize', methods=['POST'])
def optimize():
    source = request.form['source']
    destination = request.form['destination']

    paths_data = []  # List to store paths and their fuel consumption

    # Get all paths from source to destination
    try:
        all_paths = list(nx.all_simple_paths(G, source, destination))

        for path in all_paths:
            total_distance = nx.path_weight(G, path, weight='weight')  # Calculate the distance
            fuel_consumed = total_distance / 20  # Fuel consumption, assuming 20 km/liter
            paths_data.append((path, total_distance, round(fuel_consumed, 2)))  # Append path and fuel info

        # Sort the paths by fuel consumption (or total distance)
        paths_data.sort(key=lambda x: x[1])

        # Separate the optimal path (lowest fuel consumption)
        optimal_path = paths_data[0]
        other_paths = paths_data[1:] if len(paths_data) > 1 else None

        return render_template('result.html', optimal_path=optimal_path, other_paths=other_paths)
    except nx.NetworkXNoPath:
        error_message = f"No path found from {source} to {destination}."
        return render_template('index.html', error=error_message, cities=list(G.nodes))

@app.route('/visualize')
def visualize():
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True)
    labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
    
    plt.title("City Connectivity Graph")
    plt.savefig('static/exp_graph.png')  # Save the graph as an image in static folder
    plt.close()  # Close the plot
    
    return render_template('visualize.html')

if __name__ == '__main__':
    app.run(debug=True)
