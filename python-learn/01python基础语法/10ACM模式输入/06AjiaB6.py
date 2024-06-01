"""
输入描述：

输入数据有多组, 每行表示一组输入数据。
每行的第一个整数为整数的个数n(1 <= n <= 100)。
接下来n个正整数, 即需要求和的每个正整数。

输出描述：

每组数据输出求和的结果

示例1
输入例子：

4 1 2 3 4
5 1 2 3 4 5

输出例子：

10
15


"""
import sys

for line in sys.stdin:
    nums = list(map(int, line.split()))
    print(sum(nums[1:]))
