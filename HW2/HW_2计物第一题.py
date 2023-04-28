import numpy as np
#不愿再用完全节点遴选

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

def SlvL(A, b):#下三角矩阵求解
    n = len(A[0])
    x = []
    for i in range(0, n):
        x = x+[0]
    for i in range(0, n):
        x[i] = b[i]
        for j in range(0, i):
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
    return SlvU(A1 ,b1)


def Cholesky(A, b):#Cholesky分解方法解实对称方程组
    n = len(A[0])
    H = []
    for i in range(0, n):
        temp = []
        for j in range(0, n):
            temp = temp+[0]
        H = H+[temp]
    H[0][0] = np.sqrt(A[0][0])
    for i in range(1, n):
        Htemp = []
        for j in range(0, i):
            temp = []
            for k in range(0, i):
                temp = temp+[H[k][j]]
            Htemp = Htemp+[temp]
        a = []
        for j in range(0, i):
            a = a+[A[i][j]]
        v = SlvL(Htemp, a)
        for j in range(0, i):
            H[j][i] = v[j]
        sum = 0
        for j in range(0, i):
            sum = sum+v[j]**2
        H[i][i] = np.sqrt(A[i][i]-sum)
    print(H)
    Htrs = []
    for i in range(0, n):
        temp = []
        for j in range(0, n):
            temp = temp+[H[j][i]]
        Htrs = Htrs+[temp]
    xtemp = SlvL(Htrs, b)
    return SlvU(H, xtemp)


A = [[0.05, 0.07, 0.06, 0.05], [0.07, 0.10, 0.08, 0.07], [0.06, 0.08, 0.10, 0.09], [0.05, 0.07, 0.09, 0.10]]
b = [0.23, 0.32, 0.33, 0.31]
print(GEM(A, b))
print(Cholesky(A, b))