import numpy as np


def intgrt(r):#积分
    result = 4*np.math.pi*r+np.math.sqrt(2)*np.math.pi*np.math.log((np.math.sqrt(2)*r-1)/(1+np.math.sqrt(2)*r))
    return result


def roof(x):#上限函数
    if x == np.math.ceil(x):
        return x
    else:
        return np.math.ceil(x)-1


def sigma(r, grid):#级数求和
    sum = 0
    for n1 in range(1, r+1):
        limit1 = int(roof(np.math.sqrt(r**2-n1**2)))
        if limit1 >= n1:
            limit1 = n1-1
        for n2 in range(1, limit1+1):
            limit2 = int(roof(np.math.sqrt(r**2-n1**2-n2**2)))
            if limit2 >= n2:
                limit2 = n2-1
            for n3 in range(1, limit2+1):
                sum = sum+48/(n1**2+n2**2+n3**2-0.5)
                plot(grid, n1, n2, n3)
    sum = sum-2
    for n1 in range(1, r+1):
        limit1 = int(roof(np.math.sqrt(r**2-n1**2)))
        if limit1 >= n1:
            limit1 = n1-1
        for n2 in range(1, limit1+1):
            for n3 in range(0, 1):
                sum = sum+24/(n1**2+n2**2+n3**2-0.5)
                plot(grid, n1, n2, n3)
    for n1 in range(1, r+1):
        for n2 in range(0, 1):
            for n3 in range(0, 1):
                sum = sum+6/(n1**2+n2**2+n3**2-0.5)
                plot(grid, n1, n2, n3)
    for n1 in range(1, r+1):
        limit1 = int(roof(np.math.sqrt((r**2-n1**2)/2)))
        if limit1 >= n1:
            limit1 = n1-1
        for n2 in range(1, limit1+1):
            sum = sum+24/(n1**2+n2**2+n2**2-0.5)
            plot(grid, n1, n2, n2)
    limit = int(roof(np.math.sqrt(r**2/2)))
    for n1 in range(1, limit+1):
        limit1 = int(roof(np.math.sqrt(r**2-2*n1**2)))
        if limit1 >= n1:
            limit1 = n1-1
        for n3 in range(1, limit1+1):
            sum = sum+24/(n1**2+n1**2+n3**2-0.5)
            plot(grid, n1, n1, n3)
    for n1 in range(1, r+1):
        if (3*n1**2 < r**2):
            sum = sum+8/(n1**2+n1**2+n1**2-0.5)
            plot(grid, n1, n1, n1)
    return sum
    

def grd(n):
    lttc = []
    for i in range(-n, n+1):
        temp = []
        for j in range(-n, n+1):
            temp2 = []
            for k in range(-n, n+1):
                temp2 = temp2+[0]
            temp = temp+[temp2]
        lttc = lttc+[temp]
    return lttc


def plot(grid, n1, n2, n3):
    n = int((len(grid[0][0])-1)/2)
    grid[n1+n][n2+n][n3+n] = grid[n1+n][n2+n][n3+n]+1


grid = grd(2)
print(sigma(2, grid), grid)