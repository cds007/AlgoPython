"""
演示List常用操作的课后练习
"""

# 定义列表
ages = [21, 25, 21, 23, 22, 20]
# 追加31
ages.append(31)
# 追加新列表
age_new = [29, 33, 30]
ages.extend(age_new)
# 取出第一个元素
ele_fir = ages.pop(0)
print(ele_fir)
# 取出最后一个元素
ele_last = ages.pop(-1)
print(ele_last)
# 查找31的下标
index = ages.index(31)
print(index)
print(ages)
