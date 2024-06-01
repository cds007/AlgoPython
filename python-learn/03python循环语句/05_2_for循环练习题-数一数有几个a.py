"""
演示for循环的练习题：数一数有几个a
"""
name = "itheima is a brand of itcast"
cnt = 0
for ch in name:
    if ch == "a":
        cnt += 1
print(f"itheima is a brand of itcast有{cnt}个a")
