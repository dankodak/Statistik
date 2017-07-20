'''
Created on 16.07.2017

@author: Gruppe 7
@summary: Durchlaufe einen Baum von gegebenen Index und haenge jedes durchlaufene Element an die Wurzel

@param index: (int) Der index von dem gestartet wird
@param cluster: (dict) Der Baum als Dictionary

@return: cluster (dict) Der Baum als Dictionary
'''
def BaumOrdnen(index, cluster):
    #Initialisieren der Liste der besuchten Elemente
    umordnen = []
    k = index
    #Durchlaufen des Baumes bis man bei der Wurzel ist
    while k != cluster[k]:
        #und abspeichern der Indices
        umordnen.append(k)
        k = cluster[k]
        #Alle Eltern umschreiben
    for l in umordnen:
        cluster[l] = k
        
    return cluster