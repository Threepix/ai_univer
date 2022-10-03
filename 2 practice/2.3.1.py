import pandas as pd
import math as m

a = [int(input()),int(input())]
b = [int(input()),int(input())]

a = pd.Series(a)
b = pd.Series(b)

distance = m.sqrt(pow(a[0]-b[0],2)+pow(b[0]-a[0],2))

print(distance)
