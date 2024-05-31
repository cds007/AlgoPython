# 1.input
import argparse
import sys
import getpass
name = input("请输入你的名字: ")
print(f"你好, {name}!")

# 2.getpass密码
password = getpass.getpass("请输入你的密码: ")
print(f"你的密码是: {password}")

# 3.sys
if len(sys.argv) == 2:
    name = sys.argv[1]
    print(f"你好, {name}! 我是sys")
else:
    print("命令行参数错误，需要输入一个名字。")
# python python-learn\01python基础语法\09python数据输入.py ch

# 4.argparse
parser = argparse.ArgumentParser(description="这是一个简单的命令行程序。")
parser.add_argument("name", help="请输入你的名字。")
args = parser.parse_args()
print(f"你好, {args.name}! 我是argparse")

# 5.高级用法
parser2 = argparse.ArgumentParser(description="参数解析程序2")
# 所以最规范的是无论是必需还是非必需都加上-
parser2.add_argument('-param1', type=str, help='第一个必选参数。')
# invalid option string 'arg2': must start with a character '-'
parser2.add_argument("-arg2", "--param2", help='第二个可选参数。',
                     required=False)  # 如果不是必需的，那么得开始with -
parser2.add_argument('-param3', help='第三个必选参数。', required=True)
args = parser2.parse_args()
# 输出结果
print(f"第一个必选参数: {args.param1}")
if args.param2:
    print(f"第二个可选参数: {args.param2}")
print(f"第三个必选参数: {args.param3}")
# python python-learn\01python基础语法\09python数据输入.py -param1=ch -arg2=22 -param3=33
