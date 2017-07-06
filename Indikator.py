'''
Created on 28.06.2017

@author: Gruppe 7
'''
import numpy as np
from math import floor
def Indikator (data,delta, anzahl, dim):
    #Initialisierung eines Dictionarys
    indikator={}
    #Schleife ueber den Datensatz
    for i in range(0,anzahl):
        #Kugelnum ist Index der durchnummerierten m^dim Kugeln
        kugelnum=(floor(data[i][0]/delta),floor(data[i][1]/delta))
        #Wenn in noch keine Kugel mit Index kugelnum existiert fuege kugelnum als neuen Schluessel ein mit Wert i 
        #ansonsten fuege i zu Schluessel kugelnum hinzu      
        if kugelnum not in indikator:
            indikator[kugelnum] = [i] 
        else:
            indikator[kugelnum].append(i)
    
    return indikator