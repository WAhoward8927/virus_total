"""程式起點"""
import sys
from virus_total import general_func, globals


class Mode(object):
    """判斷使用者輸入功能"""
    def __init__(self, mode=None):
        self.mode = mode

    @property
    def mode(self):
        return self._mode

    @mode.setter
    def mode(self, user_mode):
        self._mode = user_mode
        if user_mode != str(1) and user_mode != str(2):
            print("輸入錯誤")
            sys.exit()
        else:
            self._mode = user_mode


if __name__ == '__main__':
    user_in = input("請輸入模式(1代表加入黑名單，2代表解管黑名單)：")
    user_input_mode = Mode(user_in)
    globals.set_demo_value(user_input_mode.mode)
    print("\r程式運行中", end='')
    general_func.file_check()  # 程式起點
    print("\r程式已結束\r", end='')

