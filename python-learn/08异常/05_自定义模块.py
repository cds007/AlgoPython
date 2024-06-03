"""
演示自定义模块
"""

# 1.导入自定义模块使用
# import my_module1
# from my_module1 import test
# test(1, 2)

# 2.导入不同模块的同名功能 ！会使用后一个的功能
# from my_module1 import test
# from my_module2 import test
# test(1, 2)

# 3.__main__变量
# from my_module1 import test
# 如果在module1中调用了test，那么在导入的时候就会直接执行模块1里的test函数，所以在module1需要这样写： if __name__ == "__main__":


# 4.__all__变量
# 如果一个模块文件中有`_all_`变量，当使用from xxx import*为导入时，只能导入这个列表中的元素
from my_module1 import testB  # 可以手动导入
from my_module1 import *
test_a(1, 2)
testA(1, 2)
# test_b(2, 1)
testB(2, 1)
