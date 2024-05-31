# 算术运算符
# 1.除法
print(3/2)  # 浮点数除
# 2.整除
print(3//2)
# 3.幂运算
print(3**2)

# 赋值运算符
# 1.除法赋值
a = 6
a /= 4
print(a)
# 2.整除赋值
a = 6
a //= 4
print(a)
# 3.幂赋值
a = 6
a **= 2
print(a)

# 逻辑运算符
# 与或非
# 和java中的区别 && || !  <-> and or not

# 身份运算符
# 1.is：判断两个变量是否引用同一个对象，例如 a is b
a = [1, 2, 3]
b = a
print(a is b)
# 2.is not：判断两个变量是否不引用同一个对象，例如 a is not b
a = [1, 2, 3]
b = [1, 2, 3]
print(a is not b)

# 成员运算符
# 1.in
a = ["apple", "orange", "banana"]
b = "apple"
print(b in a)
# 2.not in
b = "cherry"
print(b not in a)

# 位运算符
# 1.按位与
print(3 & 2)
# 2.按位或
print(3 | 2)
# 3.按位异或
print(3 ^ 2)
# 4.按位取反
# 补码：0000 0000 0000 0000 0000 0000 0000 0011 3
#       1111 1111 1111 1111 1111 1111 1111 1100 -4
print(~3)
# 5.左移
print(3 << 2)
# 6.右移
print(3 >> 2)
