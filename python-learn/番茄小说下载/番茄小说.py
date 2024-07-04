"""
获取小说名字和章节id
"""
import requests
import re
# 导入selector
from parsel import Selector
# 请求链接
url = 'https://fanqienovel.com/reader/7276663560427471412?enter_from=page'
# 模拟浏览器
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36'
}
# 发送请求
response = requests.get(url=url, headers=headers)
# 获取网页源代码
html_data = response.text
"""
解析数据方法有：
re：正则表达式
css：根据标签属性提取数据
xpath：根据标签节点提取数据
"""
# 正则提取小说名
print(html_data)
name: list = re.findall(
    '<div class="info-name"><h1>(.*?)</h1></div>', html_data)[0]

# css提取法
selector = Selector(text=html_data)
css_name = selector.css('.info-name h1::text').get()

# xpath提取法
xpath_name = selector.xpath('//div[@class="info-name"]/h1/text()').get()
print(name, css_name, xpath_name)

# 提取章节id，用css选择器
href = selector.css('.chapter-item a::attr(href)').getall()
# for循环遍历列表元素
for index in href:
    # 字符串分割提取id
    chapter_id = index.split('/')[-1]
    # 构建小说数据连接地址
    link = f'https://novel.snssdk.com/api/novel/book/reader/full/v1/?device_platform=android&parent_enterform=novel_channel_search.tab.&aid=2329&platform_id=1&group_id={chapter_id}&item_id={chapter_id}'
    # 对于内容链接地址发送请求，获取数据
    json_data = requests.get(url=url, headers=headers).json()
    print(json_data)
    break
    print(chapter_id)
