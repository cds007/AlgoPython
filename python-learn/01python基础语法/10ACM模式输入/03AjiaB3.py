"""
输入描述：

输入包括两个正整数a,b(1 <= a, b <= 10^9),输入数据有多组, 如果输入为0 0则结束输入

输出描述：

输出a+b的结果

示例1
输入例子：

1 5
10 20
0 0

输出例子：

6
30

"""
import sys
for line in sys.stdin:
    a = line.split(" ")
    if (int(a[0]) == 0 and int(a[1]) == 0):
        break
    print(int(a[0])+int(a[1]))


# 法2
for line in sys.stdin:
    # map是一个迭代函数，用于将line.split()之后的结果都执行一遍int函数，然后返回一个迭代器
    a = list(map(int, line.split()))
    # list用于将迭代器再转换为list类型
    if a == [0, 0]:
        break
    else:
        print(a[0]+a[1])

# 法3
while (nums := input()) != "0 0":  # :=是海象运算符，可以在表达式中执行赋值的操作
    nums = list(map(int, nums.split(" ")))
    print(sum(nums))

# map的应用
# 示例1：数据类型转换
strings = ['1', '2', '3', '4']
numbers = list(map(int, strings))  # 结果：[1, 2, 3, 4]

# 示例2：统一数据格式
dates = ['2023-01-01', '2023/02/02', '2023-03-03']
# 结果：['2023/01/01', '2023/02/02', '2023/03/03']
formatted_dates = list(map(lambda x: x.replace('-', '/'), dates))

# 示例3：数值计算
numbers = [1, 2, 3, 4]
squared = list(map(lambda x: x**2, numbers))  # 结果：[1, 4, 9, 16]

# 示例4：字符串操作
words = ['hello', 'world']
capitalized = list(map(str.capitalize, words))  # 结果：['Hello', 'World']

# 示例5：函数组合


def add(a, b):
    return a + b


def multiply(a, b):
    return a * b


funcs = [add, multiply]
for func in funcs:
    result = list(map(func, [1, 2, 3], [4, 5, 6]))
    print(result)  # 结果：[5, 7, 9] 和 [4, 10, 18]

# 示例6：自定义操作
people = [{'name': 'John', 'age': 28}, {'name': 'Jane', 'age': 24}]
ages = list(map(lambda x: x['age'], people))  # 结果：[28, 24]
