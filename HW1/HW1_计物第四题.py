from tkinter import N
import numpy as np

def roof(x):#下限函数
    if x == np.math.ceil(x):
        return x
    else:
        return np.math.ceil(x)-1


def sigma1(n):#式中第一个求和
    sum = 0
    for n1 in range(-n, n+1):
        limit1 = int(roof(np.sqrt(n**2-n1**2)))
        for n2 in range(-limit1, limit1+1):
            limit2 = int(roof(np.sqrt(n**2-n1**2-n2**2)))
            for n3 in range(-limit2, limit2+1):
                sum = sum+np.exp(0.5-n1**2-n2**2-n3**2)/(n1**2+n2**2+n3**2-0.5)
    return sum


def sigma2(n,t):#式中第二个求和
    sum = 0
    for n1 in range(-n, n+1):
        limit1 = int(roof(np.sqrt(n**2-n1**2)))
        for n2 in range(-limit1, limit1+1):
            limit2 = int(roof(np.sqrt(n**2-n1**2-n2**2)))
            for n3 in range(-limit2, limit2+1):
                sum = sum+np.exp(-np.pi**2*(n1**2+n2**2+n3**2)/t)
    return sum-1


def intgrt(n):#积分项
    t = np.linspace(0.0001, 1, 1000)
    y = sigma2(n, t)*np.exp(0.5*t)*np.pi**(3/2)*t**(-3/2)
    result = np.sum(y)/1000
    return result


for n in range(1, 7):
    print(f'{n} {sigma1(n)+intgrt(n)-2*np.pi**(3/2)*np.exp(0.5)+2*np.pi**2*np.sqrt(0.5)*0.953438:.7f}')