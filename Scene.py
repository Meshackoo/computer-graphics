# Scene Graph for a Bicycle using Python

class SceneNode:
    def __init__(self, name):
        self.name = name
        self.children = []

    def add_child(self, child):
        self.children.append(child)

    def display(self, level=0):
        print('  ' * level + self.name)
        for child in self.children:
            child.display(level + 1)

# Building the scene graph
bicycle = SceneNode("Bicycle")

frame = SceneNode("Frame")
seat = SceneNode("Seat")
pedals = SceneNode("Pedals")
chain = SceneNode("Chain")
frame.add_child(seat)
frame.add_child(pedals)
frame.add_child(chain)

front_wheel = SceneNode("Front Wheel")
front_spokes = SceneNode("Spokes")
front_wheel.add_child(front_spokes)

rear_wheel = SceneNode("Rear Wheel")
rear_spokes = SceneNode("Spokes")
rear_wheel.add_child(rear_spokes)

handlebar = SceneNode("Handlebar")
left_grip = SceneNode("Left Grip")
right_grip = SceneNode("Right Grip")
brake_levers = SceneNode("Brake Levers")
handlebar.add_child(left_grip)
handlebar.add_child(right_grip)
handlebar.add_child(brake_levers)

bicycle.add_child(frame)
bicycle.add_child(front_wheel)
bicycle.add_child(rear_wheel)
bicycle.add_child(handlebar)

# Output the scene graph
bicycle.display()