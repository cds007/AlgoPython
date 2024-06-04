"""
数据定义的类
"""


class Record:

    def __init__(self, date: str, orderid: str, money: int, province: str) -> None:
        self.date = date
        self.orderid = orderid
        self.money = money
        self.province = province

    def __str__(self) -> str:
        return f"日期是{self.date}，订单号是{self.orderid}，销售额是{self.money}，省份是{self.province}"
