'''
Created on 29.06.2017

@author: anjaschwenk
'''
def Dichte(delta, indikator, anzahl, dim, rho):
    #Inizialisierung einer Liste 
    m_rho = []
    #siehe Dichteschaetzung
    nenner = anzahl*(2**dim)*(delta**dim)
    #Schleife ueber Indices der Kugeln
    for kugelnum in indikator.keys():
        #Anzahl der Daten pro Kugel/Nenner
        dichte = len(indikator[kugelnum])/nenner
        #wenn dichte groesser als rho dann fuege Indices i der Daten welche in kugelnum liegen der Liste m_rho hinzu
        if dichte >= rho:
            m_rho = m_rho + indikator[kugelnum]
    return m_rho