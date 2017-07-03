'''
Created on 28.06.2017

@author: anjaschwenk
'''
import numpy as np
from math import floor
def Indikator (data,delta, anzahl, dim):
    #m^dim maximale Anzahl der Kugeln
    m = 1/delta
    #Initialisierung eines Dictionarys
    indikator={}
    #Schleife ueber den Datensatz
    for i in range(0,anzahl):
        #Kugelnum ist Index der durchnummerierten m^dim Kugeln
        kugelnum = 0
        #Schleife ueber Dimension der Daten 
        for k in range(0,dim):
            #Bestimmen in welcher Kugel die Datei i liegt
            kugelnum = kugelnum + floor(data[i,k]/delta)*m**(k)
        #Wenn in noch keine Kugel mit Index kugelnum existiert fuege kugelnum als neuen Schluessel ein mit Wert i 
        #ansonsten fuege i zu Schluessel kugelnum hinzu      
        if kugelnum not in indikator:
            indikator[kugelnum] = [i] 
        else:
            indikator[kugelnum].append(i)
    
    return indikator