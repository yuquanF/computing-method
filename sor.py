import numpy as np

"""
逐次超松弛迭代法(SOR方法):
  SOR方法是将赛德尔迭代公式(3.44）稍加改进而得到的一种加速迭代法﹐是解大型稀疏矩阵方程组的有效方法之一．
  该方法具有计算公式简单,程序设计容易﹐占用计算机内存较少等优点,若能选择较好的松弛因子,其收敛速度就得到加快．

公式： x^(k+1) = (D−ωL)^−1 * (ωU+(1−ω)D)x^(k) + ω(D−ωL)^−1*b

"""

def sor(A, b, w, k):
    n = A.shape[1]  # 获取系数矩阵的列数
    D = np.eye(n)
    D[np.arange(n), np.arange(n)] = A[np.arange(n), np.arange(n)]
    LU = D - A
    L = np.tril(LU)
    U = np.triu(LU)
    D_wL = D - w * L
    X = np.zeros(n)
    print("第", 0, "次迭代的结果：", X)
    for i in range(k):
        D_wL_inv = np.linalg.inv(D_wL)
        X = np.dot(np.dot(D_wL_inv, w * U + (1 - w) * D), X) + w * np.dot(D_wL_inv, b)
        print("第", i + 1, "次迭代的结果：", X)
    return X


if __name__ == '__main__':
    A = np.array([
        [4, -2, -4],
        [-2, 17, 10],
        [-4, 10, 9]
    ])
    b = np.array([10, 3, -7])
    w = 1.46
    k = 20
    sor(A, b, w, k)  # 精确解是（2，1，-1）
