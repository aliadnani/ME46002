import numpy as np 
import math as m

# def fx(x):
#   expression = (0.2 + (25 * x) - (200 * (x ** 2)) + (675 * (x ** 3)) - (900 * (x ** 4)) + (400 * (x ** 5)))
#   return expression

def fx(x):
  expression = (x ** 2) * m.exp(x)
  return expression

def trapezRule(a,b,h):

  # Generate x series
  intervalArray = []
  i = round(a + h, 9)
  while i < b:
    intervalArray.append(i)
    i += h
    i = round(i , 9)

  # Generate f(x) sereies
  fxArray = np.array([fx(x) for x in intervalArray])
  # return fxArray
  result = (h / 2)* (fx(a) + fx(b) + (2 * fxArray.sum()))

  intervalArrayAB = intervalArray
  intervalArrayAB.append(b)
  intervalArrayAB.insert(0,a)
  fxArrayAB = np.array([fx(x) for x in intervalArray])
  
  # Print statements
  print(f'\nTrapezoid Rule: a = {a}, b = {b}, h = {h}\n')
  print(f'Interval Series (with a & b) = {intervalArrayAB}')
  print(f'f(x) Series (with a & b) = {fxArrayAB}')
  print(f'Result: {result}\n')
  return result

def simpsonRule(a,b,h):

  # Generate x series
  intervalArray = []
  intervalArrayOdd = []
  intervalArrayEven = []

  i = round(a + h, 9)
  counter = 1
  while i < b:
    if (counter % 2 != 0):
      intervalArrayOdd.append(i)
    else:
      intervalArrayEven.append(i)
    intervalArray.append(i)
    counter += 1
    i += h
    i = round(i , 9)

  # Generate f(x) sereies
  fxArray = np.array([fx(x) for x in intervalArray])
  fxArrayOdd = np.array([fx(x) for x in intervalArrayOdd])
  fxArrayEven = np.array([fx(x) for x in intervalArrayEven])
  # return fxArray
  result = (h / 3) * (fx(a) + fx(b) + (4 * fxArrayOdd.sum()) + (2 * fxArrayEven.sum()))

  intervalArrayAB = intervalArray
  intervalArrayAB.append(b)
  intervalArrayAB.insert(0,a)
  fxArrayAB = np.array([fx(x) for x in intervalArray])
  
  # Print statements
  print(f'\nSimpson Rule: a = {a}, b = {b}, h = {h}\n')
  print(f'Interval Series (with a & b) = {intervalArrayAB}')
  print(f'f(x) Series (with a & b) = {fxArrayAB}')
  print(f'Result: {result}\n')
  return result




def calcH(a,b):
  return ((b - a) / 4)

ai = 0
bi = 3
hi = calcH(ai,bi)
print('\n\n\n\n')
tr = trapezRule(a=ai,b=bi,h=hi)
si = simpsonRule(a=ai,b=bi,h=hi)

# print(tr)
# print(si)
  
