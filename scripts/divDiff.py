import pandas as pd
import numpy as np
from tabulate import tabulate

def makeNDDpyramid(x, y):
  # Create N x N 2D array to store pyramid
  N = np.shape(y)[0]
  # Fills N x N with 0s
  NDDPyramid = np.zeros([N,N])
  NDDPyramid[:,0] = y

  for j in range(1,N):
    for i in range(0 , (N-j)):
      NDDPyramid[i][j] = round(((NDDPyramid[i+1][j-1] - NDDPyramid[i][j-1]) / (x[i+j] - x[i])),7)
  return NDDPyramid
    # NDDPyramid[::,1] = y

def getCoeffs(pyramid):
  return pyramid[0]

def getPolynomials(coeffs):
  pass

# -------------------------------------------------------
# Input Data as X and Y Vectors

x = np.array([6,8,10,12,14])
y = np.array([2.4,4.0,6.6,7.2,9.8])
# x = np.array([7,12,15,18,19])
# y = np.array([6.5,7,11.2,10.8,8.5])

pyramid = makeNDDpyramid(x,y)
pd.DataFrame(pyramid).to_excel('NDDPyramid.xlsx')
print('\nHeaders are: i, xi, yi, g[xi+1.. , g[xi+2..')
print(tabulate(pyramid))
coeffs = getCoeffs(pyramid)
print(f'Coeffecients are: {coeffs}\n')