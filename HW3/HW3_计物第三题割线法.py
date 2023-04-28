import numpy as np


def f(x):
    return x-2*np.sin(x)


x1 = 0.9
x2 = 1
while np.abs(f(x1)) > 1e-6 or np.abs(x1-x2) > 1e-6:
    temp = x2
    x2 = x2-f(x2)*(x2-x1)/(f(x2)-f(x1))
    x1 = temp
print(f'{x2:.9e}')