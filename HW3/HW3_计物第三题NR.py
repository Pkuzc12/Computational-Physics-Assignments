import numpy as np


def f(x):
    return x-2*np.sin(x)


def df(x):
    return 1-2*np.cos(x)


x1 = 0.1
x2 = 1
while np.abs(f(x1)) > 1e-6 or np.abs(x1-x2) > 1e-6:
    x1 = x2
    x2 = x2-f(x2)/df(x2)
print(f'{x2:.9e}')