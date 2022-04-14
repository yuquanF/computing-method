import numpy as np


def solving(A):
    A = A.astype(np.float64)
    col = A.shape[1]  # 增广矩阵列数
    for i in range(col - 2):
        current_column = A[i:, i]
        max_index = np.argmax(current_column) + i  # 寻找最大元
        A[[i, max_index], :] = A[[max_index, i], :]  # 交换
        l = A[i + 1:, i] / A[i, i]  # 计算系数
        m = np.tile(A[i, :], (l.shape[0], 1)) * np.tile(l, (col, 1)).T  # 计算消元时减去的矩阵
        A[i + 1:, :] = A[i + 1:, :] - m  # 消元
    x = np.zeros(col - 1)
    for i in range(col - 2, -1, -1):
        x[i] = (A[i, -1] - np.dot(A[i, :-1], x.T)) / A[i, i]
    return x


if __name__ == '__main__':
    # 增广矩阵
    A = np.array([[1, 2, -1, 3],
                  [1, -1, 5, 0],
                  [4, 1, -2, 2]])
    x = solving(A)
    print(x)
