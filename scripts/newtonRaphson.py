import pandas as pd
import numpy as np
import mpmath as math
from tabulate import tabulate




def calcx(xi):
  result = (xi - ((f(xi)/dF(xi))))
  return result


def calcError(xi ,x):
  return (100 * (abs(((x - xi) / (x)))))


def newtonRaphson(xi=2.,maxerror=2,precision=9,maxiterations=15,toexcel=False):
  # df = pd.DataFrame(columns=['Iteration','xi','f(x)','dF(x)','x', 'error'])
  list_vals = []

  iteration = 1
  fx = f(xi)
  dFx = dF(xi)
  x = calcx(xi)
  error = calcError(xi, x)
  print('\n------- NEWTON RAPHSON --------\n')
  print(f"Initial Guess xi: {xi} // Max error: {maxerror}%\n")

  while ((iteration < 15) and (dFx != 0) and (fx != 0) and (error > maxerror)):
    fx = f(xi)
    dFx = dF(x)
    x = calcx(xi)
    error = calcError(xi, x)
    row = [iteration, xi, fx, dFx, x, error]
    row_round = [ round(i, 9) for i in row]
    list_vals.append(row_round)
    xi = x
    iteration += 1
  print(tabulate(list_vals,headers=['Iteration','xi','f(x)','dF(x)','x', 'error']))
  print(f'\nFinal root: {round(x,6)} with error {round(error,5)}%\n')
  pd.DataFrame(list_vals,columns=['Iteration','xi','f(x)','dF(x)','x', 'error']).to_excel('newtonResults.xlsx')
  return list_vals


# ---------------------------------------------------------------------------------------------------------------------------------------------------------------
# Main work here

def f(x):
  # (4 * (x ** 2))
  result = math.exp(x) - math.cos(x) - 2
  return result

def dF(x):
  result = math.exp(x) + math.sin(x) 
  return result


newtonRaphson(xi=2,maxerror=0.1,precision=9,maxiterations=15,toexcel='')



  




