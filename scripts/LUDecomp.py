import numpy as np

def LU_decomposition(A):
    """Perform LU decomposition using the Doolittle factorisation."""

    L = np.zeros_like(A)
    U = np.zeros_like(A)
    N = np.size(A, 0)
    print("L:")
    print(L)
    print('\n')
    print("U:")
    print(U)
    print('\n')

    for k in range(N):
        L[k, k] = 1
        U[k, k] = (A[k, k] - np.dot(L[k, :k], U[:k, k])) / L[k, k]
        print("L:")
        print(L)
        print('\n')
        print("U:")
        print(U)
        print('\n')
        for j in range(k+1, N):
            U[k, j] = (A[k, j] - np.dot(L[k, :k], U[:k, j])) / L[k, k]
            print("U:")
            print(U)
            print('\n')
        for i in range(k+1, N):
            L[i, k] = (A[i, k] - np.dot(L[i, :k], U[:k, k])) / U[k, k]
            print("L:")
            print(L)
            print('\n')
    print("FINAL:")
    print("L:")
    print(L)
    print('\n')
    print("U:")
    print(U)
    print('\n')
    return L, U


a = np.array([
  [1,4,1],
  [1,6,1],
  [2,-1,2]
])
LU_decomposition(a)



