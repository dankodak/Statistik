'''
Created on 28.06.2017

@author: Gruppe 7
'''
import numpy as np
from Cluster.Indikator import Indikator
from Cluster.DichteMax import DichteMax
from Cluster.StartRho import StartRho
from Cluster.Dichte import Dichte
from Cluster.Zusammenhang3 import Zusammenhang3
from Cluster.Elimination2 import Elimination2
from Cluster.ZusammenhangRho import ZusammenhangRho
import time
from math import sqrt
def cluster (name, epsilon, delta, tau):
    #name=Name des Datensatzes
    #eps=Toleranz der verbleibenden Zusammenhangskomponenten
    #delta=Radius einer Kugel
    #tau=maximaler Abstand zweier durch Streckenzug verbundener Daten in einer Zuasmmenhangskomponente
    start = time.time()
    #einlesen der Daten
    data = np.genfromtxt(name, delimiter = ",")
    #Anzahl der Daten im Datensatz data
    anzahl = np.shape(data)[0]
    #Dimension einer einzelnen Datei des Datensatzes data
    dim = np.shape(data)[1]
    #Bestimmen des Maximums der Dichtefunktion

    
    #Erster Aufruf aller Funktionen
    indikator = Indikator(data, delta, anzahl, dim)
    dichteMax = DichteMax(delta, indikator, anzahl, dim)
    eps = epsilon*sqrt(abs(dichteMax/(anzahl*delta**dim)))
    #Bestimmen des naechstens Rhos in der Form der Rhos in der Aufgabenstellung
    k = StartRho(dichteMax,delta,anzahl,dim)
    rho = k/(anzahl*delta**dim)
    rhoeps = rho+2*eps
    m_rho = Dichte(delta, indikator, anzahl, dim, rho)
    zusammenhang = Zusammenhang3(data, m_rho, tau)
    k = k - 1
    
    while k> 0 :
        print(k)
        print(zusammenhang)
        #Neues Rho bestimmen
        rho = k/(anzahl*delta**dim)
        rhoeps = rho + 2*eps
        #Neues m_rho bestimmen
        m_rho = Dichte(delta,indikator,anzahl,dim,rho)
        #Neue Zusammenhangskomponenten berechnet
        zusammenhangNeu = ZusammenhangRho(data, m_rho, tau,zusammenhang)
        #Pruefung fuer Clusterzahlvergleich
        dichteEps = Dichte(delta, indikator, anzahl, dim, rhoeps)
        elimination = Elimination2(zusammenhang, dichteEps)
        
        if len(elimination.keys()) > 1:
            zusammenhang = zusammenhangNeu
        else:
            break
        k = k - 1
   
    

    
    #Bestimmen der Gesamtzahl der Elemente
    zaehler = 0
    for i in elimination.keys():
        zaehler = zaehler + len(elimination[i])
    #Array Groesse noch falsch
    output = np.ndarray(shape = (zaehler,dim + 1))
    
    #Schreiben der Cluster in die output Daten
    counter = 0
    for i in elimination.keys():
        for j in range(0,len(elimination[i])):
            output[counter] = [i, data[elimination[i][j]][0], data[elimination[i][j]][1]]
            counter = counter + 1
    
    #Cluster in Datei speichern
    np.savetxt('test1.csv', output, delimiter = ',', fmt = '%1.4f')
    

    end = time.time()
    print(end - start)
    return [1]