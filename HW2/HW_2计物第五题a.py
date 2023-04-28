import numpy as np


def x(t):
    return (1-np.cos(t*np.pi/4))*np.cos(t*np.pi/4)


def y(t):
    return (1-np.cos(t*np.pi/4))*np.sin(t*np.pi/4)


print("xt yt")
for i in range(0, 9):
    print(f'{x(i):.3e} {y(i):.3e}')