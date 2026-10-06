import numpy as np
a = np.random.random((5,5))
print("Original matrix:\n", a)
a = (a - a.min()) / (a.max() - a.min())
print("Normalized matrix:\n", a)