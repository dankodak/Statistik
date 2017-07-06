'''
Created on 06.07.2017

@author: anjaschwenk
'''
def DichteMax(delta, indikator, anzahl, dim): 
    #siehe Dichteschaetzung
    dichteMax=0
    nenner = anzahl*(2**dim)*(delta**dim)
    #Schleife ueber Indices der Kugeln
    for kugelnum in indikator.keys():
        #Anzahl der Daten pro Kugel
        dichte = len(indikator[kugelnum])
        if dichte > dichteMax:
            dichteMax = dichte
    dichteMax = dichteMax/nenner
    return dichteMax    