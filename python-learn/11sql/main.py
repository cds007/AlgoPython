"""
SQL 综合案例，读取文件，写入MySQL数据库中
"""
from file_define import TextFileReader, JsonFileReader
from data_define import Record
from pymysql import Connection
import os

cur_path = os.path.abspath(__file__)
cur_dir = os.path.dirname(cur_path)
path1 = os.path.join(cur_dir, '2011年1月销售数据.txt')
path2 = os.path.join(cur_dir, '2011年2月销售数据JSON.txt')
text_file_reader = TextFileReader(path1)
json_file_reader = JsonFileReader(path2)

jan_data: list[Record] = text_file_reader.read_data()
feb_data: list[Record] = json_file_reader.read_data()
# 将2个月份的数据合并为1个list来存储
all_data: list[Record] = jan_data + feb_data

# 构建MySQL链接对象
conn = Connection(
    host="localhost",
    port=3306,
    user="root",
    password="123456",
    autocommit=True
)
# 获得游标对象
cursor = conn.cursor()
# 选择数据库
conn.select_db("py_sql_test")
# 组织SQL语句

sql_create = f'create table if not exists orders(order_date varchar(255),order_id varchar(255),money int,province varchar(255))'
cursor.execute(sql_create)

for record in all_data:
    sql = f"insert into orders(order_date, order_id, money, province) " \
          f"values('{record.date}', '{record.order_id}', {record.money}, '{record.province}')"
    # 执行SQL语句
    cursor.execute(sql)

# 关闭MySQL链接对象
conn.close()
