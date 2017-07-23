'''
Created on 11.07.2017

@author: Daniel
'''
import numpy as np
import matplotlib.pyplot as plt
from Cluster.Kugelnum import Kugelnum

def Plots(elimination, dim, data, delta, indikator, mittelpunkte):
    
    DatenCluster = {}
    for k in elimination:
        DatenCluster[k] = {}
        for i in elimination[k]:
            DatenCluster[k][i] = []
            for j in elimination[k][i]:
                index = Kugelnum(mittelpunkte[j], delta, dim)
                DatenCluster[k][i] = DatenCluster[k][i] + indikator[index]
    
    zaehler = 1
    for a in DatenCluster:
        counter = 0
        laenge = 0
        for l in DatenCluster[a]:
            laenge += len(DatenCluster[a][l])
        output = np.ndarray(shape = (laenge,dim + 1))
        for i in DatenCluster[a].keys():
        #Zeile
            for j in range(0,len(DatenCluster[a][i])):
                #Spalte
                for k in range(0,dim+1):
                    if k == 0:
                        output[counter][k] = i
                    elif k == dim:
                        output[counter][k] = data[DatenCluster[a][i][j]][k-1]
                        counter = counter + 1
                    else:
                        output[counter][k] = data[DatenCluster[a][i][j]][k-1]
        output = np.transpose(output)
        x = output[1]
        y = output[2]
        color = output[0]
        
        #plt.subplot(len(DatenCluster),1,zaehler)
        plt.scatter(x, y, s=0.07, c=color)
        zaehler += 1
        plt.show()
    return 0