import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton
from PyQt5 import uic
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtCore import Qt
import random


class Window(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        uic.loadUi('UI.ui', self)
        self.do_paint = False
        self.dx = self.frameGeometry().width()
        self.dy = self.frameGeometry().height()
        self.pushButton.clicked.connect(self.paint)

    def circle(self, qp):
        self.x = random.randint(1, self.dx - 1)
        self.y = random.randint(1, self.dy - 1)
        qp.setBrush(QColor(255, 255, 0))
        width = 50
        qp.drawEllipse(self.x - width // 2, self.y - width // 2, width, width)

    def paintEvent(self, event):
        if self.do_paint is True:
            # Создаем объект QPainter для рисования
            qp = QPainter(self)
            # Начинаем процесс рисования
            qp.begin(self)
            self.circle(qp)
            # Завершаем рисование
            qp.end()

    def paint(self):
        self.do_paint = True
        self.repaint()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())
