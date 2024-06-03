"""
文件处理相关的工具模块
"""


def print_file_info(file_path: str) -> None:
    """
    打印文件的信息
    """
    f = None
    try:
        f = open(file_path, "r", encoding="utf-8")
        content = f.read()
        print(content)
    except Exception as e:
        print(f"出现异常，异常名称为{e}")
    finally:
        if f:
            f.close()


def append_to_file(file_path: str, content: str) -> None:
    """
    追加文件的内容
    """
    f = open(file_path, "a", encoding="utf-8")  # append也会创建新文件
    f.write(content+"\n")
    f.close()


if __name__ == "__main__":
    print_file_info("data.json")
