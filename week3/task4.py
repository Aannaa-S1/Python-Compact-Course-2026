import numpy as np
A = np.random.random((5,3))
B = np.random.random((3,2))

C = A.dot(B)

print("Matrix A:\n",A)
print("Matrix B:\n",B)
print("Result:\n", C)