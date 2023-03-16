#print("n", '\t', "2**n")     #table column headings
#print("---", '\t', "-----")
#print("---", '\t', "-----")

def printRow(x):
    const = 1
    m = 1
    print('\n')
    for i in range(x):
        for col in range(x):
            print(const * m, '\t', end="")
            m +=1
        print('\n')
        const += 1
        m = 1

def printTables(x): # prints 1 - x top row
    
    for i in range(x):
        print("---", '\t', end="")
        
    printRow(x)

  
printTables(13)

