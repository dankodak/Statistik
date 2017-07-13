'''
Created on 07.07.2017

@author: Gruppe 7

@summary: Berechnet zu einer gegebenen Menge an Daten die Zusammenhangskomponenten bzgl.
der gegebenen Nachbarschaftsrelation. Es wird ausgenutzt, dass durch Verringerung der
Dichte Daten, die bereits zusammenhaengend waren, weiterhin zusammenhaengen.
Gespeichert werden die Daten in einem Baum. Fuer jeden Datenpunkt wird nur ein Pointer
auf einen anderen hoeher gelegenen gespeichert. Die Wurzel des Baumes zeigt auf sich selbst
und ist Repraesentant des Clusters.


@param cluster: (Dict) Die bisherigen Cluster abgespeichert in einem Dictionary
@param dichte: (Dict) Alle Daten sortiert nach Dichte
@param betrachteteDichte: (int) Die fuer diese Iteration betrachtete Dichte
@param data: (np.ndarray) Der Datensatz
@param tau: maximaler Abstand zweier durch Streckenzug verbundener Daten in einer Zuasmmenhangskomponente

@output cluster: Gibt die Zusammenhangskomponenten für kleineres Rho zurueck
'''
import numpy as np
def Zusammenhang4(cluster, dichte, betrachteteDichte, data, tau):
    #Durchgehen aller neu hinzugefuegten x_i
    for i in dichte[betrachteteDichte]:
        #Wahrheitswert ob x_i bereits einem Baum hinzugefügt wurde
        wahrheit = 0
        #Initialisieren als neuen Cluster
        cluster[i] = i
        #Vergleichen mit allen x_i, die schon in einer Zusammenhangskomponente sind
        for j in cluster.keys():
            #Abstand berechnen:
            abstand = np.linalg.norm(data[i] - data[j], np.inf)
            #Wenn naher Datenpunkt gefunden,
            if abstand < tau and wahrheit == 0:
                #Suche die Wurzel von x_j
                k = cluster[j]
                while k != cluster[k]:
                    k = cluster[k]
                #fuege x_i der Wurzel hinzu
                cluster[i] = k
                wahrheit = 1
            elif abstand < tau and wahrheit == 1:
                #Suche die Wurzel von x_j
                k = cluster[j]
                while k != cluster[k]:
                    k = cluster[k]
                '''
                Wenn x_i einem neuen Baum hinzugefuegt wird (Wurzeln sind gleich),
                dann haenge den einen Baum an den anderen
                '''
                if k != cluster[i]:
                    cluster[cluster[i]] = k
    return cluster