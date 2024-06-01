"""
输入描述：

输入数据有多组, 每行表示一组输入数据。

每行不定有n个整数，空格隔开。(1 <= n <= 100)。

输出描述：

每组数据输出求和的结果

示例1
输入例子：

1 2 3
4 5
0 0 0 0 0

输出例子：

6
9
0


"""
import sys

for line in sys.stdin:
    nums = list(map(int, line.split()))
    print(sum(nums))
