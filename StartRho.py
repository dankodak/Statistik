'''
Created on 06.07.2017

@author: anjaschwenk
'''
def StartRho(dichteMax,delta,anzahl,dim):
    k = 0
    #Groesstes k bestimmen, fuer welches Rho kleiner ist als die maximale Dichte
    while dichteMax-k/(anzahl*(delta**dim)) > 0:
        k=k+1
    return k-1    