"""
演示带有时间线的柱状图开发
"""
from pyecharts.charts import Bar, Timeline
from pyecharts.options import LabelOpts
from pyecharts.globals import ThemeType as Themes
import os
bar1 = Bar()
bar1.add_xaxis(["中国", "美国", "英国"])
bar1.add_yaxis("GDP", [30, 30, 20], label_opts=LabelOpts(position="right"))
bar1.reversal_axis()

bar2 = Bar()
bar2.add_xaxis(["中国", "美国", "英国"])
bar2.add_yaxis("GDP", [50, 50, 50], label_opts=LabelOpts(position="right"))
bar2.reversal_axis()

bar3 = Bar()
bar3.add_xaxis(["中国", "美国", "英国"])
bar3.add_yaxis("GDP", [70, 60, 60], label_opts=LabelOpts(position="right"))
bar3.reversal_axis()

timeline = Timeline({'theme': Themes.LIGHT})  # 这个可以改变图例的颜色
# 在时间线内添加柱状图对象
timeline.add(bar1, '点1')
timeline.add(bar2, '点2')
timeline.add(bar3, '点3')

# 自动播放设置
timeline.add_schema(
    play_interval=1000,  # 1秒间隔播放
    is_timeline_show=True,  # 是否显示时间线
    is_auto_play=True,  # 是否自动播放
    is_loop_play=True  # 是否循环播放
)
cur_path = os.path.abspath(__file__)
cur_dir = os.path.dirname(cur_path)
file_path = os.path.join(cur_dir, "基础时间线柱状图.html")
timeline.render(file_path)
