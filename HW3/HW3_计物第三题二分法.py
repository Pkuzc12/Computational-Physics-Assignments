import numpy as np


def f(x):
    return x-2*np.sin(x)


a = 1
b = 2
while b-a>1e-6:
    x = a+(b-a)/2
    if np.sign(f(x))==np.sign(f(a)):
        a = x
    else:
        b = x
x = a+(b-a)/2
print(f'{x:.9e}')