'''
Created on 29.06.2017

@author: Gruppe 7
'''
import numpy as np
def Zusammenhang(data, m_rho, tau):
    #Initialisierung eines Dictionarys in welchem die Zusammenhangskompnonenten gespeichert werden
    B = {}
    #Zusammenhangskomponentenindex k
    k = 0
    #Index der Liste m_rho
    e = 0
    #solange in m_rho Indix der Daten ungleich -1 existieren
    while m_rho.count(-1) != len(m_rho):
        #Initialisierung der Liste der Datenindices zur Zusammenhangskomponente k bzw Schluessel k
        B[k] = []
        #ueberpruefen ob aktueller Listeneintrag an der Stelle e schon auf -1 ist falls ja zaehle solange hoch bis Eintrag ungleich -1 ist
        while m_rho[e] == -1:
            e = e + 1
        #speicher erstes e in den Anfang der Zusammenhangskompnonentenliste B[k]    
        B[k].append([m_rho[e]])
        #wurde e der Liste als Wert hinzugefuegt setze den Listeneintrag in m_rho auf -1
        m_rho[e] = -1
        # Listenindex in der Liste B(k)
        t = 0 
        # Wahrheitswert j: solange eine Datei der Zusammenhangskomponente hinzugefuegt wurde wird Algorithmus fortgesetzt
        j = 1
        while j == 1:
            j = 0
            #Schleife ueber m_rho 
            for i in range(0, np.shape(m_rho)[0]):
                #Schleife ueber Liste in der Liste B[k]
                for l in B[k][t]:
                    #pruefe ob Listeneintrag ungleich -1 ist und der Abstand von x_l zu x_i kleiner tau 
                    #falls ja fuege den Listeneintrag i in die Zusammenhangskomponente B[k][t] hinzu
                    if m_rho[i] != -1 and np.linalg.norm(data[l] - data[m_rho[i]]) <= tau:
                        #wenn B[k][t] noch nicht existiert erzeuge eine neue Liste ansonsten fuege i hinzu
                        if j == 0:
                            B[k].append([m_rho[i]])
                            m_rho[i] = -1
                            j = 1
                            break
                        else:
                            B[k][t+1].append(m_rho[i])
                            m_rho[i] = -1
                            break
            t = t + 1
        k = k + 1
        print(k)
    C = {}
    a = 0
    #Die Unterlisten entfernen
    #Funktioniert, ist aber schlecht, umschreiben mit + Variante
    for i in B.keys():
        C[a] = []
        for j in range(0,len(B[i])):
            for k in range(0,len(B[i][j])):
                C[a].append(B[i][j][k])
        a = a + 1
    return C    