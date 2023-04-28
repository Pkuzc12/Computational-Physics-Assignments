import numpy as np
import matplotlib.pyplot as pl


def neville(x, left, right):#Neville递归方法
    if left == right:
        return 1/(1+25*(-1+left*0.1)**2)
    else:
        return (neville(x, left+1, right)*(x-(-1+left*0.1))+neville(x, left, right-1)*((-1+right*0.1)-x))/((right-left)*0.1)


print('x f(x) P20(x) |f(x)-P20(x)|')
nev = []
x = []
for i in range(0, 41):
    x = x+[-1+i*0.1/2]
    nev = nev+[neville(-1+0.1*i/2, 0, 20)]
    print(f'{(-1+0.1*i/2)} {1/(1+25*(-1+i*0.1/2)**2):.3e} {nev[i]:.3e} {np.abs(1/(1+25*(-1+i*0.1/2)**2)-nev[i]):.3e}')
x1 = np.linspace(-1, 1, 10000)
pl.plot(x, nev, linestyle = '-', label = 'P20(x)')
pl.plot(x1, 1/(1+25*(x1)**2), linestyle = '-', label = 'f(x)')
pl.legend()
pl.grid()
pl.show()