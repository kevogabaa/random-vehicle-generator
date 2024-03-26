# Vehicle and Flower Simulation

This project is a Python-based simulation that generates a graphical representation of vehicles and flowers. The simulation uses the `tkinter` library for the graphical user interface, and the `random` and `math` libraries for generating random attributes for the vehicles and flowers.

## Features

- The simulation generates three types of vehicles: 'suv', 'sedan', and 'truck'. Each vehicle is randomly assigned a size and color, and is positioned in the top half of the screen.
- The simulation also generates flowers with random colors and positions. The flowers are positioned in the bottom half of the screen.
- The simulation ensures that all three types of vehicles are generated before any type is repeated.
- The simulation can be rerun by clicking the "Simulate" button.

## Code Structure

The code is structured into several functions:

- `random_color()`: Generates a random color.
- `draw_vehicles()`: Draws the vehicles on the screen.
- `draw_flowers()`: Draws the flowers on the screen.
- `simulate()`: Runs the simulation by calling `draw_vehicles()` and `draw_flowers()`.

The main part of the code creates a `tkinter` window, sets up the canvas for drawing, and creates a "Simulate" button that reruns the simulation when clicked.

## Running the Simulation

To run the simulation, simply execute the `main.py` file. This will open a new window displaying the simulation. Click the "Simulate" button to rerun the simulation.

## Requirements

- Python 3
- tkinter library
- random library
- math library

## Future Improvements

- Add more types of vehicles and flowers.
- Allow the user to customize the number and types of vehicles and flowers.
- Improve the graphical representation of the vehicles and flowers.