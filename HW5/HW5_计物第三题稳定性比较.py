import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import matplotlib.cm as cm


I = 128
J = 16
dt = 0.001
dx = 1/I
dy = 1/J
lam = 1
C = lam*dt*dt/(dy*dy)
kappa = np.pi*dy
N = 1000


def x(n): #和第三题的其他程序一样
    return n/I


def y(n):
    return n/J


def ini_discr(i, j):
    return np.sin(np.pi*x(i))*np.sin(2*np.pi*y(j))


def ini_fourier(i, j):
    sum = 0
    for k in range(0, I+1):
        sum = sum+2/I*ini_discr(k, j)*np.sin(i*k*np.pi/I)
    return sum


def inv_fourier(i, j, T):
    sum = 0
    for k in range(0, J+1):
        sum = sum+T[k][j]*np.sin(i*k*np.pi/I)
    return sum


def Thomas(i, T, emm):
    a = []
    b = []
    c = []
    a.append(1)
    for j in range(1, J):
        a.append(1+C*(1+i*i*kappa*kappa/2))
    a.append(1)
    b.append(0)
    for j in range(1, J):
        b.append(-C/2)
    b.append(0)
    c.append(0)
    for j in range(1, J):
        c.append(-C/2)
    c.append(0)
    alpha = []
    beta = []
    alpha.append(a[0])
    beta.append(0)
    for j in range(1, J+1):
        beta.append(b[j]/alpha[j-1])
        alpha.append(a[j]-beta[j]*c[j-1])
    b = []
    b.append(0)
    for j in range(1, J):
        b.append(C/2*T[i][j-1]+(2-C*(1+i*i*kappa*kappa/2))*T[i][j]+C/2*T[i][j+1]-emm[i][j])
    b.append(0)
    y = []
    y.append(b[0])
    for j in range(1, J+1):
        y.append(b[j]-beta[j]*y[j-1])
    x = []
    x.append(y[J]/alpha[J])
    for j in range(J-1, -1, -1):
        x = [(y[j]-c[j]*x[0])/alpha[j]]+x
    return x


T = []
Temp = []
for i in range(0, I+1):
    temp = []
    for j in range(0, J+1):
        temp.append(ini_fourier(i, j))
    Temp.append(temp)
T.append(Temp)
T.append(Temp)
for n in range(2, N+1):
    temp = []
    for i in range(0, I+1):
        temp.append(Thomas(i, T[n-1], T[n-2]))
    T.append(temp)


fig = plt.figure(figsize = (8, 8))


def update(n):
    print(n)
    Temp = []
    for i in range(0, I+1):
        temp = []
        for j in range(0, J+1):
            temp.append(inv_fourier(i, j, T[5*n]))
        Temp.append(temp)
    plt.cla()
    plt.xlabel("x")  
    plt.ylabel("y")  
    plt.xlim(0, 1)  
    plt.ylim(0, 1)
    plt.grid()
    X, Y = np.meshgrid(np.linspace(0, 1, J+1), np.linspace(0, 1, I+1))
    plt.contourf(Y, X, Temp, alpha=0.75, cmap = 'PuBu')
    plt.clim(-1, 1)


ani = FuncAnimation(fig, update, frames = 200, interval = 50, blit = False, repeat = False)
plt.show()
# ani.save('OscillationLattice.gif', writer = 'imagemagick')