# Koch Triangle generation using a recursive approach (conceptual BSP tree)

import turtle

def koch(t, order, size):
    if order == 0:
        t.forward(size)
    else:
        for angle in [60, -120, 60, 0]:
            koch(t, order - 1, size / 3)
            t.left(angle)

# Setup turtle graphics
screen = turtle.Screen()
t = turtle.Turtle()
t.speed(0)
t.penup()
t.goto(-150, 90)
t.pendown()

# Draw Koch snowflake
for _ in range(3):
    koch(t, 3, 300)  # 3rd order Koch triangle
    t.right(120)

turtle.done()