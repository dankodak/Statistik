'''
Created on 03.07.2017

@author: anjaschwenk
'''
def Elimination(zusammenhang, dichteEps):
    #Initialisierung eines Dictionarys in dem Zusammenhangskomponenten nach der Elimination gespeichert werden
    Cluster={}
    #Schleife ueber Zusammenhangskomponenten
    for l in zusammenhang.keys():
        #Schleife ueber Indices der in dichtEps liegende Daten
        for i in dichteEps:
            #falls Schnitt nicht leer schreibe Zusammenhangkomponente in Cluster
            if i.contains(zusammenhang[l]):
                Cluster[l].append(zusammenhang[l])
                break
    return Cluster        
        