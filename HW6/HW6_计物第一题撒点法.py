import numpy as np
import random as rand
import matplotlib.pyplot as plt


N = 1000
result = []
for i in range(0, 1000):
    sum = 0
    for j in range(0, N):
        sum = sum+np.exp(-100*(rand.random()-0.5)**2)
    result.append(sum/N)
x = range(0, 1000)


fig = plt.figure(figsize = (10, 8))
plt.xlabel("times")  
plt.ylabel("result")  
plt.xlim(0, 1000)
plt.ylim(0, 1)
plt.grid()
plt.scatter(x, result, s = 3)
plt.show()