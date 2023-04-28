import numpy as np


def PolySeries(A, x, k): #多项式序列
    b = []
    d = []
    n = len(A)
    for i in range(0, n):
        d = d + [A[i][i]]
    for i in range(0, n - 1):
        b = b + [A[i + 1][i]]
    if k == 0:
        return 1
    if k == 1:
        return d[0] - x
    return (d[k - 1] - x) * PolySeries(A, x, k - 1) - b[k - 2]**2 * PolySeries(A, x, k - 2)


def counter(A, x): #计数器
    n = len(A)
    result = 0
    for i in range(1, n+1):
        if PolySeries(A, x, i) * PolySeries(A, x, i - 1) <= 0 and PolySeries(A, x, i - 1) != 0:
            result = result + 1
    return result


def limit(A): #Sturm中的边界判定
    b = []
    d = []
    n = len(A)
    b = b+[0]
    for i in range(0, n):
        d = d + [A[i][i]]
    for i in range(0, n - 1):
        b = b + [A[i + 1][i]]
    b = b+[0]
    alpha = d[0]-(np.math.fabs(b[0])+np.math.fabs(b[1]))
    beta = d[0]+(np.math.fabs(b[0])+np.math.fabs(b[1]))
    for i in range(2, n+1):
        alpha_next = d[i-1]-(np.math.fabs(b[i-1])+np.math.fabs(b[i]))
        beta_next = d[i-1]+(np.math.fabs(b[i-1])+np.math.fabs(b[i]))
        if alpha_next < alpha:
            alpha = alpha_next
        if beta_next > beta:
            beta = beta_next
    return [alpha, beta]


def Sturm(A, n, k):
    a = limit(A)[0]
    b = limit(A)[1]
    for i in range(0, k):
        c = (a+b)/2
        if counter(A, c) < n:
            a = c
        else:
            b = c
    return c


A = [[1, -1, 0, 0], [-1, 2, -1, 0], [0, -1, 3, -1], [0, 0, -1, 4]]
for i in range(1, 5):
    print(Sturm(A, i, 5))
    print(Sturm(A, i, 10))
    print(Sturm(A, i, 15))
    print(Sturm(A, i, 20))