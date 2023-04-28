import random as rand
import numpy as np
import matplotlib.pyplot as plt


prob = []
for i in range(0, 10000):
    array = []
    n = 0
    for j in range(0, 1000):
        array.append(rand.random())
    for j in range(0, 1000):
        if array[j] >= 0.3 and array[j] < 0.4:
            n = n+1
    prob.append(n/1000)


fig = plt.figure(figsize = (10, 8))
plt.xlabel("times")  
plt.ylabel("value")  
plt.xlim(0, 10000)  
plt.ylim(0, 1)
plt.grid()
x = range(1, 10001)
plt.plot(x, prob)
plt.show()