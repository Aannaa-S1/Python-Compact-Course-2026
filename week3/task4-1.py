import numpy as np

A = np.random.random((3, 3))

print("Original:\n",A)

for i in range(len(A)):
    A[i] = np.subtract(A[i], np.mean(A[i]))

print("Result:\n",A)
