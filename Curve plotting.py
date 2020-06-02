#deltoid curve
#x = 2cos(theta) + cos(2theta)
#y = 2sin(theta) + sin(2theta)
#0 <= theta < 2pi
#polar plot r = f(theta)
#x = rcos(theta), y = rsin(theta)
#Galilean spiral = r=(theta)^2 for 0 <= theta < 10pi
# Fey's Function
#r = e^(cos(theta)) - 2 cos(4theta) + sin^5(theta/12)

from numpy import pi, cos, sin, linspace, e
from pylab import plot, show

#Deltoid Curve
theta = linspace(0, 2*pi, 100)
x = 2*cos(theta) + cos(2*theta)
y = 2*sin(theta) + sin(2*theta)
plot(theta, x)
plot(theta, y)
show()

#Polar Plot to Galilean Spiral
theta = linspace(0, 10*pi, 1000)
r = theta**2
x = r*cos(theta)
y = r*sin(theta)
plot(x, y)
show()

#Fey's Function
theta = linspace(0, 24*pi, 1000)
r = e**(cos(theta)) - 2*cos((4*theta)) + (sin((theta/12)))**5
x = r*cos(theta)
y = r*sin(theta)
plot(x, y)
show()