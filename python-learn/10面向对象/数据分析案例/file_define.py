"""
和文件相关的类定义
"""
from data_define import Record
import json

# 抽象类


class FileReader:
    def read_data(self) -> list[Record]:
        pass


# 文本读取类
class TextFileReader(FileReader):
    def __init__(self, path) -> None:
        super().__init__()
        self.path = path

    def read_data(self) -> list[Record]:
        result = []
        with open(self.path, "r", encoding='utf-8') as f:
            for line in f:
                # 读取每一行
                line_list = line.strip().split(',')
                record = Record(
                    line_list[0], line_list[1], int(line_list[2]), line_list[3])
                result.append(record)
        return result

# json读取类


class JSONFileReader(FileReader):
    def __init__(self, path) -> None:
        super().__init__()
        self.path = path

    def read_data(self) -> list[Record]:
        result = []
        with open(self.path, "r", encoding='utf-8') as f:
            for line in f:
                # 读取每一行
                line_dict = json.loads(line)
                record = Record(line_dict['date'], line_dict['order_id'], int(
                    line_dict['money']), line_dict['province'])
                result.append(record)
        return result


if __name__ == "__main__":
    import os
    cur_path = os.path.abspath(__file__)
    cur_dir = os.path.dirname(cur_path)
    file_path = os.path.join(cur_dir, '2011年1月销售数据.txt')
    readerText = TextFileReader(file_path)
    print(readerText.read_data()[0])
    file_path2 = os.path.join(cur_dir, '2011年2月销售数据JSON.txt')
    readerJSON = JSONFileReader(file_path2)
    print(readerJSON.read_data()[0])
