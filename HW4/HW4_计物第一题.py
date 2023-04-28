import numpy as np


def MtrxMtp(A, b): #矩阵乘法
    n = len(b)
    result = []
    for i in range(0, n):
        sum = 0
        for j in range(0, n):
            sum = sum+b[j]*A[i][j]
        result = result+[sum]
    return result


def VctDot(x, y): #向量点乘
    n = len(x)
    result = 0
    for i in range(0, n):
        result = result+x[i]*y[i]
    return result


def Norm(x): #向量求模
    n = len(x)
    sum = 0
    for i in range(0, n):
        sum = sum+x[i]**2
    return np.math.sqrt(sum)


def VctPls(x, y): #向量加法
    n = len(x)
    result = []
    for i in range(0, n):
        result = result+[x[i]+y[i]]
    return result


def VctMns(x, y): #向量减法
    n = len(x)
    result = []
    for i in range(0, n):
        result = result+[x[i]-y[i]]
    return result


def VctSclMtp(k, x): #向量数乘
    n = len(x)
    result = []
    for i in range(0, n):
        result = result+[k*x[i]]
    return result


def SDM(A, b): #最速下降法
    x = [0, 0, 0, 0]
    r = VctMns(b, MtrxMtp(A, x))
    while Norm(r) > 1e-6:
        alpha = VctDot(r, r)/VctDot(r, MtrxMtp(A, r))
        x = VctPls(x, VctSclMtp(alpha, r))
        r = VctMns(r, VctSclMtp(alpha, MtrxMtp(A, r)))
    return x


def CGM(A, b): #共轭梯度法
    x = [0, 0, 0, 0]
    r = VctMns(b, MtrxMtp(A, x))
    p = r
    while Norm(r) > 1e-6:
        alpha = VctDot(r, r)/VctDot(p, MtrxMtp(A, p))
        x = VctPls(x, VctSclMtp(alpha, p))
        rnext = r
        r = VctMns(r, VctSclMtp(alpha, MtrxMtp(A, p)))
        beta = VctDot(r, r)/VctDot(rnext, rnext)
        p = VctPls(r, VctSclMtp(beta, p))
    return x


A = [[0.05, 0.07, 0.06, 0.05], [0.07, 0.10, 0.08, 0.07], [0.06, 0.08, 0.10, 0.09], [0.05, 0.07, 0.09, 0.10]]
b = [0.23, 0.32, 0.33, 0.31]
print(SDM(A, b))
print(CGM(A, b))
