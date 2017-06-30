'''
Created on 29.06.2017

@author: anjaschwenk
'''
def Dichte(delta, indikator, anzahl, dim, rho):
    m_rho = []
    nenner = anzahl*(2**dim)*(delta**dim)
    for kugelnum in indikator.keys():
        dichte = len(indikator[kugelnum])/nenner
        if dichte >= rho:
            m_rho = m_rho + indikator[kugelnum]
    return m_rho