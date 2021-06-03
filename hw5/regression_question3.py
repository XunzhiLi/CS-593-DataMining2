import csv as cvs
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

data = pd.read_csv('lung.csv')
X = data[['Height_father','Weight_father','Height_mother','Weight_mother','Age_oldest_child','Weight_oldest_child']]

Y = data['Height_oldest_child']

lr = LinearRegression()
lr.fit(X,Y)
a = lr.coef_
b = lr.intercept_
print('coefficients are :',a)
print('interseption :',b)

score = lr.score(X,Y)
print(score)
# so y = 0.29604883a- 0.00917303b + 30515682c - 0.01132795d + 1.19843784e + 0.07913887f + 0.10417110688868547
# a:Height_father  b: Weight_father  c: Height_mother  d:Weight_mother  e:Age_oldest_child  f:Weight_oldest_child

''' with a 92% score(r^2:SSR/SST), it indicates that our linear regression model is a perfect fit'''

t = np.arange(len(X))
plt.xlabel('the index of data')
plt.ylabel('height of the oldest child')
plt.plot(t, lr.predict(X), 'r-', linewidth=1, label='raw_data')
plt.plot(t, Y, 'go-', linewidth=1, label='predicet_data')
plt.legend(loc='upper left')
plt.grid(b=True, ls=':')
plt.show()