"""
演示类的构造方法
"""
# 演示使用构造方法对成员变量进行赋值
# 构造方法的名称：__init__

"""
案例，通过构造方法完成学生信息的录入
"""


class Student:

    def __init__(self, name, age, addr):
        self.name = name
        self.age = age
        self.addr = addr


if __name__ == "__main__":
    for i in range(10):
        print(f"当前录入{i+1}名同学的信息，总共需要10名同学信息")
        name = input("请输入学生姓名：")
        age = int(input("请输入学生年龄："))
        addr = input("请输入学生地址：")
        stu = Student(name, age, addr)
        print(f"学生{i+1}的信息录入完成，信息为【学生姓名：{stu.name}】")
