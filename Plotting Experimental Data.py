from pylab import plot, show, xlim, ylabel, xlabel
from matplotlib.pyplot import legend
from numpy import loadtxt, sum

data = loadtxt("sunspots.txt", float)
avgX = []
avgY = []
months = data[:, 0]
sunspots = data[:, 1]

r = 5
for n in range(5, 995):
    avgX.append(n)
    avgY.append((1./(2.*r)) * sum(sunspots[-5+n: 5+n]))

ylabel("Sunspots")
xlabel("Months")
xlim(0, 1000)
plot(months, sunspots, "r", label="sunspots")
plot(avgX, avgY, "g", label="running average")
legend(loc="upper left")

show()
