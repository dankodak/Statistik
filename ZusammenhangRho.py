'''
Created on 06.07.2017

@author: anjaschwenk
'''
import numpy as np
from Cluster.Zusammenhang3 import Zusammenhang3
def ZusammenhangRho(data, m_rho, tau,zusammenhang):
    
    for i in range(0,len(zusammenhang)):
        if zusammenhang[i]!=0:
            m_rho[i] = zusammenhang[i]
    m_rho = Zusammenhang3(data, m_rho, tau)
    clusternummern=[]
    for i in range (0,len(m_rho)):
        if m_rho[i]  not in clusternummern:
            clusternummern.append(m_rho[i])
    for i in clusternummern:
        for j in range(0,len(m_rho)):
            if m_rho[j]==i:  
                for k in range(0,len(m_rho)):
                    if m_rho[k]!=i and np.linalg.norm(data[j] - data[k]) <= tau:
                        cluster = m_rho[k]
                        for l in range(0,len(m_rho)):
                            if m_rho[l] == cluster:
                                m_rho[l] = i
    return m_rho