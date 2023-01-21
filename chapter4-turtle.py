import turtle
wn = turtle.Screen()
wn.bgcolor("red")
moose = turtle.Turtle()
moose.color("black")
moose.shape("turtle")
moose.speed(5) # 1 is slowest, 10is fastest, 0 = turn off animation and go as fast as possible
moose.pensize(3)

# print(list(range(5, 60, 2)))
moose.up()

for size in range(5, 60, 2):
    moose.stamp()
    moose.forward(size)
    moose.right(24)

# Moose draws a small square

# for i in ["one", "two", "three", "four"] :
#     moose.forward(75)
#     moose.left(90)

# for i in [0, 1, 2, 3] :
#     moose.forward(75)
#     moose.left(90)

# Moose draws a big triangle
# for i in [0, 1, 2] :
#     moose.forward(100)
#     moose.left(120)

# Moose draws a perfect circle
# for i in range(1, 360, 1):     
#     moose.forward(1)
#     moose.left(1)

# Moose draws a penatgram
# for i in [0, 1, 2, 3, 4, 5] :
#     moose.forward(100)
#     moose.left(500)


wn.exitonclick()

# print(list(range(0, 19, 2)))
# print(list(range(0, 20, 2)))
# print(list(range(10, 0, -1)))

# print(list(range(5, 55, 5)))
      
 #prints out values in 5 - 55 in increments of       
for i in range(5, 55, 5):
      print(i)

start = 0
lastPlusOne = 11
step = 1

for i in range(start, lastPlusOne, step):
    print(":", i)

#alex.backward(-100) to move alex forward!)
for i in ["arrow", "blank", "circle", "classic", "square", "triangle", "turtle"] :
    print('Your turtle can be shaped like a', i )

moose.shape("turtle")
moose.speed(5) # 1 is slowest, 10is fastest, 0 = turn off animation and go as fast as possible