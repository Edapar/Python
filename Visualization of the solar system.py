from vpython import sphere, rate, color, vector
from numpy import arange, cos, sin, pi

#Proportionality constant for Planet Radii
c1 = 10000

#Proportionality for Planet Positions
c2 = 10000000

#Star + Planet positions
sun = sphere(pos=vector(0, 0, 0), radius=69550000, color=color.yellow)

mercury = sphere(pos=vector(c2*57.9, 0, 0), radius=c1*2440, color=color.red)
venus = sphere(pos=vector(c2*108.2, 0, 0), radius=c1*6052)
earth = sphere(pos=vector(c2*149.6, 0, 0), radius=c1*6371)
mars = sphere(pos=vector(c2 * 227.9, 0, 0), radius=c1*3386)
jupiter = sphere(pos=vector(.5 * c2 * 778.5, 0, 0), radius=.5 * c1*69173)
saturn = sphere(pos=vector(.5 * c2 * 1433.4, 0, 0), radius=.5 * c1 * 57316)

#Radii of Planet's Orbit
rMercury = c2 * 57.9
rVenus = c2 * 108.2
rEarth = c2 * 149.6
rMars = c2 * 227.9
rJupiter = .5 * c2 * 778.5
rSaturn = .5 * c2 * 1433.4

for theta in arange(0, 10000000*pi, 2):
    rate(500)
    xMercury = rMercury*cos(theta/88.)
    yMercury = rMercury*sin(theta/88.)
    mercury.pos = vector(xMercury, yMercury, 0)

    xVenus = rVenus*cos(theta/224.7)
    yVenus = rVenus*sin(theta/224.7)
    venus.pos = vector(xVenus, yVenus, 0)

    xEarth = rEarth*cos(theta/365.3)
    yEarth = rEarth*sin(theta/365.3)
    earth.pos = vector(xEarth, yEarth, 0)

    xMars = rMars*cos(theta/687.0)
    yMars = rMars*sin(theta/687.0)
    mars.pos = vector(xMars, yMars, 0)

    xJupiter = rJupiter*cos(theta/4331.6)
    yJupiter = rJupiter*sin(theta/4331.6)
    jupiter.pos = vector(xJupiter, yJupiter, 0)

    xSaturn = rSaturn*cos(theta/10759.2)
    ySaturn = rSaturn*sin(theta/10759.2)
    saturn.pos = vector(xSaturn, ySaturn, 0)
