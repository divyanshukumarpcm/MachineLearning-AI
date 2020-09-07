# -*- cding: utf-8 -*-
"""
Created on Wed Apr  8 17:35:57 2020

@author: Divyanshu kumar
"""
import numpy as np
x=np.array([92,56,88,70,80,49,65,35,66,67])
y=np.array([98,68,81,80,83,52,66,30,68,73])
x=np.sort(x)
y=np.sort(y)
import matplotlib.pyplot as plt
plt.plot(x,y,'ro')
a=[]
b=[]
for i in range(0,100):
    a.append(i)
    b.append(a[i]*1.0178+1.9167)
plt.plot(a,b)