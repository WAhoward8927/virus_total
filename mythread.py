from PyQt5 import QtCore
import time


class Mythread(QtCore.QThread):
    def __init__(self, parent=None):
        super(Mythread, self).__init__(parent)

    update_text = QtCore.pyqtSignal()

    def run(self):
        while(True):
            time.sleep(2)
            self.update_text.emit('pythonnnn')
