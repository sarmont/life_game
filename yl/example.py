import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPainter, QColor, QBrush

class Labella(QLabel):

    def __init__(self, parent):
        super().__init__(parent=parent)

        self.setStyleSheet('QFrame {background-color:grey;}')
        self.resize(200, 200)

    def paintEvent(self, e):
        qp = QPainter(self)
        self.drawRectangles(qp)
        qp.setBrush(QColor(200, 0, 0))
        qp.drawRect(0,0,20,20)

    def drawRectangles(self, qp):
        qp.setBrush(QColor(255, 0, 0, 100))
        qp.save() # save the QPainter config

        qp.drawRect(10, 15, 20, 20)

        qp.setBrush(QColor(0, 0, 255, 100))
        qp.drawRect(50, 15, 20, 20)

        qp.restore() # restore the QPainter config
        qp.drawRect(100, 15, 20, 20)

class Example(QWidget):

    def __init__(self):
        super().__init__()

        lb = Labella(self)

        self.setGeometry(300, 300, 350, 300)
        self.setWindowTitle('Colours')
        self.show()

if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())