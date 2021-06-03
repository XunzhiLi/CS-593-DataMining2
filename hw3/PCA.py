#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/3/18 14:21
# @Author  : Xunzhi Li
# @Site    :
# @File    : cs593_PCA.py
# @Software: PyCharm
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
import pandas as pd
import numpy as np
import csv as csv

#read the data from Depression.csv
csv_file = csv.reader(open(r'Depression.csv','r'))

X=[] #put the data into list and then transform the list into array
for line in csv_file:
    line = line[8:28] #only choose the Cat parts data
    X.append(line)
X = np.array(X)
X = np.delete(X,0,axis=0)
mat = pd.DataFrame(X) #use pandas.DataFrame to create a kind of data_construction which is similar to Excel table.

pca = PCA()
pca_line = pca.fit_transform(mat)

#Step 1: we use Sklearn to draw a line chart to show the relationship between numbers of Cats and cumulative explained variance.
plt.plot([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20],np.cumsum(pca.explained_variance_ratio_))
plt.xticks([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20])
plt.xlabel('numbers of Cats')
plt.ylabel('cumulative explained variance')
plt.show()

'''after noticing the line chart ,we notice if we choose the eight components 
and they have accounted for about 75% of total data .The least 12 characters are not very important.
We can also make this decision after comparing the clope.
'''

# data transform
Mat = np.array(mat, dtype='float64')
p,n = np.shape(Mat) # shape of Mat
Mean_ = np.mean(Mat, 0) # calculate mean of each column
#Loop through each data ,and use it to minus mean
for i in range(p):
    for j in range(n):
        Mat[i,j] = float(Mat[i,j]-Mean_[j])
#get the cov
cov_Matrix = np.dot(Mat.T, Mat)/(p-1)

print(cov_Matrix)
# calculate eigvalues and eigenvectors
U,V = np.linalg.eigh(cov_Matrix)
# Rearrange
U = U[::-1]
for i in range(n):
     V[i,:] = V[i,:][::-1]

'like what i did before ,we choose 8 main components'
Conponents_numbers = 8
v = V[:,:Conponents_numbers]  # subset of Unitary matrix
# data transformation
result = np.dot(Mat, v)
# print the transformed data
print('PCA result data is :\n',result)


'''i have run the code and create the new_csv file to store the data'''
# with open('new.csv','w',newline='')as f:
#     f_csv = csv.writer(f)
#     f_csv.writerow(['Cat_01','Cat_02','Cat_03','Cat_04','Cat_05','Cat_06','Cat_07','Cat_08'])
#     f_csv.writerows(result)



