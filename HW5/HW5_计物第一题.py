import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


def index_x(n): #差分序号与x值的转换
    return n*2/128


u = []
utemp = []
for i in range(0, 129):
    utemp = utemp+[np.cos(index_x(i)*np.pi)]
utemp = utemp+[utemp[0], utemp[1]]
u = u+[utemp]
delta = 0.022
dt = 12.6/600000
dx = 2/128
for i in range(1, 600001): #差分法递推
    print(i)
    utemp = []
    utemp.append(u[i-1][0]-dt/dx*(1/6*(u[i-1][1]-u[i-1][128])*(u[i-1][128]+u[i-1][0]+u[i-1][1])+delta*delta/(2*dx*dx)*(u[i-1][2]+2*u[i-1][128]-2*u[i-1][1]-u[i-1][127])))
    utemp.append(u[i-1][1]-dt/dx*(1/6*(u[i-1][2]-u[i-1][0])*(u[i-1][0]+u[i-1][1]+u[i-1][2])+delta*delta/(2*dx*dx)*(u[i-1][3]+2*u[i-1][0]-2*u[i-1][2]-u[i-1][128])))
    for j in range(2, 129):
        utemp.append(u[i-1][j]-dt/dx*(1/6*(u[i-1][j+1]-u[i-1][j-1])*(u[i-1][j-1]+u[i-1][j]+u[i-1][j+1])+delta*delta/(2*dx*dx)*(u[i-1][j+2]+2*u[i-1][j-1]-2*u[i-1][j+1]-u[i-1][j-2])))
    utemp.append(utemp[0])
    utemp.append(utemp[1])
    u = u+[utemp]


fig = plt.figure(figsize = (8, 5))  


def update(n): #动画帧
    print(n)
    plt.cla()
    plt.xlabel("x")  
    plt.ylabel("u")  
    plt.xlim(-0.1, 2.1)  
    plt.ylim(-1, 3)
    plt.grid()
    x = np.arange(0, 2+2/128, 2/128)
    ax = plt.plot(x, u[n*1200][0:129])
    return ax


ani = FuncAnimation(fig, update, frames = 500, interval = 50, blit = False, repeat = False)
plt.show()
# ani.save('KZ.gif', writer = 'imagemagick')