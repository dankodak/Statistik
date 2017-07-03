'''
Created on 28.06.2017

@author: anjaschwenk
'''
import numpy as np
from Cluster.Indikator import Indikator
from Cluster.Dichte import Dichte
from Cluster.Zusammenhang import Zusammenhang
from Cluster.Elimination import Elimination
import time
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
    tau=0.01
    rho=0.1
    eps=0.0001
    rhoeps=rho+2*eps
    #Funktionsaufruf
    indikator = Indikator(data, delta, anzahl, dim)
    m_rho = Dichte(delta, indikator, anzahl, dim, rho)
    zusammenhang = Zusammenhang(data, m_rho, tau)
    dichteEps = Dichte(data, delta, anzahl, dim, rhoeps)
    elimination = Elimination(zusammenhang, dichteEps)
    print(elimination)
    end = time.time()
    print(end - start)
    return [1]