import numpy as np
import random as rand
from scipy.stats import chi2


def floor(n): #向下取整函数
    return int(np.ceil(n)-1)


for n in range(0, 10):
    x = []
    y = []
    for i in range(0, 10000):
        x.append(rand.random())
        y.append(rand.random())
    lattice = []
    for i in range(0, 10):
        temp = []
        for j in range(0, 10):
            temp.append(0)
        lattice.append(temp)
    for i in range(0, 10000):
        lattice[floor(x[i]*10)][floor(y[i]*10)] = lattice[floor(x[i]*10)][floor(y[i]*10)]+1
    chi = 0
    for i in range(0, 10):
        for j in range(0, 10):
            chi = chi+(lattice[i][j]-100)**2/100
    print(f'{chi:.3e} {1-chi2.cdf(chi, 9009):.3e}')