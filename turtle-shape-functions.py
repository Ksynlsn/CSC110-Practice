import turtle
wn = turtle.Screen()

timmy = turtle.Turtle()
lou = turtle.Turtle()
lou.color('pink')
bob = turtle.Turtle()
bob.color('green')

def drawSquare(t, sz):
    """Make turtle t draw a square of sz."""

    for i in range(4):
        t.forward(sz)
        t.left(90)

drawSquare(timmy, 20)   

def drawTriangle(t, sl):
    """Make a turtle (t) draw a triangle with side of length sl"""
    
    for i in range(3):
        t.forward(sl)
        t.left(120)
        
drawTriangle(lou, 75)

def drawOctogon(t, l):
    """Make a turtle (t) draw an octogon with side of length sl"""

    for i in range(8):
        bob.forward(l)
        bob.left(360/8)
        
drawOctogon(bob, 100)

def drawHexagon(t, l):
    """Make a turtle (t) draw a hexagon with side of length sl"""
    
    for i in range(6):
        bob.forward(l)
        bob.left(360/6)
        
drawHexagon(bob, 100)