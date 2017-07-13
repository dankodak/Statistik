'''
Created on 13.07.2017

@author: Daniel
'''
from math import floor
def Kugelnum(date, delta, dim):
    kugelnummer = []
    for i in range(0, dim):
        kugelnummer.append(floor(date[i]/delta))
        
    kugelnum = tuple(kugelnummer)
    return kugelnum