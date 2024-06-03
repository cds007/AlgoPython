"""
演示异常、模块、包的综合案例练习
"""
# 创建my_utils 包， 在包内创建：str_util.py 和 file_util.py 2个模块，并提供相应的函数

import my_utils.str_util
from my_utils import file_util
import os

print(my_utils.str_util.str_reverse("ch是我"))
print(my_utils.str_util.substr("ch是谁", 0, 3))

cur_path = os.path.abspath(__file__)
cur_dir = os.path.dirname(cur_path)
file_path = os.path.join(cur_dir, "test_append.txt")
file_util.append_to_file(file_path, "hello!")
file_util.print_file_info(file_path)
