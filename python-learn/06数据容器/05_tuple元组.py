"""
演示tuple元组的定义和操作
"""

# 定义元组
t1 = (1, "Hello", True)
t2 = ()
t3 = tuple()
print(f"t1的类型是：{type(t1)}, 内容是：{t1}")
print(f"t2的类型是：{type(t2)}, 内容是：{t2}")
print(f"t3的类型是：{type(t3)}, 内容是：{t3}")

# 定义单个元素的元素
t4 = ("hello", )  # 必须加上这个空的逗号，不然会被识别为str类型
print(f"t4的类型是：{type(t4)}, t4的内容是：{t4}")
# 元组的嵌套
t5 = ((1, 2, 3), (4, 5, 6))
print(f"t5的类型是：{type(t5)}, 内容是：{t5}")

# 下标索引去取出内容
num = t5[1][2]
print(f"从嵌套元组中取出的数据是：{num}")

# 元组的操作：index查找方法
t6 = ("传智教育", "黑马程序员", "Python")
index = t6.index("黑马程序员")
print(f"在元组t6中查找黑马程序员，的下标是：{index}")
# 元组的操作：count统计方法
t7 = ("传智教育", "黑马程序员", "黑马程序员", "黑马程序员", "Python")
num = t7.count("黑马程序员")
print(f"在元组t7中统计黑马程序员的数量有：{num}个")
# 元组的操作：len函数统计元组元素数量
t8 = ("传智教育", "黑马程序员", "黑马程序员", "黑马程序员", "Python")
num = len(t8)
print(f"t8元组中的元素有：{num}个")
# 元组的遍历：while
index = 0
while index < len(t8):
    print(f"元组的元素有：{t8[index]}")
    # 至关重要
    index += 1

# 元组的遍历：for
for element in t8:
    print(f"2元组的元素有：{element}")

# 修改元组内容
# t8[0] = "itcast"

# 定义一个元组
t9 = (1, 2, ["itheima", "itcast"])
print(f"t9的内容是：{t9}")
# 如果元组里是list，那么这个list的内容是可以改的，但是list整体是不能改的，这还是引用类型的知识，内存地址不可变，里面的值可以变。
t9[2][0] = "黑马程序员"
t9[2][1] = "传智教育"
# t9[2] = [1, 2]  # 不行
print(f"t9的内容是：{t9}")

# 元组的拼接 不能修改，但是能拼接，因为tuple1和tuple2并没有修改，拼接后的是一个新元组！不矛盾。
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
combined_tuple = tuple1 + tuple2
print(combined_tuple)
