import numpy as np

A = np.array([[1,2,3,4],[10,20,30,40],[100,200,300,400],[1000,2000,3000,4000]])


#create identity matrixies
I = np.eye(2)

#create a zero array of n x m
zero = np.zeros((5,5))

#create a one matrix of n x m
one = np.ones((5,5))

#constant matrix of n x m (shape, fill value, dtype = None, order ="c")
C = np.full((4, 5), 10)

#random matrix .random.random
Rand = np.random.random((10000,1))
