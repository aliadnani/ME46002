import numpy as np

def leastSquares(x, y):
  n = x.shape[0]
  if (x.shape[0] != y.shape[0]):
    raise ValueError("X & Y Shape Mismatch")
    return
  a0 = ((( np.sum(y) * np.sum(np.square(x)) ) - ( np.sum(x) * np.sum(np.multiply(x,y)) ) ) )/ (  (n * np.sum(np.square(x))) - (np.sum(x) ** 2 ) )
  a1 = (( n * np.sum(np.multiply(x,y))) - ( np.sum(y) * np.sum(x) )) / (  (n * np.sum(np.square(x))) - (np.sum(x) ** 2 ) )

  return (a0, a1)


def getSteps(x, y):
  n = x.shape[0]
  if (x.shape[0] != y.shape[0]):
    raise ValueError("X & Y Shape Mismatch")
    return
  a0String = f'(( {np.sum(y)} * {np.sum(np.square(x))} ) - ( {np.sum(x)} * {np.sum(np.multiply(x,y))} ) ) / (  {(n * np.sum(np.square(x)))} - {(np.sum(x) ** 2 )} )'
  a1String = f'({( n * np.sum(np.multiply(x,y)))} - ( {np.sum(y)} * {np.sum(x)} )) / (  {(n * np.sum(np.square(x)))} - {(np.sum(x) ** 2 )} )'

  return (a0String, a1String)
xi = np.array([1.5, 2.1, 3.8, 4.2, 7.6], dtype=np.float64)
yi = np.array([2.4, 4.1, 5.2, 7.5, 8.2], dtype=np.float64)

# xi = np.array([1.5, 2.5, 3.5, 4.5 ], dtype=np.float64)
# yi = np.array([3., 5., 7.2, 8.6 ], dtype=np.float64)
print('\n')
print(leastSquares(xi,yi))
print('\n')
print(getSteps(xi,yi)[0])
print('\n')
print(getSteps(xi,yi)[1])