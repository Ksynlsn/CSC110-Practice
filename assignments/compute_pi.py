def pi():
    n =2
    e = 1
    y =3
    terms = int(input("How many iterations?"))
    for i in range(terms):
        y = y + (4 / ((n) * (n+1) * (n+2)) * e)
        n = n + 2
        e = e * -1            
    return(y)
print(pi())