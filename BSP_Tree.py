# Koch Triangle generation using a recursive approach (conceptual BSP tree)

import turtle  # Import the turtle graphics module

# Define the recursive Koch function
def koch(t, order, size):
    """
    Draws a Koch curve using recursion.
    t: turtle object
    order: recursion depth
    size: length of line segment
    """
    if order == 0:
        t.forward(size)  # Base case: draw a straight line
    else:
        # The Koch curve splits each line into 4 segments with 3 angles: 60°, -120°, and 60°
        for angle in [60, -120, 60, 0]:  # Angles to create the snowflake pattern
            koch(t, order - 1, size / 3)  # Recursive call with reduced size
            t.left(angle)  # Turn the turtle by the current angle

# Setup the drawing environment
screen = turtle.Screen()  # Create a screen object
t = turtle.Turtle()       # Create a turtle object
t.speed(0)                # Set turtle speed to fastest
t.penup()                 # Lift the pen to move without drawing
t.goto(-150, 90)          # Move turtle to a starting position
t.pendown()               # Put the pen down to start drawing

# Draw the full Koch snowflake (3 sides of an equilateral triangle)
for _ in range(3):              # Repeat 3 times for 3 sides of the triangle
    koch(t, 3, 300)             # Draw one side of the snowflake with recursion depth 3
    t.right(120)               # Turn right to start next side

turtle.done()  # Keep the turtle window open until closed manually
