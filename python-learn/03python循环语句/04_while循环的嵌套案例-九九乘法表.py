"""
演示使用while的嵌套循环
打印输出九九乘法表
"""
# 1.输出不换行： print("Hello",end="")
# 2.制表符： print("Hello\tWorld")
for i in range(1, 10):
    for j in range(1, i+1):
        print(f"{j}*{i}={j*i}\t", end="")
    print("")
