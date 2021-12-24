import sys

from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow

SCREEN_SIZE = [400, 400]


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.coords_x = 0
        self.coords_y = 0
        self.setMouseTracking(True)
        self.initUI()

    def initUI(self):
        self.setGeometry(200, 200, *SCREEN_SIZE)
        self.setWindowTitle('Машинка')
        self.draw_image()

    def draw_image(self):
        ## Изображение
        self.pixmap = QPixmap('car1.PNG')
        # Если картинки нет, то QPixmap будет пустым,
        # а исключения не будет
        self.image = QLabel(self)
        self.image.move(self.coords_x, self.coords_y)
        self.image.resize(60, 60)
        # Отображаем содержимое QPixmap в объекте QLabel
        self.image.setPixmap(self.pixmap)

    def mouseMoveEvent(self, event):
        self.coords_x = event.x()
        self.coords_y = event.y()
        print(self.coords_x, self.coords_y)
        self.change_img_coords()

    def change_img_coords(self):
        if self.coords_x + 60 > SCREEN_SIZE[0]:
            self.coords_x = SCREEN_SIZE[0] - 60
        if self.coords_y + 60 > SCREEN_SIZE[1]:
            self.coords_y = SCREEN_SIZE[1] - 60
        self.image.move(self.coords_x, self.coords_y)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
