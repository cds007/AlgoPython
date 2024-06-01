"""
演示函数综合案例开发
"""
money = 50000
name = ""

# 查询余额


def query(show_board: bool) -> None:
    if (show_board):
        print("-------------查询余额------------")
    print(f"{name}您好，您的余额剩余{money}元")

# 存款


def saving(num: int) -> None:
    print("-------------存款------------")
    global money
    money += num
    print(f"存款{num}成功")
    query(False)

# 取款


def get_money(num: int) -> None:
    print("-------------取款------------")
    global money
    money -= num
    print(f"取款{num}成功")
    query(False)

# 主菜单


def main():
    print(f"{name}你好，欢迎来到ATM，请选择操作：")
    print("查询余额请按1")
    print("存款请按2\n取款请按3\n退出请按4\n")
    return input("请输入你的选择:")


if __name__ == "__main__":
    name = input("请输入姓名")
    while True:
        print("")
        key_input = main()
        if (key_input == '1'):
            # 查询余额
            query(True)
        elif (key_input == '2'):
            # 存款
            num = int(input("您想要存多少钱？请输入："))
            saving(num)
        elif (key_input == '3'):
            # 取款
            num = int(input("您想要取多少钱？请输入："))
            get_money(num)
        else:
            print("程序退出")
            break
