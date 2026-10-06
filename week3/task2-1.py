import numpy as np

A = np.random.random((3, 3))
B = np.random.random((3, 3))

print("A:\n",A)
print("B:\n",B)
print("Equal:", np.array_equal(A, B))