"""
演示文件的写入
"""

# 打开文件，不存在的文件, r, w, a
import time
import json
# f = open("D:/test.txt", "w", encoding="UTF-8")
# # write写入
# f.write("Hello World!!!")       # 内容写入到内存中
# # flush刷新
# # f.flush()                       # 将内存中积攒的内容，写入到硬盘的文件中
# # close关闭
# f.close()                       # close方法，内置了flush的功能的
# 打开一个存在的文件
# f = open("D:/test.txt", "w", encoding="UTF-8")
# # write写入、flush刷新
# f.write("黑马程序员")
# # close关闭
# f.close()

# 直接用with open as f ，包括了上述方法
data = {'name': 'John', 'age': 30, 'city': 'New York'}
info_dict = {
    "王力鸿": {
        "部门": "科技部",
        "工资": 3000,
        "级别": 1
    },
    "周杰轮": {
        "部门": "市场部",
        "工资": 5000,
        "级别": 2
    },
    "林俊节": {
        "部门": "市场部",
        "工资": 7000,
        "级别": 3
    },
    "张学油": {
        "部门": "科技部",
        "工资": 4000,
        "级别": 1
    },
    "刘德滑": {
        "部门": "市场部",
        "工资": 6000,
        "级别": 2
    }
}

# data：这是一个Python数据结构（如字典、列表等），你想要将其转换为JSON格式并写入文件。
# file：这是一个文件对象，通常是通过使用open函数以写入模式打开的文件。
# ensure_ascii=False：这个参数指定是否确保所有非ASCII字符被转义。设置为False意味着非ASCII字符（如中文）将被直接写入文件，而不是转换为\uXXXX形式的转义序列。
# indent=4：这个参数指定JSON输出时的缩进级别。设置为4意味着每个层级将被缩进4个空格，这样可以使JSON文件的格式更加可读。

with open("./python-learn/07文件操作/info.json", "w", encoding="utf-8") as f:  # 文件不存在会自动创建
    json.dump(info_dict, f, ensure_ascii=False, indent=8)

# 目录的说明："data.json"直接这样写，会在根目录下创建一个文件。
# 想在当前目录下创建，还是得这样写了 "./python-learn/07文件操作/data.json"
