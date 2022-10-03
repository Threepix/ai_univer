import math as m
import numpy as np
import matplotlib.pyplot as plt

def fullly():
    d= []
    for x in range(1, 11):
        a= m.fabs(m.cos(x*pow(m.exp(1),m.cos(x)+m.log(x+1))))
        d.append(a)
    return d

f = fullly()
print(f)
print(np.trapz(f))
plt.plot(f)
plt.show()