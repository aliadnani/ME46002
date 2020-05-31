import pandas as pd
import numpy as np
import mpmath as math
from tabulate import tabulate


def calcError(a ,b):
  return (100 * (abs(((b - a) / (b + a)))))

def calcC(a , b):
  return ((a + b) * 0.5)

def bisectionMethod(ai=0,bi=2,precision=9,maxerror=2,maxiterations=15):
  print(f"Initial Guess (a, b): ({ai} ,{bi}) // Max error: {maxerror}%\n")
  math.mp.dps = precision
  a = math.mpf(ai)
  b = math.mpf(bi)
  error = 8888
  c = 0
  iteration = 1
  df_list_vals = []
  while ((error > maxerror) and (iteration < (maxiterations + 1) )):
    error = calcError(a, b)
    c = calcC(a ,b)
    fa = f(a)
    fc = f(c)
    fafc = ( fa * fc)

    row_value = [iteration, a, b, c , fa, fc, fafc, error]
    row_value_rounded = [ round(i, 9) for i in row_value]
    df_list_vals.append(row_value_rounded)

    if (fafc == 0):
      error = 0
    elif (fafc > 0):
      a = c
    else:
      b = c
    iteration += 1
  df = pd.DataFrame(df_list_vals ,columns=['Iteration','a','b','c (root)','f(a)','f(c)','f(a) * f(c)', 'error'])
  df.to_excel('bisectionResults.xlsx')
  print(tabulate(df_list_vals, headers=['Iteration','a','b','c (root)','f(a)','f(c)','f(a) * f(c)', 'error']))
  print('\nFinal Root : ',c,' with error: ', round(error,5),'%')
  return df_list_vals

# ---------------------------------------------------------------------------------------------------------------------------------------------------------------
# Main work here

# Write your f(x) function here
def f(x):
  result = (math.sin(x)**2) + ((x-1)/math.cos(x))
  return result
print('\n---- BISECTION METHOD ----')
bisectionMethod(ai=0,bi=1,maxerror=2,precision=14,maxiterations=15)
print('\n')

# print(result)



