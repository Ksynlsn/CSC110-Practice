#Many people keep time using a 24 hour clock (11 is 11am and 23 is 11pm, 0 is midnight). 
#If it is currently 13 and you set your alarm to go off in 50 hours, it will be 15 (3pm).
#Write a Python program to solve the general version of the above problem. 
#Ask the user for the time now (in hours), and then ask for the number of hours 
#to wait for the alarm. Your program should output what the time will be on the clock 
#when the alarm goes off.


# It is possible to name the days 0 through 6 where day 0 is Sunday and day 6 is Saturday. 
# If you go on a wonderful holiday leaving on day number 3 (a Wednesday) and you return home 
# after 10 nights you would return home on a Saturday (day 6) Write a general version of 
# the program which asks for the starting day number, and the length of your stay, 
# and it will tell you the number of day of the week you will return on.

day0 = "Sunday"
day1 = "Monday"
day2 = "Tuesday"
day3 = "Wednesday"
day4 = "Thursday"
day5 = "Friday"
day6 = "Saturday"

leaveOn = int(input("What day are you leaving?"))
lengthOf = int(input("How long are you staying"))
uhOh = input("Are you flying Southwest? ( Y or N)")

if uhOh == "Y":
    totalDays = leaveOn + lengthOf + 5
else: totalDays = leaveOn + lengthOf
print(totalDays % 7)


# Write a Python program that assigns the principal amount of 10000 to variable P, 
# assign to n the value 12, and assign to r the interest rate of 8% (0.08). 
# Then have the program prompt the user for the number of years, t, that the money will be compounded for. 
# Calculate and print the final amount after t years.
# A = P(1+r/n)**nt

P = 10000 # principle
n = 12 # how mnay times per year interest is compounded
r = 0.08 # 8% interest rate


# Write a program that will compute the area of a circle. Prompt the user to enter the radius 
# and print a nice message back to the user with the answer.

# pi = 3.14159
r = float(input("What is the radius of our circle?"))
print(f"The area of a circle with a radius of {r} is", pi * r**2)

# Write a program that will compute the area of a rectangle. Prompt the user to enter the width and height of the rectangle. 
# Print a nice message with the answer.
l = float(input("What is the length of the rectangle?"))
w = float(input("What is the width of the rectangle?"))
u = input("What unit of measurement are these in?")
print("The area of this rectangle is", l * w, u, "squared")

# Write a program that will compute MPG for a car. Prompt the user to enter the number of miles driven and the number of gallons used.
#  Print a nice message with the answer.
miles = int(input("Please enter the ammount of miles driven:"))
gallons = int(input("How many gallons of gas did you use?"))
MPG = miles / gallons
print("Your miles per gallon on this trip were", round(MPG, 2))

# Write a program that will convert degrees celsius to degrees fahrenheit. and vise versa
temp = int(input("What is the tempature in fahrenheit?"))
temp_to_celsius = (temp - 32) * 5/9
print(temp, "degrees fahrenheit is", round(temp_to_celsius, 2), "celsius")

temp = int(input("What is the tempature in celsius?"))
temp_to_fahrenheit = (temp * 1.8) + 32
print(temp, "degrees celsius is", round(temp_to_fahrenheit, 2), "fahrenheit")