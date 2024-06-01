"""
输入描述：

输入有两行，第一行n

第二行是n个字符串，字符串之间用空格隔开

输出描述：

输出一行排序后的字符串，空格隔开，无结尾空格

示例1
输入例子：

5
c d a bb e

输出例子：

a bb c d e


"""
import sys

n = sys.stdin.readline()
str_list = list(map(str, sys.stdin.readline().split()))
str_list.sort()
new_str = ""
for i in range(len(str_list)):
    new_str += str_list[i]
    new_str += " "
print(new_str[0:len(new_str)])

# 法2
# t=int(input().strip()) # strip()函数是去除首尾空白字符的
# list1=list(input().strip().split())
# list1.sort()
# result=' '.join(list1)
# print(result)
