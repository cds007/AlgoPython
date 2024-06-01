"""
输入描述：

多个测试用例，每个测试用例一行。
每行通过,隔开，有n个字符，n＜100

输出描述：

对于每组用例输出一行排序后的字符串，用','隔开，无结尾空格

示例1
输入例子：

a,c,bb
f,dddd
nowcoder

输出例子：

a,bb,c
dddd,f
nowcoder


"""
import sys

for line in sys.stdin:
    str_list = list(line.strip().split(","))
    str_list.sort()
    result = ",".join(str_list)
    print(result)
