import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton, QLabel
from PyQt5 import uic
from PyQt5.QtGui import QPainter, QColor, QPixmap
from PyQt5.QtCore import Qt
import random


class Window(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        uic.loadUi('UI.ui', self)
        self.pixmap = QPixmap()
        #self.image = QLabel(self)
        self.flag = False
        self.dx = self.frameGeometry().width()
        self.dy = self.frameGeometry().height()
        self.pushButton.clicked.connect(self.paint)

    def paintEvent(self, event):
        if self.flag == True:
            painter = QPainter(self)
            painter.drawPixmap(self.rect(), self.pixmap)
            self.circle(painter)


    def circle(self, qp):
        self.x = random.randint(1, self.dx - 1)
        self.y = random.randint(1, self.dy - 1)
        qp.setBrush(QColor(255, 255, 0))
        width = random.randint(1, min(min(abs(self.x - self.dx), abs(self.y - self.dy)), min(self.x, self.y)))
        qp.drawEllipse(self.x - width // 2, self.y - width // 2, width, width)

    def paint(self):
        self.flag = True
        self.repaint()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())
