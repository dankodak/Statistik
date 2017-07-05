'''
Created on 05.07.2017

@author: anjaschwenk
'''
import numpy as np
def RekursionZusammenhang(k, cluster, data, m_rho, tau):
    #Durchgehen von m_rho
    for j in range(k,len(m_rho)):
        #Wenn m_rho[j] noch keinem Cluster zugewiesen ist und Distanz kleiner tau, dann
        if m_rho[j] == -1 and np.linalg.norm(data[j] - data[m_rho[k]]) <= tau:
            #weise m_rho den Cluster zu
            m_rho[j] = cluster
            #und rufe rekursiv auf
            RekursionZusammenhang(k, cluster, data, m_rho, tau)
    return m_rho