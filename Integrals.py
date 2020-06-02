from numpy import sqrt
N = 10000000000
h = 2 / N

def x(k):
    return -1 + h*k

def y(k):
    return sqrt(1-x(k)*x(k))

I = 0.0
for i in range(1, N):
    I += y(i)

print(2*I/N)