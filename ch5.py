import math
pi = 3.14159265359
d = float(input("First, we need to know the diamter of the circle to find it's circumfrence. What is the diameter:"))
c = pi * d
print(f"Great! This circle's circumfrence is: {c}")

myPi = c/d

print(f"One way to approximate pi is to divide the circumfrence of a circle by it's diamter.\n",
      f"Using your input values {c} for circumfrence and {d} for diamter,\n",
      f"pi has been approximated to the value {myPi}")

# From Documentation:
print(math.pi)

# print 10 random numbers
import random

for i in range(10):
    print("Random Number is:", random.randrange(1, 100), "\n")
    
for i in range(10):
    print("Random Number is:", round(random.random(), 2), "\n")
    
for num in ["first", "second", "third", "fourth", "fifth", "sixth", "seventh",
           "eigth", "ninth", "tenth"]:
    print(f'The {num} random number is:', random.randrange(1, 11))

# Repeat the above exercise but this time print 10 random numbers between 25 and 35, inclusive.
import random

for i in range(10):
    print(random.randrange(25, 36), "\n")

###The Pythagorean Theorem tells us that the length of the hypotenuse of a right triangle 
#is related to the lengths of the other two sides. Look through the math module and see if you 
#can find a function that will compute this relationship for you. Once you find it, write a short program 
#to try it out.
import math
"""
c**2 = a**2 + b**2
"""

a = int(input("What is the length of side a:"))
b = int(input("What is the length of side b:"))
c = math.sqrt(a**2 + b**2)

print("The hypotenuse of this triangle is", c)

# from documentation :
print("The hypotenuse of this triangle is", math.hypot(a, b))

valToRound = math.hypot(a, b)
print("The hypotenuse of this triangle is", round(math.hypot(a, b), 2))
print("The hypotenuse of this triangle is", math.floor(valToRound))
print("The hypotenuse of this triangle is", math.ceil(valToRound))


# functions
import turtle

def drawSquare(t, sz):
    """Make turtle t draw a square of with side sz."""

    for i in range(4):
        t.forward(sz)
        t.left(90)
  
def drawPolygon(t, l, numSides):
    '''Makes a turtle draw a polygon'''
    for i in range(numSides):
        t.forward(l)
        t.left(360/numSides)