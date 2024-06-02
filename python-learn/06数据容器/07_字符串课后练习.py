"""
字符串课后练习演示
"itheima itcast boxuegu"
"""
my_str = "itheima itcast boxuegu"
# 统计字符串内有多少个"it"字符
count = my_str.count("it")
print(count)
# 将字符串内的空格，全部替换为字符："|" # replace对原字符串是没有影响的，会将结果返回给一个新字符串
new_str = my_str.replace(" ", "|")
print(new_str)
# 并按照"|"进行字符串分割，得到列表
my_list = new_str.split("|")
print(my_list)
