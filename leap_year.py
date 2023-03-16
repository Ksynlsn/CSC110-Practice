# Kacie Nielsen - CSC 110 - Week 7 Assignment: Boolean Function

def isLeap(year):
# if year is evenly divisible by 4 and evenly divisible by both 100 and 400
    if (year % 4 == 0 and year % 100 == 0 and year % 400 == 0): 
        return True
# if year is evenly divisible by 100 and not by 400 
    if (year % 100 == 0 and not year % 400 == 0): 
        return False
# if year is evenly divisible by 4
    if (year % 4 == 0):
        return True
    else:
        return False

print(isLeap(1900))
   