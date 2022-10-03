import numpy as np

a = np.arange(64).reshape(8, 8)
for x in range(8):
    for y in range(8):
        if (x + 1 + y + 1)%2 == 0:
            a[x][y] = 1
        else:
            a[x][y]=0
print(a)