'''
Created on 06.07.2017

@author: anjaschwenk
'''
import numpy as np
from Cluster.Zusammenhang3 import Zusammenhang3
def ZusammenhangRho(data, m_rho, tau,zusammenhang):
    #Zusammenhangskomponenten von groesserem Rho uebernehmen:
    for i in range(0,len(zusammenhang)):
        if zusammenhang[i]!=0:
            m_rho[i] = zusammenhang[i]
            
    #Fuer die neu dazu gekommenen Werte die Zusammenhangskomponenten bestimmen
    m_rho = Zusammenhang3(data, m_rho, tau)
    
    #Bestimmen aller Clusternummern
    clusternummern=[]
    for i in range (0,len(m_rho)):
        if m_rho[i]  not in clusternummern:
            clusternummern.append(m_rho[i])
            
    clusternummern.remove(0)
    #Kopie von zusammenhang anlegen
    kopie = m_rho
    
    #Durchgehen aller Cluster
    for i in clusternummern:
        #Betrachten aller x_j aus Cluster i
        for j in range(0,len(m_rho)):
            if kopie[j]==i:
                #Vergleichen aller x_j aus Cluster i mit allen x_k aus Cluster ungleich i
                for k in range(0,len(m_rho)):
                    if kopie[k] > i and np.linalg.norm(data[j] - data[k]) <= tau:
                        #cluster ist der zu ueberschreibende Cluster
                        cluster = kopie[k]
                        #ueberschreiben des Clusters cluster
                        for l in range(0,len(m_rho)):
                            if kopie[l] == cluster:
                                m_rho[l] = m_rho[j]
    return m_rho