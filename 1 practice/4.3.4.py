import csv
import numpy as np
import pandas as pd
import pylab
import matplotlib.pyplot as plt

appl = []
micro = []
google = []


with open('appl.csv',encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
         appl.append(row['Price'])

with open('micro.csv',encoding='utf-8') as csvfile2:
    reader2 = csv.DictReader(csvfile2)
    for row in reader2:
         micro.append(row['Price'])

with open('google.csv',encoding='utf-8') as csvfile3:
    reader3 = csv.DictReader(csvfile3)
    for row in reader3:
         google.append(row['Price'])

pylab.plot (appl, label="X по возрастанию")
pylab.plot (micro, label="X по убыванию")
pylab.plot (google, label="X по убыванию")
pylab.title ("три линейных графика")

pylab.show()