import numpy as np

# vector = np.arange(15)
# print(vector)
# matrix = vector.reshape(3,5)
# print(matrix)
# print(matrix.shape)

# nfl = np.genfromtxt("D:/WorkSpace/PyCharm/insurance/sinsoft/data/testdata.csv",dtype='float',delimiter=",")
# n = nfl[1:,2:]
# print(n)

ns = np.arange(0,111,10)
n = ns.reshape(3,4)
print(n)
print(n.sum(axis=1))
print(n.sum(axis=0))
