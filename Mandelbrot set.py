#z' = z**2 + c
from numpy import linspace, zeros
from pylab import imshow, figure, show, xlabel, ylabel

def Mandelbrot_set(Re, Im, max_iter):
    c = complex(Re, Im)
    z = 0.0j
    for i in range(max_iter):
        z = z*z + c
        if (z.real*z.real + z.imag*z.imag) >= 4:
            return i
    return max_iter

rows = 2000
columns = 2000

results = zeros([rows, columns])
for row_index, Re in enumerate(linspace(-2, 1, num=rows)):
    for column_index, Im in enumerate(linspace(-1.5, 1.5, num=columns)):
        results[row_index, column_index] = Mandelbrot_set(Re, Im, 100)

figure(dpi=100)
imshow(results.T, cmap='jet', extent=[-2, 1, -1.5, 1.5])
xlabel("Re")
ylabel("Im")
show()