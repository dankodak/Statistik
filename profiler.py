'''
Created on 16.07.2017

@author: Daniel
'''
from Cluster.Cluster2 import Cluster2
import numpy as np
def profiler():
    name = 'bananas-1-2d'
    Name = 'Daten/' + name + '.csv'
    #einlesen der Daten
    data = np.genfromtxt(Name, delimiter = ",")

    Cluster2(name, data, 2, 0.02, 2)