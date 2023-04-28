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


def VctDot(x, y): #向量点乘
    n = len(x)
    result = 0
    for i in range(0, n):
        result = result+x[i]*y[i]
    return result


def VctPls(x, y): #向量加法
    n = len(x)
    result = []
    for i in range(0, n):
        result = result+[x[i]+y[i]]
    return result


def VctScl(k, x): #向量数乘
    n = len(x)
    result = []
    for i in range(0, n):
        result = result+[k*x[i]]
    return result


def QRdeco(A): #QR分解
    n = len(A)
    B = MtrxTrans(A)
    C = []
    for i in range(0, n):
        temp = B[i]
        for j in range(0, i):
            temp = VctPls(temp, VctScl(-VctDot(temp, C[j])/VctDot(C[j], C[j]), C[j]))
        temp = VctScl(1/np.math.sqrt(VctDot(temp, temp)), temp)
        C = C+[temp]
    Q = MtrxTrans(C)
    return Q


def QRM(A, n): #QR算法迭代
    T = A
    for i in range(0, n):
        Q = QRdeco(T)
        T = MtrxMtp(MtrxTrans(Q), MtrxMtp(T, Q))
    return T
    

A = [[1, -1, 0, 0], [-1, 2, -1, 0], [0, -1, 3, -1], [0, 0, -1, 4]]
print(QRM(A, 5))
print(QRM(A, 10))
print(QRM(A, 15))
print(QRM(A, 20))
print(QRM(A, 500))