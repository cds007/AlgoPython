"""
输入描述：

输入第一行包括一个数据组数t(1 <= t <= 100)
接下来每行包括两个正整数a,b(1 <= a, b <= 1000)

输出描述：

输出a+b的结果

示例1
输入例子：

2
1 5
10 20

输出例子：

6
30


"""
import sys  # 我觉得只有一行一行读是符合题意的，所以不能用sys.stdin
n = int(sys.stdin.readline())  # 只读一行
for i in range(n):
    line = sys.stdin.readline().split(" ")
    print(int(line[0])+int(line[1]))

# 法2 ，我觉得这个有点抽象了，是停不下来的
# for i in sys.stdin:
#     for line in sys.stdin:
#         a = line.split()
#         print(int(a[0]) + int(a[1]))

# 法3，更抽象了
# n = int(input())

# for line in sys.stdin:
#     aa = line.split()
#     print(int(aa[0]) + int(aa[1]))
