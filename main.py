'''
Created on 28.06.2017

@author: Gruppe 7
'''
from Cluster.Cluster2 import Cluster2
import numpy as np
import cProfile


name = 'toy-10d'
Name = 'Daten/' + name + '.csv'
#einlesen der Daten
data = np.genfromtxt(Name, delimiter = ",")

#cProfile.run('Cluster2(name, data, 1, 0.01, 2)')
#Cluster2(name, data, 1, 0.04, 2)

eps = [1, 1.5, 2]
delta = [0.2, 0.1, 0.06, 0.05, 0.04]
tau = [2, 4]

eps = np.linspace(0, 2, 21)
delta = np.linspace(0.01, 0.3, 30)
for i in eps:
    for j in delta:
        for k in tau:
            print(i, j, k)
            Cluster2(name, data, i, j, k)
#0.07, 0.035, 0.14
