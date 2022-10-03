import numpy as np

a = np.arange(25).reshape(5,5)

for x in range(5):
    for y in range(5):
        a[x][y]=y


print(a)