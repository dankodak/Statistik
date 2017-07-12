'''
Created on 11.07.2017

@author: Daniel
'''
import numpy as np
import matplotlib.pyplot as plt

def Plots(elimination, dim, data):
    for a in elimination.keys():
        counter = 0
        output = np.ndarray(shape = (len(elimination[a]),dim + 1))
        for i in elimination[a].keys():
        #Zeile
            for j in range(0,len(elimination[a][i])):
                #Spalte
                for k in range(0,dim+1):
                    if k == 0:
                        output[counter][k] = i
                    elif k == dim:
                        output[counter][k] = data[elimination[a][i][j]][k-1]
                        counter = counter + 1
                    else:
                        output[counter][k] = data[elimination[a][i][j]][k-1]
        output = np.transpose(output)
        x = output[1]
        y = output[2]
        color = output[0]
        
        plt.scatter(x, y, s=0.07, c=color)
    return 0