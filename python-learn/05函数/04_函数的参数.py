"""
演示函数使用参数
"""

# 定义2数相加的函数，通过参数接收被计算的2个数字


def add(x, y, z):
    result = x + y + z
    print(f"{x} + {y} + {z}的计算结果是：{result}")


# 调用函数，传入被计算的2个数字
add(5, 6, 7)


def put(list):
    list[0] = 2


list = [1, 2]
put(list)
print(list[0])  # 输出2，说明list这种跟java差不多的，是引用类型
