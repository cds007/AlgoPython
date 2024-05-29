n, v = map(int, input().split())

weight_list = []
value_list = []
for _ in range(n):
    weight, value = map(int, input().split())
    weight_list.append(weight)
    value_list.append(value)
# print(n,v)
# print(weight_list, value_list)


def func(weight_list, value_list, bag_size):
    n = len(weight_list)
    dp = [0] * (bag_size + 1)
    for i in range(len(weight_list)):   # 遍历物品
        for j in range(weight_list[i], bag_size + 1):    # 正序遍历背包
            dp[j] = max(dp[j], dp[j-weight_list[i]]+value_list[i])
    # print(dp)
    return dp[bag_size]


print(func(weight_list, value_list, v))
