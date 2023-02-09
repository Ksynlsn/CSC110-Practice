# CSC 110 Week 5 Assignment
import turtle
wn = turtle.Screen()
wn.setup(800,500)
t = turtle.Turtle()

def drawMaze(t, length):
    for i in range(0, 24, 1):
        t.forward(length)
        t.left(90)
        length = length + 7

drawMaze(t, 7)

turtle.Screen().exitonclick()