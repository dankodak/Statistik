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
import time
from Cluster import ZusammenhangRho
def cluster (name, eps, delta, tau):
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
    tau = 0.01
    rho = 0.1
    eps = 0.45
    rhoeps = rho+2*eps
    M = 0
    
    #Funktionsaufruf
    indikator = Indikator(data, delta, anzahl, dim)
    dichteMax = DichteMax(delta, indikator, anzahl, dim)
    k = StartRho(dichteMax,delta,anzahl,dim)
    rho = k/(anzahl*delta**dim)
    m_rho = Dichte(delta, indikator, anzahl, dim, rho)
    zusammenhang = Zusammenhang3(data, m_rho, tau)
    k = k - 1
    while k> 0 :
        rho = k/(anzahl*delta**dim)
        m_rho = Dichte(delta,indikator,anzahl,dim,rho)
        zusammenhangNeu = ZusammenhangRho(data, m_rho, tau,zusammenhang)
        #Pruefung für Clusterzahlvergleich
        j = 0
        #Falls bool= 0 am ende dann existiert eine Zusammenhangskomponente ansonsten mehrere, also muss Algorithmus fortgesetzt werden
        bool=0
        for i in range(0,len(zusammenhang)):
            if zusammenhangNeu[i] != 0:
                if j == 0:
                    j = zusammenhangNeu[i] 
                elif j != zusammenhangNeu[i]:
                    bool = 1
                    break
        if bool ==1:
            zusammenhang = zusammenhangNeu
        else:
            break
        k = k - 1
   
    
    dichteEps = Dichte(delta, indikator, anzahl, dim, rhoeps)
    elimination = Elimination2(zusammenhang, dichteEps)
    
    #Array Groesse noch falsch
    output = np.ndarray(shape = (10000,3))
    
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