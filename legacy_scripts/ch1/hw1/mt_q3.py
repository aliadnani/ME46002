import numpy as np
from scipy import linalg

F = np.array([[4,1,6],[5,1,2],[1,8,2]])
A = np.array([[4,1,6,6],[5,1,2,3],[1,8,2,2]])
B = np.array([6,3,2])

LU, P = linalg.lu_factor(F)



print(f'LU = {LU}')
print('\n')

print(f'P = {P}')


ANS = linalg.lu_solve((LU,P),B)

print('\n')
print(f'ANS = {ANS}')
