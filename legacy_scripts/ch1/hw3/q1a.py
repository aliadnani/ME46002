import pandas as pd
import numpy as np

def makeNDDpyramid(x, y):
  # Create N x N 2D array to store pyramid
  N = np.shape(y)[0]
  # Fills N x N with 0s
  NDDPyramid = np.zeros([N,N])
  NDDPyramid[:,0] = y

  for j in range(1,N):
    for i in range(0 , (N-j)):
      NDDPyramid[i][j] = (NDDPyramid[i+1][j-1] - NDDPyramid[i][j-1]) / (x[i+j] - x[i])
  return NDDPyramid
    # NDDPyramid[::,1] = y

def getCoeffs(pyramid):
  return pyramid[0]

def getPolynomials(coeffs):
  pass

x = np.array([7,12,15,18,19])
y = np.array([6.5,7,11.2,10.8,8.5])

pyramid = makeNDDpyramid(x,y)
print(pyramid)
coeffs = getCoeffs(pyramid)
# print(coeffs)
