import math

"""
设迭代方程为：x^3 - x^2 - 1 = 0, 在x=1.5附近有一个根
则 x = g(x) = math.pow(x ** 2 + 1, 1 / 3)
"""

x = 1.5  # 定义迭代初始值
err = 1e-4  # 定义误差

count = 0

if __name__ == '__main__':
    """
    默认收敛
    """
    x_next = math.pow(x ** 2 + 1, 1 / 3)
    while abs(x_next - x) > err:  # 当x+1 和 x 之间的相差的绝对值小于等于err时，说明收敛了
        x = x_next
        x_next = math.pow(x ** 2 + 1, 1 / 3)

        count += 1
        print("第{}次迭代：".format(count))
    print(x_next)
