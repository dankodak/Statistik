'''
Created on 06.07.2017

@author: anjaschwenk
'''
def DichteMax(delta, indikator, anzahl, dim): 
    dichteMax=0
    nenner = anzahl*(2**dim)*(delta**dim)
    #Schleife ueber alle Kugeln
    for kugelnum in indikator.keys():
        #Dichte einer Kugel bestimmen
        dichte = len(indikator[kugelnum])
        #groesste Kugel speichern
        if dichte > dichteMax:
            dichteMax = dichte
    #Dichte groesster Kugel berechnen
    dichteMax = dichteMax/nenner
    return dichteMax    