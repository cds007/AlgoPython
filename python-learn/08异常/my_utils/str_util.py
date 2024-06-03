"""
字符串相关的工具模块
"""


def str_reverse(str: str) -> str:
    """
    翻转字符串
    """
    result = ""
    for ch in range(len(str)-1, -1, -1):
        result += str[ch]
    return result
    # return s[::-1] 这样写也可以的


def substr(str: str, start: int, end: int) -> str:
    """
    截取字符串
    左开右闭的原则
    """
    return str[start:end]


if __name__ == "__main__":
    print(str_reverse("12345"))
    print(substr("12345", 1, 3))
