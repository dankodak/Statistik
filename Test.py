'''
Created on 03.07.2017

@author: Daniel
'''
import numpy as np


data = np.genfromtxt('bananas-1-2d.csv', delimiter = ",")
output = np.ndarray(shape = (10000,3))
for i in range(0,np.shape(data)[0]):
    output[i] = [1, data[i][0], data[i][1]]



np.savetxt('Ausgabe/test1.csv', output, delimiter = ',', fmt = '%1.4f')