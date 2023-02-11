import turtle

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
    
def drawPrettyPattern(t, sz):
    for i in range(5):
        draw4Squares(t, sz)
        t.left(90//5)
                
def main():
    wn = turtle.Screen()
    boo = turtle.Turtle()
    drawPrettyPattern(boo, 150) 
       
main()