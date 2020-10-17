"""跨檔案變數，entrance.py與grep_dict.py，從entrance.py取得使用者輸入值，直到grep_dict.py取值"""


class GlobalVar:
    input_value = None


def set_demo_value(value):
    GlobalVar.input_value = value


def get_demo_value():
    return GlobalVar.input_value
