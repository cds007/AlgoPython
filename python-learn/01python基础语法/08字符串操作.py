# 1.字符串定义：单引号、双引号、三引号
# 在引号中包含引号
name = "'ch' "
name2 = '"ch" '
name3 = "\"ch\""
print(name+name2+name3)

# 2.字符串的拼接
# 字符串字面量之间的拼接
# 字符串字面量和字符串变量的拼接
# 全部用加号拼接就行
# 但是只能用于字符串拼接，整数类型需要先转换为字符串类型
name = "ch"
address = "建材城东路9号院"
tel = 4006189090
print("我是：" + name + "，我的地址是：" + address + "，我的电话是：" + str(tel))

# 3.字符串格式化
# 3种占位方式，%s string.format() f'string
name = "ch"
message = "学IT来：%s" % name
print(message)
# 通过占位的形式，完成数字和字符串的拼接
class_num = 57
avg_salary = 16781
message = "Python大数据学科，北京%s期，毕业平均工资：%s" % (class_num, avg_salary)
print(message)
name = "ch"
setup_year = 2006  # 不能用str了
stock_price = 19.99
message = "%s，成立于：%d，我今天的股价是：%f" % (name, setup_year, stock_price)
print(message)

# 第二种方式
name = "John"
age = 30
print("My name is {} and I am {} years old.".format(name, age+1))
print("My name is {0} and I am {1} years old.".format(name, age))
print("My name is {name} and I am {age} years old.".format(
    name="John", age=30))

# 第三种方式
name = "John"
age = 30
print(f"My name is {name} and I am {age} years old.")
print(
    f"My name is {name.upper()} and I will be {age + 1} years old next year.")


# 3.数字精度化控制
number = 3.14159
print("Number with width 10 and precision 3: %10.3f" % number)  # 宽度是10，精度是3
number = 3.14159
print("Number with width 10 and precision 3: {:10.3f}".format(number))
number = 3.14159
print(f"Number with width 10 and precision 3: {number:10.3f}")
number = 3.14159
print(f"Number left-aligned with width 10 and precision 3: {number:<10.3f}")
print(f"Number centered with width 10 and precision 3: {number:^10.3f}")
print(f"Number right-aligned with width 10 and precision 3: {number:>10.3f}")
print(f"nihao{number:10.3f}")

# 4.表达式格式化
expression = "1+2"
print(f"{expression}={1+2}")
print(f"type is {type(expression)}")
# 使用表达式作为 format() 方法的参数
width = 10
precision = 3
number = 3.14159
formatted_number = "{:.{precision}f}".format(number, precision=precision)
print(
    f"Number formatted with width {width} and precision {precision}: {formatted_number:>{width}}")
