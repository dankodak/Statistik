'''
Created on 16.07.2017

@author: Daniel
'''
def BaumOrdnen(index, cluster):
    umordnen = []
    k = index
    while k != cluster[k]:
        umordnen.append(k)
        k = cluster[k]
    for l in umordnen:
        cluster[l] = k
        
    return cluster