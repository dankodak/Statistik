'''
Created on 13.07.2017

@author: Daniel
'''
def Dichte3(indikator, kugelnum):
    
    m_rho = {}
    for i in range(0,len(kugelnum)):
        if len(indikator[kugelnum[i]]) not in m_rho.keys():
            m_rho[len(indikator[kugelnum[i]])] = [i]
        else:
            m_rho[len(indikator[kugelnum[i]])] = m_rho[len(indikator[kugelnum[i]])] + [i]
            
    return m_rho