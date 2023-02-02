import turtle
wn = turtle.Screen()
t = turtle.Turtle()

t.up()
t.goto(-150, -150)
t.down()

def drawMaze(t, size):
    for i in range(0, 24, 1):
        t.forward(size)
        t.left(90)
        size = size + 7

drawMaze(t, 7)

turtle.Screen().exitonclick()