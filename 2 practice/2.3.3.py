import pandas as pd
import csv

#2.2.5-2.2.7

df = pd.read_csv('ex.csv')

print(df.head(2))
print(df.tail(3))
print(df.shape)
df.describe()

print(df.iloc[1:4])

print(df[df['Per']=="-0,35"].head(5))
