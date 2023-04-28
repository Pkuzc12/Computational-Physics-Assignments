import time
import numpy


def DirExp(x):#直接展开
    s_prvs = 0.1
    s = 1
    n = 1
    while numpy.math.fabs((s-s_prvs)/s_prvs) > 10**(-12):
        s_prvs = s
        s = s+(-1)**n*x**n/numpy.math.factorial(n)
        n = n+1
    return s


def Rcrsn(x):#递推
    s_prvs = 0.1
    s = 1
    n = 1
    s_n = 1
    while numpy.math.fabs((s-s_prvs)/s_prvs) > 10**(-12):
        s_n = -s_n*x/n
        s_prvs = s
        s = s+s_n
        n = n+1
    return s


def IndirRcrsn(x):#间接递推
    return 1/Rcrsn(-x)


rslt1 = rslt2 = rslt3 = tm1 = tm2 = tm3 = []
for x in range(0, 110, 10):
    t1 = time.time()
    rslt1 = rslt1+[DirExp(x)]
    t2 = time.time()
    tm1 = tm1+[t2-t1]
    t1 = time.time()
    rslt2 = rslt2+[Rcrsn(x)]
    t2 = time.time()
    tm2 = tm2+[t2-t1]
    rslt3 = rslt3+[IndirRcrsn(x)]
print('三种方法计算所得结果分别为：')
print('x 方法1 方法2 方法3 实际值')
for x in range(0, 11):
    print(f'{x*10} {rslt1[x]:.3e} {rslt2[x]:.3e} {rslt3[x]:.3e} {numpy.math.e**(-x*10):.3e}')
print('前两种方法计算所用时间分别为：')
print('x 方法1 方法2')
for x in range(0, 11):
    print(f'{x*10} {tm1[x]:.3e} {tm2[x]:.3e}')