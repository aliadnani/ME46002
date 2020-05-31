import sympy
import numpy as np
from pprint import pprint

def findEigen(A):
  c = sympy.Symbol('c')
  print('\nMatrix A:\n',A)

  A = sympy.Matrix(A)
  Y = A.charpoly(c)
  rawEx = sympy.factor(Y.as_expr())
  Ex = sympy.expand(rawEx)

  print('\nUnexpanded:',rawEx)
  print('Expanded:',Ex)

  print('Solved EigenVals:',sympy.solve((Ex),c),'\n')

# ----------------------------------------------------------
# Define Matrix to find Eigenvalue here

# a = np.array([
#   [-0.25, -2.25, 0.25],
#   [1.75, 4.75, 0.25],
#   [-1, 1, 3],
# ])
a = np.array([
  [1, 0, 2],
  [1, 1, 3],
  [6, 2, 2],
])

findEigen(a)