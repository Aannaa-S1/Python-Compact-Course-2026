import numpy as np
a = 10 * np.random.random(5)
print ("Original:\n" ,a)

print ("Method 1:\n",np.floor(a))
print ("Method 2:\n",np.trunc(a))
print ("Method 3:\n",a.astype(int))
print ("Method 4:\n",a // 1)
print ("Method 5:\n",a - a % 1)

