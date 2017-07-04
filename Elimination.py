'''
Created on 03.07.2017

@author: anjaschwenk
'''
def Elimination(zusammenhang, dichteEps):
    #Initialisierung eines Dictionarys in dem Zusammenhangskomponenten nach der Elimination gespeichert werden
    Cluster={}
    counter = 0
    #Schleife ueber Zusammenhangskomponenten
    for l in zusammenhang.keys():
        #Schleife ueber Indices der in dichtEps liegende Daten
        for i in dichteEps:
            #falls Schnitt nicht leer schreibe Zusammenhangkomponente in Cluster
            if i in zusammenhang[l]:
                Cluster[counter] = zusammenhang[l]
                counter = counter + 1
                break
    return Cluster