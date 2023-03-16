# Write a Python program that takes a list of integers as input and 
# returns the second largest number in the list. If the list contains 
# only one element, return that element as the second largest. If the 
# list is empty, return None.

def findSecondLargest(numList):
    empty = []
    index = 1
    largest = 0
    secondLargest = 0
    if (numList == empty):
            return "List is empty"
    for num in numList:
        if num > largest:
            secondLargest = largest
            largest = num
        elif num > secondLargest:
            secondLargest = num
    return secondLargest

numbers = [12, 23, 11, 24, 66, 45, 67]
print(findSecondLargest(numbers))
        
def isPalindrome(string):
    backwardStr = ""
    space = " "
    punct = "!?:;"
    string = string.lower()
    for char in range(len(string)-1, -1, -1):
        if (char != space) and (char != punct):
            backwardStr += string[char]
    if (string == backwardStr):
        return True
    else:
        return False
 
print(isPalindrome("Racecar"))

        


        
