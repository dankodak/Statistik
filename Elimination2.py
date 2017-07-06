'''
Created on 06.07.2017

@author: Daniel
'''
def Elimination2(zusammenhang, dichteEps):
    elimination = {}
    for i in range(0, len(dichteEps)):
        if dichteEps(i) == -1:
            cluster = zusammenhang(i)
            if cluster not in elimination.keys():
                elimination[cluster] = []
                for j in range(0,len(zusammenhang)):
                    if zusammenhang(j) == cluster:
                        elimination(cluster).append(j)
    return elimination