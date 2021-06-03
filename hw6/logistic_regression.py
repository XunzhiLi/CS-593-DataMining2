import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
import math
#this is a function to calculate the probability that a persib has depression using  use age, sex, log(income), bed days and health 5 varibles
def g(intercept,x1,x2,x3,x4,x5):
    result = intercept+coefficients[0][0]*x1+coefficients[0][1]*x2+coefficients[0][2]*x3+coefficients[0][3]*x4+coefficients[0][4]*x5
    Pi_x = math.exp(result)/(math.exp(result)+1)
    return Pi_x

#use sklearn to create the logistic model
dataset = pd.read_csv('Depression.csv', delimiter=',')
# to simplify calculation, i have completed Logarithm operation to INCOME DATA.
X = np.array(dataset.get(['SEX', 'AGE','HEALTH','BEDDAYS','LN_INCOME']))
print(X)
Y = np.asarray(dataset.get('CASES'))
classifer = LogisticRegression()
classifer.fit(X,Y)
intercept = classifer.intercept_
print('a0:',intercept)
coefficients = classifer.coef_
print('a1,a2,a3,a4 are:',coefficients)
score = classifer.score(X,Y)
prediction=classifer.predict(X)
print(score)

print('with the high score,it means our model fits well')
print('-------------------------------------')
print('our prediction of depression is ',prediction)

print('lets examine the result ,using the data of ID=1 ,ID=2,ID=3 to get their probabilities of getting depression')
for i in range(5):
    id_number = i+1
    probability = g(intercept, X[i][0], X[i][1], X[i][2], X[i][3], X[i][4])
    print('this result means the estimated probability that ID:%d is suffered by  depression is :' % id_number,probability)
    print('-----------------------------------------')
