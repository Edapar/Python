"""Condensed Matter Physics: Madelung Constant gives the total electric potential felt by an atom in a solid"""
from math import sqrt, pi
from numpy import array
# electron, epsilon_0, atom amount, Total Potential felt by original atom
e, e_0, M = 1.60217662e-19, 8.854187817e-12, 0.0
L = int(input("Enter lattice Size: "))
a = int(input("Enter the spacing of atoms on the lattice: "))

for i in range(-L, L+1):
    for j in range(-L, L+1):
        for k in range(-L, L+1):
            r = array([i, j, k], float)
            d = a * sqrt(r[0] ** 2 + r[1] ** 2 + r[2] ** 2)
            if (i == j == k == 0):
                continue
            V_T = e / (4 * pi * e_0 * a * d)

            if (i+j+k) % 2 == 1:
                V_T *= -1

            M += V_T
print(M)


