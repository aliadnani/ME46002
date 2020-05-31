import numpy as np
import math

def leastSquares(x, y):
  n = x.shape[0]
  if (x.shape[0] != y.shape[0]):
    raise ValueError("X & Y Shape Mismatch")
    return
  a0 = ((( np.sum(y) * np.sum(np.square(x)) ) - ( np.sum(x) * np.sum(np.multiply(x,y)) ) ) )/ (  (n * np.sum(np.square(x))) - (np.sum(x) ** 2 ) )
  a1 = (( n * np.sum(np.multiply(x,y))) - ( np.sum(y) * np.sum(x) )) / (  (n * np.sum(np.square(x))) - (np.sum(x) ** 2 ) )

  return (round(a0,9), round(a1,9))


def getSteps(x, y):
  n = x.shape[0]
  if (x.shape[0] != y.shape[0]):
    raise ValueError("X & Y Shape Mismatch")
    return
  a0String = f'[( {round((np.sum(y)),7)} * {round((np.sum(np.square(x))),7)} ) - ( {round((np.sum(x)),7)} * {round((np.sum(np.multiply(x,y))),7)} ) ] ÷ [  {round(((n * np.sum(np.square(x)))),7)} - {round(((np.sum(x) ** 2 )),7)} ]'
  a1String = f'[{round(( n * np.sum(np.multiply(x,y))),7)} - ( {round((np.sum(y)),7)} * {round((np.sum(x)),7)} )] ÷ [  {round(((n * np.sum(np.square(x)))), 7)} - {round(((np.sum(x) ** 2 )),7)} ]'

  return (a0String, a1String)

# -------------------------------------------------------
# Input Data as X and Y Vectors

x = np.array([1, 2, 3, 4, 5])
y = np.array([0.5, 1.7, 3.4, 5.7, 8.4])

xi = np.array([math.log(i,10) for i in x])
yi = np.array([math.log(i, 10) for i in y])
print(xi)
print(yi)

print('\n')
print(f'B0,B1 = {leastSquares(xi,yi)}')
print('\n')
print(f'a0 = {getSteps(xi,yi)[0]}')
print(f'a1 = {getSteps(xi,yi)[1]}')
# print('\n')
# print(getSteps(xi,yi)[1])