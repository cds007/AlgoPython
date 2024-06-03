"""
演示对文件的读取
"""

# 打开文件
import os
import time
current_directory = os.getcwd()
file_path = os.path.join(current_directory, 'python-learn\\07文件操作\\test.txt')

f = open(file_path, "r", encoding="UTF-8")  # mode：r,w,a
print(type(f))
# 读取文件 - read()
# print(f"读取10个字节的结果：{f.read(10)}")
# print(f"read方法读取全部内容的结果是：{f.read()}")
print("-----------------------------------------------")
# 读取文件 - readLines()
lines = f.readlines()   # 读取文件的全部行，封装到列表中
print(f"lines对象的类型：{type(lines)}")
print(f"lines对象的内容是：{lines}")

# 读取文件 - readline()
f = open(file_path, 'r', encoding="utf-8")
line1 = f.readline()
line2 = f.readline()
line3 = f.readline()
print(f"第一行数据是：{line1}")
print(f"第二行数据是：{line2}")
print(f"第三行数据是：{line3}")

# for循环读取文件行
for line in f:
    print(f"每一行数据是:{line}")
# 文件的关闭
f.close()
# time.sleep(2000)
# with open 语法操作文件

with open(file_path, "r", encoding="UTF-8") as f:  # 可以自动完成close的操作
    for line in f:
        print(f"每一行数据是：{line}")

# time.sleep(500000)
