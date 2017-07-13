'''
Created on 28.06.2017

@author: Gruppe 7

@summary: Unterteilt den Datensatz in Kugeln in Unendlich-Norm mit Radius Delta
und bestimmt wie viele Daten in jeder Kugel enthalten sind.

Eingabe:
@param data: (np.ndarray) Der Datensatz
@param delta: (int) Radius einer Kugel
@param anzahl: (int) Die Anzahl aller Elemente
@param dim: (int) Dimension des Datensatzes

@return indikator: (Dict) Die Anzahl der Elemente in den einzelnen Kugeln
'''
import numpy as np
from Cluster.Kugelnum import Kugelnum
def Indikator (data,delta, anzahl, dim):
    #Initialisierung eines Dictionarys
    indikator={}
    #Schleife ueber den Datensatz
    for i in range(0,anzahl):
        #Kugelnum ist Index der durchnummerierten m^dim Kugeln
        #kugelnum=(floor(data[i][0]/delta),floor(data[i][1]/delta))
        kugelnum = Kugelnum(data[i],delta, dim)
        #Wenn in noch keine Kugel mit Index kugelnum existiert fuege kugelnum als neuen Schluessel ein mit Wert i 
        #ansonsten fuege i zu Schluessel kugelnum hinzu      
        if kugelnum not in indikator:
            indikator[kugelnum] = [i] 
        else:
            indikator[kugelnum].append(i)
    
    return indikator