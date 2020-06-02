from numpy import loadtxt, average
from pylab import show, scatter, plot
#X**2 = sum(i=1 to N) of (m*xi +c - yi)**2
#N data points
#coordinates (xi,yi)
#y-int c
#slope m

#minimum by differentiating with respect to both m and c and setting the derivatives to zero
# m*sum(i=1 to N) of (xi)**2 + c*sum(i=1 to N) of (xi) - sum(i=1 to N) of (xi*yi) = 0
def Ex(x,N):

    return sum(x)/N

def Ey(y, N):

    return sum(y)/N

def Exx(x, N):

    return sum(x**2)/N

def Exy(x, y, N):

    return sum(x*y)/N

def m(x, y, N):
    return (Exy(x, y, N) - Ex(x, N)*Ey(y, N))/(Exx(x, N) - Ex(x, N)**2)

def c(x, y, N):
    return (Exx(x, N)*Ey(y, N)-Ex(x, N)*Exy(x, y, N))/(Exx(x, N) - Ex(x, N)**2)

data = loadtxt("millikan.txt")
x = data[:, 0]
y = data[:, 1]

m_calc = m(x, y, len(data))
c_calc = c(x, y, len(data))

new_y = []

for i in range(len(data)):
    new_y.append(m_calc*x[i]+c_calc)

scatter(x, y)
plot(x, new_y)
show()

v = data[:, 0] #frequencies in Hertz
V = data[:, 1] #Voltages in Volts
e = 1.602*10**-19 #charge of an electron


m_calc = m(v, V, len(data))
phi = c(v, V, len(data))

new_V = []

for i in range(len(data)):
    new_V.append(m_calc*v[i]+phi)

h = e*(new_V + phi) / v
print(average(h))