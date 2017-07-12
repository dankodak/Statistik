'''
Created on 28.06.2017

@author: Gruppe 7
'''
from Cluster.Cluster2 import Cluster2
eps = [1, 1.5, 2]
delta = [0.2, 0.1, 0.06, 0.05, 0.04]
tau = [2, 4]
for i in eps:
    for j in delta:
        for k in tau:
            Cluster2('Daten/crosses-2d.csv',i,j,k,0)
