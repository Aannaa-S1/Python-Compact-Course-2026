import numpy as np

A = np.array([
    [5, 2, 8],
    [1, 9, 3],
    [4, 6, 7]
])

print("Original:\n",A)

n = 1

A = A[A[:, n].argsort()]

print("Sorted:\n", A)