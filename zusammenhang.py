'''
Created on 29.06.2017

@author: anjaschwenk
'''
import numpy as np
def zusammenhang(data, m_rho, tau):
    B = {}
    k = 0 #Zusammenhangskomponentenindex
    e = 0 #Die am Anfang, die schon Null sind
    while m_rho.count(-1) != len(m_rho):
        B[k] = []
        while m_rho[e] == -1:
            e = e + 1
        B[k].append([m_rho[e]])
        m_rho[e] = -1
        j = 1 # Wahrheitswert
        t = 0 # Listenindex in der Liste B(k)
        while j == 1:
            j = 0 # Wahrheitswert
            for i in range(0, np.shape(m_rho)[0]):
                for l in B[k][t]:
                    if m_rho[i] != -1 and np.linalg.norm(data[l] - data[m_rho[i]]) <= tau:
                        if j == 0:
                            B[k].append([m_rho[i]])
                            m_rho[i] = -1
                            j = 1
                        else:
                            B[k][t+1].append(m_rho[i])
                            m_rho[i] = -1
                        break
            t = t + 1
        k = k + 1
        print(k)