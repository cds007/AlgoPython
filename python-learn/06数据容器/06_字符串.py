"""
演示以数据容器的角色，学习字符串的相关操作
"""
my_str = "itheima and itcast"
# 通过下标索引取值
value = my_str[2]
value2 = my_str[-16]
print(f"从字符串{my_str}取下标为2的元素，。值是：{value},取下标为-16的元素。值是：{value2}")

# my_str[2] = "H"

# index方法
value = my_str.index("and")
print(f"在字符串{my_str}中查找and，其起始下标是：{value}")

# replace方法
new_my_str = my_str.replace("it", "程序")
print(f"将字符串{my_str}，进行替换后得到：{new_my_str}")

# split方法
my_str = "hello python itheima itcast"
my_str_list = my_str.split(" ")
print(f"将字符串{my_str}进行split切分后得到：{my_str_list}, 类型是：{type(my_str_list)}")
# 这里可以加上map函数实现int数组的转换
my_str = "1 2 3 4 5"
my_int_list = list(map(lambda x: int(x), my_str.split(" "))
                   )  # 也可以直接写map(int,my_str.split(" "))
print(f"将字符串{my_str}进行split切分后得到：{my_int_list}, 类型是：{type(my_int_list)}")

# strip方法
my_str = "  itheima and itcast  "
new_my_str = my_str.strip()  # 不传入参数，去除首尾空格
print(f"字符串{my_str}被strip后，结果：{new_my_str}")

my_str = "12itheima and itcast21"
new_my_str = my_str.strip("12")
print(f"字符串{my_str}被strip('12')后，结果：{new_my_str}")

# 统计字符串中某字符串的出现次数, count
my_str = "itheima and itcast"
count = my_str.count("it")
print(f"字符串{my_str}中it出现的次数是：{count}")
# 统计字符串的长度, len()
num = len(my_str)
print(f"字符串{my_str}的长度是：{num}")

# 分割和连接
s = "Hello, World!"
words = s.split(", ")  # 输出: ['Hello', 'World!']
joined = "-".join(words)  # 输出: 'Hello-World!'

"""
学了以下方法：
1.下标索引获取值
2.index()
3.replace()
4.split()
5.strip()
6.count()
7.len()
8.join()
"""
