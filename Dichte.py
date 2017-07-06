'''
Created on 29.06.2017

@author: Gruppe 7
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
            
    #Wenn k-ter Eintrag von ausgabe = -1 ist, dann ist x_k in m_rho
    ausgabe = []
    for k in range(0,anzahl):
        if k in m_rho:
            ausgabe.append(-1)
        else:
            ausgabe.append(0)
    return ausgabe