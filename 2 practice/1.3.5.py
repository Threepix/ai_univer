import numpy as np
import random as r

n= int(input())

a = np.arange(n)
r.shuffle(a)
a = list(a)

a.sort()
a.reverse()

print(a)

