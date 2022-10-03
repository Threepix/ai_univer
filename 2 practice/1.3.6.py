import numpy as np

n = int(input())
m = int(input())

a = np.arange(n*m).reshape(n,m)

n = a.shape[0]
m = a.shape[1]

if n>m or n<m:
    print(f'прямоугольная {n} строк и {m} столбцов, A{n}x{m}')
if n==m:
    print(f'квадратная {n} строк и {m} столбцов, A{n}x{m}')