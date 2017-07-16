'''
Created on 03.07.2017

@author: Daniel
'''
import numpy as np
import  matplotlib.pyplot as plt
'''
a = 'Ausgabe'
delta = 0.04

deltas = str(delta)
deltas = deltas.replace('.', ',')
data = np.genfromtxt('bananas-1-2d.csv', delimiter = ",")
data = np.transpose(data)
x = data[0]
y = data[1]

output = np.ndarray(shape = (10000,3))


N = 10000
colors = 1
area = 0.07  # 0 to 15 point radii

plt.scatter(x, y, s=area)
plt.show()
'''
#np.savetxt(a + '/' + deltas + 'test2.csv', output, delimiter = ',', fmt = '%1.4f')



liste= [0]
for i in range(1, len(liste)):
    print(i)