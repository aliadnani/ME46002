import scipy.interpolate 
import numpy as np
import matplotlib.pyplot as plt

x = np.array([0., 10., 30.])
y = np.array([30., 130., 150.])

xvals = np.linspace(0, len(y)-1, len(y)*100, endpoint = False)
func = scipy.interpolate.splrep(x, y, s=0)
yvals = scipy.interpolate.splev(xvals, func, der=0)

# display original vs cubic spline representation for security...
plt.figure()
plt.plot(x, y, 'x', xvals, yvals, x, y, 'b')
plt.legend(['Linear', 'Cubic Spline'])
plt.axis([-0.05, 20, -2, 20])
plt.title('Cubic-spline interpolation')
plt.show()

# pp = scipy.interpolate.spltopp(func[0][1:-1],func[1],func[2])

# pp = scipy.interpolate.spltopp(func[0][1:-1],func[1],func[2])

#Print the coefficient arrays, one for cubed terms, one for squared etc
# print(pp.coeffs)
