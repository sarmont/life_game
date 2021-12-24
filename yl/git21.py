import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5 import uic


class Window(QWidget):
    def __init__(self, *args, **kwargs):
        super(Window, self).__init__(*args, **kwargs)
        uic.loadUi('UI.ui', self)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())
