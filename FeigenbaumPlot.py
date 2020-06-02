#x' = rx(1-x)
from numpy import arange
from pylab import scatter, yscale, show

x =.0001
x1 = [0]
r1 = [0]

for r in arange(0, 4, .001):
    for i in range(0, 1000):
        if r < 1:
            x1.append(0)
            r1.append(r)
            i += 1
        else:
            x = r*x*(1-x)
            r1.append(r)
            x1.append(x)
            i += 1
scatter(r1, x1)
show()
