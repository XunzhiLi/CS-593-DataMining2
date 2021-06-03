#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/3/19 20:47
# @Author  : Ryu
# @Site    :
# @File    : Similarities.py
# @Software: PyCharm
import csv as cvs
import numpy as np
import pandas as pd

#read the data from Recipe.csv
csv_file = cvs.reader(open(r'Recipe.csv','r'))
X=[]

#put the data into a list
for line in csv_file:
    line = line[1:35]
    X.append(line)

#transform list into array
X = np.array(X)
X = np.delete(X,0,axis=0)

#store data of six recipes in dict
Recipe= {
        'Spag Sauce' :X[0],
        'Spag Meat Sauce':X[1],
        'Eggplant Relish':X[2],
        'Creole Sauce':X[3],
        'Salsa':X[4],
        'Enchilada Sauce':X[5]
}
#Corresponds recipes with numbers to facilitate later loops
numbers = {
    0:'Spag Sauce',
    1:'Spag Meat Sauce',
    2:'Eggplant Relish',
    3:'Creole Sauce',
    4: 'Salsa',
    5:'Enchilada Sauce'
}

#calculate Jaccard Similarity
def  Jaccard(A,B,Recipe):
    A = Recipe[A]
    B = Recipe[B]
    intersection = 0
    unions = len(A)
    for i in range(len(A)):
        if A[i]==B[i] == '1':
            intersection+=1
        if A[i]== B[i] == '0':
            unions-=1
    Jaccard_sim = intersection/unions
    print('Jaccard_sim :'+str(Jaccard_sim))


#Calculate Cosine Similarity
def cosine(A,B,Recipe):
    #because all the '1' or '0' in table is still string,Which is not good to handle .So we change each item into number
    #use int(str)
    A_new = []
    B_new = []
    for i in Recipe[A] :
        i  = int(i)
        A_new.append(i)
    for j in Recipe[B]:
        j = int(j)
        B_new.append(j)
    #This is the function to caculate cosine similarity
    dot_product = 0
    square_sum_a = 0
    square_sum_b = 0
    for i in range(len(A_new)):
        dot_product +=  A_new[i]*B_new[i]
        square_sum_a += A_new[i] * A_new[i]
        square_sum_b += B_new[i] * B_new[i]
    #calculate the cosine similarity
    cos = dot_product / (np.sqrt(square_sum_a) * np.sqrt(square_sum_b))
    print('Similarity(%s,%s) :'%(A,B))
    print('cos='+str(cos))
    print('The similarities are normalized to the interval [0,1]')
    print('cosineSIM :'+str(0.5*cos + 0.5)) #cosineSIM = 0.5cosθ + 0.5


for i in range(6):
    for j in range(i+1,6):
        cosine(numbers[i],numbers[j],Recipe)
        Jaccard(numbers[i],numbers[j],Recipe)
        print('-----------------------------------------------------')
        print('')


