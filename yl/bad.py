import sys

from PIL import Image
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QFileDialog


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.current = QFileDialog.getOpenFileName(self, 'Выбрать картинку', '')[0]
        print(self.current)
        self.new_img = 'new_img.' + self.current[self.current.find('.'):]
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 400, 240)
        self.setWindowTitle('PIL 2.0')
        self.pixmap = QPixmap(self.current)
        self.image = QLabel(self)
        self.image.move(180, 20)
        self.image.resize(200, 200)
        self.image.setPixmap(self.pixmap)
        self.btn = QPushButton('R', self)
        self.btn.resize(140, 30)
        self.btn.move(20, 20)
        self.btn.clicked.connect(self.r_color)
        self.btn = QPushButton('G', self)
        self.btn.resize(140, 30)
        self.btn.move(20, 60)
        self.btn.clicked.connect(self.g_color)
        self.btn = QPushButton('B', self)
        self.btn.resize(140, 30)
        self.btn.move(20, 100)
        self.btn.clicked.connect(self.b_color)
        self.btn = QPushButton('ALL', self)
        self.btn.resize(140, 30)
        self.btn.move(20, 140)
        self.btn.clicked.connect(self.full_color)
        self.btn = QPushButton('Влево', self)
        self.btn.resize(60, 30)
        self.btn.move(20, 190)
        self.btn.clicked.connect(self.l_turn)
        self.btn = QPushButton('Вправо', self)
        self.btn.resize(60, 30)
        self.btn.move(100, 190)
        self.btn.clicked.connect(self.r_turn)

    def r_color(self):
        img = Image.open(self.current)
        img = img.convert('RGB')
        img = img.resize((200, 200))
        pixels = img.load()

        x, y = img.size
        for i in range(x):
            for j in range(y):
                r, g, b = pixels[i, j]
                pixels[i, j] = r, 0, 0
        img.save(self.new_img)
        self.pixmap = QPixmap(self.new_img)
        self.image.setPixmap(self.pixmap)

    def g_color(self):
        img = Image.open(self.current)
        img = img.convert('RGB')

        pixels = img.load()
        x, y = img.size
        for i in range(x):
            for j in range(y):
                r, g, b = pixels[i, j]
                pixels[i, j] = 0, g, 0
        img.save(self.new_img)
        self.pixmap = QPixmap(self.new_img)
        self.image.setPixmap(self.pixmap)

    def b_color(self):
        img = Image.open(self.current)

        img = img.convert('RGB')
        pixels = img.load()
        x, y = img.size
        for i in range(x):
            for j in range(y):
                r, g, b = pixels[i, j]
                pixels[i, j] = 0, 0, b
        img.save(self.new_img)
        self.pixmap = QPixmap(self.new_img)
        self.image.setPixmap(self.pixmap)

    def full_color(self):
        img = Image.open(self.current)
        img = img.convert('RGB')
        pixels = img.load()
        x, y = img.size
        for i in range(x):
            for j in range(y):
                r, g, b = pixels[i, j]
                pixels[i, j] = r, g, b
        img.save(self.new_img)
        self.pixmap = QPixmap(self.new_img)
        self.image.setPixmap(self.pixmap)

    def l_turn(self):
        img = Image.open(self.new_img)
        img = img.rotate(90)
        img.save(self.new_img)
        self.pixmap = QPixmap(self.new_img)
        self.image.setPixmap(self.pixmap)

    def r_turn(self):
        img = Image.open(self.new_img)
        img = img.rotate(90)
        img = img.transpose(Image.ROTATE_180)
        img.save(self.new_img)
        self.pixmap = QPixmap(self.new_img)
        self.image.setPixmap(self.pixmap)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
