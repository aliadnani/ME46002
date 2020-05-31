import numpy as np
from sklearn.linear_model import LinearRegression
# xi = np.array([1,2.2,2,3])
# yi = np.array([1,2.4,3.2,4.1])
X = np.array([[1, 1], [2.2, 2.4], [2, 3.2], [3, 4.1]])
y = np.dot(X, np.array([1, 2])) + 3
reg = LinearRegression().fit(X, y)
reg.score(X, y)
print(reg.coef_)