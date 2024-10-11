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

    # Calculate the shortest path and fuel consumption
    try:
        path = nx.astar_path(G, source, destination, weight='weight')
        total_fuel = nx.path_weight(G, path, weight='weight')
        return render_template('result.html', path=path, total_fuel=total_fuel)
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
