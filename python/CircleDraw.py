# draw a circle

# cmd: python3 CircleDeaw.py

import turtle
ninja = turtle.Turtle()
ninja.speed(25)

for i in range(180):
    ninja.forward(100)
    ninja.right(45)
    ninja.forward(15)
    ninja.left(70)
    ninja.forward(50)
    ninja.right(30)

    ninja.penup()
    ninja.setposition(0, 0)
    ninja.pendown()

    ninja.right(2)

turtle.done()
