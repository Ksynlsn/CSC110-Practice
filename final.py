alist = []
print(alist)
names = "dan dave mike cameron tina harvey tim amy"
names = names.split(' ')
for i in names:
    alist.append(i.upper())
    
print(alist)

def sortNums(alist):
    evenList = []
    oddList = []
    for value in alist:
        if (value != 0):
            if (value % 2 == 0):
                evenList.append(value)
            else:
                oddList.append(value)
    #sortedList = [evenList.sort(), oddList.sort()]
    evenList.sort()
    oddList.sort()
    return evenList, oddList
    
myNums = [3, 40, 2, 12, 76, 99, 100, 50, 16, 33, 27, 16] 

print(sortNums(myNums))
    
