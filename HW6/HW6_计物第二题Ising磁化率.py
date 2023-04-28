import numpy as np
import matplotlib.pyplot as plt
import random as rand


N = 80
J = 2
q = 2


def SingleE(A, i, j):
    E = 0
    if i >= 1 and i <= N-2 and j >= 1 and j <= N-2:
        if A[i][j] == A[i+1][j]:
            E = E-J
        if A[i][j] == A[i-1][j]:
            E = E-J
        if A[i][j] == A[i][j-1]:
            E = E-J
        if A[i][j] == A[i][j+1]:
            E = E-J
    if i >= 1 and i <= N-2 and j == 0:
        if A[i][0] == A[i+1][0]:
            E = E-J
        if A[i][0] == A[i-1][0]:
            E = E-J
        if A[i][0] == A[i][1]:
            E = E-J
        if A[i][0] == A[i][N-1]:
            E = E-J
    if i >= 1 and i <= N-2 and j == N-1:
        if A[i][N-1] == A[i+1][N-1]:
            E = E-J
        if A[i][N-1] == A[i-1][N-1]:
            E = E-J
        if A[i][N-1] == A[i][0]:
            E = E-J
        if A[i][N-1] == A[i][N-2]:
            E = E-J
    if j >= 1 and j <= N-2 and i == 0:
        if A[0][j] == A[0][j+1]:
            E = E-J
        if A[0][j] == A[0][j-1]:
            E = E-J
        if A[0][j] == A[1][j]:
            E = E-J
        if A[0][j] == A[N-1][j]:
            E = E-J
    if j >= 1 and j <= N-2 and i == N-1:
        if A[N-1][j] == A[N-1][j+1]:
            E = E-J
        if A[N-1][j] == A[N-1][j-1]:
            E = E-J
        if A[N-1][j] == A[0][j]:
            E = E-J
        if A[N-1][j] == A[N-2][j]:
            E = E-J
    if i == 0 and j == 0:
        if A[0][0] == A[0][1]:
            E = E-J
        if A[0][0] == A[1][0]:
            E = E-J
        if A[0][0] == A[N-1][0]:
            E = E-J
        if A[0][0] == A[0][N-1]:
            E = E-J
    if i == 0 and j == N-1:
        if A[0][N-1] == A[1][N-1]:
            E = E-J
        if A[0][N-1] == A[0][0]:
            E = E-J
        if A[0][N-1] == A[0][N-2]:
            E = E-J
        if A[0][N-1] == A[N-1][N-1]:
            E = E-J
    if i == N-1 and j == 0:
        if A[N-1][0] == A[N-1][1]:
            E = E-J
        if A[N-1][0] == A[N-1][N-1]:
            E = E-J
        if A[N-1][0] == A[N-2][0]:
            E = E-J
        if A[N-1][0] == A[0][0]:
            E = E-J
    if i == N-1 and j == N-1:
        if A[N-1][N-1] == A[0][N-1]:
            E = E-J
        if A[N-1][N-1] == A[N-1][0]:
            E = E-J
        if A[N-1][N-1] == A[N-2][N-1]:
            E = E-J
        if A[N-1][N-1] == A[N-1][N-2]:
            E = E-J
    return E 



def Energy(A):
    E = 0
    for i in range(0, N):
        for j in range(0, N):
            E = E+SingleE(A, i, j)+2*J
    E = E/2
    for i in range(0, N):
        for j in range(0, N):
            E = E-(A[i][j]-1/2)
    return E


def Magnetic(A):
    M = 0
    for i in range(0, N):
        for j in range(0, N):
            M = M+(A[i][j]-1/2)
    return M


M = []
for T in np.arange(1.25, 3.25, 0.25):
    print(T)
    lattice = []
    for i in range(0, N):
        temp = []
        for j in range(0, N):
            temp.append(rand.randint(0, q-1))
        lattice.append(temp)
    sum = 0
    m = Magnetic(lattice)
    for n in range(0, 100000):
        for i in range(0, N):
            for j in range(0, N):
                spin_old = lattice[i][j]
                energy_old = SingleE(lattice, i, j)-lattice[i][j]
                spin_new = rand.randint(0, q-1)
                lattice[i][j] = spin_new
                energy_new = SingleE(lattice, i, j)-lattice[i][j]
                delta = energy_new-energy_old
                deltam = spin_new-spin_old
                if delta <= 0:
                    break
                if delta > 0:
                    if rand.random() < np.exp(-delta/(T)):
                        break
                    else:
                        lattice[i][j] = spin_old
                        delta = 0
                        deltam = 0
                m = m+deltam
                sum = sum+m/(N*N*100000)
    M.append(sum)


fig = plt.figure(figsize = (10, 8))
plt.xlabel("T")  
plt.ylabel("M")  
plt.xlim(1, 3.25)
plt.grid()
plt.plot(np.arange(1.25, 3.25, 0.25), M)
plt.show()