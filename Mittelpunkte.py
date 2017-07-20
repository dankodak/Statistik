'''
Created on 13.07.2017

@author: Gruppe 7

@summary: Berechnung der Mittelpunkte der Kugeln

@param kugelnum: (list) Indiz7es aller Kugeln
@param delta: (float) Kugeldurchmesser
@param dim: (int) Dimension Datensatz

@return: Mittelpunkte (np.ndarray): Mittelpunkte der Kugeln
'''
import numpy as np
def Mittelpunkte(kugelnum, delta, dim):
    #Initialisierung np.ndarray
    Mittelpunkte = np.ndarray(shape = (len(kugelnum),dim))
    #alle Mittelpunkte berechnen durch Schleife ueber alle Kugelindizes
    for i in range(0,len(kugelnum)):
        for j in range(0,dim):
            Mittelpunkte[i][j] = delta/2 + delta*kugelnum[i][j]
            
    return Mittelpunkte