import numpy as np
import matplotlib.pyplot as plt


def ChebyshevT(n, x):#n阶Chebyshev多项式函数
    y = np.arccos(x)
    return np.cos(n*y)


def func1(x):#四阶最佳平方近似
    return(0.543107*ChebyshevT(0, 2*x-3)+0.495055*ChebyshevT(1, 2*x-3)-0.042469*ChebyshevT(2, 2*x-3)+0.00485768*ChebyshevT(3, 2*x-3)
    -0.000625085*ChebyshevT(4, 2*x-3))


def func2(x):#四阶另一种近似
    return(0.543107*ChebyshevT(0, 2*x-3)+0.495055*ChebyshevT(1, 2*x-3)-0.0424687*ChebyshevT(2, 2*x-3)+0.00485588*ChebyshevT(3, 2*x-3)
    -0.000612818*ChebyshevT(4, 2*x-3))


def func3(x):#六阶最佳平方近似
    return(0.543107*ChebyshevT(0, 2*x-3)+0.495055*ChebyshevT(1, 2*x-3)-0.042469*ChebyshevT(2, 2*x-3)+0.00485768*ChebyshevT(3, 2*x-3)
    -0.000625085*ChebyshevT(4, 2*x-3)+0.0000857981*ChebyshevT(5, 2*x-3)-0.0000122672*ChebyshevT(6, 2*x-3))


def func4(x):#六阶另一种近似
    return(0.543107*ChebyshevT(0, 2*x-3)+0.495055*ChebyshevT(1, 2*x-3)-0.042469*ChebyshevT(2, 2*x-3)+0.00485768*ChebyshevT(3, 2*x-3)
    -0.000625079*ChebyshevT(4, 2*x-3)+0.0000857568*ChebyshevT(5, 2*x-3)-0.0000119964*ChebyshevT(6, 2*x-3))


fig = plt.figure()
ax = plt.axes()
x = np.linspace(1, 2, 10000)
plt.plot(x, func3(x)-np.log2(x), linestyle = '-', label = 'func3')
plt.plot(x, func4(x)-np.log2(x), linestyle = '-', label = 'func4')
plt.xlim(0.97, 2.03)
plt.ylim(-0.0001, 0.0001)
plt.grid()
plt.legend()
plt.show()