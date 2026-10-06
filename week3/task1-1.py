import numpy as np

def generator():
    n = 10
    for i in range(1, n + 1):
        yield i

a = np.array(list(generator()))

print(a)