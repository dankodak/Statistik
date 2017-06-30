'''
Created on 28.06.2017

@author: anjaschwenk
'''
import numpy as np
from math import floor
def Indikator (data,delta, anzahl, dim):
    m = 1/delta
    indikator={}
    for i in range(0,anzahl):
        kugelnum = 0
        for k in range(0,dim):
            kugelnum = kugelnum + floor(data[i,k]/delta)*m**(k)
        if kugelnum not in indikator:
            indikator[kugelnum] = [i] 
        else:
            indikator[kugelnum].append(i)
    
    return indikator