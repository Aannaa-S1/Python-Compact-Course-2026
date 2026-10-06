import numpy as np

A = np.array([
    [1, 2, 3],
    [2, 4, 6],
    [1, 1, 1]
])

rank = np.linalg.matrix_rank(A)

print("Matrix:\n",A)

print("Rank:\n", rank)