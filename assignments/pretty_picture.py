import turtle
wn = turtle.Screen()

def drawSquare(t, sz):
    sz = 100
    for i in range(4):
        t.forward(sz)
        t.left(90)
        
def draw4Squares(t, sz):
    for i in range(2):
        drawSquare(t, sz)
        t.left(180)
        drawSquare(t, sz)
        t.right(90)
        #drawSquare(t, sz)
        #t.left(180)
        #drawSquare(t, sz)
        #t.right(180)
    
def drawPrettyPattern(t, sz):
    for i in range(10):
        draw4Squares(t, sz)
        t.left(90//10)
        
# def main():
#     wn = turtle.Screen()
#     boo = turtle.Turtle()
#     wn.exitonclick()
#     drawPrettyPattern(boo, 150)
#     #draw4Squares(boo, 150)
    
# main()
#wn = turtle.Screen()
boo = turtle.Turtle()
wn.exitonclick()
drawPrettyPattern(boo, 150)    