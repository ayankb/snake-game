from turtle import Turtle


class Line:
    def __init__(self):
        for x in range(-300, 300):
            t = Turtle("square")
            t.penup()
            t.color("white")
            # t.speed(0)
            t.shapesize(.1)
            t.goto(x, 270)
