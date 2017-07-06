'''
Created on 06.07.2017

@author: Gruppe 7
'''
def Elimination2(zusammenhang, dichteEps):
    '''
    Initialisierung eines Dictionaries in der als Schluessel Clusternummer und 
    als Wert die zugehoerigen Daten gespeichert werden
    '''
    elimination = {}
    # Schleife ueber jedes Element in dichteEps
    for i in range(0, len(dichteEps)):
        # wenn Datenelement in dichetEps liegt, speicher in Cluster die Clusternummer ein
        if dichteEps[i] == -1:
            cluster = zusammenhang[i]
            # wenn Clusternummer noch kein Schluessel in elimination ist, wird dieser zu einem neuen Schluessel
            if cluster not in elimination.keys():
                elimination[cluster] = []
                # Schleife ueber Daten
                for j in range(0,len(zusammenhang)):
                    '''
                    wenn Datenelement j im Cluster cluster ist, 
                    dann fuege Datenelement j zum Dic mit Schluessel cluster hinzu
                    '''
                    if zusammenhang[j] == cluster:
                        elimination[cluster].append(j)
    return elimination