import numpy as np
from pprint import pprint
def LU(A,b):
    n = len(A)
    A, b = np.asarray(A,dtype=np.float64),np.asarray(b,dtype=np.float64)
    L = np.asarray(np.identity(n))
    U = np.copy(A)
    P = np.identity(n)

    permutation = abs(U[:,0]).argsort()[::-1]
    U=U[permutation]
    P=P[permutation]
    print('\n\nSteps\n\n')
    for k in range(n):                          #for each column of A in Ab

        #Forward Elimination - Subtracting rows
        for j in range(k+1,n):                      #for each row under the diagonal of the kth column
            q = float(U[j][k]) / U[k][k]              #calculate the ratio to the value in the main diagonal

            L[j][k] = q
            print('\nL',L)

            for m in range(k, n):                     #for each each column in a Row j
                # A[j][m] -=  q * A[k][m]                   #calculate Rj - q*Rk.  This will result in all zeros under the main diagonal
                print('\nA:',A)
                print('\n')
                if m<len(U):
                    A[j][m] -=  q * A[k][m]                   #calculate Rj - q*Rk.  This will result in all zeros under the main diagonal
                    U[j][m] -= q * U[k][m]
                    print('\nU',U)
                    print('\n')
    x = np.zeros(n)

    U = np.triu(U)
    return (np.asmatrix(L), np.asmatrix(U),np.asmatrix(P))

A = [
  [-8,1,-2],
  [-3,-1,7],
  [2,-6,-1],
  ]
b = [
  [-20],
  [-34],
  [-38],
]


L,U,P = LU(A,b)

print('L: ')
pprint(L)
print('U: ')
pprint(U)
print('P: ')
pprint(P)

#Ly=b
bb = np.asmatrix(P) * np.asmatrix(b)
print('bb: ')
pprint(bb)

n = len(L)
#Lb = np.asarray(np.c_[L, bb],dtype=np.float64)


y = np.zeros(n)
for i in range(n):
    y[i] = bb[i]
    for j in range(i):
        y[i] -= L[i, j]*y[j]
    y[i] = y[i]/L[i, i]
y = np.asmatrix(y).T
print('y: ')
pprint(y)

#Ux=y
x = np.zeros(n)
Uy = np.asarray(np.c_[U, np.asarray(y)],dtype=np.float64)
#Backwards Substitution - Solve for one variable and substite that back in to solve for another
x[n-1] =float(Uy[n-1][n])/Uy[n-1][n-1]      #simply solve the last row, since there should be only one unknown
for i in range (n-1,-1,-1):                 #start,stop, step - starting from the second last row work back up the rows
    z = 0.0                                     #let z=0 or reset to 0
    for j in range(i+1,n):                      #for each column in a Row j
        z = z  + float(Uy[i][j])*x[j]               #substitute answers from below(stored in x) into the equation of the current row
    x[i] = float(Uy[i][n] - z) / Uy[i][i]       #solve for this row, where there should now be only one unknown
x = np.asmatrix(x).T
print('x: ')
pprint(x)