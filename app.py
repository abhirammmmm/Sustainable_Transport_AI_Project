from flask import Flask, render_template, request
import networkx as nx
from Data.init_data import create_graph
import matplotlib.pyplot as plt

app = Flask(__name__)

# Create the graph using the data from init_data.py
G = create_graph()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/optimize', methods=['POST'])
def optimize():
    source = request.form['source']
    destination = request.form['destination']

    # Calculate the path and fuel consumption
    try:
        path = nx.astar_path(G, source, destination, weight='weight')
        total_fuel = nx.path_weight(G, path, weight='weight')
        return render_template('result.html', path=path, total_fuel=total_fuel)
    except nx.NetworkXNoPath:
        return render_template('index.html', error="No path found from {} to {}.".format(source, destination))

@app.route('/visualize')
def visualize():
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True)
    labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
    plt.title("City Connectivity Graph")
    plt.savefig('static/graph.png')  # Save the graph to static folder
    plt.close()  # Close the plot to prevent displaying it immediately
    return render_template('visualize.html')

if __name__ == '__main__':
    app.run(debug=True)
