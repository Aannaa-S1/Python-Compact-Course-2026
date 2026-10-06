import numpy as np

A = np.arange(256).reshape(16, 16)

result = np.zeros((4, 4))

for i in range(4):
    for j in range(4):
        block = A[i*4:(i+1)*4, j*4:(j+1)*4]
        result[i, j] = block.sum()

print("Array:")
print(A)

print("Block sums:")
print(result)