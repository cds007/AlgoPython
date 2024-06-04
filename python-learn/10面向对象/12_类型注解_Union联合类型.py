"""
演示Union联合类型注解
"""
# 使用Union类型，必须先导包
from typing import Union

my_list: list[Union[int, str]] = [1, 2, "itheima", "itcast"]

my_dict: dict[str, Union[int, str]] = {'a': 1, 'b': '周杰伦'}


def func(data: Union[int, str]) -> Union[int, str]:
    pass

# 联合类型注解，既可以是int也可以是str
