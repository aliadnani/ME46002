import pandas as pd
import numpy as np
import mpmath as math

# Write your f(x) function here
def f(x):
  # result = (math.sin(x) / x) + (x / (1 + math.tan(x)) - 1.2)
  result = math.sin(x) + (((1 - x) * math.exp(x)) / (1.2 + math.cos(x)))

  return result


def calcError(a ,b):
  return (100 * (abs(((b - a) / (b + a)))))

def calcC(a , b):
  return ((a + b) * 0.5)


def bisectionMethod(precision=9,maxerror=2,maxiterations=15):
  math.mp.dps = precision

  b = math.mpf(2)
  a = math.mpf(0)
  maxerror = 5
  error = 8888

  iteration = 1
  df_list_vals = []
  while ((error > maxerror) and (iteration < (maxiterations + 1) )):

    error = calcError(a, b)
    c = calcC(a ,b)
    fa = f(a)
    fc = f(c)
    fafc = ( fa * fc)

    row_value = [iteration, a, b, c , fa, fc, fafc, error]
    df_list_vals.append(row_value)

    if (fafc == 0):
      error = 0
    elif (fafc > 0):
      a = c
    else:
      b = c
    iteration += 1
  df = pd.DataFrame(df_list_vals ,columns=['Iteration','a','b','c (root)','f(a)','f(c)','f(a) * f(c)', 'error'])
  return df


result =  bisectionMethod(precision=9,maxerror=2,maxiterations=15)

print(result)



