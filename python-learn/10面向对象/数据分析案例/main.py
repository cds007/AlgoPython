"""
面向对象，数据分析案例，主业务逻辑代码
实现步骤：
1. 设计一个类，可以完成数据的封装
2. 设计一个抽象类，定义文件读取的相关功能，并使用子类实现具体功能
3. 读取文件，生产数据对象
4. 进行数据需求的逻辑计算（计算每一天的销售额）
5. 通过PyEcharts进行图形绘制
"""
import os
from data_define import Record
from file_define import TextFileReader, JSONFileReader
from pyecharts.charts import Bar
from pyecharts.options import *
from pyecharts.globals import ThemeType


cur_path = os.path.abspath(__file__)
cur_dir = os.path.dirname(cur_path)
# 1.读取文件，获取数据
path1 = os.path.join(cur_dir, '2011年1月销售数据.txt')
path2 = os.path.join(cur_dir, '2011年2月销售数据JSON.txt')
textReader = TextFileReader(path1)
jsonReader = JSONFileReader(path2)
data_20111 = textReader.read_data()
data_20112 = jsonReader.read_data()

# 2.x轴是当天日期
data_all: list[Record] = data_20111+data_20112
# 构建一个dict数据
data_dict: dict[str, int] = {}
for record in data_all:
    date = record.date
    if not date in data_dict:
        data_dict[date] = int(record.money)  # 不加int其实也行的，我这里保险一点
    else:
        data_dict[date] += int(record.money)

# x轴
bar = Bar(init_opts=InitOpts(theme=ThemeType.LIGHT))
bar.add_xaxis(list(data_dict.keys()))

# 3.y轴是当天日期的金额总和
bar.add_yaxis('2011年1月和2月销售总额', list(data_dict.values()),
              label_opts=LabelOpts(is_show=False))
bar.set_global_opts(
    title_opts=TitleOpts(title='每日销售额')
)
show_path = os.path.join(cur_dir, '每日销售额柱状图.html')
bar.render(show_path)
