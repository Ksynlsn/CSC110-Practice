# Kacie Nielsen - CSC 110 - Week 6 Homework - Draw 'Pretty Pattern'
import turtle

# drawSquare function
def drawSquare(t, sz):
    for i in range(4):
        t.forward(sz)
        t.left(90)

# draw4Squares calls drawSquare function      
def draw4Squares(t, sz):
    for i in range(2):
        drawSquare(t, sz)
        t.left(180)
        drawSquare(t, sz)
        t.right(90)

# drawPrettyPattern calls draw4Squares function
def drawPrettyPattern(t, sz):
    for i in range(5):
        draw4Squares(t, sz)
        t.left(90//5) # turns left 90 degrees divided by number of squares
                                    # required to complete pattern 
                
def main():
    wn = turtle.Screen()
    boo = turtle.Turtle()
    drawPrettyPattern(boo, 150) 
       
main()