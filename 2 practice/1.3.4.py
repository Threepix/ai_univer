import numpy as np

Z = np.ones((10,10))

Z[1:-1,1:-1] = 0

print(Z)