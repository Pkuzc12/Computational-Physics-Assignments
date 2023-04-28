import numpy


def HbtGnrt(n):
    # 生成Hilbert矩阵，n阶数
    Hbt = []
    for i in range(1, n+1):
        row = []
        for j in range(1, n+1):
            row = row+[1/(i+j-1)]
        Hbt = Hbt+[row]
    row = []
    for i in range(0, n):
        row = row+[i]
    Hbt = Hbt+[row]
    return Hbt


def bGnrt(n):
    # 生成b向量，n维数
    b = []
    for i in range(1, n+1):
        b = b+[1]
    return b


def FulFcrmSlctn(H, k):
    # 完全支点遴选，H为矩阵，k为开始搜寻的行列数，返回支点的位置
    n = len(H[0])
    indx = [k, k]
    max = numpy.math.fabs(H[k][k])
    for j in range(k, n):
        for i in range(k, n):
            if numpy.math.fabs(H[i][j]) > max:
                max = numpy.math.fabs(H[i][j])
                indx[0] = i
                indx[1] = j
    return indx


def Swtch(H, b, indx, k):
    # 支点交换，H为矩阵，b为向量，indx为支点位置，k为支点要放置的行列数
    n = len(H[0])
    temp = 0
    for i in range(0, n+1):
        temp = H[i][k]
        H[i][k] = H[i][indx[1]]
        H[i][indx[1]] = temp
    for j in range(0, n):
        temp = H[k][j]
        H[k][j] = H[indx[0]][j]
        H[indx[0]][j] = temp
    temp = b[k]
    b[k] = b[indx[0]]
    b[indx[0]] = temp


def Trglrz(H, b, k):
    # 上三角化，H为矩阵，b为向量，k为三角化开始的行列数
    n = len(H[0])
    if H[k][k] == 0:
        exit
    for i in range(k+1, n):
        li = H[i][k]/H[k][k]
        for j in range(k, n):
            H[i][j] = H[i][j]-li*H[k][j]
        b[i] = b[i]-li*b[k]


def SlvU(H, b, flag):
    # 求解上三角矩阵，flag为1时，考虑完全支点遴选导致的未知量顺序的交换，为0时不考虑，返回解列表
    n = len(H[0])
    sol = []
    solution = []
    temp = 0
    for i in range(0, n):
        sol = sol+[0]
        solution = solution+[0]
        if H[i][i] == 0:
            exit
    for i in range(n-1, -1, -1):
        temp = b[i]
        for j in range(n-1, i, -1):
            temp = temp-H[i][j]*sol[j]
        sol[i] = temp/H[i][i]
    if flag:
        for j in range(0, n):
            solution[H[n][j]] = sol[j]
        return solution
    else:
        return sol


def GEM(H, b):
    # GEM方法，返回解列表
    n = len(H[0])
    for k in range(0, n):
        Swtch(H, b, FulFcrmSlctn(H, k), k)
        Trglrz(H, b, k)
    return SlvU(H, b, 1)


def SlvL(H, b, flag):
    # 求解下三角矩阵，flag为1时，考虑完全支点遴选导致的未知量顺序的交换，为0时不考虑，返回解列表
    n = len(H[0])
    sol = []
    solution = []
    temp = 0
    for i in range(0, n):
        sol = sol+[0]
        solution = solution+[0]
        if H[i][i] == 0:
            exit
    for i in range(0, n):
        temp = b[i]
        for j in range(0, i):
            temp = temp-H[i][j]*sol[j]
        sol[i] = temp/H[i][i]
    if flag:
        for j in range(0, n):
            solution[H[n][j]] = sol[j]
        return solution
    else:
        return sol
    

def CholeskyDsmb(A):
    # Cholesky分解，返回H矩阵对应的列表
    n = len(A[0])
    H = []
    for i in range(0, n):
        row = []
        for j in range(0, n):
            row = row+[0]
        H = H+[row]
    row = []
    for i in range(0, n):
        row = row+[i]
    H = H+[row]
    H[0][0] = numpy.math.sqrt(A[0][0])
    for i in range(1, n):
        v = []
        for j in range(0, i):
            v = v+[A[i][j]]
        HTrnsCj = []
        for j in range(0, i):
            row = []
            for k in range(0, i):
                row = row+[H[k][j]]
            HTrnsCj = HTrnsCj+[row]
        h = SlvL(HTrnsCj, v, 0)
        for j in range(0, i):
            H[j][i] = h[j]
        norm = 0
        for j in range(0, i):
            norm = norm+(h[j])**2
        H[i][i] = numpy.math.sqrt(A[i][i]-norm)
    return H
    

def MtrxMltp(A, B):
    # 矩阵乘法，返回矩阵对应队列，没用到
    n = len(A[0])
    C = []
    for i in range(0, n):
        row = []
        for j in range(0, n):
            row = row+[0]
        C = C+[row]
    for i in range(0, n):
        for j in range(0, n):
            for k in range(0, n):
                C[i][j] = C[i][j]+A[i][k]*B[k][j]
    return C


def MtrxTrns(A):
    # 矩阵转置
    n = len(A[0])
    B = []
    for i in range(0, n):
        row = []
        for j in range(0, n):
            row = row+[A[j][i]]
        B = B+[row]
    row = []
    for i in range(0, n):
        row = row+[i]
    B = B+[row]
    return B


def Cholesky(H, b):
    # Cholesky方法，返回解列表
    A = CholeskyDsmb(H)
    B = MtrxTrns(A)
    y = SlvL(B, b, 1)
    x = SlvU(A, y, 1)
    return x


def Numpy(H, b): 
    # numpy方法，返回接列表
    n = len(H[0])
    del H[n]
    A = numpy.mat(H)
    c = numpy.array(b)
    x = numpy.linalg.solve(A, c)
    return (x.tolist())

print(f'n GEM Cholesky numpy')
for n in range(1, 11):
    Hn1 = HbtGnrt(n)
    Hn2 = HbtGnrt(n)
    Hn3 = HbtGnrt(n)
    b1 = bGnrt(n)
    b2 = bGnrt(n)
    b3 = bGnrt(n)
    x1 = GEM(Hn1, b1)
    x2 = Cholesky(Hn2, b2)
    x3 = Numpy(Hn3, b3)
    for i in range(0, n):
        print(f'{n} {x1[i]:.3e} {x2[i]:.3e} {x3[i]:.3e}')