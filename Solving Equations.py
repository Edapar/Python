#Ax = b
import numpy as np
A = np.array([[1, 5, 6], [1, 8, 9], [0, 1, 6]])
b = np.random.random((3, 1))

#x1 = A**-1 b
x1 = np.matmul(np.linalg.inv(A),b)
#x2 = built in api to solve for matrix x
x2 = np.linalg.solve(A,b)

#Moore-Penrose Pseudo-Inverse A**+
#S = real entries == S**+
#S = invertible == S**+ = A**-1
#S = zeroes(n,n) @ transpose
#(S**+)**+ == S
#Pseudoinversion commutes with transposition, conjugation, and taking the conjugate transpose
#(aS)**+ = a**-1 S**+ for a != 0
S = np.array([[1, 2], [2, 4]])

print(np.matmul(np.linalg.pinv(S), S))