'''
Created on 28.06.2017

@author: Gruppe 7
'''
from Cluster.Cluster2 import Cluster2
Cluster2('bananas-1-4d', 2, 0.5,2)
'''
eps = [1, 1.5, 2]
delta = [0.2, 0.1, 0.06, 0.05, 0.04]
tau = [2, 4]
for i in eps:
    for j in delta:
        for k in tau:
            Cluster2('bananas-5-2d',i,j,k)
#0.07, 0.035, 0.14
'''