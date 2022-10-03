from sklearn.preprocessing import MinMaxScaler
from sklearn import preprocessing
import pandas as pd
import numpy as np
import csv

df = pd.read_csv("iris.csv")

keep_f1 = ['sepal.length']
keep_f2 = ['sepal.width']

min_max = df[keep_f1]
z_mash = df[keep_f2]

scaler = preprocessing.StandardScaler()
scaler.fit(z_mash)

min_max = preprocessing.normalize(min_max,norm='max',axis=0)
print(f"min max {min_max},z mash {scaler.transform(z_mash)}")