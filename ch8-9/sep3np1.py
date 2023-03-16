def seq3np1(n):
    """ Print the 3n+1 sequence from n, terminating when it reaches 1."""
    count = 0
    while n != 1:
        #print(n)
        if n % 2 == 0:        # n is even  -  n // 2 
            n = n // 2
            count += 1
        else:                 # n is odd  -  multiply it by three and add 1
            n = n * 3 + 1
            count += 1
    #print(n)                  # the last print is 1
        
    return count
print(seq3np1(18))
print(seq3np1(19))
print(seq3np1(20))
start = 0
for start in range(1, 51, 1):
    print(f'Starting Value: {start} Iterations to 1: {seq3np1(start)}')
