'''
Created on 13.07.2017

@author: Gruppe 7

@summary: Gibt fuer gegebenen Datenpunkt die Kugelnummer zurueck

@param date: (np.ndarray) Datenpunkt
@param delta: (float) Kugeldurchmesser
@param dim: (int) Dimension Datensatz

@return: kugelnum: (tuple) Kugelnummer fuer Datenpunkt
'''
from math import floor
def Kugelnum(date, delta, dim):
    #Initialisierung Liste
    kugelnummer = []
    #Obergrenze fuer kugelnummer, so dass wir im [-1,1]^dim bleiben
    Obergrenze = 1/delta
    #Jeder Eintrag des Datenpunktes wird betrachtet
    for i in range(0, dim):
        #kugelnummereintrag berechnen
        num = floor(date[i]/delta)
        '''
        Wenn Obergrenze erreicht wird, reduziere kugelnummer um 1, 
        sonst lassen
        '''
        if num == Obergrenze:
            kugelnummer.append(num - 1)
        else:
            kugelnummer.append(num)
    #Einspeichern als Tuple   
    kugelnum = tuple(kugelnummer)
    return kugelnum