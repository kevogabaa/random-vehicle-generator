import tkinter as tk
import random
from math import cos, sin


# Function to generate random color
def random_color():
    return "#{:06x}".format(random.randint(0, 0xFFFFFF))


# Function to draw vehicles
def draw_vehicles():
    canvas.delete("vehicle")  # Clear previous vehicles

    # Define positions for each vehicle
    num_vehicles = 3
    vehicle_width = 300  # Maximum vehicle size
    spacing = (screen_width - (num_vehicles * vehicle_width)) // (num_vehicles + 1)

    positions = [(spacing + i * (vehicle_width + spacing), screen_height // 4) for i in range(num_vehicles)]

    vehicle_types = ('suv', 'sedan', 'truck')
    generated_types = []

    for index, pos in enumerate(positions):
        x, _ = pos
        size = random.randint(200, 500)  # Random size for each vehicle
        # Ensure all vehicle types are present
        if not generated_types or len(generated_types) == len(vehicle_types):
            generated_types = []  # Reset the list if it's empty or all types have been generated
            vehicle_type = random.choice(vehicle_types)
        else:
            available_types = [vt for vt in vehicle_types if vt not in generated_types]
            vehicle_type = random.choice(available_types)

        generated_types.append(vehicle_type)  # Add the selected type to the list of generated types

        vehicle_width = size  # Adjust the vehicle width to match the size of other vehicles
        height = size * 0.6  # Adjust the screen height to match the size of other vehicles
        body_color = random_color()

        y = screen_height // 2 - height  # Adjust the y position to match the size of other vehicles and in the top half

        if vehicle_type == 'suv':
            body_points = [x, y + height * 0.6,  # Bottom left
                           x + vehicle_width * 0.5, y + height * 0.6,  # Start of hood (longer and flatter than SUV)
                           x + vehicle_width * 0.5, y + height * 0.2,  # Start of windscreen
                           x + vehicle_width * 0.6, y + height * 0.2,  # End of windscreen
                           x + vehicle_width, y + height * 0.6,  # Bottom right (flat back)
                           x + vehicle_width, y + height,  # Bottom right
                           x, y + height]  # Bottom left
        elif vehicle_type == 'sedan':
            body_points = [x, y + height * 0.6,  # Bottom left
                           x + vehicle_width * 0.2, y + height * 0.4,  # Start of hood
                           x + vehicle_width * 0.4, y + height * 0.2,  # Start of windscreen
                           x + vehicle_width * 0.6, y + height * 0.2,  # End of windscreen
                           x + vehicle_width, y + height * 0.6,  # Bottom right (flat back)
                           x + vehicle_width, y + height,  # Bottom right
                           x, y + height]  # Bottom left
        elif vehicle_type == 'truck':
            body_points = [x, y + height,  # Bottom left
                           x, y + height * 0.6,  # Start of front
                           x + vehicle_width * 0.2, y + height * 0.6,  # End of front
                           x + vehicle_width * 0.2, y + height * 0.2,  # Start of cargo area
                           x + vehicle_width, y + height * 0.2,  # End of cargo area
                           x + vehicle_width, y + height,  # Bottom right
                           x, y + height]  # Bottom left
        else:
            body_points = [x, y + height,  # Bottom left
                           x + vehicle_width, y + height,  # Bottom right
                           x + vehicle_width, y,  # Top right
                           x, y]

        canvas.create_polygon(body_points, fill=body_color, outline="black", width=2, tags="vehicle")

        wheel_radius = height * 0.1
        wheel_distance = vehicle_width * 0.2
        canvas.create_oval(x + wheel_distance - wheel_radius, y + height - wheel_radius,
                           x + wheel_distance + wheel_radius,
                           y + height + wheel_radius, fill="black", tags="vehicle")
        canvas.create_oval(x + vehicle_width - wheel_distance - wheel_radius, y + height - wheel_radius,
                           x + vehicle_width - wheel_distance + wheel_radius,
                           y + height + wheel_radius, fill="black", tags="vehicle")


# Function to draw flowers
def draw_flowers():
    canvas.delete("flower")  # Clear previous flowers

    # Define positions for each flower
    num_flowers = 5
    flower_width = 200  # Maximum flower size
    spacing = (screen_width - (num_flowers * flower_width)) // (num_flowers + 1)

    positions = [(spacing + i * (flower_width + spacing), 3 * screen_height // 4) for i in range(num_flowers)]

    # Draw flowers
    for pos in positions:
        x, y = pos
        center_color = random_color()
        canvas.create_oval(
            x - flower_width // 8, y - flower_width // 8,
            x + flower_width // 8, y + flower_width // 8,
            fill=center_color, outline=""
        )

        # Draw petals
        for i in range(0, 360, 30):
            petal_color = random_color()
            angle_radians = i * (3.14159 / 180)
            petal_x1 = x + flower_width * 0.5 * cos(angle_radians)
            petal_y1 = y + flower_width * 0.5 * sin(angle_radians)
            petal_x2 = x + flower_width * 0.5 * cos(angle_radians + 0.523)
            petal_y2 = y + flower_width * 0.5 * sin(angle_radians + 0.523)
            petal_x3 = x + flower_width * 0.5 * cos(angle_radians + 1.047)
            petal_y3 = y + flower_width * 0.5 * sin(angle_radians + 1.047)
            canvas.create_polygon(petal_x1, petal_y1, petal_x2, petal_y2, petal_x3, petal_y3, fill=petal_color,
                                  outline="")


# Function to simulate
def simulate():
    draw_vehicles()
    draw_flowers()


# Create tkinter window
root = tk.Tk()
root.title("Vehicle and Flower Simulation")

# Get screen width and height
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Create canvas
canvas = tk.Canvas(root, width=screen_width, height=screen_height, bg="white")
canvas.pack(fill=tk.BOTH, expand=True)

# Initial simulation
simulate()

# Create simulate button
simulate_button = tk.Button(root, text="Simulate", command=simulate)
simulate_button.place(relx=0.5, rely=1.0, anchor=tk.S)

# Run tkinter event loop
root.mainloop()
