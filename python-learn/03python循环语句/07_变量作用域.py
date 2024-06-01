"""
演示Python for循环临时变量的作用域
"""
# i = 0 # 也可以提前定义
for i in range(5):
    print(i)

print(i)
# 规范上不可以访问，规范上不建议这么做
# 实际上可以访问到，i是4.
