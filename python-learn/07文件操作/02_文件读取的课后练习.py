# 通过文件读取操作，读取此文件，统计itheima单词出现的次数
import os
# 获取当前python文件的绝对路径
current_file_path = os.path.abspath(__file__)
# 获取当前python文件的所在目录
current_dir = os.path.dirname(current_file_path)
# 拼接成文件的目录
file_path = os.path.join(current_dir, "word.txt")
# 打开文件
cnt = 0
with open(file_path, "r", encoding="UTF-8") as f:
    # 开始统计
    for line in f:
        num = line.count("itheima")
        cnt += num
    print(f"共有单词数{cnt}")
