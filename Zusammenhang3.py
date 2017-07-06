'''
Created on 05.07.2017

@author: Gruppe 7
'''
from Cluster.RekursionZusammenhang import RekursionZusammenhang

def Zusammenhang3(data, m_rho, tau):
    #Cluster Index
    cluster = 1
    #Durch ganz m_rho laufen und auf jeder Zusammenhangskomponente rekursiv RekursionZusammenhang aufrufen
    for k in range(0,len(m_rho)):
        #Wenn x_k in m_rho ist und noch keinem Cluster zugewiesen, dann rufe Rekursion auf
        if m_rho[k] == -1:
            m_rho[k] = cluster
            m_rho = RekursionZusammenhang(k, cluster, data, m_rho, tau)
            cluster = cluster + 1
    print(m_rho)
    
    '''    
    ausgabe = {}
    for i in range(0,cluster):
        ausgabe[i] = []
        for j in range(0,len(m_rho)):
            if m_rho[j] == i+1:
                ausgabe[i].append(j)
    '''
    return m_rho