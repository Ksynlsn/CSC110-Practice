# Chapter One

cats = ["Moose", "Ashes", "Willy", "Pat", "Suily"]
for c in cats:
    invitation = "Hello " + c + "! Please come to my stupid cat party"
    print(invitation)

# to view this output in the terminal, type 'python3 filename.py'   Yay!

# Syntax rules pertain to TOKENS and STRUCTURES. TOKENS are basic elements of the language
# TOKENS are the basic elements of the lanuage
#                   like *WORDS *NUMBERS *PARENTHESES *COMMAS

print("Happy New Year For", 2023) # this has 6 tokens, a function name, (, a string, a comma, a number, )

# DATA TYPES OH BOY
animals = ["cat", "dog", "chicken", "fly"]
fruit = ("apple", "banana", "cherry")
person1 = {"Name" : "Kacie", "Age" : 33}
print(type("string"))
print(type(666))
print(type(3.14))
print(type(animals)) #list
print(type(fruit)) #tuple
print(type(person1)) #dict
print(person1)

# VARIABLES
message = "Hi" #string
n = 17 #int
pi = 3.14159 #float
this_is_a_legal_variable_name = True #bool

print(type(this_is_a_legal_variable_name))

# Reserved Keywords in Python
pythonKeywords = ["and", "as", "assert", "break", "class", "continue", "def", 
"del", "elif", "else", "except", "exec", "finally", "for", "from", "global", "if",
"import", "in", "is", "lambda", "nonlocal", "not", "or", "pass", "raise", "return",
"try", "while", "with", "yeild", "True", "False", "None",]

print(pythonKeywords)
