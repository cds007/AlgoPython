"""
演示第三个图表：GDP动态柱状图开发
"""
from pyecharts.charts import Bar, Timeline
from pyecharts.options import *
from pyecharts.globals import ThemeType
import os
# 1.读取数据
cur_path = os.path.abspath(__file__)
cur_dir = os.path.dirname(cur_path)
file_path = os.path.join(cur_dir, "1960-2019全球GDP数据.csv")
with open(file_path, "r", encoding='GB2312') as f:
    data_csv = f.readlines()  # list
# 2.预处理，去除第一行
data_csv.pop(0)  # 不需要重新赋值
# 3.构建格式化数据{1960:[['美国',111],['中国',222]]}
data_dict = {}

for line in data_csv:
    line_list = line.split(",")
    year = int(line_list[0])
    country = line_list[1]
    gdp = float(line_list[2])
    if not year in data_dict:
        data_dict[year] = []
        list_temp = [country, gdp]
        data_dict[year].append(list_temp)
    else:
        list_temp = [country, gdp]
        data_dict[year].append(list_temp)

# 从数据中获取所有年份，并升序排序
year_list = list(data_dict.keys())
sorted(year_list)
# 根据每一年的数据，构建每一年的bar图，并添加到时间线图中去
timeline = Timeline({'theme': ThemeType.LIGHT})
for line in year_list:
    country_list = data_dict[line]
    country_list.sort(
        key=lambda element: element[1], reverse=True)  # 根据gdp进行降序排序
    # 选取前八个来构建bar图
    country_list = country_list[:8]
    x_data = []
    y_data = []
    for i in country_list:
        x_data.append(i[0])  # x轴数据
        y_data.append(i[1] / 100000000)  # y轴数据
    bar = Bar()
    x_data.reverse()
    y_data.reverse()
    bar.add_xaxis(x_data)
    bar.add_yaxis('GDP(亿)', y_data, label_opts=LabelOpts(position='right'))
    bar.reversal_axis()
    # 设置每一年的标题
    bar.set_global_opts(title_opts=TitleOpts(title=f"{line}年全球前八GDP数据"))
    # 时间线图添加
    timeline.add(bar, str(line))

# 时间线图的全局设置
timeline.add_schema(
    play_interval=1000,
    is_timeline_show=True,  # 是否显示时间线
    is_auto_play=True,
    is_loop_play=True
)
# 生成时间线图
show_path = os.path.join(cur_dir, '1960-2019全球GDP前8国家.html')
timeline.render(show_path)
