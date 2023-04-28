import numpy as np
import matplotlib.pyplot as plt


def Lorentz(beta, rho, sigma, x0, y0, z0, start, end, stepnum):
    step = (end-start)/stepnum
    x = [x0]
    y = [y0]
    z = [z0]
    index = 0
    for i in range(0, stepnum):
        x = x+[x[index]+step*(-beta*x[index]+y[index]*z[index])]
        y = y+[y[index]+step*(-sigma*y[index]+sigma*z[index])]
        z = z+[z[index]+step*(-x[index]*y[index]+rho*y[index]-z[index])]
        index = index+1
    plt.axes(projection='3d')
    plt.plot(x, y, z)
    plt.show()


Lorentz(8/3, 28, 5, 12, 4, 0, 0, 50, 10000)