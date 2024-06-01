# 整数转字符串 str int float list tuple set bytes dict
num_int = 5
num_str = str(num_int)
print(type(num_str), num_str)
# 整数转浮点数
num_int = 5
num_float = float(num_int)
print(type(num_float), num_float)
# 浮点数转字符串
num_float = 13.14
num_str = str(num_float)
print(type(num_str), num_str)
# 浮点数转整数
num_float = 13.14
num_int = int(num_float)
print(type(num_int), num_int)
# 字符串转整数
# num_str = "你好"  # 错误示例
# num_int = int(num_str) #会报错
# print(num_int)
num_str = "123"
num_int = int(num_str)
print(type(num_int), num_int)
# 字符串转浮点数
num_str = "123.12"
num_float = float(num_str)
print(type(num_float), num_float)
# 字符串转布尔值
num_str = "111"  # 有值则为True
num_bool = bool(num_str)
print(type(num_bool), num_bool)
# 列表转元组
num_list = [1, 2, 3]
num_tuple = tuple(num_list)
print(type(num_tuple), num_tuple)
# 字符串转元组
num_str = "apple123"
num_tuple = tuple(num_str)
print(type(num_tuple), num_tuple)
# 字符串转列表
num_str = "apple123"
num_list = list(num_str)
print(type(num_list), num_list)
# 字符串转集合
num_str = "apple123"
num_set = set(num_str)
print(type(num_set), num_set)
# 字符串转字节
num_str = "apple123"
num_byte = bytes(num_str, encoding='utf-8')
print(type(num_byte), num_byte)
