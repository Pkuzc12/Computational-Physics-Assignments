import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import matplotlib.cm as cm


I = 128
J = 128


def x(n): #查分序号与x值转换
    return n/128


def y(n): #差分序号与y值转换
    return n/128



U = []
for n in np.arange(0, 1.001, 0.001):
    Temp = []
    for i in range(0, I+1):
        temp = []
        for j in range(0, J+1):
            temp.append(np.sin(np.pi*x(i))*np.sin(2*np.pi*y(j))*np.cos(np.sqrt(5)*np.pi*n))
        Temp.append(temp)
    U.append(Temp)


fig = plt.figure(figsize = (8, 8))


def update(n): #动画帧
    print(n)
    plt.cla()
    plt.xlabel("x")  
    plt.ylabel("y")  
    plt.xlim(0, 1)  
    plt.ylim(0, 1)
    plt.grid()
    X, Y = np.meshgrid(np.linspace(0, 1, 129), np.linspace(0, 1, 129))
    plt.contourf(Y, X, U[n*5], alpha=0.75, cmap = 'PuBu')
    plt.clim(-1, 1)


ani = FuncAnimation(fig, update, frames = 200, interval = 50, blit = False, repeat = False)
# plt.show()
ani.save('OscillationAna.gif', writer = 'imagemagick')