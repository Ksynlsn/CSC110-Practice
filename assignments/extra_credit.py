# Kacie Nielsen - CSC110 - Extra Credit Assignment 2/8
import turtle

def drawPolygon(t, numSides):
    for i in range(numSides):
        t.left(360/numSides)
        t.forward(600/numSides)
                       
def main():
    boo = turtle.Turtle()
    wn = turtle.Screen()
    numSides = int(input("How many sides?"))
    drawPolygon(boo, numSides)
    
main()