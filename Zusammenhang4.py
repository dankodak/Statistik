'''
Created on 07.07.2017

@author: Gruppe 7
@output: Gibt die Zusammenhangskomponenten für kleineres Rho zurueck
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
            #Wenn naher Datenpunkt gefunden,
            if np.linalg.norm(data[i] - data[j]) < tau and wahrheit == 0:
                #Suche die Wurzel von x_j
                k = cluster[j]
                while k != cluster[k]:
                    k = cluster[k]
                #fuege x_i der Wurzel hinzu
                cluster[i] = k
                wahrheit = 1
            else:
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