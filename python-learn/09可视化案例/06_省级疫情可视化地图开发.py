"""
演示河南省疫情地图开发
"""
import json
import os
from pyecharts.charts import Map
from pyecharts.options import *

# 1.读取数据
cur_path = os.path.abspath(__file__)
cur_dir = os.path.dirname(cur_path)
file_path = os.path.join(cur_dir, "疫情.txt")
with open(file_path, "r", encoding="utf-8") as f:
    data = f.read()

# 2.需要读取河南省级信息，拼接成元组列表的数据
data_json = json.loads(data)
data_henan = data_json['areaTree'][0]['children'][3]  # dict类型
henan_childs = data_henan['children']  # list类型
data_list = []
for line in henan_childs:
    item_name = line['name']+'市'
    item_confirm = line['total']['confirm']
    if item_name == '济源示范区市':
        item_name = '济源市'
    data_list.append((item_name, item_confirm))


# 3.构建map
map = Map()
map.add('河南省疫情分布', data_list, "河南")
map.set_global_opts(
    title_opts=TitleOpts(title="河南省疫情地图"),
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
show_path = os.path.join(cur_dir, '河南省疫情地图.html')
map.render(show_path)
