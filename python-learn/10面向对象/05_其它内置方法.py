"""
演示Python内置的各类魔术方法
"""


class Student:
    def __init__(self, name, age):
        self.name = name        # 学生姓名
        self.age = age          # 学生年龄

    # __str__魔术方法
    def __str__(self):
        return f"Student类对象，name:{self.name}, age:{self.age}"

    # __lt__魔术方法
    def __lt__(self, other):
        return self.age < other.age  # 前一个小于后一个返回True

    # __le__魔术方法
    def __le__(self, other):
        return self.age <= other.age  # 前一个小于等于后一个返回True

    # __eq__魔术方法
    def __eq__(self, other):
        return self.age == other.age  # 前一个等于后一个返回True


stu1 = Student("周杰轮", 31)
stu2 = Student("林俊节", 36)
print(stu1 >= stu2)
print(stu1 == stu2)


#
