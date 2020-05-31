import pandas as pd
import numpy as np
import mpmath as math
math.mp.dps = 9


def f(x):
  # result = (5 * (x ** 3)) - (5 * (x ** 2)) + (6 * x) - 2
  # result = ((-2) * (x **6)) - ((1.5) * (x **4)) + (10 * x) + 2
  result = ((math.sin(x))**2) + ((x -1) / math.cos(x))
  return result

def calcError(a ,b):
  return (100 * (abs(((b - a) / (b + a)))))

def calcC(a , b):
  return ((a + b) * 0.5)

b = math.mpf(1)
a = math.mpf(0)
maxerror = 2
error = 8888

df = pd.DataFrame(columns=['Iteration','a','b','c (root)','f(a)','f(c)','f(a) * f(c)', 'error'])

iteration = 1

while ((error > maxerror) and (iteration < 16)):
  error = calcError(a, b)
  c = calcC(a ,b)
  fa = f(a)
  fc = f(c)
  fafc = ( fa * fc)
  df.loc[len(df)] = [iteration, a, b, c , fa, fc, fafc, error]
  if (fafc == 0):
    error = 0
  elif (fafc > 0):
    a = c
  else:
    b = c
  iteration += 1




  
df.to_excel('q2.xlsx')

print(df)



