import random
import math
num1 = 3.14
num2 = 12
number = "four"
number2 = "100"

print(type(num1))
print(type(num2))
print(type(number))

print(int(14.999))
print(int(number2))

print(7/5*4%3)

print("Using random.random():", random.random())

print("Using random.randrange():", float(random.randrange(1, 10)))

print("Using random.randit():", random.randint(50, 56))

print(math.pow(3, 3))

# myStr = "moose"
# print(len(myStr))
# print(myStr[1])
# print(myStr[4])

def getOhs(string):
    numberOfOhs = []
    for x in len(string):
        if x == 'o':
            numberOfOhs.append(x)
        elif x != 'o':
            print(f"Sorry there are no 'o's in {string}")
    return numberOfOhs

    print(getOhs(moose))

string_name = input("What word should we test:")

# Iterate over the string
for element in string_name:
    print(element, end=' - ')
print("\n")
 
 
string_name2 = input("What should the second word be:)")

# Iterate over index
for element in range(0, len(string_name2)):
    print(string_name2[element])    


string_name3 = input("What should the third word be:")
for i, v in enumerate(string_name3):
    print(v)

string_name4 = input("What should the fourth word be:")
# slicing the string in reverse fashion
for element in string_name4[ : :-1]:
    print(element, end =' ')
print('\n')

# Getting length of string
string_name5 = input("What should the fifth word be:")
ran = len(string_name5)
 
# using reversed() function
for element in reversed(range(0, ran)):
    print(string_name5[element])
