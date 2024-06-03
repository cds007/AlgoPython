"""
演示全国疫情可视化地图开发
"""
import json
import os
from pyecharts.charts import Map
from pyecharts.options import *

# 1.读取文件
cur_path = os.path.abspath(__file__)
cur_dir = os.path.dirname(cur_path)
data_path = os.path.join(cur_dir, "疫情.txt")
with open(data_path, "r", encoding="utf-8") as f:
    data = f.read()
data_json = json.loads(data)  # dict类型

# 2.获取元组列表数据
children = data_json['areaTree'][0]["children"]  # list 类型
data_list = []
for line in children:
    item_name = line['name']
    item_num = line['total']['confirm']
    data_list.append((item_name, item_num))

# 3.可视化图表
map = Map()
map.add("全国疫情可视化地图", data_list, "china")
map.set_global_opts(
    visualmap_opts=VisualMapOpts(
        is_show=True,           # 是否显示
        is_piecewise=True,      # 是否分段
        pieces=[
            {"min": 1, "max": 99, "lable": "1~99人", "color": "#CCFFFF"},
            {"min": 100, "max": 999, "lable": "100~9999人", "color": "#FFFF99"},
            {"min": 1000, "max": 4999, "lable": "1000~4999人", "color": "#FF9966"},
            {"min": 5000, "max": 9999, "lable": "5000~99999人", "color": "#FF6666"},
            {"min": 10000, "max": 99999, "lable": "10000~99999人", "color": "#CC3333"},
            {"min": 100000, "lable": "100000+", "color": "#990033"},
        ]
    )
)
show_path = os.path.join(cur_dir, "全国疫情可视化地图.html")
map.render(show_path)
