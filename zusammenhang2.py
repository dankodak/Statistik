'''
Created on 30.06.2017

@author: anjaschwenk
'''
import numpy as np
def zusammenhang2(data, m_rho, tau):
    anzahl = np.shape(data)[0]
    adjazenz={}
    for i in range(0,anzahl):
        adjazenz[i]=[]
        for j in range(i+1,anzahl):
            if np.linalg.norm(data[i] - data[j]) <= tau:
                adjazenz[i].append(j)
        print(i)        
    for k in range(0,anzahl):
        for i in range(0,anzahl):
            for j in range(i+1,anzahl):
                if j not in adjazenz[i]:
                    if k in adjazenz[i] and j in adjazenz[k]:
                        adjazenz[i].append(j); 
                    
        print(k)                