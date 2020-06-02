#takes three numbers: a, b, c
#prints out two solutions
#solution for 0.001x^2+1000x+0.001=0
from numpy import sqrt, average
def quadratic(a, b, c):
    x1 = (-b + sqrt(b**2 - 4*a*c)) / (2*a)
    x2 = (-b - sqrt(b**2 - 4*a*c)) / (2*a)
    return x1, x2
print(quadratic(.001,1000,.001))

def quadratic2(a, b, c):
    x1 = (2*c) / (-b - sqrt(b**2 - 4*a*c))
    x2 = (2*c) / (-b + sqrt(b**2 - 4*a*c))
    return x1, x2

print(quadratic2(.001,1000,.001))

def quadratic3(a, b, c):
    x1 = (-b + sqrt(b ** 2 - 4 * a * c)) / (2 * a)
    x2 = (-b - sqrt(b ** 2 - 4 * a * c)) / (2 * a)
    resolution = 0.00000001
    newX1 = int(round(x1 / resolution)) * resolution
    newX2 = int(round(x2 / resolution)) * resolution
    return newX1, newX2

print(quadratic3(.001,1000,.001))

