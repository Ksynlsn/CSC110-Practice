import turtle
xs = [48, 117, 200, 240, 160, 260, 220]

def writeString(t, xs, i):
        t.up()
        t.left(90)
       
        t.write(str(xs[i]))
    
        t.right(90)
        t.down()
        
def drawChart(t, xs):
    t.up()
    t.goto(-150,-150)
    t.down()
    t.right(90)
    
    for i in range(len(xs)):
        t.left(180)
        t.begin_fill()
        if ((xs[i]) >= 200):
            t.fillcolor('red')
        elif (xs[i] >= 100 and xs[i] < 200):
            t.fillcolor('yellow')
        else:
            t.fillcolor('green')
        t.forward(xs[i])
        t.right(90)
        t.forward(20)
        writeString(t, xs, i)
        t.forward(20)
        t.right(90)
        t.forward(xs[i])
        t.end_fill()
     

def main():
    wn = turtle.Screen()
    boo = turtle.Turtle()
    boo.speed(2)
    drawChart(boo, xs)


main()
