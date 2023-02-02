import modf
# Iterate over index
string_name2 = "Elephant"
for element in range(0, len(string_name2)):
    print(string_name2[element]) 

string_name3 = "Catus Farm"
for v in enumerate(string_name3):
    print(v)
# above method reults in this:
# (1, 'a')
# (2, 't')
# (3, 'u')
# (4, 's')
# (5, ' ')
# (6, 'F')
# (7, 'a')
# (8, 'r')
# (9, 'm')

string_name4 = "Catus Farm"
for i, v in enumerate(string_name4):
    print(v)

modf.printGreeting("Mark")
modf.printGreeting("TeTee")
modf.printGreeting("Ashes")