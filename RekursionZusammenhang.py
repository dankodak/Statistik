'''
Created on 05.07.2017

@author: anjaschwenk
'''
import numpy as np
import sys
sys.setrecursionlimit(10000)
def RekursionZusammenhang(k, cluster, data, m_rho, tau):
    #Durchgehen von m_rho
    for j in range(0,len(m_rho)):
        #Wenn m_rho[j] noch keinem Cluster zugewiesen ist und Distanz kleiner tau, dann
        if m_rho[j] == -1 and np.linalg.norm(data[j] - data[k]) <= tau and j != k:
            #weise m_rho den Cluster zu
            m_rho[j] = cluster
            #und rufe rekursiv auf
            m_rho = RekursionZusammenhang(j, cluster, data, m_rho, tau)
    return m_rho