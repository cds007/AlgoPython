"""
演示面向对象封装思想中私有成员的使用
"""

# 定义一个类，内含私有成员变量和私有成员方法


class Phone:
    __current_voltage = 0.5        # 当前手机运行电压

    _aa = 0.5  # 单下划线是不强制私有

    def __keep_single_core(self):  # 方法和属性前面加两个下划线是私有属性（私有方法）只能内部自己使用
        print("让CPU以单核模式运行")

    def call_by_5g(self):
        if self.__current_voltage >= 1:
            print("5g通话已开启")
        else:
            self.__keep_single_core()
            print("电量不足，无法使用5g通话，并已设置为单核运行进行省电。")


phone = Phone()
phone.call_by_5g()
print(phone._aa)
