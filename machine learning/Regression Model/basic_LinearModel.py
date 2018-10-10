# http://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LinearRegression.html


import numpy as np
from sklearn.linear_model import LinearRegression

x = np.array([[1,1],[1,2],[2,2],[2,3]])

 # y = 1 * x_0 + 2 * x_1 + 3
y = np.dot(x, np.array([1,2])) + 3
reg = LinearRegression().fit(x,y)
reg.score(x,y)
print(reg.score(x,y))
print(reg.coef_)
print(reg.intercept_)
print(reg.predict(np.array([[3,5]])))
