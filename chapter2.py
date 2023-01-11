# Chapter 2

# Evaluating Expressions
# EXPRESSION = a combination of values, operators, and calls to functions

1 + 1

print(len("how many characters are in this string?")) #including spaces
print(len("hello"))
print(len("hello 123")) 

#quotes
print('this is a string')
print('''this is a string''')
print("this is a string")
print('''"Oh No!", she exclaimed! "I'm worried I'll need to escape my quotation marks!"''')

# OPPERANDS
print(2 ** 2) # prints 4
print(2 + 3 + 6 - 11) # prints 0
print(0 * 100) #prints 0

# let's convert 645 minutes into hours
minutes = 645
hours = minutes / 60

print(f'645 minutes is equal to {hours} hours') #prints 10.75

# in python, the division operator always yeilds a floating point result
# if we want a whole number result, we use // called FLOOR DIVISION
# if it has to adjust the number, it always moves it to the left on the number line

print(7 / 4) #prints 1.75
print(7 // 4) #prints 1

#CONVERTER FUNCTIONS
# The INT function takes a float or a string and turns it into an int. For floats, it
# discards the number after the decimal (trunctation towards zero)

myNumber = 2

print(int(6.2)) #prints 6
print(int("1234")) #prints 1234
print(int(6.9999)) #prints 6
print(int(6)) #prints 6
print(int(6 / myNumber)) #prints 3

# TYPE CONVERTOR FLOAT - turns an interger or syntatctically legal str into float
print(float(100)) #prints 100.0
print(float("666")) #prints 666.0

# TYPE CONVERTER STR TURNS ITS ARGUMENT INTO A STRING
print(str(17)) #prints "17"
print(str(17.77)) #prints "17.77"

# INPUT
n = input("Please enter your name: ")
print(n)

response = input("What is your radius? ")
r = float(response)
area = 3.14159 * r**2
print(
    "The area is ", area
)

# let's do this same thing but in two lines of code
r = float(input("What is the radius?"))
print("The area is ", 3.14159 * r**2)

# now let's do all of this in one line
print("The area is ", 3.14159*float(input("What is your radius now?"))**2)

# MODULUS
# gives the remainder when the first number has been divided by the second