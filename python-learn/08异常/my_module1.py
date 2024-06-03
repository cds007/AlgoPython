__all__ = ['test_a', 'testA']  # * 只能导入all里面的


def test_a(a, b):
    return a+b


def testA(a, b):
    return a+b


def testB(a, b):
    return a-b


def test(a, b):
    return a+b
