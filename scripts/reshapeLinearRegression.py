import numpy as np

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
  a0String = f'[( {round((np.sum(y)),9)} * {round((np.sum(np.square(x))),9)} ) - ( {round((np.sum(x)),9)} * {round((np.sum(np.multiply(x,y))),9)} ) ] ÷ [  {round(((n * np.sum(np.square(x)))),9)} - {round(((np.sum(x) ** 2 )),9)} ]'
  a1String = f'[{round(( n * np.sum(np.multiply(x,y))),9)} - ( {round((np.sum(y)),9)} * {round((np.sum(x)),9)} )] ÷ [  {round(((n * np.sum(np.square(x)))), 9)} - {round(((np.sum(x) ** 2 )),9)} ]'

  return (a0String, a1String)

# -------------------------------------------------------
# Input Data as X and Y Vectors

xi = np.array([1.5, 2.5, 3.5, 4.5])
yi = np.array([3, 5, 7.2, 8.6])


print('\n')
print(f'B0,B1 = {leastSquares(xi,yi)}')
print('\n')
print(f'B0 (Y-Inter): {getSteps(xi,yi)[0]}')
print(f'B1 (Slope): {getSteps(xi,yi)[1]}')
# print('\n')
# print(getSteps(xi,yi)[1])