"""
输入描述：

输入包括两个正整数a,b(1 <= a, b <= 1000),输入数据包括多组。

输出描述：

输出a+b的结果

示例1
输入例子：

1 5
10 20

输出例子：

6
30

"""
import sys

for line in sys.stdin:  # 会读取每一行，然后将每一行分为两个值，直到ctrl+c
    a = line.split()
    print(int(a[0]), int(a[1]))
