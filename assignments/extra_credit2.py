# Kacie Nielsen - CSC 110 - Extra credit assignment #2 
# using the main() function
import turtle

def drawPolygon(t, numSides):
    for i in range(numSides):
        t.left(360/numSides)
        t.forward(600/numSides) # value keeps shape within window
                       
def main():
    chooseSides = int(input("How many sides?"))
    boo = turtle.Turtle()
    wn = turtle.Screen()
    drawPolygon(boo, chooseSides)
    
main()
