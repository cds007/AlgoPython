"""
讲解面向对象-封装特性课后练习题
设计带有私有成员的手机
"""

# 设计一个类，用来描述手机


class Phone:
    __is_5g_enable = False

    def __check_5g(self):
        if self.__is_5g_enable:
            print('5g开启')
        else:
            print('5g关闭，使用4g网络')

    def call_by_5g(self):
        self.__check_5g()
        print('正在通话中')

    def __init__(self, radius):
        self.__radius = radius

    @property
    def radius(self):
        return self.__radius

    @radius.setter
    def radius(self, value):
        if value < 0:
            raise ValueError("Radius cannot be negative")
        self.__radius = value


phone = Phone(21)
phone.call_by_5g()
print(phone.radius)  # 装饰器对于私有属性也是可以访问的
