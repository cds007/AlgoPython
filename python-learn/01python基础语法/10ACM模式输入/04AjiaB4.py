"""
输入描述：

输入数据包括多组。
每组数据一行,每行的第一个整数为整数的个数n(1 <= n <= 100), n为0的时候结束输入。
接下来n个正整数,即需要求和的每个正整数。

输出描述：

每组数据输出求和的结果

示例1
输入例子：

4 1 2 3 4
5 1 2 3 4 5
0

输出例子：

10
15


"""
import sys
for line in sys.stdin:
    a = list(map(int, line.split(" ")))
    if (a[0] == 0):
        break
    sum = 0
    for cnt in range(1, a[0]+1):
        sum += a[cnt]
    print(sum)
    # 也可以修改为
    # print(sum(a[1:]))
    # 切片操作 a[2:5:1] start stop step 左开右闭
