import numpy as np
import matplotlib.pyplot as plt


def Runge(x):#Runge函数
    return 1/(1+25*x**2)


def Chebyshev(n, x):#n阶Chebyshev多项式函数
    y = np.arccos(x)
    return np.cos(n*y)


def coefgnr(n):#第n项展开系数生成
    sum = 0
    for i in range(0, 20):
        sum = sum+np.cos(n*np.pi*(i+1/2)/20)*Runge(np.cos(np.pi*(i+1/2)/20))
    if n == 0:
        return sum/20
    else:
        return sum/10


def ApproxExpansion(x):#内插结果得到的多项式函数
    sum = 0
    for i in range(0, 20):
        sum = sum+coefgnr(i)*Chebyshev(i, x)
    return sum


print('index c')
for i in range(0, 20):
    print(f'{i} {coefgnr(i):.3e}')
print('x f(x) P20(x) |f(x)-P20(x)|')
for i in range(0, 41):
    print(f'{-1+i*0.05} {Runge(-1+i*0.05):.3e} {ApproxExpansion(-1+i*0.05):.3e} {np.abs(Runge(-1+i*0.05)-ApproxExpansion(-1+i*0.05)):.3e}')
x = np.linspace(-1, 1, 10000)
plt.plot(x, Runge(x)-ApproxExpansion(x), linestyle = '-', label = 'f(x)-P20(x)')
plt.grid()
plt.legend()
plt.show()