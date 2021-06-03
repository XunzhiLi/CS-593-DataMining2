import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt

data = pd.read_csv('Depression.csv')
X = data[['SEX','AGE','INCOME']]
Y = data['Cat_total']
lr = LinearRegression()
lr.fit(X,Y)
a = lr.coef_
b = lr.intercept_
print('coefficients are :',a)
print('interseption :',b)
score = lr.score(X,Y)
print(score)

#from the score data(0.07393578909477616) we can know that there is even no linear relation between level of regression
#and three varibles.And we can still guess the residuals can be in a normal distribution

#then we are going to prove our suspect

predicted_data = []
for i in range(150):
    item = int(a[0]*data['SEX'][i]+a[1]*data['AGE'][i]+a[2]*data['INCOME'][i])
    predicted_data.append(item)
print(len(predicted_data))

predicted_data.sort()
print(predicted_data)
mean = np.mean(predicted_data)

print(mean)

x = set(predicted_data)

list = []
for i in x:
    count = predicted_data.count(i)
    list.append([i,count])
print(list)

plt.xlabel("approximate residuals")
plt.ylabel("numbers(frequency)")
for p in list:
    plt.bar(p[0],p[1], 1, color="black")
plt.show()

'''So according to the bar chart ,it is not reasonable to assume 
dependent variable and three independent variales follow a normal
distribution'''