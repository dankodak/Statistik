'''
Created on 28.06.2017

@author: Gruppe 7
'''
from Cluster.Cluster2 import Cluster2
import numpy as np
import cProfile

name = 'bananas-1-2d'
Name = 'Daten/' + name + '.csv'
ordner = 'Ausgabe/' + name + '/'
#einlesen der Daten
data = np.genfromtxt(Name, delimiter = ",")
eps = [1]
delta = [0.04]
tau = [2]
#cProfile.run('Cluster2(name, data, 1, 0.02, 2)')
#Cluster2(name, data, 1, 0.04, 2)

output = np.ndarray(shape = (len(eps)*len(delta)*len(tau),4))

counter = 0
for i in eps:
        for j in delta:
            for k in tau:
                print(i, j, k)
                output[counter][0] = i
                output[counter][1] = j
                output[counter][2] = k
                output[counter][3] = Cluster2(name, data, i, j, k)
                counter += 1


np.savetxt(ordner + 'Laufzeit2.csv', output, delimiter = ',', fmt = '%1.4f')
