import numpy as np

dt = np.dtype([
    ("x", float),
    ("y",float),
    ("r",int),
    ("g",int),
    ("b",int)
])

a = np.array([(1.0,2.0,1,0,0),(3.0,4.0,0,1,0)], dtype=dt)
print("Array:",a)