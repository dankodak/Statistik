'''
Created on 07.07.2017

@author: anjaschwenk
'''
import numpy as np
import time 
from Cluster.Indikator import Indikator
from Cluster.Dichte2 import Dichte2
from Cluster.Zusammenhang4 import Zusammenhang4

def Cluster2 (name, epsilon, delta, tau):
    #name=Name des Datensatzes
    #eps=Toleranz der verbleibenden Zusammenhangskomponenten
    #delta=Radius einer Kugel
    #tau=maximaler Abstand zweier durch Streckenzug verbundener Daten in einer Zuasmmenhangskomponente
    start = time.time()
    #einlesen der Daten
    data = np.genfromtxt(name, delimiter = ",")
    #Anzahl der Daten im Datensatz data
    anzahl = np.shape(data)[0]
    #Dimension einer einzelnen Datei des Datensatzes data
    dim = np.shape(data)[1]
    #Bestimmen des Maximums der Dichtefunktion

    
    #Bestimmen welche x_i in welchen Kugeln liegen
    indikator = Indikator(data, delta, anzahl, dim)
    #Gibt die x_i soritert nach Dichte in einem Dicionary zurueck
    dichte = Dichte2(indikator)
    #Schluessel in einer Liste speichern und absteigend sortieren
    dichten = sorted(dichte.keys(), reverse = True)
    #Ueber die Dichten iterieren bis wir nur noch einen Cluster haben
    cluster ={}
    for i in dichten:
        cluster = Zusammenhang4(cluster, dichte, i, data, tau)
        #Umspeichern der Cluster in Dictionary mit Listen
        clusterAlsListe = {}
        for j in cluster:
            #Wurzel (also Clusternummer) bestimmen
            k = j
            while k != cluster[k]:
                k = cluster[k]
                #Wenn Cluster noch nicht existiert,
            if k not in clusterAlsListe.keys():
                #erstelle ihn
                clusterAlsListe[k] = [j]
            else:
                #ansonsten haenge an
                clusterAlsListe[k].append(j)
    end = time.time()
    
    print(end-start)
    return[1]