# x != y               # x is not equal to y
# x > y                # x is greater than y
# x < y                # x is less than y
# x >= y               # x is greater than or equal to y
# x <= y               # x is less than or equal to y

def getGrade(mark):
    if mark >= 90:
        print('A')
    elif mark >= 80:
            print('B')
    elif mark >= 70:
            print('C')
    elif mark >= 60:
            print('D')
    else:
        print('FAIL')
            

getGrade(100)