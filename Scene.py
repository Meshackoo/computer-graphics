# Scene Graph for a Bicycle using Python

# Define a class to represent each node in the scene graph
class SceneNode:
    def __init__(self, name):
        self.name = name          # Name of the scene node (e.g., "Frame", "Seat", etc.)
        self.children = []        # List to store child nodes (subcomponents)

    def add_child(self, child):
        self.children.append(child)  # Add a child node to the current node

    def display(self, level=0):
        # Print the node name with indentation based on the depth level
        print('  ' * level + self.name)
        # Recursively display all children of the current node
        for child in self.children:
            child.display(level + 1)

# ----------------------------
# Building the scene graph
# ----------------------------

# Root node representing the entire bicycle
bicycle = SceneNode("Bicycle")

# Create the frame and its components
frame = SceneNode("Frame")
seat = SceneNode("Seat")             # Seat is a child of Frame
pedals = SceneNode("Pedals")         # Pedals are a child of Frame
chain = SceneNode("Chain")           # Chain is a child of Frame

# Attach the components to the frame node
frame.add_child(seat)
frame.add_child(pedals)
frame.add_child(chain)

# Create the front wheel and its subcomponent (spokes)
front_wheel = SceneNode("Front Wheel")
front_spokes = SceneNode("Spokes")
front_wheel.add_child(front_spokes)  # Spokes are a child of the front wheel

# Create the rear wheel and its spokes
rear_wheel = SceneNode("Rear Wheel")
rear_spokes = SceneNode("Spokes")
rear_wheel.add_child(rear_spokes)    # Spokes are a child of the rear wheel

# Create handlebar and its components
handlebar = SceneNode("Handlebar")
left_grip = SceneNode("Left Grip")       # Left grip on the handlebar
right_grip = SceneNode("Right Grip")     # Right grip on the handlebar
brake_levers = SceneNode("Brake Levers") # Brake levers on the handlebar

# Attach the components to the handlebar
handlebar.add_child(left_grip)
handlebar.add_child(right_grip)
handlebar.add_child(brake_levers)

# Attach main components to the bicycle root node
bicycle.add_child(frame)
bicycle.add_child(front_wheel)
bicycle.add_child(rear_wheel)
bicycle.add_child(handlebar)

# ----------------------------
# Output the scene graph
# ----------------------------

bicycle.display()  # Start displaying from the root ("Bicycle"), showing hierarchy
