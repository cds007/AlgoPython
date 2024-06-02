"""
演示使用while和for循环遍历列表
"""

# 1.while循环


def list_while_func(list):
    """
    使用while循环遍历列表的演示函数
    :return: None
    """
    # 循环控制变量：通过下标索引来控制，默认0
    # 每一次循环将下标苏姚
    index = 0
    print("######while#######")
    while index < len(list):
        print(f"列表的第{index}个元素的值是{list[index]}")
        index += 1

# 2.for循环


def list_for_func(list):
    """
    使用for循环遍历列表的演示函数
    :return:
    """
    print("######for#######")
    for i in range(len(list)):
        print(f"列表的第{i}个元素的值是{list[i]}")


# 其他遍历方法：（高级）
# 3.enumerate()函数返回索引和元素值
def list_enumerate_func(list):
    print("######enumerate#######")
    for index, element in enumerate(list):
        print(f"列表的第{index}个元素的值是{element}")

# 4.列表推导式


def list_infer_func(list):
    print("######infer#######")
    # 列表推导式是一种更高级的遍历方法，它可以用来创建新的列表。
    # 以下方法将只计算列表中整数元素的平方，并创建一个新的列表。
    # isinstance() 是 Python 中的一个内置函数，用于检查一个对象是否是一个已知的类型，或者来自一个继承自那种类型的子类。
    square_list = [x**2 for x in list if isinstance(x, int)]
    print(square_list)

# 5.map和filter函数


def list_map_filter_func(list_input):
    print("######map filter#######")
    # map() 和 filter() 函数也可以用于遍历列表，并对列表元素进行操作。
    # 以下方法将使用 filter() 函数来选择整数元素，然后使用 map() 函数来计算它们的平方。
    square_list = list(
        map(lambda x: x**2, filter(lambda x: isinstance(x, int), list_input)))
    # filter函数和map函数都是返回一个迭代器。
    # 他们俩的参数都是一个函数和一个可迭代对象（列表、元组、字符串或迭代器等）
    # 迭代对象也可以是多个，对应的，函数的参数也是多个
    print(square_list)

# 6.小练习取偶数


def list_even_func(list_input):
    num_list = filter(lambda x: isinstance(x, int), list_input)  # 是整数
    even_list = list(filter(lambda x: x % 2 == 0, num_list))  # 是偶数
    return even_list


mylist = [1, 2, 3, 4, 6, 'a', 'b', 'c']
list_for_func(mylist)
list_while_func(mylist)
list_enumerate_func(mylist)
list_infer_func(mylist)
list_map_filter_func(mylist)
print(list_even_func(mylist))
