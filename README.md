# Sustainable_Transport_AI_Project
Developing an AI-powered web app for optimizing vehicle routes using Python and Flask, to reduce carbon emissions.


## Overview

This project is an AI-powered web application designed to optimize vehicle routes, thereby reducing carbon emissions. The application uses Python and Flask to provide a user-friendly interface for selecting source and destination cities. It calculates the optimal route based on fuel consumption and displays the results to the user.

I have used A* path finding algorithm for this project. The project uses data collected and prepared by me as there are no standard city and distances graph data available online. The project asks users to inout the source city and the destination city using drop downs and once clicked on submit, the A* algorithm finds the best fuel efficient path and other paths shown in increasingorder of fuel consumption, thereby effecting the carbon foot print and leading to sustainability.

## Project Structure

```
Project Structure of: Sustainable_Transport_AI_Project

|-- app.py
|-- Data
    |-- expanded_data.py
    |-- init_data.py
    |-- __pycache__
        |-- expanded_data.cpython-311.pyc
        |-- init_data.cpython-311.pyc
        |-- init_data.cpython-312.pyc
|-- generate_requirements.py
|-- print_structure.py
|-- README.md
|-- requirements.txt
|-- static
    |-- exp_graph.png
    |-- graph.png
    |-- style.css
|-- templates
    |-- index.html
    |-- result.html
    |-- visualize.html
```

## Installation Instructions

1. **Download the project**:
    - You can either clone the repository using Git:
      ```bash
      gh repo clone abhirammmmm/Sustainable_Transport_AI_Project
      ```
    - Or download the project as a ZIP file from GitHub and unzip it.

2. **Install the required packages**:
    - Navigate to the project directory in your terminal.
    - Run the following command to install the dependencies:
      ```bash
      pip install -r requirements.txt
      ```

3. **Run the application**:
    - Start the Flask application by running:
      ```bash
      python app.py
      ```
    - Open your web browser and go to `http://127.0.0.1:5000` to access the application.

## Features

- **Route Optimization**: Select source and destination cities to find the optimal route based on fuel consumption.
- **Visual Representation**: Visualize the connectivity graph of cities used in the project.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Collaboration

Im free to collaborate in expanding the project to use better AI path finding algorithm possibly Genetic Algorithms, etc; Expand the data to be closer to real world swedish city data, or even to make a complex correlated data using other parameters like finding an average vehicle consumption, etc.

## Acknowledgements

- [Flask](https://flask.palletsprojects.com/) - For the web framework.
- [NetworkX](https://networkx.org/) - For graph manipulation.
- [Matplotlib](https://matplotlib.org/) - For graph visualization.
