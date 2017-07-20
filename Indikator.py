'''
Created on 28.06.2017

@author: Gruppe 7

@summary: Unterteilt den Datensatz in Kugeln in Unendlich-Norm mit Durchmesser Delta
und bestimmt wie viele Daten in jeder Kugel enthalten sind.

Eingabe:
@param data: (np.ndarray) Der Datensatz
@param delta: (float) Durchmesser einer Kugel
@param anzahl: (int) Die Anzahl aller Elemente
@param dim: (int) Dimension des Datensatzes

@return indikator: (Dict) Elemente in den einzelnen Kugeln, Schluessel=kugelnum, Wert=Elemente i
'''
import numpy as np
from Cluster.Kugelnum import Kugelnum
def Indikator (data,delta, anzahl, dim):
    #Initialisierung eines Dictionarys
    indikator={}
    #Schleife ueber den Datensatz
    for i in range(0,anzahl):
        #Kugelnum ist Index der durchnummerierten m^dim Kugeln
        kugelnum = Kugelnum(data[i],delta, dim)
        '''
        Wenn noch keine Kugel mit Index kugelnum existiert fuege kugelnum als neuen Schluessel ein mit Wert i 
        ansonsten fuege i zu Schluessel kugelnum hinzu  
        '''    
        if kugelnum not in indikator:
            indikator[kugelnum] = [i] 
        else:
            indikator[kugelnum].append(i)
    return indikator