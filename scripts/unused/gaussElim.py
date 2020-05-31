import numpy as np

def gaussElim(A,b):
  Ab = np.hstack([A, b.reshape(-1, 1)])

  n = len(b)

  for i in range(n):
      a = Ab[i]

      for j in range(i + 1, n):
          b = Ab[j]
          m = a[i] / b[i]
          Ab[j] = a - m * b
          print('\n')
          print(Ab)

  for i in range(n - 1, -1, -1):
      Ab[i] = Ab[i] / Ab[i, i]
      a = Ab[i]

      for j in range(i - 1, -1, -1):
          b = Ab[j]
          # print(b)
          m = a[i] / b[i]
          Ab[j] = a - m * b
          print('\n')
          print(Ab)

  x = Ab[:, 3]

  print(Ab)
  print(x)


A = np.array([
  [2, 6, 1],
  [7, 1, 4],
  [8, 5, 2]
  ])

b = np.array([1, 3, 1])

gaussElim(A,b)
