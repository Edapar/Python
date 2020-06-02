import numpy as np
A = np.array([[1,3,4],[2,-6,7],[5,8,9]])
B = np.array([[1,4,6],[-3,0,1],[12,3,-21]])

#################################Matrix Addition
###############Add array duck issue to computers
C = A + B

#numpy adding array
C = np.add(A, B, dtype=np.float)

##############################Matrix Subtraction
#Duck
C = A - B

#numpy subtracting
C = np.subtract(A, B, dtype=np.float)

##Matrix Muliplication(Pointwise Multiplication)
#duck
C = A*B

#numpy
C = np.multiply(A, B, dtype=np.float)

################################Matrix Division
#duck
#C = A/B

#numpy
#C = np.divide(A, B)

#Hermitian matrix
#a complex suare matrix that is equal to its own conjugate transpose
#i-th row and j-th column = complex conjugate of j-th row and i-th column
x = np.array([[0, 1j], [-1j, 0]])
x_c = np.conjugate(x)
y = np.conjugate(x_c)

################################################

###############Matrix Products#################

################################################

# sum of (Row A elements multiply to Column B elements) = Row C
#C_ij = Sum k =1 to N   A_ik * B_kj
C = np.matmul(A,B)

R = np.array([[1,2,3,4],[2,3,4,5],[3,4,5,6]])

#C != np.matmul(R,A)
#.transpose flip x and y
C = np.matmul(R.transpose(), A)

a = A[:,0]
b = B[:,0]
c = np.matmul(a,b)

# <a,b> = a**T *b = sum i=1 to n a_i*b_i
#dot product
d = np.dot(a,b)

#inner product
i = np.inner(a,b)

#tensor dot product
a = np.arange(60.).reshape(3,4,5)
b = np.arange(24.).reshape(4,3,2)
C = np.tensordot(a,b, axes=([1,0],[0,1]))

#Matrix Exponential to the power
P = np.linalg.matrix_power(A,10)

#Kronecker Product
#A (otimes) B
#[[A[0,0] * B, A[0,1] * B, ..... A[0,m] * B],
#[A[1,0] * B, A[0,1] * B, ..... A[1,m] * B],
#[A[n,0] * B, A[0,1] * B, ..... A[n,m] * B]]
K = np.kron(A,B)

########## Matrix Decompositions ###############

#Cholesky Decompostion: A = UU**H
"""print(A)
U = np.linalg.cholesky(A)
print(U)
C = np.matmul(U, U.transpose().conj())
#print(C)"""

#given a complex array
D = np.array([[1, -2j], [2j, 5]])
#cholesky gives lower diagonal matrix
U = np.linalg.cholesky(D)
#if you dot L with L(transpose conjugate) you should get back original complex matrix
C = np.dot(U, U.T.conj())

#QR decomposition or A = QR Q = orthogonal matrix, R = upper triangle matrix
#Orthogonal matrix = Q**T * Q = Q * Q**T = I
#if A = complex square matrix
# then Q = unitary(conjugate transpose) matrix or Q*Q = QQ* = I
Q = np.linalg.qr(A)[0]
R = np.linalg.qr(A)[1]

#EigenValue Decomposition(EVD)
# A = PDP**-1
# Given Matrix A get P = EigenVectors D = Diagonal Matrix of EigenValues of A
(d, P) = np.linalg.eig(A)
#d = Eigen Values
#P = Eigen Vectors
D = np.diag(d)
#D = transform d to diagonal matrix
R = np.matmul(np.matmul(P,D),np.linalg.inv(P))
R_e = np.real(R)
#just eigen values
E = np.linalg.eigvals(A)

#Singular Valued Decomposition(SVD) - Factorization of a real or complex matrix
#Good for generalization of the eigendecomposition of a positive semidefinite normal matrix
#to any m x n matrix via an extension of the polar decomposition.
#given time given matrix or square matrix
#M = USV**T
#M = m x n
#U = m x m(Real or Complex Unitary Matrix, Unitary == U*U = UU* = I)
#S = m x n(Rectangular Diagonal Matrix with non-negative numbers on the diagonal)
#V = n x n(Real or complex unitary matrix)

(U,s,V) = np.linalg.svd(A)

########################################################

################ Matrix NORM    ########################

########################################################
#Vector norm is a vector sapce whose element(vectors) are matrices(of given dimensions)
#1- norm Sum of abs(elements in vector)
#Matrix Norm sum of all columns and take max of each column = norm(matrix)
#Euclidian/Frobenius Norm sqrt(sum of elements)
#p-norm (sum abs(element of vector) to power p) to the power (1/p)
#infinity norm(vector) = largest in the vector
#infinity norm(matrix) = sum  row and take max value of each row
#f norm = sqrt(sum of all elements in the matrix **2)
#p norm(matrix) = (sum of all elements**p)^(1/p)
np.linalg.norm(A)
np.linalg.norm(B)

#determinate of the matrix(Square) is the n-dimension volume scaling factor of
#the linear transformation described by the matrix
np.linalg.det(A)
#rank of a matrix is the dimension of the vector space generated or spanned by its columns
#Identical to the dimensions of the space spanned by its rows
#
np.linalg.matrix_rank(A)
#trace is the sum of the diagonal of the matrix(square)
#trace of a matrix is the sum of the complex eigenvalues, and it is invariant with respect
#to a change of basis.
#Inveriant change to basis
np.trace(A)
