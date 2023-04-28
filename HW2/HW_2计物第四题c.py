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


def GEM(A, b):#解线性方程组用的
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


def Runge(x):#Runge函数
    return 1/(1+25*x**2)


def dRunge(x):#Runge函数的导数
    return -50*x/(1+25*x**2)**2


def x(n):#节点
    return (-1+0.1*n)


def EqnGrt(A, b):#线性方程矩阵元生成
    for m in range(0, 20):
        A[m][m+2] = (x(m+2)-x(m+1))/6
        A[m][m+1] = (x(m+2)-x(m))/3
        A[m][m] = (x(m+1)-x(m))/6
        b[m] = (Runge(x(m+2))-Runge(x(m+1)))/(x(m+2)-x(m+1))-(Runge(x(m+1))-Runge(x(m)))/(x(m+1)-x(m))
    A[20][0] = (x(1)-x(0))/3
    A[20][1] = (x(1)-x(0))/6
    b[20] = -dRunge(x(0))+(Runge(x(1))-Runge(x(0)))/(x(1)-x(0))
    A[21][20] = (x(21)-x(20))/6
    A[21][21] = (x(21)-x(20))/3
    b[21] = dRunge(x(20))-(Runge(x(21))-Runge(x(20)))/(x(21)-x(20))


def EmptyAGrt():#空矩阵生成
    A = []
    for i in range(0, 22):
        temp = []
        for j in range(0, 22):
            temp = temp+[0]
        A = A+[temp]
    return A


def EmptybGrt():#空向量生成
    b = []
    for i in range(0, 22):
        b = b+[0]
    return b


def AGrt(M):#已知M，生成A
    A = []
    for i in range(0, 21):
        A = A+[(Runge(x(i+1))-Runge(x(i)))/(x(i+1)-x(i))-(M[i+1]-M[i])/6*(x(i+1)-x(i))]
    return A


def BGrt(M):#已知M，生成B
    B = []
    for i in range(0, 21):
        B = B+[Runge(x(i))-M[i]/6*(x(i+1)-x(i))**2]
    return B


def S(n, t, M, A, B):#第n段的三次样条函数，自变量为t
    return M[n+1]/6*(t-x(n))**3/(x(n+1)-x(n))-M[n]/6*(t-x(n+1))**3/(x(n+1)-x(n))+A[n]*(t-x(n))+B[n]


H = EmptyAGrt()
b = EmptybGrt()
EqnGrt(H, b)
M = GEM(H, b)
A = AGrt(M)
B = BGrt(M)
for i in M:
    print(f'{i:.3e}', end=',')
print('')
for i in A:
    print(f'{i:.3e}', end=',')
print('')
for i in B:
    print(f'{i:.3e}', end=',')
print('x f(x) S(x) |f(x)-S(x)|')
for i in range(0, 41):
    print(f'{x(0.5*i):.2f} {Runge(x(0.5*i)):.3e} {S(i//2, x(i/2), M, A, B):.3e} {np.abs(Runge(x(0.5*i))-S(i//2, x(i/2), M, A, B)):.3e}')
for i in range(0, 21):
    t = np.linspace(x(i), x(i+1), 10000)
    y = Runge(t)-S(i, t, M, A, B)
    plt.plot(t, y, linestyle='-')
plt.legend()
plt.grid()
plt.show()