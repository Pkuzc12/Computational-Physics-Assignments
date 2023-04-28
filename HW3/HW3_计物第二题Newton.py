import numpy as np


def f(x):#被积函数
    return np.exp(-x)/x


def trapezoidal(a, b):#梯形法则
    return (b-a)*(f(a)+f(b))/2


def Simpson(a, b):#辛普森法则
    return (b-a)*(f(a)+4*f((a+b)/2)+f(b))/6


def x(n, i):#积分节点
    return 1+i*99/(n-1)


n = 10
I1 = 0
I2 = 0
for i in range(0, n-1):
    I1 = I1+trapezoidal(x(n, i), x(n, i+1))
    I2 = I2+Simpson(x(n, i), x(n, i+1))
print(f'n 梯形 Simpson')
print(f'{n} {I1:.3e} {I2:.3e}')
n = 100
I1 = 0
I2 = 0
for i in range(0, n-1):
    I1 = I1+trapezoidal(x(n, i), x(n, i+1))
    I2 = I2+Simpson(x(n, i), x(n, i+1))
print(f'{n} {I1:.3e} {I2:.3e}')
n = 1000
I1 = 0
I2 = 0
for i in range(0, n-1):
    I1 = I1+trapezoidal(x(n, i), x(n, i+1))
    I2 = I2+Simpson(x(n, i), x(n, i+1))
print(f'{n} {I1:.3e} {I2:.3e}')