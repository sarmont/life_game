import sys

from PyQt5 import uic  # Импортируем uic
from PyQt5.QtWidgets import QApplication, QMainWindow


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('calc.ui', self)  # Загружаем дизайн
        self.action = ''
        self.dot = False
        self.new_num = False
        self.table.display('0')
        self.btn1.clicked.connect(self.add_num)
        self.btn2.clicked.connect(self.add_num)
        self.btn3.clicked.connect(self.add_num)
        self.btn4.clicked.connect(self.add_num)
        self.btn5.clicked.connect(self.add_num)
        self.btn6.clicked.connect(self.add_num)
        self.btn7.clicked.connect(self.add_num)
        self.btn8.clicked.connect(self.add_num)
        self.btn9.clicked.connect(self.add_num)
        self.btn0.clicked.connect(self.add_num)

        self.btn_clear.clicked.connect(self.clear_c)

        self.btn_plus.clicked.connect(self.plus)

        self.btn_minus.clicked.connect(self.minus)

        self.btn_div.clicked.connect(self.div)

        self.btn_mult.clicked.connect(self.mult)

        self.btn_eq.clicked.connect(self.btn_equal)

        self.btn_pow.clicked.connect(self.pow)

        self.btn_sqrt.clicked.connect(self.sqrt)

        self.btn_fact.clicked.connect(self.fact)

        self.btn_dot.clicked.connect(self.add_dot)

    def add_dot(self):
        pre_num = self.table.intValue()
        self.pre_num_dot = str(pre_num) + '.'
        self.table.display(self.pre_num_dot)
        self.dot = True

    def add_num(self):

        btn_number = self.sender().text()

        if self.dot is True:
            self.table.display(self.pre_num_dot + btn_number)
            self.dot = False

        elif self.table.intValue() == 0:
            self.table.display(btn_number)
        else:
            if self.new_num is True:
                self.table.display(btn_number)
                self.new_num = False
            else:
                if btn_number == '0':
                    self.table.display(btn_number)
                else:
                    self.table.display(str(self.table.value()) + btn_number)

    def clear_c(self):
        self.table.display('0')

    def plus(self):
        self.new_num = True
        self.action = '+'
        self.a = self.table.value()

    def minus(self):
        self.new_num = True
        self.action = '-'
        self.a = self.table.value()

    def pow(self):
        self.new_num = True
        self.action = '^'
        self.a = self.table.value()

    def sqrt(self):

        self.action = 'sqrt'
        self.a = self.table.value()
        self.table.display(self.a ** 0.5)

    def mult(self):
        self.new_num = True
        self.action = '*'
        self.a = self.table.value()

    def div(self):
        self.new_num = True
        self.action = '/'
        self.a = self.table.value()

    def fact(self):
        s = 1
        self.action = 'sqrt'
        self.a = self.table.value()
        for i in range(1, int(self.a) + 1):
            s *= i
        self.table.display(str(s))

    def btn_equal(self):
        self.b = self.table.value()
        if self.action == '+':
            self.table.display(self.a + self.b)
        if self.action == '-':
            self.table.display(self.a - self.b)
        if self.action == '*':
            self.table.display(self.a * self.b)
        if self.action == '/':
            if self.b != 0:
                self.table.display(self.a / self.b)
            else:
                self.table.display('ERROR')
        if self.action == '^':
            self.table.display(self.a ** self.b)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
