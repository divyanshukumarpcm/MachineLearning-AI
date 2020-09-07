
# -*- coding: utf-8 -*-

"""
Created on Wed Apr  8 18:02:20 2020
DETECTING NEW CASES USING MACHINE LEARNING-INDIA
@author: Divyanshu kumar

REQUIRES INTERNET CONNECTION and pandas, numpy, matplotlib,math
The graph of all cases detected vs new cases is a straight line for any exponentially growing pandemic. True for covid-19 too. If we get a best fit line to represent the uneven dots, we may predict future cases.
Most importantly, this graph gives better standing of a country against th epandeic. If present dots are below the line, the day was good and if dots are forming below the line again and again, then we are doing great and flattening the curve.

Can be applied to any country. See comment to know more.
"""


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math

#function to find best fit line on graph
def gradient_dec(x1,y):
    lr=0.00000000000005 #learnign rate for slope
    #if data output says 'nan' then increase a zero before '5' in above lr.
    lr1=0.3 #learning rate for constant
    i=1000 #number of iterations
    m_curr=0 #current slope
    b_curr=0 #current constant
    n=len(x1) 
    print("|Iteration|slope|Constant|Cost|")
    for l in range(0,i):
        y_pred=m_curr*x1+b_curr
        md=-(2/n)*sum(x1*(y-y_pred))
        bd=-(2/n)*sum(y-y_pred)
        m_curr-=(lr*md)
        b_curr-=(lr1*bd)
        cost=(1/n)*sum([val**2 for val in (y-y_pred)])
        print(l,"    ",m_curr, "     ",b_curr,"  ",cost)
        if l==i-1:
            m_learnt=m_curr
            b_learnt=b_curr
    what_learnt=[m_learnt,b_learnt]
    return what_learnt

#main code
    #collecting real time raw data from covid.ourworldindata.org
data1=pd.read_csv("https://covid.ourworldindata.org/data/ecdc/total_cases.csv")
x=data1['India'] #change India with any country but adjust the learning rates
#processing data for errors - removing missed ('nan') values
for e in range(0,len(x)):
    if math.isnan(x[e]):
        x[e]=(x[e+1]+x[e-1])/2

#declaring numpy array as it has faster matrix multiplication
y=np.array([])
x1=np.array([])

#calculating daily cases. current-previous
for i in range(0,len(x)-1):
    x1=np.append(x1,[float(x[i])])        
    y=np.append(y,[float(x[i+1])-float(x[i])])

#real time graph plot
plt.figure()
plt.title("India - new cases vs previous cases- linear regression")
plt.plot(x1,y,'ro')


#ML function call
what_learnt=gradient_dec(x1,y)

#best fit line obtained and plotting it
y_for_plot=[]
for t in range(len(x1)):
    y_for_plot.append(what_learnt[0]*x1[t]+what_learnt[1])
plt.plot(x1,y_for_plot)
plt.xlabel("All cases detected to date")
plt.ylabel("New cases (daily)")
ren=len(x)-1

#predicting future :)
print("New Cases predicted=", x[ren]*what_learnt[0]+what_learnt[1], "Total predicted=",x[ren]*what_learnt[0]+what_learnt[1]+x[ren])
plt.show()
