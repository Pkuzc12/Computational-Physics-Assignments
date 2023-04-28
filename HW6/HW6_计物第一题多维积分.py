import numpy as np
import random as rand
import matplotlib.pyplot as plt


N = 10000000


def xGrt():
    x = []
    for i in range(0, 9):
        x.append(rand.random())
    return x


def function(x):
    sum = 0
    for i in range(0, 9):
        sum = sum-100*(x[i]-0.5)**2
    return np.exp(sum)


result  = []
for n in range(0, 100):
    print(n)
    sum = 0
    for i in range(0, N):
        sum = sum+function(xGrt())
    sum = sum/N
    result.append(sum)


fig = plt.figure(figsize = (10, 8))
plt.xlabel("times")  
plt.ylabel("result")  
plt.xlim(0, 100)
plt.ylim(0, 1e-6)
plt.grid()
plt.scatter(range(0, 100), result, s = 5)
plt.show()