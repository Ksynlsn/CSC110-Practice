import turtle
wn = turtle.Screen()
wn.bgcolor('black')
tri = turtle.Turtle()
tri.color('yellow')
poly = turtle.Turtle()
poly.color('pink')
hexa = turtle.Turtle()
hexa.color('red')
s = turtle.Turtle()
s.color('green')

def drawPolygon(t, s):
    for i in range(s):
        t.forward(100)
        t.left(360 / s)
# Tri draws a triangle
tri.up()
tri.goto(-200, 200)
tri.down()
tri.fillcolor('yellow')
tri.begin_fill()
drawPolygon(tri, 3)
tri.end_fill()

# Poly draws a polygon
poly.up()
poly.goto(-200, -200)
poly.down()
poly.fillcolor('pink')
poly.begin_fill()
drawPolygon(poly, 5)
poly.end_fill()

# S draws a square
s.up()
s.goto(200, 200)
s.down()
s.fillcolor('green')
s.begin_fill()
drawPolygon(s, 4)
s.end_fill()

# Hexa draws a hexagon
hexa.up()
hexa.goto(200, -200)
hexa.down()
hexa.fillcolor('red')
hexa.begin_fill()
drawPolygon(hexa, 6)
hexa.end_fill()














turtle.Screen().exitonclick()