import numpy as np

A = np.array([[4,2,3],[2,0,1],[2,1,4]])



W,V = np.linalg.eig(A)
print('\n')

print('EIGNENVALS = ')
print(W)


print('\n')
print('EIGNENVECs = ')

print('\n')

print(V)