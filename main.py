'''
Created on 28.06.2017

@author: Gruppe 7
'''
from Cluster.Cluster2 import Cluster2
import numpy as np
import cProfile

name = 'svmguide1'
Name = 'Daten/' + name + '.csv'
#ordner = 'Ausgabe/' + name + '/genauer/'
#ordner = 'Ausgabe/' + name + '/test/'
ordner = 'Ausgabe/' + name + '/genauer/'
#einlesen der Daten
data = np.genfromtxt(Name, delimiter = ",")
eps = [0.1]
delta = [0.04]
tau = [2,4]
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

'''
namen = ['cod-rna.5000', 'cycle-power-plant', 'svmguide1']
Namen = ['Daten/cod-rna.5000.csv', 'Daten/cycle-power-plant.csv', 'Daten/svmguide1.csv']
Ordner = ['Ausgabe/cod-rna.5000/genauer/', 'Ausgabe/cycle-power-plant/genauer/', 'Ausgabe/svmguide1/genauer/']


eps = np.linspace(0, 1, 11)
delta = np.linspace(0.01, 0.1, 10)


output = np.ndarray(shape = (len(eps)*len(delta)*len(tau),4))
counter = 0
for l in range(0,4):
    counter = 0
    data = np.genfromtxt(Namen[l], delimiter = ",")
    for i in eps:
        for j in delta:
            for k in tau:
                print(i, j, k)
                output[counter][0] = i
                output[counter][1] = j
                output[counter][2] = k
                output[counter][3] = Cluster2(namen[l], data, i, j, k)
                counter += 1
#0.07, 0.035, 0.14
    np.savetxt(Ordner[l] + 'Laufzeit2.csv', output, delimiter = ',', fmt = '%1.4f')
'''