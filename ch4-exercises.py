numSides = int(input("How many sides should there be?:"))
sideLength = int(input("How long should each side be?:"))
fillcolor = input("What color should this polygon be?")

import turtle
userTurtle = turtle.Turtle()
userTurtle.fillcolor(fillcolor)

userTurtle.begin_fill()
for num in range(numSides):
    userTurtle.forward(sideLength)
    userTurtle.left(360/numSides)
    
userTurtle.end_fill()

import turtle
blue = turtle.Turtle()
blue.shape("arrow")
blue.color("green")

# An equilateral triangle
for side in ['one', 'two', 'three']:
    blue.forward(150)
    blue.left(120)

# A square
blue.penup()
blue.backward(125)
blue.down()
for num in range(4):
    blue.forward(200)
    blue.left(90)

blue.penup()
blue.right(90)
blue.forward(125)
blue.down()
# An octogon
blue.color('purple')
for i in range(8):
    blue.backward(100)
    blue.right(45)
    
# A hexagon
blue.color('pink')
blue.left(90)
blue.penup()
blue.forward(65)
blue.down()
for i in range(6):
    blue.forward(100)
    blue.left(360/6)

# turtle.setworldcoordinates(llx, lly, urx, ury)
# Parameters
# llx  a number, x-coordinate of lower left corner of canvas

# lly  a number, y-coordinate of lower left corner of canvas

# urx  a number, x-coordinate of upper right corner of canvas

# ury  a number, y-coordinate of upper right corner of canvas