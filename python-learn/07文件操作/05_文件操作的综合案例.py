"""
综合案例：

读取文件
将文件写出到bill.txt.bak文件作为备份
同时，将文件内标记为测试的数据行丢弃

"""
import os
cur_path = os.path.abspath(__file__)
cur_dir = os.path.dirname(cur_path)
file_path_rd = os.path.join(cur_dir, "bill.txt")
file_path_wt = os.path.join(cur_dir, "bill.txt.bak")

frd = open(file_path_rd, "r", encoding="utf-8")
fwt = open(file_path_wt, "w", encoding="utf-8")
for line in frd:
    if not "测试" in line:
        fwt.write(line)

frd.close
fwt.close
