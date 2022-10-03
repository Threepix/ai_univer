import csv
import random
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
e=[]
o=[0.0,1.0]
n=int(input())
for x in range(n):
    e.append(x)
    e[x] = e[x]/random.randint(100,1000)
random.shuffle(e)

df = np.array(e)

outfile = open('example2.csv','w')
out = csv.writer(outfile)
out.writerows(map(lambda x: [x], df))
outfile.close()

mid_val= sum(e)/n
print(mid_val)
print(np.median(e))

ds = pd.read_csv('example2.csv')

sns.scatterplot(data=ds)

plt.show()