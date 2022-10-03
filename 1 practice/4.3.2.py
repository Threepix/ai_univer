import math as m
import seaborn as sns
import matplotlib.pyplot as plt

def function():
    d=[]
    for x in range(1,11):
        a = m.sqrt(1+m.exp(1)**m.sqrt(x)+m.cos(x**2))/m.fabs(1-pow(m.sin(x),3))+m.log(2*x)
        d.append(a)
    return d
fact = function()
ds = fact[:5]
print(ds)
print(fact)
plt.plot(fact)
plt.show()
sns.scatterplot(data=ds)
plt.show()
