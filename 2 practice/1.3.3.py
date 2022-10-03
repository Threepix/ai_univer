import numpy as np
import random as r

a = np.arange(27).reshape(3,3,3)

for x in range(3):
    for y in range(3):
        for z in range(3):
            a[x][y][z] = r.randint(1,1000)

print(a)