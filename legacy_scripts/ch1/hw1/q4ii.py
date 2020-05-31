import pandas as pd
import numpy as np
import mpmath as m


def f(x):
  # (4 * (x ** 2))
  result = m.power(x,3) - m.mpf(x) - m.mpf(3)
  return result

def dF(x):
  result = (3 * m.power(x,2)) - m.mpf(1)
  return result

def calcx(xi):
  result = (xi - ((f(xi)/dF(xi))))
  return result


def calcError(xi ,x):
  return (100 * (abs(((x - xi) / (x)))))



xi = m.mpf(0.0)
maxerror = 0.1 # in Percent

df = pd.DataFrame(columns=['Iteration','xi','f(x)','dF(x)','x', 'error'])

iteration = 1
fx = f(xi)
dFx = dF(xi)
x = calcx(xi)
error = calcError(xi, x)

while ((iteration < 25) and (dFx != 0) and (fx != 0) and (error > maxerror)):
  fx = f(xi)
  dFx = dF(x)
  x = calcx(xi)
  error = calcError(xi, x)
  df.loc[len(df)] = [iteration, xi, fx, dFx, x, error]

  xi = x
  iteration += 1

df.to_excel('q4ii.xlsx')


print(df)
  

# print(df)



