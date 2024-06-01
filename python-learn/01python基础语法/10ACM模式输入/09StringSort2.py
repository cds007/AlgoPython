"""
输入描述：

多个测试用例，每个测试用例一行。

每行通过空格隔开，有n个字符，n＜100

输出描述：

对于每组测试用例，输出一行排序过的字符串，每个字符串通过空格隔开

示例1
输入例子：

a c bb
f dddd
nowcoder

输出例子：

a bb c
dddd f
nowcoder


"""
import sys

for line in sys.stdin:
    str_list = list(line.split())
    str_list.sort()
    result = " ".join(str_list)
    print(result)
