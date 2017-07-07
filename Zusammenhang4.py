'''
Created on 07.07.2017

@author: anjaschwenk
'''
import numpy as np
def Zusammenhang4(cluster, dichte, betrachteteDichte, data, tau):
    for i in dichte[betrachteteDichte]:
        for j in cluster.keys():
            if np.linalg.norm(data[i] - data[j]) < tau:
                cluster[i] = j