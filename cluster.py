'''
Created on 28.06.2017

@author: anjaschwenk
'''
import numpy as np
from Cluster.Indikator import Indikator
from Cluster.Dichte import Dichte
from Cluster.zusammenhang import zusammenhang
import time
def cluster (name, eps, delta, tau):
    start = time.time()
    data = np.genfromtxt(name, delimiter = ",")
    anzahl = np.shape(data)[0]
    dim = np.shape(data)[1]
    indikator = Indikator(data, delta, anzahl, dim)
    m_rho = Dichte(delta, indikator, anzahl, dim, 0.1)
    zusammenhang(data, m_rho, 0.01)
    end = time.time()
    print(end - start)
    return [1]