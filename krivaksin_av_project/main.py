import sys
from PyQt5 import uic
from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtWidgets import (QMainWindow, QAction, qApp, QApplication,
                             QWidget, QDialog)
from PyQt5.QtGui import QIcon

from PyQt5 import QtCore, QtGui, QtWidgets
from main_form_ui import GeneralWidget


class PreDialog(QDialog):
    def __init__(self, parent=None):  # + parent
        super(PreDialog, self).__init__(parent)  #
        self.parent = parent  #

        self.setWindowTitle('Host Parameters')
        self.setModal(True)
        self.line_host = QtWidgets.QLineEdit()
        self.line_user = QtWidgets.QLineEdit()
        self.line_pass = QtWidgets.QLineEdit()
        self.line_pass.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.connect = QtWidgets.QPushButton("connect")
        self.spinBox_port = QtWidgets.QSpinBox()
        self.spinBox_port.setProperty("value", 22)
        self.hbox = QtWidgets.QHBoxLayout()
        self.ssh_radio = QtWidgets.QRadioButton("SSH")
        self.telnet_radio = QtWidgets.QRadioButton("Telnet")

        self.hbox.addWidget(self.ssh_radio)
        self.hbox.addWidget(self.telnet_radio)

        self.form = QtWidgets.QFormLayout()
        self.form.setSpacing(20)

        self.form.addRow("&Host:", self.line_host)
        self.form.addRow("&User:", self.line_user)
        self.form.addRow("&Password:", self.line_pass)
        self.form.addRow("&Port:", self.spinBox_port)
        self.form.addRow("Session:", self.hbox)
        self.form.addRow(self.connect)

        self.setLayout(self.form)

    def closeEvent(self, event):  # +++
        self.parent.show()


class G_Widget(QWidget, GeneralWidget):
    def __init__(self, parent=None):  # + parent
        super(G_Widget, self).__init__(parent)  #
        self.setupUi(self)
        #self.parent = parent

        # uic.loadUi('main_form.ui', self)

    def createDialog(self):
        #        self.dialog = PreDialog(self)
        self.dialog = PreDialog(self.parent)
        self.dialog.show()

    def stopDialog(self):
        self.dialog.destroy()


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.general = G_Widget(self)
        self.setCentralWidget(self.general)

        self.general.createDialog()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    # window.show()

    sys.exit(app.exec_())
