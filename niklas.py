
import math
from numpy import linalg as LA
import numpy as np
data = np.genfromtxt("bananas-1-4d.csv", delimiter=',')
np.savetxt('first10.csv', data[0:10], delimiter=',', fmt='%1.4f')

def get_data_size(data):
    num_data = len(data)
    x_dimension = len(data[0])

    return num_data, x_dimension

def h(data,delta,y):
    dict={}
    size, dim = get_data_size(data)
    i=0
    while i < size:
        dict[i]=LA.norm(data[i,:]-y) # #""""""math.sqrt((data[i,1]-y[0])**2+(data[i,2]-y[1])**2) 
        i=i+1
    indic = [1 if x<delta else 0 for x in dict.values()]
    h=sum(indic)/(delta**dim*size)
    return h
 
y=[0.4,0.2,0.5,0.7]
delta=0.2
rho=0.5
a=h(data,delta,y)
hp={}
i=0
size, dim = get_data_size(data)
while i < size:
    a=h(data,delta,data[i,:])
    if(h<rho):
        hp[i]=data[i,:]
    i=i+1
