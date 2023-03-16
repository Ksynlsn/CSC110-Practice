def printNumber(start, upperBound):
    num = start                      
    while upperBound + 1 > num:
        print(num)
        num = num + 1
    print(f'Done! You printed numbers {start} through {num - 1}.')

printNumber(3, 16)

def seq3np1(n):
    """ Print the 3n+1 sequence from n, terminating when it reaches 1."""
    while n != 1:
        print(n)
        if n % 2 == 0:        # n is even
            n = n // 2
        else:                 # n is odd
            n = n * 3 + 1
    print(n)                  # the last print is 1

seq3np1(5)

