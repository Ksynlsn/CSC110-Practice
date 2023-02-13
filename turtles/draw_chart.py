import turtle
xs = [48, 117, 200, 240, 160, 260, 220]
z = turtle.Turtle()  
boo = turtle.Turtle()

def drawChart(t, xs):
    t.up()
    t.goto(-150,-150)
    t.down()
    t.right(90)
    for i in range(len(xs)):
        t.left(180)
        t.forward(xs[i])
        t.write(str(xs[i]))
        t.right(90)
        t.forward(40)
        t.right(90)
        t.forward(xs[i])
#-----------------------------------------#
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
    #drawPrettyPattern(boo, 150) 
    drawChart(boo, xs)
       
main()