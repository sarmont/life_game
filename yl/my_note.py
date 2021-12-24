import sys
import datetime
from PyQt5 import uic  # Импортируем uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QRadioButton


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("my_note.ui", self)

        self.add_but.clicked.connect(self.add_event)

    def add_event(self):
        t = self.time.time()
        my_date = self.calendar.selectedDate().toString('dd-MM-yyyy')
        time = my_date + ' ' + t.toString() + ' - ' + self.event.text()
        self.listWidget.addItem(time)
        self.listWidget.sortItems(order=sorted([self.listWidget.item(i) for i in range(self.listWidget.count)], key=datetime.date(time[:4],time[5:7],time[9:])))
        self.event.setText('')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
