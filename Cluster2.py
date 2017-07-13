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
from Cluster.Dichte3 import Dichte3
from Cluster.Zusammenhang4 import Zusammenhang4
from math import floor, sqrt
from Cluster.Elimination3 import Elimination3
from Cluster.Mittelpunkte import Mittelpunkte
from Cluster.Kugelnum import Kugelnum

def Cluster2 (name, epsilon, delta, Tau):
    #Zeitmessung starten
    start = time.time()
    Name = 'Daten/' + name + '.csv'
    #einlesen der Daten
    data = np.genfromtxt(Name, delimiter = ",")
    #Anzahl der Daten im Datensatz data
    anzahl = np.shape(data)[0]
    #Dimension einer einzelnen Datei des Datensatzes data
    dim = np.shape(data)[1]
    #tau berechnen
    tau = Tau*delta
    #Bestimmen welche x_i in welchen Kugeln liegen
    indikator = Indikator(data, delta, anzahl, dim)
    kugelnum = list(indikator.keys())
    #Gibt die Mittelpunkte aller verwendeter Kugeln zurück mit
    #mittelpunkte[i] entspricht kugelnum[i]
    mittelpunkte = Mittelpunkte(kugelnum, delta, dim)
    #Gibt die x_i soritert nach Dichte in einem Dicionary zurueck
    dichte = Dichte3(indikator, kugelnum)
    #Schluessel in einer Liste speichern und absteigend sortieren
    dichten = sorted(dichte.keys(), reverse = True)
    #Berechnen des Epsilons fuer die Elimination
    nenner = (anzahl*(2**dim)*(delta**dim))
    maxDichte = dichten[0]/nenner
    eps = sqrt(maxDichte/(anzahl*(delta**dim)))
    
    #Ueber die Dichten iterieren bis wir nur noch einen Cluster haben
    cluster = {}
    elimination = {}
    #Anzahl Zusammenhangskomponenten
    amountElimination = []
    #Zaehlt in welcher Dichteiteration wir sind
    zaehler = 0
    for i in dichten:
        cluster = Zusammenhang4(cluster, dichte, i, mittelpunkte, tau)
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
        #Elimination durchführen und alle Schritte abspeichern
        elimination[zaehler] = Elimination3(dichte, dichteeps, clusterAlsListe)
        #Schreibt die Anzahl der Zusammenhangskomponenten in einer Liste
        amountElimination.append(len(elimination[zaehler]))
        zaehler = zaehler + 1
        
    #Bestimmen des Rhos, bei dem erstmals, von unten gesehen, mehr als eine Zusammenhangskomponente entsteht
    index = len(amountElimination) - 1
    while amountElimination[index] == 1:
        index = index - 1
        
    #und diese Zusammenhangskomponente abspeichern
    finalElimination = elimination[index]
    
    DatenCluster = {}
    for i in finalElimination:
        DatenCluster[i] = []
        for j in finalElimination[i]:
            index = Kugelnum(mittelpunkte[j], delta, dim)
            DatenCluster[i] = DatenCluster[i] + indikator[index]
    #Bestimmen der Gesamtzahl der Elemente
    zaehler = 0
    for i in DatenCluster.keys():
        zaehler = zaehler + len(DatenCluster[i])
        
    #Output-Array anlegen
    output = np.ndarray(shape = (zaehler,dim + 1))
    
    #Schreiben der Cluster in die output Daten
    counter = 0
    for i in DatenCluster.keys():
        #Zeile
        for j in range(0,len(DatenCluster[i])):
            #Spalte
            for k in range(0,dim+1):
                if k == 0:
                    output[counter][k] = i
                elif k == dim:
                    output[counter][k] = data[DatenCluster[i][j]][k-1]
                    counter = counter + 1
                else:
                    output[counter][k] = data[DatenCluster[i][j]][k-1]
    #Cluster in Datei speichern
    
    ordner = 'Ausgabe/' + name + '/'
    deltas = str(delta)
    deltas = deltas.replace('.', ',')
    epsilons = str(epsilon)
    epsilons = epsilons.replace('.', ',')
    taus = str(Tau)
    np.savetxt(ordner + epsilons + '-' + deltas + '-' + taus + '.csv', output, delimiter = ',', fmt = '%1.4f')
    end = time.time()
    print(end - start)
    return[1]