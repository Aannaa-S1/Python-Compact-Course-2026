import numpy as np
A = np.random.random((100,2))
distances = np.zeros((100,100))
for i in range(100):
    for j in range(100):
        distances[i,j] = np.sqrt(
            (A[i,0]-A[j,0])**2 + (A[i,1]-A[j,1])**2)
print("Vector:\n",A)
print("Distances:\n",distances)