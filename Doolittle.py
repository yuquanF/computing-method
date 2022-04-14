import numpy as np


def Doolittle(A):
    """杜立特分解求LU"""
    n = len(A)
    L = np.zeros((n, n), dtype=np.float64)
    U = np.zeros((n, n), dtype=np.float64)
    A = A.astype(np.float64)

    for k in range(0, n):
        L[k][k] = 1

        # 求U
        for j in range(k, n):
            suma = 0
            s = 0
            while (s <= k - 1):
                suma = suma + (L[k][s] * U[s][j])
                s = s + 1
            U[k][j] = A[k][j] - suma

        # 求L
        for i in range(k + 1, n):
            suma = 0
            s = 0
            while (s <= k - 1):
                suma = suma + (L[i][s] * U[s][k])
                s = s + 1
            if U[k][k] == 0.0:
                raise ZeroDivisionError("0在矩阵A的对角线处。")
            else:
                L[i][k] = (A[i][k] - suma) / U[k][k]
    return L, U


def calcY(L, B):
    n = len(B)
    B = B.astype(np.float64)
    Y = np.zeros((n), dtype=np.float64)
    Y[0] = B[0]

    for row in range(0, n):
        sum = 0
        column = 0
        while (column <= row - 1):
            sum = sum + (L[row][column] * Y[column])
            column = column + 1
        Y[row] = B[row] - sum

    return Y


def calcX(U, Y):
    n = len(Y)
    Y = Y.astype(np.float64)
    X = np.zeros((n), dtype=np.float64)

    row = n - 1
    X[row] = Y[n - 1] / U[row][row]
    row -= 1

    # runs in reverse order lol
    while (row >= 0):
        sum = 0
        column = n - 1
        while (column >= 0):
            sum = sum + (U[row][column] * X[column])
            column = column - 1
        if U[row][row] == 0.0:
            raise ZeroDivisionError("0在矩阵A的对角线处。.")
        else:
            X[row] = (Y[row] - sum) / U[row][row]
        row -= 1

    return X


if __name__ == '__main__':
    A = np.array([[1, 2, -1],
                  [1, -1, 5],
                  [4, 1, -2]])
    B = np.array([3, 0, 2])
    L, U = Doolittle(A)
    print("Matrix L: \n{} \nMatrix U: \n{}\n".format(L, U))
    Y = calcY(L, B)
    X = calcX(U, Y)
    print("Matrix Y: \n{}\n".format(Y))
    print("Matrix X: \n{}\n".format(X))
