import math

if __name__ == '__main__':
    MIN = 1
    MAX = 2
    copy_min = MIN
    copy_max = MAX
    count = 0

    while True:
        MID = (MIN + MAX) / 2
        fun_min = math.pow(MIN, 3) + 10 * MIN - 20
        fun_max = math.pow(MAX, 3) + 10 * MAX - 20
        fun_mid = math.pow(MID, 3) + 10 * MID - 20

        count += 1
        print("第{}次迭代：".format(count))
        if abs(fun_mid) < 0.0001:
            print("函数在（{}, {}）上的根是：".format(copy_min, copy_max))
            print(MID)
            break
        elif fun_min * fun_mid < 0:
            MAX = MID
        else:
            MIN = MID
