class GlobalVar:
    input_value = None


def set_demo_value(value):
    GlobalVar.input_value = value


def get_demo_value():
    return GlobalVar.input_value
