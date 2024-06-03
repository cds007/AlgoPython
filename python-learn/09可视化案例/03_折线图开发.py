"""
演示可视化需求1：折线图开发
"""

# 1.处理数据（打开文件）
import os
import json
from pyecharts.charts import Line
from pyecharts.options import TitleOpts, LabelOpts, LegendOpts, ToolboxOpts, VisualMapOpts

cur_path = os.path.abspath(__file__)
cur_dir = os.path.dirname(cur_path)

us_path = os.path.join(cur_dir, "美国.txt")
f_us = open(us_path, "r", encoding="utf-8")
f_content_us = f_us.read()
f_us.close()

jp_path = os.path.join(cur_dir, "日本.txt")
f_jp = open(jp_path, "r", encoding="utf-8")
f_content_jp = f_jp.read()
f_jp.close()

india_path = os.path.join(cur_dir, "印度.txt")
f_india = open(india_path, "r", encoding="utf-8")
f_content_india = f_india.read()
f_india.close()

# 2.去掉不规范的开头
f_content_us = f_content_us.replace("jsonp_1629344292311_69436(", "")
f_content_jp = f_content_jp.replace("jsonp_1629350871167_29498(", "")
f_content_india = f_content_india.replace("jsonp_1629350745930_63180(", "")

# 3.去掉不规范的结尾
f_content_us = f_content_us[:-2]
f_content_jp = f_content_jp[:-2]
f_content_india = f_content_india[:-2]


# 4.获取trend
json_us = json.loads(f_content_us)
trend_us = json_us['data'][0]['trend']  # 字典类型

json_jp = json.loads(f_content_jp)
trend_jp = json_jp['data'][0]['trend']

json_india = json.loads(f_content_india)
trend_india = json_india['data'][0]['trend']

# 5.x轴数据，日期：只要2020年的
x_data_us = trend_us['updateDate'][:314]  # list类型


# 6.y轴数据，确诊人数
y_data_us = trend_us['list'][0]['data'][:314]  # list类型
y_data_jp = trend_jp['list'][0]['data'][:314]
y_data_india = trend_india['list'][0]['data'][:314]

# 7.根据数据绘制图表
line = Line()
line.add_xaxis(x_data_us)
line.add_yaxis("美国确诊人数", y_data_us, label_opts=LabelOpts(
    is_show=False))  # 折线图上不显示标签的值
line.add_yaxis("日本确诊人数", y_data_jp, label_opts=LabelOpts(is_show=False))
line.add_yaxis("印度确诊人数", y_data_india, label_opts=LabelOpts(is_show=False))
# 设置全局配置项set_global_opts来设置,
line.set_global_opts(
    title_opts=TitleOpts(title="2020年美日印三国确诊人数对比折线图", pos_left="center",
                         pos_bottom="1%"),  # 关键字传参：标题(名称，居中显示，距离底部距离)
    toolbox_opts=ToolboxOpts(is_show=True),  # 工具箱
    visualmap_opts=VisualMapOpts(is_show=True),  # 视觉映射
)
show_path = os.path.join(cur_dir, "美日印确诊.html")
line.render(show_path)
