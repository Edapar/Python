from pylab import imshow,show
from numpy import loadtxt

data = loadtxt("circular.txt",float)
#imshow density plot base on color scale
imshow(data)
show()
