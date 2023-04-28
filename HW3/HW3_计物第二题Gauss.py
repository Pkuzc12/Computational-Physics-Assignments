import numpy as np


def SlvU(A, b):#上三角矩阵求解
    n = len(A[0])
    x = []
    for i in range(0, n):
        x = x+[0]
    for i in range(n-1, -1, -1):
        x[i] = b[i]
        for j in range(i+1, n):
            x[i] = x[i]-x[j]*A[i][j]
        x[i] = x[i]/A[i][i]
    return x



def SearchSwitchDiagnolize(A, b):#不完全支点遴选，对角化
    n = len(A[0])
    for i in range(0, n): 
        index = i
        max = A[i][i]
        for j in range(i+1, n):
            if np.abs(A[j][i])>max:
                max = np.abs(A[j][i])
                index = j
        for j in range(i, n):
            temp = A[i][j]
            A[i][j] = A[index][j]
            A[index][j] = temp
        temp = b[i]
        b[i] = b[index]
        b[index] = temp
        for j in range(i+1, n):
            l = A[j][i]/A[i][i]
            for k in range(i, n):
                A[j][k] = A[j][k]-l*A[i][k]
            b[j] = b[j]-l*b[i]


def GEM(A, b):#高斯方法解线性方程组
    n = len(A[0])
    A1 = []
    for i in range(0, n):
        temp = []
        for j in range(0, n):
            temp = temp+[A[i][j]]
        A1 = A1+[temp]
    b1 = []
    for i in range(0, n):
        b1 = b1+[b[i]]
    SearchSwitchDiagnolize(A1, b1)
    return SlvU(A1, b1)


def ChebyshevPoly(n, x):#认为已知的切比雪夫多项式
    return np.cos(n*np.arccos(x))


def node(n, k):#认为已知的切比雪夫多项式零点，即积分节点
    return np.cos(np.pi*((n-1-k)+0.5)/n)


def WeightEqnGrt(n):#积分权重方程组矩阵生成
    A = []
    temp = []
    for i in range(0, n):
        temp = temp+[1]
    A = A+[temp]
    for i in range(1, n):
        temp = []
        for j in range(0, n):
            temp = temp+[ChebyshevPoly(i, node(n, j))]
        A = A+[temp]
    return A


def bGrt(n):#积分权重方程组向量生成
    b = [np.pi]
    for i in range(1, n):
        b = b+[0]
    return b


def Weight(n):#积分权重解向量
    A = WeightEqnGrt(n)
    b = bGrt(n)
    return GEM(A, b)


def f(x):#被积函数
    return 99*np.exp(-99*x/2)*np.sqrt(1-x**2)/(np.exp(101/2)*(99*x+101))


n = 10
wei = Weight(n)
inte = 0
for i in range(1, n+1):
    inte = inte+wei[i-1]*f(node(n, i-1))
print('n I')
print(f'{n} {inte:.3e}')
n = 100
wei = Weight(n)
inte = 0
for i in range(1, n+1):
    inte = inte+wei[i-1]*f(node(n, i-1))
print(f'{n} {inte:.3e}')