'''
Created on 07.07.2017

@author: Gruppe 7

@summary: Fuehrt eine Cluster-Analyse basierend auf dem Histogramm Verfahren durch. Zunaechst wird der Datensatz
in Unendlich-Norm-Kugeln zerlegt. In diesen wird die Dichte bestimmt (Indikator) und dann nur noch die Menge
der x_i betrachtet, die dichter als ein bestimmtes Rho sind (Dichte2). Von diesen Daten werden dann die 
Zusammenhangskomponenten bestimmt (Zusammenhang4). Nachdem wir kleine Zusammenhangskomponenten eliminiert
haben (Elimination3), suchen wir das kleinste Rho fuer das erstmalig mehr als eine Zusammenhangskomponente
existiert. Diese Cluster werden dann in einer Datei abgespeichert.

Eingabe:
@param name: (String) Name des Datensatzes
@param epsilon: (int) Toleranz der verbleibenden Zusammenhangskomponenten
@param delta: (int) Radius einer Kugel
@param tau: (int) maximaler Abstand zweier durch Streckenzug verbundener Daten in einer Zuasmmenhangskomponente

@return: Cluster in Datei gespeichert
'''
import numpy as np
import time 
from Cluster.Indikator import Indikator
from Cluster.Dichte2 import Dichte2
from Cluster.Zusammenhang4 import Zusammenhang4
from math import floor, sqrt
from Cluster.Elimination3 import Elimination3

def Cluster2 (name, epsilon, delta, Tau):
    #Zeitmessung starten
    start = time.time()
    #einlesen der Daten
    data = np.genfromtxt(name, delimiter = ",")
    #Anzahl der Daten im Datensatz data
    anzahl = np.shape(data)[0]
    #Dimension einer einzelnen Datei des Datensatzes data
    dim = np.shape(data)[1]
    #tau berechnen
    tau = Tau*delta
    #Bestimmen welche x_i in welchen Kugeln liegen
    indikator = Indikator(data, delta, anzahl, dim)
    #Gibt die x_i soritert nach Dichte in einem Dicionary zurueck
    dichte = Dichte2(indikator)
    #Schluessel in einer Liste speichern und absteigend sortieren
    dichten = sorted(dichte.keys(), reverse = True)
    #Berechnen des Epsilons fuer die Elimination
    nenner = (anzahl*(2**dim)*(delta**dim))
    maxDichte = dichten[0]/nenner
    eps = sqrt(maxDichte/(anzahl*(delta**dim)))
    
    #Ueber die Dichten iterieren bis wir nur noch einen Cluster haben
    cluster = {}
    elimination = {}
    amountElimination = []
    zaehler = 0
    for i in dichten:
        print(i)
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
                
        #Berechnen des aktuellen Rhos und des Rhos zum löschen
        rho = i/nenner
        rhoeps = rho + 2*eps
        dichteeps = floor(rhoeps * nenner)
        print('Dichteeps' , dichteeps)
        #Elimination durchführen und alle Schritte abspeichern
        elimination[zaehler] = Elimination3(dichte, dichteeps, clusterAlsListe)
        amountElimination.append(len(elimination[zaehler]))
        zaehler = zaehler + 1
        
    #Bestimmen des Rhos, bei dem erstmals, von unten gesehen, mehr als eine Zusammenhangskomponente entsteht
    index = len(amountElimination) - 1
    while amountElimination[index] == 1:
        index = index - 1
        
    #und diese Zusammenhangskomponente abspeichern
    finalElimination = elimination[index]
        
    #Bestimmen der Gesamtzahl der Elemente
    zaehler = 0
    for i in finalElimination.keys():
        zaehler = zaehler + len(finalElimination[i])
        
    output = np.ndarray(shape = (zaehler,dim + 1))
    
    #Schreiben der Cluster in die output Daten
    counter = 0
    for i in finalElimination.keys():
        for j in range(0,len(finalElimination[i])):
            output[counter] = [i, data[finalElimination[i][j]][0], data[finalElimination[i][j]][1]]
            counter = counter + 1
    
    #Cluster in Datei speichern
    np.savetxt('Ausgabe/1,5-0,05-2.csv', output, delimiter = ',', fmt = '%1.4f')
    end = time.time()
    
    print(end-start)
    return[1]