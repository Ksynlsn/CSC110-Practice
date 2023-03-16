import turtle
import math
import random

z = turtle.Turtle()

wn = turtle.Screen()
wn.setworldcoordinates(-1,-1,1,1)
wn.tracer(100)

z.up()

numdarts = 5000 #10,000,00 iterations to approx pi
insideCount = 0
for i in range(numdarts):
    randx = random.random()
    randy = random.random()
    x = randx*2-1
    y = randy*2-1
    z.goto(x, y)
    count = z.distance(0, 0)
    if count <= 1:
        insideCount += count
        z.color('red')
        z.stamp()
    else:
        z.color('blue')
        z.stamp()
print(insideCount)
print((insideCount / numdarts) * 4)

wn.exitonclick()
