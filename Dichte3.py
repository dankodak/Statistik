'''
Created on 13.07.2017

@author: Gruppe 7

@summary: Befuellen eines Dictionaries mit Anzahl Datenpunkte als Schluessel 
        und Indizes der Datenpunkte als Wert
        
@param indikator: (dict) Elemente in den einzelnen Kugeln, Schluessel=kugelnum, Wert=Elemente i
@param kugelnum: (list) Kugelnummern       

@return: m_rho (dict): Schluessel:Anzahl der Datenpunkte in einer Kugel, Werte:Indizes der Datenpunkte
'''
def Dichte3(indikator, kugelnum):
    #Initialisierung des Dict
    m_rho = {}
    #Schleife ueber alle Kugelnummern
    for i in range(0,len(kugelnum)):
        #Wenn Anzahl der Datenpunkte in einer Kugel noch nicht als Schluessel existiert, fuege ihn hinzu
        #und speichere Datenpunkt ab
        if len(indikator[kugelnum[i]]) not in m_rho:
            m_rho[len(indikator[kugelnum[i]])] = [i]
        #Ansonsten speichere einfach ab
        else:
            m_rho[len(indikator[kugelnum[i]])] = m_rho[len(indikator[kugelnum[i]])] + [i]
            
    return m_rho