# 检查一个变量是否是整数
x = 100
print(isinstance(x, int))  # 输出: True

# 检查一个变量是否是字符串
y = "hello"
print(isinstance(y, str))  # 输出: True

# 检查一个变量是否是列表
z = [1, 2, 3]
print(isinstance(z, list))  # 输出: True

# 检查一个变量是否是元组
t = (1, 2, 3)
print(isinstance(t, tuple))  # 输出: True

# 检查一个变量是否是多种类型中的一种
a = 200
print(isinstance(a, (int, str, list)))  # 输出: True

# 检查一个类是否是另一个类的子类


class Parent:
    pass


class Child(Parent):
    pass


child_instance = Child()
print(isinstance(child_instance, Parent))  # 输出: True


"""
isinstance() 是 Python 中的一个内置函数，用于检查一个对象是否是一个已知的类型，
或者来自一个继承自那种类型的子类。这个函数通常用于确保一个变量是期望的类型，或者在执行特定操作之前进行类型检查。
"""
