import numpy as np


def MtrxTrans(A): #矩阵转置
    n = len(A)
    result = []
    for i in range(0, n):
        temp = []
        for j in range(0, n):
            temp = temp+[A[j][i]]
        result = result+[temp]
    return result


def MtrxMtp(A, B): #矩阵乘法
    n = len(A)
    C = []
    for i in range(0, n):
        temp = []
        for j in range(0, n):
            sum = 0
            for k in range(0, n):
                sum = sum+A[i][k]*B[k][j]
            temp = temp+[sum]
        C = C+[temp]
    return C


def zeros(n): #单位矩阵创建
    result = []
    for i in range(0, n):
        temp = []
        for j in range(0, n):
            temp = temp+[0]
        result = result+[temp]
    for i in range(0, n):
        result[i][i] = 1
    return result


def jacobi(A): #jacobi算法
    n = len(A)
    T = A
    for i in range(1, n):
        for j in range(0, i):
            if T[i][j] == 0:
                continue
            eta = (T[j][j]-T[i][i])/(2*T[i][j])
            if eta >= 0:
                t = 1/(eta+np.math.sqrt(1+eta*eta))
            else:
                t = -1/(-eta+np.math.sqrt(1+eta*eta))
            c = 1/np.math.sqrt(1+t*t)
            s = c*t
            G = zeros(n)
            G[i][i] = c
            G[j][j] = c
            G[i][j] = s
            G[j][i] = -s
            T = MtrxMtp(MtrxTrans(G), MtrxMtp(T, G))
    return T


def Jacobi(A, n): #jacobi的迭代
    T = A
    for i in range(0, n):
        T = jacobi(T)
    return T


A = [[1, -1, 0, 0], [-1, 2, -1, 0], [0, -1, 3, -1], [0, 0, -1, 4]]
print(Jacobi(A, 5))
print(Jacobi(A, 10))
print(Jacobi(A, 15))
print(Jacobi(A, 20))