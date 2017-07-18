'''
Created on 07.07.2017

@author: Gruppe 7

@summary: Eliminiert kleine Zusammenhangskomponenten


@param dichte: (Dict) Alle Daten sortiert nach Dichte
@param dichteeps: (int) Die Dichte, ab der eliminiert werden muss
@param cluster: (Dict) Die Cluster

@return ausgabe: Die Cluster mit kleinen Zusammenhangskomponenten eliminiert
'''
def Elimination3(dichte, dichteeps, cluster):
    #Variablen anlegen
    ausgabe = {}
    liste = []
    counter = 1
    
    #Die Cluster mit Dichte groesser als dichteeps in eine Liste speichern
    for i in dichte:
        if i >= dichteeps:
            liste = liste + dichte[i]
            
    #Falls ein Element im Schnitt der Liste und eines Clusters ist, dann speichere den Cluster in der Ausgabe
    for i in cluster:
        for j in liste:
            if j in cluster[i]:
                ausgabe[counter] = cluster[i]
                counter = counter + 1
                break
            
    return ausgabe