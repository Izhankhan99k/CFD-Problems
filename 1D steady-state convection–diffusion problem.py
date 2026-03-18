# -*- coding: utf-8 -*-
"""
Created on Sun Jan 11 23:43:58 2026

@author: izhan
"""

import numpy as np
import matplotlib.pyplot as plt

N=51
T=np.zeros(N)
T[0]=100
T[N-1]=500   

T_new=np.zeros(N)
T_new[0]=100
T_new[N-1]=500  
                                        
L=1

h=np.float64(L/(N-1))
gamma=np.float64(0.1)
rho=np.float64(1)
u=np.float64(0.5)

pe=(rho*u*h)/gamma

epsilon=1.E-8
numerical_error=1
iterations=0
while numerical_error>epsilon:
    for i in range(1,N-1):
        a_w=gamma/h +(rho*u)/2
        a_e=gamma/h-(rho*u)/2
        a_p= a_w + a_e
        T_new[i]=(T[i-1]*a_w+T[i+1]*a_e)/a_p
        
    iterations+=1    
    numerical_error=0
    for i in range(1,N-1):
        numerical_error+=abs(T_new[i]-T[i])
    T=T_new.copy()    
  # if iterations%500==0:
        #lt.figure(20)
       #plt.semilogy(numerical_error,iterations)
      #pt.pause(0.1)
x_dom=np.arange(N)*h
plt.figure(35)
plt.plot(x_dom,T,'gx--',markersize=10)
plt.show()
