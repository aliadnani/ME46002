import pandas as pd
import numpy as np
import math


def f(x):
  # (4 * (x ** 2))
  result = -1 + ( 5.5 * x) - (4 * (x ** 2)) + (0.5 * (x ** 3))
  return result

def dF(x):
  result = 5.5 - (8 * x) + (1.5 * (x ** 2))
  return result

def calcx(xi):
  result = (xi - ((f(xi)/dF(xi))))
  return result


def calcError(xi ,x):
  return (100 * (abs(((x - xi) / (x)))))



xi = 2
maxerror = 0.4 # in Percent

df = pd.DataFrame(columns=['Iteration','xi','f(x)','dF(x)','x', 'error'])

iteration = 1
fx = f(xi)
dFx = dF(xi)
x = calcx(xi)
error = calcError(xi, x)

while ((iteration < 15) and (dFx != 0) and (fx != 0) and (error > maxerror)):
  m.mp.dps = 6 
  fx = f(xi)
  dFx = dF(x)
  x = calcx(xi)
  error = calcError(xi, x)
  df.loc[len(df)] = [iteration, xi, fx, dFx, x, error]

  xi = x
  iteration += 1



print(df)
  

# print(df)



