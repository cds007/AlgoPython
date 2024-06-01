import random

money = 10000
for i in range(20):  # 0到20的员工
    pay = random.randint(1, 10)  # 包括1和10
    if pay < 5:
        print(f"员工{i+1}，绩效为{pay}，低于5，不发工资，下一位")
    else:
        if (money > 0):
            money -= 1000
            print(f"向员工{i+1}发工资1000元，账户余额还剩{money}元")
        if (money == 0):
            print(f"工资发完了，下个月领取吧")
            break
