#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/4/27 16:45
# @Author  : Xunzhi Li
# @Site    :
# @File    : Regression.py.py
# @Software: PyCharm
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt


#get data from csv file
data = pd.read_csv('lung.csv')
#get Height_father as Independent variable
x_list = data[['Height_father']]
#get FVC_father as dependent variable
y_list = data['FVC_father']

#use LinearRegression function in Sklean  library.
lr = LinearRegression()
lr.fit(x_list,y_list)

print(lr.coef_)   #it is coefficient
print(lr.intercept_)  #it is intercept
#the score of whether this model fits
print(lr.score(x_list,y_list))


plt.scatter(x_list, y_list, color='green')
plt.plot(x_list, lr.predict(x_list), color='darkblue', linewidth=4)
plt.show()
