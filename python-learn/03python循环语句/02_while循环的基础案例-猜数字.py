"""
演示while循环的基础案例 - 猜数字
"""

# 获取范围在1-100的随机数字
import random
target = random.randint(1, 100)
cnt = 0
while True:
    cnt += 1
    guess_num = int(input("猜一猜："))
    if guess_num == target:
        print(f"恭喜，猜中了，数字是{target}")
        break
    elif guess_num > target:
        print("猜大了")
    elif guess_num < target:
        print("猜小了")

print(f"猜了{cnt}次")
