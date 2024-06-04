"""
演示面向对象类中的成员方法定义和使用
"""

# 定义一个带有成员方法的类


class Student:
    name = None     # 学生的姓名

    def say_hi(self):
        print(f"大家好呀，我是{self.name}，欢迎大家多多关照")

    def say_hi2(self, msg):
        print(f"大家好，我是：{self.name}，{msg}")


stu = Student()
stu.name = "周杰轮"
stu.say_hi2("哎哟不错哟")

stu2 = Student()
stu2.name = "林俊节"
stu2.say_hi2("小伙子我看好你")

# 实例方法、类方法、静态方法的区别如下：


class MyClass:
    # 类属性
    class_attribute = "I'm a class attribute"

    def __init__(self, value):
        # 实例属性
        self.instance_attribute = value

    # 实例方法
    def instance_method(self):
        print(f"Instance method: {self.instance_attribute}")

    # 类方法
    @classmethod
    def class_method(cls):
        print(f"Class method: {cls.class_attribute}")

    # 静态方法
    @staticmethod
    def static_method():
        print("Static method. No access to class or instance attributes.")


# 创建 MyClass 的一个实例
my_instance = MyClass("I'm an instance attribute")

# 调用实例方法
my_instance.instance_method()

# 调用类方法
MyClass.class_method()

# 调用静态方法
MyClass.static_method()
