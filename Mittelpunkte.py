'''
Created on 13.07.2017

@author: Daniel
'''
import numpy as np
def Mittelpunkte(kugelnum, delta, dim):
    
    Mittelpunkte = np.ndarray(shape = (len(kugelnum),dim))
    
    for i in range(0,len(kugelnum)):
        for j in range(0,dim):
            Mittelpunkte[i][j] = delta/2 + delta*kugelnum[i][j]
            
    return Mittelpunkte