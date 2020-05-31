import numpy as np
import math as m

def fx(x):
  expression = ( m.e ** ( -1 * (( x) ** 2)) )
  return expression

def firstFwdDiff(x, h):
  result = (( fx(x + h) - fx(x) ) / h )
  return result

def firstBckDiff(x, h):
  result = (( fx(x) - fx(x - h) ) / h )
  return result

def firstCentrlDiff(x, h):
  result = (( fx(x + h) - fx(x - h) ) / (2 * h) )
  return result

def secondFwdDiff(x,h):
  result = (( fx(x + h + h) - (2 * fx( x + h)) + fx(x) ) / ( h ** 2 ) )
  return result

def secondBckDiff(x,h):
  result = ((  fx(x)  + fx(x - h - h) - (2 * fx( x - h))  ) / ( h ** 2 ) )
  return result

def secondCentrlDiff(x,h):
  result = ((  fx(x + h)  + fx(x - h) - (2 * fx( x ))  ) / ( h ** 2 ) )
  return result

ans = secondCentrlDiff(0,0.2)
print(ans)




