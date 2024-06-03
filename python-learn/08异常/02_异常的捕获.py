"""
演示捕获异常
"""

# 1.基本捕获语法
# try:
#     f = open("D:/abc.txt", "r", encoding="UTF-8")
# except:
#     print("出现异常了，因为文件不存在，我将open的模式，改为w模式去打开")
#     f = open("D:/abc.txt", "w", encoding="UTF-8")

# 2.捕获指定的异常
# try:
#     print(name)
#     # 1 / 0
# except NameError as e:
#     print("出现了变量未定义的异常")
#     print(e)
# 3.捕获多个异常
# try:
#     # 1 / 0
#     print(name)
# except (NameError, ZeroDivisionError) as e:
#     print("出现了变量未定义 或者 除以0的异常错误")
# 未正确设置捕获异常类型，将无法捕获异常

# 3.捕获所有异常
try:
    f = open("D:/123.txt", "r", encoding="UTF-8")
except Exception as e:
    print("出现异常了")
    print(f"异常名为{e}")
    # f = open("D:/123.txt", "w", encoding="UTF-8")
else:  # 没有异常的时候执行
    print("好高兴，没有异常。")
finally:  # 无论是否出现异常都执行
    print("我是finally，有没有异常我都要执行")
    # f.close()
