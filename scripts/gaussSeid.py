import numpy as np
from scipy.linalg import solve
from tabulate import tabulate
import pandas as pd

def calcRe(new, old):
  return  round((abs( ((float(new) - float(old)) / float(new)) * 100)),9)

def gauss(A, b, x, n, maxErr):
    iterArr = []
    Re = [100,100,100]
    L = np.tril(A)
    U = A - L
    i = 1
    while i < 12:
        x = np.dot(np.linalg.inv(L), b - np.dot(U, x))
        x = [round(((1.66 * u) + (1 - 1.66)),4) for u in x.tolist() ]
        x = np.array(x)
        if i == 1:
          Re = [100,100,100]
        else:
          Re = [100,100,100]
          Re[0] = round((abs((x[0] - (-37.5)) / (-37.5)) * 100),6)
          Re[1] = round((abs((x[1] - (18)) / (18)) * 100),6)
          Re[2] = round((abs((x[2] - (33.5)) / (33.5))* 100),6)

        appArr = [i,np.round(x, 7),np.round(np.array(Re), 7), round(max(Re), 7)]
        iterArr.append(appArr)
        i += 1
    pd.DataFrame(iterArr,columns=['Iter','[x1, x2, x3]','TE [x1, x2, x3]%', 'Max TE%']).to_excel('gaussSeidelResults.xlsx')
    print('\n',tabulate(iterArr,headers=['Iter','[x1, x2, x3]','TE [x1, x2, x3]', 'Max TE']))
    print('\nFinal Sol:',)
    print(x,'\n')
    return x

# ----------------------------------------------------------
# Define Matrix to find Eigenvalue here


# MUST BE DIAGONALLY DOMINANT
a = np.array([
  [3, 1, 3],
  [4, 5, 2],
  [2, 1, 2],
])

b = np.array([
  6,
  7,
  10,
])

x = np.array([0, 0, 0])
n = 20

gauss(a, b, x, n, 1)
