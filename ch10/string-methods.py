# Kacie Nielsen - CSC 110 - Extra Credit In-Class 3/8

# Removes the first given substring in a given string
def remove(substr, theStr):
    return theStr.replace(substr, "", 1)

# counts the number of non-overlapping occurrences of a substring in a string
def count(substr, theStr):
    return theStr.count(substr, 0, )

print(remove("at", "cat in the hat"))
print(count("at", "cat cat cat"))
print(count("e", "home alone"))
