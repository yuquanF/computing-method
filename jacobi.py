# -!- coding: utf-8 -!-
def Jacobi(mx, mr, n=100, c=0.0001):
    if len(mx) == len(mr):  # 若mx和mr长度相等则开始迭代 否则方程无解
        x = []  # 迭代初值 初始化为单行全0矩阵
        for i in range(len(mr)):
            x.append([0])
        count = 0  # 迭代次数计数
        while count < n:
            nx = []  # 保存单次迭代后的值的集合
            for i in range(len(x)):
                nxi = mr[i][0]
                for j in range(len(mx[i])):
                    if j != i:
                        nxi = nxi + (-mx[i][j]) * x[j][0]
                nxi = nxi / mx[i][i]
                nx.append([nxi])  # 迭代计算得到的下一个xi值
            lc = []  # 存储两次迭代结果之间的误差的集合
            for i in range(len(x)):
                lc.append(abs(x[i][0] - nx[i][0]))
            if max(lc) < c:
                print("迭代了{}次".format(count))
                return nx  # 当误差满足要求时 返回计算结果
            x = nx
            count = count + 1
        return False  # 若达到设定的迭代结果仍不满足精度要求 则方程无解
    else:
        return False


if __name__ == '__main__':
    mx = [[10, -1, -2], [-1, 10, -2], [-1, -1, 5]]

    mr = [[7.2], [8.3], [4.2]]
    res = Jacobi(mx, mr, 100, 0.00001)
    for v in res:
        print("%.6f" % v[0])
