from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5.QtWidgets import QApplication
import time


class SubThread(QThread):
    message = pyqtSignal(str)
    def __init__(self):
        super().__init__()
        # 以下加入需要的程式碼

    def __del__(self):
        self.wait()

    def run(self):
        self.message.emit("子執行續開始")
        time.sleep(2)
        self.message.emit('子執行緒結束')


def callback(msg):
    print(msg)


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    window = SubThread()
    window.message.connect(callback)
    window.start()
    sys.exit(app.exec_())
