# -*- coding: utf-8 -*-
"""
Created on Thu Jan  8 20:25:17 2026

@author: izhan
"""
import numpy as np 
import matplotlib.pyplot as plt
rows =21
columns=21
T=np.zeros((rows,columns))
T[0,:]=1
T_new=np.zeros((rows,columns))
T_new[0,:]=1    
L=1
h_r=L/(rows-1)
h_c=L/(columns-1)
numerical_error=1
epsilon=1.E-8
K=0.1
a=0.001


numerical_error=1
epsilon=1.E-8
iterations=0
plt.figure(10)
while numerical_error>epsilon:
    for i in range(1,rows-1):
        for j in range(1,columns-1):
            a_e=np.float64(K*a/h_r)
            a_w=np.float64(K*a/h_c)
            a_n=np.float64(K*a/h_c)
            a_s=np.float64(K*a/h_c)
            a_p=a_e + a_w + a_n + a_s
            T_new[i][j]=(T[i][j+1]*a_e+T[i][j-1]*a_w+T[i-1][j]*a_n+T[i+1][j]*a_s)/a_p
        numerical_error=0
        for i in range(1,rows-1):
            for j in range(1,columns-1):
                numerical_error+=abs(T_new[i][j]-T[i][j])
      
    iterations+=1  
    T=T_new.copy() 
    
x_dom=np.arange(rows)*h_r
y_dom=L-np.arange(columns)*h_c
[X,Y]=np.meshgrid(x_dom,y_dom)

plt.figure(11)
plt.contourf(X,Y,T,12)     
plt.grid(True,color='k')
plt.title('T(x,y)')
plt.show()