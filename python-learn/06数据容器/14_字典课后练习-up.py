"""
演示字典的课后练习：升职加薪，对所有级别为1级的员工，级别上升1级，薪水增加1000元
"""
import sys

if __name__ == "__main__":
    # 组织字典记录数据
    info_dict = {
    }
    # 输入员工个数
    print("请输入员工个数")
    nums = int(sys.stdin.readline())
    for i in range(nums):
        name = input("请输入姓名：")
        deparment = input("请输入部门：")
        salary = int(input("请输入薪资："))
        level = int(input("请输入级别："))
        if (level == 1):
            level = 2
            salary += 1000
        info_dict[name] = {
            "部门": deparment,
            "工资": salary,
            "级别": level
        }
    print("姓名\t部门\t工资\t级别")
    for key, value in info_dict.items():
        deparment = value["部门"]
        salary = value["工资"]
        level = value["级别"]
        print(f"{key}\t{deparment}\t{salary}\t{level}")
