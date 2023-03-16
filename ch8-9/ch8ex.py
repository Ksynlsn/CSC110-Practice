def newtonSqrt(n):
    approx = 0.5 * n
    for i in range(n):
        betterApprox = 0.5 * (approx + n/approx)
        approx = betterApprox
        while betterApprox != approx:
               print(betterApprox)
    return betterApprox
               
print(newtonSqrt(125))