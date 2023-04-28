import numpy as np


def Kronecker(x, y): #克罗内科符号
    if x == y:
        return 1
    else:
        return 0


def EqnGrt(n): #方程组生成
    result = []
    for i in range(0, n):
        temp = []
        for j in range(0, n):
            temp = temp+[-Kronecker(i-1, j)-Kronecker(i+1, j)+2*Kronecker(i, j)]
        result = result+[temp]
    return result


def MtrxVctMtp(A, b): #矩阵向量乘法
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

 
def VctScl(k, x): #向量数乘
    n = len(x)
    result = []
    for i in range(0, n):
        result = result+[k*x[i]]
    return result


def PM(A): #幂次法
    n = len(A)
    q = [1]
    for i in range(1, n):
        q = q+[0]
    nu = VctDot(q, MtrxVctMtp(A, q))
    nu_former = nu+1
    while np.math.fabs(nu-nu_former) > 1e-6:
        q = MtrxVctMtp(A, q)
        q = VctScl(1/np.math.sqrt(VctDot(q, q)), q)
        nu_former = nu
        nu = VctDot(q, MtrxVctMtp(A, q))
    return [nu, q]


A = EqnGrt(10)
print(PM(A))