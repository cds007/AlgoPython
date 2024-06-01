"""
演示lambda匿名函数
"""


# 定义一个函数，接受其它函数输入
def test_func(compute):
    result = compute(1, 2)
    print(f"结果是:{result}")


# 通过lambda匿名函数的形式，将匿名函数作为参数传入
def add(x, y):
    return x + y


test_func(add)
test_func(lambda x, y: x + y)


# 一个简单的lambda函数，接受一个参数x并返回它的平方
def square(x): return x * x


print(square(5))  # 输出: 25

# 使用lambda函数作为sorted()函数的key参数
my_list = [{'name': 'John', 'age': 25}, {'name': 'Jane', 'age': 22}]
sorted_list = sorted(my_list, key=lambda x: x['age'])
# 输出: [{'name': 'Jane', 'age': 22}, {'name': 'John', 'age': 25}]
print(sorted_list)

# 使用lambda函数作为map()函数的参数
numbers = [1, 2, 3, 4, 5]
squared_numbers = map(lambda x: x * x, numbers)
print(list(squared_numbers))  # 输出: [1, 4, 9, 16, 25]

# 使用lambda函数作为filter()函数的参数
even_numbers = filter(lambda x: x % 2 == 0, numbers)
print(list(even_numbers))  # 输出: [2, 4]
