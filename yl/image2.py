import sys
from PIL import Image, ImageDraw

from PyQt5.QtGui import QPixmap, QColor, QPainter, QImage
from PyQt5 import uic  # Импортируем uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('image-2.ui', self)  # Загружаем дизайн
        ## Изображение
        new_image = Image.new("RGB", (100, 200), (0, 0, 0))
        # на изображении создаем рисунок для рисования
        draw = ImageDraw.Draw(new_image)
        # рисуем линию
        draw.line((0, 0, 100, 200), fill=(255, 0, 0), width=1)
        # сохраним изображением в файл формата PNG

        self.pixmap = QImage(new_image)
        # Если картинки нет, то QPixmap будет пустым,
        # а исключения не будет

        # Отображаем содержимое QPixmap в объекте QLabel
        self.image_lbl.setPixmap(self.pixmap)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
