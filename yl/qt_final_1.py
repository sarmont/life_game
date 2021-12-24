import sys
import random

from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtCore import Qt, QPoint
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtGui import QPolygon


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.do_paint = False
        self.press_key = 0
        self.setMouseTracking(True)

    def initUI(self):
        self.dx = random.randint(100, 400)
        self.dy = random.randint(100, 400)
        self.setGeometry(300, 300, self.dx, self.dy)
        self.setWindowTitle('Супрематизм')

    def mousePressEvent(self, event):
        self.x = event.x()
        self.y = event.y()

        if event.button() == Qt.LeftButton:
            self.press_key = 1
            self.paint()

        elif event.button() == Qt.RightButton:
            self.press_key = 2
            self.paint()

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Space:
            self.press_key = 3
            self.paint()

    def mouseMoveEvent(self, event):
        self.coords_x = event.x()
        self.coords_y = event.y()

    def paintEvent(self, event):
        if self.do_paint is True:
            # Создаем объект QPainter для рисования
            qp = QPainter(self)
            # Начинаем процесс рисования
            qp.begin(self)
            if self.press_key == 1:
                self.circle(qp)
            elif self.press_key == 2:
                self.square(qp)
            elif self.press_key == 3:
                self.treugolnik(qp)
            # Завершаем рисование
            qp.end()

    def paint(self):
        self.do_paint = True
        self.repaint()

    def circle(self, qp):
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        qp.setBrush(QColor(r, g, b))
        width = random.randint(1, min(min(abs(self.x - self.dx), self.x), min(abs(self.y - self.dy), self.y)))
        qp.drawEllipse(self.x - width // 2, self.y - width // 2, width, width)

    def square(self, qp):
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        qp.setBrush(QColor(r, g, b))
        width = random.randint(1, min(min(abs(self.x - self.dx), self.x), min(abs(self.y - self.dy), self.y)))
        qp.drawRect(self.x - width // 2, self.y - width // 2, width, width)

    def treugolnik(self, qp):
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        qp.setBrush(QColor(r, g, b))
        width = random.randint(1, min(min(abs(self.coords_x - self.dx), self.coords_x),
                                      min(abs(self.coords_y - self.dy), self.coords_y)))
        points = QPolygon([QPoint(self.coords_x - width // 2, self.coords_y + width // 2),
                           QPoint(self.coords_x + width // 2, self.coords_y + width // 2),
                           QPoint(self.coords_x, self.coords_y - width // 2)])
        qp.drawPolygon(points)


if __name__ == '__main__':
    app = QApplication(sys.argv)
ex = Example()
ex.show()
sys.exit(app.exec())
