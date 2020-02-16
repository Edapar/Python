from vpython import sphere,rate, vector
from math import cos,sin,pi
from numpy import arange

s = sphere(pos=vector(1, 0, 0), radius=0.1)
for theta in arange(0, 10*pi, .1):
    rate(100)
    x = cos(theta)
    y = sin(theta)
    s.pos = vector(x, y, 0)