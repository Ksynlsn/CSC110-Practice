# CSC 110 Week 5 Assignment
import turtle
wn = turtle.Screen()
tri = turtle.Turtle()
poly = turtle.Turtle()
hexa = turtle.Turtle()
s = turtle.Turtle()

def drawPolygon(t, s, l):
    for i in range(s):
        t.forward(l)
        t.left(360 / s)

# Tri draws a triangle
tri.up()
tri.goto(-300, 75)
tri.down()
drawPolygon(tri, 3, 200)

# Poly draws a pentagon
poly.up()
poly.goto(-275, -250)
poly.down()
drawPolygon(poly, 5, 150)

# S draws a square
s.up()
s.goto(50, 75)
s.down()
drawPolygon(s, 4, 150)

# Hexa draws a hexagon
hexa.up()
hexa.goto(75, -250)
hexa.down()
drawPolygon(hexa, 6, 125)















turtle.Screen().exitonclick()