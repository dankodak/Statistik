'''
Created on 07.07.2017

@author: anjaschwenk
'''
def Dichte2(indikator):
    #Initialisieren eines Dictionarys in der Schluessel= Anzahl der x_i's pro Tupel sind und Werte die zugehoerigen x_i's
    m_rho={}
    
    #Schleife ueber Indices der Kugeln
    for kugelnum in indikator.keys():
        #wenn der Schluessel noch nicht existiert dann wird ein neuer Schluessel hinzugefuegt wenn nicht wird x_i dem bereits vorhanden Schluessel angehaengt
        if len(indikator[kugelnum]) not in m_rho.keys():
            m_rho[len(indikator[kugelnum])]=indikator[kugelnum]
        else:
            m_rho[len(indikator[kugelnum])].append(indikator[kugelnum])        
    return m_rho