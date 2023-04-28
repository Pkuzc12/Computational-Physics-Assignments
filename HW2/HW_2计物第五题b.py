import numpy as np
import matplotlib.pyplot as plt


def SlvU(A, b):
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


def SearchSwitchDiagnolize(A, b):
    n = len(A[0])
    for i in range(0, n): 
        index = i
        max = A[i][i]
        for j in range(i+1, n):
            if np.abs(A[j][i]) > max:
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


def GEM(A, b):#解方程用的
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


def X(theta):#X函数
    return (1-np.cos(theta))*np.cos(theta)


def Y(theta):#Y函数
    return (1-np.cos(theta))*np.sin(theta)


def phi(n):#节点
    return (n*np.pi/4)


def EqnGrt(A, b, xflag):#线性方程组生成
    for m in range(0, 8):
        A[m][m+2] = (phi(m+2)-phi(m+1))/6
        A[m][m+1] = (phi(m+2)-phi(m))/3
        A[m][m] = (phi(m+1)-phi(m))/6
        if xflag:
            b[m] = (X(phi(m+2))-X(phi(m+1)))/(phi(m+2)-phi(m+1))-(X(phi(m+1))-X(phi(m)))/(phi(m+1)-phi(m))
        else:
            b[m] = (Y(phi(m+2))-Y(phi(m+1)))/(phi(m+2)-phi(m+1))-(Y(phi(m+1))-Y(phi(m)))/(phi(m+1)-phi(m))
    A[8][0] = (phi(1)-phi(0))/3
    A[8][1] = (phi(1)-phi(0))/6
    A[8][8] = (phi(9)-phi(8))/6
    A[8][9] = (phi(9)-phi(8))/3
    if xflag:
        b[8] = (X(phi(1))-X(phi(0)))/(phi(1)-phi(0))-X(phi(9))-X(phi(8))/(phi(9)-phi(8))
    else:
        b[8] = (Y(phi(1))-Y(phi(0)))/(phi(1)-phi(0))-Y(phi(9))-Y(phi(8))/(phi(9)-phi(8))
    A[9][0] = 1
    A[9][9] = -1
    b[9] = 0


def EmptyAGrt():#空矩阵生成
    A = []
    for i in range(0, 10):
        temp = []
        for j in range(0, 10):
            temp = temp+[0]
        A = A+[temp]
    return A


def EmptybGrt():#空向量生成
    b = []
    for i in range(0, 10):
        b = b+[0]
    return b


def AGrt(M, xflag):#X函数与Y函数内插系数A的生成，已知M
    A = []
    for i in range(0, 9):
        if xflag:
            A = A+[(X(phi(i+1))-X(phi(i)))/(phi(i+1)-phi(i))-(M[i+1]-M[i])/6*(phi(i+1)-phi(i))]
        else:
            A = A+[(Y(phi(i+1))-Y(phi(i)))/(phi(i+1)-phi(i))-(M[i+1]-M[i])/6*(phi(i+1)-phi(i))]
    return A


def BGrt(M, xflag):#X函数与Y函数内插系数B的生成，已知M
    B = []
    for i in range(0, 9):
        if xflag:
            B = B+[X(phi(i))-M[i]/6*(phi(i+1)-phi(i))**2]
        else:
            B = B+[Y(phi(i))-M[i]/6*(phi(i+1)-phi(i))**2]
    return B


def S(n, t, M, A, B):#第n段三次样条函数，自变量为t
    return M[n+1]/6*(t-phi(n))**3/(phi(n+1)-phi(n))-M[n]/6*(t-phi(n+1))**3/(phi(n+1)-phi(n))+A[n]*(t-phi(n))+B[n]


H = EmptyAGrt()
b = EmptybGrt()
EqnGrt(H, b, 1)
MX = GEM(H, b)
print ('m Mmx')
for i in range(0, 10):
    print(f'{i} {MX[i]:.3e}')
H = EmptyAGrt()
b = EmptybGrt()
EqnGrt(H, b, 0)
MY = GEM(H, b)
print ('m Mmy')
for i in range(0, 10):
    print(f'{i} {MY[i]:.3e}')
AX = AGrt(MX, 1)
print('m Amx')
for i in range(0, 9):
    print(f'{i} {AX[i]:.3e}')
AY = AGrt(MY, 0)
print('m Amy')
for i in range(0, 9):
    print(f'{i} {AY[i]:.3e}')
BX = BGrt(MX, 1)
print('m Bmx')
for i in range(0, 9):
    print(f'{i} {BX[i]:.3e}')
BY = BGrt(MY, 0)
print('m Bmy')
for i in range(0, 9):
    print(f'{i} {BY[i]:.3e}')