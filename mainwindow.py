
from PyQt5.QtWidgets import QApplication
from windows import MyWindow
import sys


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())
