# Write a function that counts how many non-overlapping occurences 
#of a substring appear in a string.
def count(substr,theStr):
    count = 0
    length = len(substr)
    idx = 0
    for i in range(len(theStr)):
        if substr == theStr[idx:length]:
            count += 1
        idx += 1
        length += length - idx    
    return count

print(count("at", "catrathat"))
print(count("boo", "boo whoo boo"))
print(count("no", "nononononono"))

#Write a function that recognizes palindromes. 
#(Hint: use your reverse function to make this easy!).
def reverse(string):
    newString = ""
    for char in range(len(string)-1, -1, -1):
        newString += string[char]
    return newString

def is_palindrome(myStr):
    #reverse(myStr)
    if (myStr == reverse(myStr)):
        return True
        #print(f'The string {myStr} is a palindrome!')
    else:
        #print(f'This is just a regular boring string')
        return False

print(is_palindrome('toot'))

# Write a function that removes all occurrences of a given letter from a string.
def remove_letter(theLetter, theString):
    newString = ""
    for i in theString:
        if i not in theLetter:
            newString += i
    return newString
            
print(remove_letter('z', 'zebra'))

# Write a function that mirrors its string argument, generating a string 
# containing the original string and the string backwards.
def mirror(string):
    backwardString = ''
    for char in range(len(string)-1, -1, -1):
        backwardString += string[char]
    mirrorString = string + backwardString
    return mirrorString

print(mirror('Tacoma'))
print(mirror('Waahooozzzaa'))
print(mirror('Alamaba'))

# Write a function that reverses its string argument.
def reverse(string):
    newString = ''
    for char in range(len(string)-1, -1, -1):
        newString += string[char]
    return newString

print(reverse('Tacoma'))

# Write a function that will return the number of digits in an integer.
def numDigits(n):
    n = str(n)
    num = 0
    for char in range(len(n)):
        num += 1
    return num
        
print(numDigits(2234567))

def count(p):
    cnt = 0
    upperE = 0
    lowerE = 0
    for char in range(len(p)):
        if (p[char] == 'e'):
            cnt += 1
            lowerE += 1
        elif (p[char] == 'E'):
            cnt += 1
            upperE += 1
    return cnt
    
p = "testE"

print(count(p))