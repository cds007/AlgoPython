"""
演示基础柱状图的开发
"""
from pyecharts.charts import Bar
from pyecharts.options import LabelOpts
import os
bar = Bar()
bar.add_xaxis(['中国', '美国', '英国'])
bar.add_yaxis('GDP', [30, 20, 10], label_opts=LabelOpts(
    position='right'))  # 数值显示在右侧
bar.reversal_axis()  # 反转x轴和y轴

cur_path = os.path.abspath(__file__)
cur_dir = os.path.dirname(cur_path)
file_path = os.path.join(cur_dir, "基础柱状图.html")
bar.render(file_path)
