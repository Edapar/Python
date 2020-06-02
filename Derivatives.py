from numpy import linspace
x = 1

def f(x):
    fx = x*(x-1)
    return fx

for i in linspace(-2,-14,7):
    d = 10**i
    derivative = (f(x+d) - f(x)) / d
    print(i, "   ", derivative)