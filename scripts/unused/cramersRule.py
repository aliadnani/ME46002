import numpy as np

def getDeterminant(M):
  determinant = round(np.linalg.det(M), 9)
  print(determinant)

testMatrix = np.array([[0, -3, 7], [1, 2, -1], [5, -2,  0]])


print("Cramer's Rule")
getDeterminant(testMatrix)

