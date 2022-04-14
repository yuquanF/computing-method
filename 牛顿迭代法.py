import math

"""
设迭代方程为：e^x - x - 3 = 0, 在x=1.5附近有一个根
导函数为：y = e^x - 1
则 迭代方程
  x_next = x - f(x) / f`(x) = x - (e^x - x - 3) / (e^x - 1)
"""

x = 2  # 定义迭代初始值
err = 1e-5  # 定义误差_

count = 0

if __name__ == '__main__':
    """
    默认收敛
    """
    x_next =  x - (math.exp(x) - x - 3) / (math.exp(x) - 1)
    while abs(x_next - x) > err:  # 当x+1 和 x 之间的相差的绝对值小于等于err时，说明收敛了
        x = x_next
        x_next = x - (math.exp(x) - x - 3) / (math.exp(x) - 1)

        count += 1
        print("%.5f"% x_next)
    print("%.5f" % x_next)
