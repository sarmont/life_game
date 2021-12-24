import sqlite3
import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(480, 343)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 471, 45))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(10, 10, 10, 10)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.comboBox = QtWidgets.QComboBox(self.verticalLayoutWidget)
        self.comboBox.setMinimumSize(QtCore.QSize(120, 0))
        self.comboBox.setMaximumSize(QtCore.QSize(120, 16777215))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.comboBox.setFont(font)
        self.comboBox.setObjectName("comboBox")
        self.horizontalLayout.addWidget(self.comboBox)
        self.search_txt = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.search_txt.setObjectName("search_txt")
        self.horizontalLayout.addWidget(self.search_txt)
        self.search_btn = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.search_btn.setObjectName("search_btn")
        self.horizontalLayout.addWidget(self.search_btn)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(190, 60, 281, 191))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.lineEdit_id = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.lineEdit_id.setObjectName("lineEdit_id")
        self.verticalLayout_2.addWidget(self.lineEdit_id)
        self.lineEdit_title = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.lineEdit_title.setObjectName("lineEdit_title")
        self.verticalLayout_2.addWidget(self.lineEdit_title)
        self.lineEdit_year = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.lineEdit_year.setObjectName("lineEdit_year")
        self.verticalLayout_2.addWidget(self.lineEdit_year)
        self.lineEdit_genre = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.lineEdit_genre.setObjectName("lineEdit_genre")
        self.verticalLayout_2.addWidget(self.lineEdit_genre)
        self.lineEdit_duration = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.lineEdit_duration.setObjectName("lineEdit_duration")
        self.verticalLayout_2.addWidget(self.lineEdit_duration)
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(10, 70, 160, 171))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_3.addWidget(self.label_2)
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.label.setObjectName("label")
        self.verticalLayout_3.addWidget(self.label)
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_3.addWidget(self.label_3)
        self.label_4 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_3.addWidget(self.label_4)
        self.label_5 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_3.addWidget(self.label_5)
        self.error_lbl = QtWidgets.QLabel(self.centralwidget)
        self.error_lbl.setGeometry(QtCore.QRect(20, 270, 91, 16))
        self.error_lbl.setText("")
        self.error_lbl.setObjectName("error_lbl")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 480, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Поиск по фильмам"))
        self.search_btn.setText(_translate("MainWindow", "Найти"))
        self.label_2.setText(_translate("MainWindow", "ID"))
        self.label.setText(_translate("MainWindow", "Название"))
        self.label_3.setText(_translate("MainWindow", "Год выпуска"))
        self.label_4.setText(_translate("MainWindow", "Жанр"))
        self.label_5.setText(_translate("MainWindow", "Продолжительность"))


class DBSample(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        # uic.loadUi('film_search.ui', self)
        self.setupUi(self)

        self.search = ''
        # заполняем combobox
        self.comboBox.addItem('Название')
        self.comboBox.addItem('Год выпуска')
        self.comboBox.addItem('Продолжительность')

        self.connection = sqlite3.connect("films_db.sqlite")
        self.search_btn.clicked.connect(self.select_data)

    def select_data(self):
        self.search = self.search_txt.text()
        if self.search:
            query = ''
            cur = self.connection.cursor()
            if self.comboBox.currentText() == 'Название':
                query = """
                SELECT films.id,
                   films.title,
                   films.year,
                   films.duration,
                   genres.title
                  FROM films
                  left join genres on genres.id = films.genre
                  where films.title = ?
                """
            elif self.comboBox.currentText() == 'Год выпуска':
                query = """
                            SELECT films.id,
                               films.title,
                               films.year,
                               films.duration,
                               genres.title
                              FROM films
                              left join genres on genres.id = films.genre
                              where films.year = ?
                            """
            elif self.comboBox.currentText() == 'Продолжительность':
                query = """
                            SELECT films.id,
                               films.title,
                               films.year,
                               films.duration,
                               genres.title
                              FROM films
                              left join genres on genres.id = films.genre
                              where films.duration = ?
                            """
            result = cur.execute(query, (self.search,)).fetchall()
            if result:
                self.error_lbl.setText('')
                self.lineEdit_id.setText(str(result[0][0]))
                self.lineEdit_title.setText(str(result[0][1]))
                self.lineEdit_year.setText(str(result[0][2]))
                self.lineEdit_genre.setText(str(result[0][4]))
                self.lineEdit_duration.setText(str(result[0][3]))
            else:
                self.error_lbl.setText('Ничего не найдено')
        else:
            self.error_lbl.setText('Неверный ввод')

    def closeEvent(self, event):
        # При закрытии формы закроем и наше соединение
        # с базой данных
        self.connection.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = DBSample()
    ex.show()
    sys.exit(app.exec())
