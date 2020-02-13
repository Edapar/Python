def factorial(n):
    if n == 1:
        return 1
    else:
        return n*factorial(n-1)


def Catan(n):
    if n == 0:
        return 1
    else:
        return ((4*n-2)/(n+1))*Catan(n-1)

def ecluid(m,n):
    if n == 0:
        return m
    else:
        return ecluid(n, m % n)

