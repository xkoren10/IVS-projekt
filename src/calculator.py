from PyQt5 import QtWidgets
from calcules_Ui import Ui_Calculator


class CalculatorWindow(QtWidgets.QMainWindow, Ui_Calculator):

    expression = "0"
    lbracket = 0
    rbracket = 0

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()
        self.label_input.setText("0 ")

        self.pushButton_0.clicked.connect(self.digit_pressed)
        self.pushButton_1.clicked.connect(self.digit_pressed)
        self.pushButton_2.clicked.connect(self.digit_pressed)
        self.pushButton_3.clicked.connect(self.digit_pressed)
        self.pushButton_4.clicked.connect(self.digit_pressed)
        self.pushButton_5.clicked.connect(self.digit_pressed)
        self.pushButton_6.clicked.connect(self.digit_pressed)
        self.pushButton_7.clicked.connect(self.digit_pressed)
        self.pushButton_8.clicked.connect(self.digit_pressed)
        self.pushButton_9.clicked.connect(self.digit_pressed)

        self.pushButton_decimal.clicked.connect(self.decimal_pressed)
        self.pushButton_root.clicked.connect(self.root_pressed)
        self.pushButton_clear.clicked.connect(self.clear_pressed)
        self.pushButton_del.clicked.connect(self.del_pressed)

        self.pushButton_plus.clicked.connect(lambda: self.function_pressed(" + "))
        self.pushButton_minus.clicked.connect(lambda: self.function_pressed(" - "))
        self.pushButton_times.clicked.connect(lambda: self.function_pressed(" * "))
        self.pushButton_divide.clicked.connect(lambda: self.function_pressed(" / "))
        self.pushButton_pow.clicked.connect(lambda: self.function_pressed(" ^ "))
        self.pushButton_nroot.clicked.connect(lambda: self.function_pressed(" √ "))
        self.pushButton_factor.clicked.connect(lambda: self.function_pressed(" ! "))

        self.pushButton_lbracket.clicked.connect(lambda: self.bracket_pressed(" ( "))
        self.pushButton_rbracket.clicked.connect(lambda: self.bracket_pressed(" ) "))

        self.pushButton_sin.clicked.connect(lambda: self.trig_pressed(" sin( "))
        self.pushButton_cos.clicked.connect(lambda: self.trig_pressed(" cos( "))
        self.pushButton_tan.clicked.connect(lambda: self.trig_pressed(" tan( "))
        self.pushButton_cotan.clicked.connect(lambda: self.trig_pressed(" cotan( "))

    def show_input(self):
        self.label_input.setText(self.expression.replace(' ', '') + ' ')

    def digit_pressed(self):
        button = self.sender()

        new_label = ""
        numbers = self.expression.split(' ')
        last = len(numbers) - 1
        new_number = format(float(numbers[last] + button.text()), '.15g')

        if last == 0:
            self.expression = new_number
        else:
            for i in range(0, last):
                new_label = new_label + ' ' + numbers[i]
            self.expression = new_label + ' ' + new_number

        self.show_input()

    def decimal_pressed(self):
        numbers = self.expression.split(' ')
        last = len(numbers) - 1
        if (numbers[last] != "") and (numbers[last].find('.') == -1):
            self.expression = self.expression + '.'
            self.show_input()

    def function_pressed(self, funct):
        self.expression = self.expression + funct
        self.show_input()

    def bracket_pressed(self, funct):
        if funct == " ( ":
            self.lbracket += 1
        else:
            self.rbracket += 1

        if self.expression == "0":
            self.expression = funct
        else:
            self.expression = self.expression + funct
        self.show_input()

    def root_pressed(self):
        if self.expression == "0":
            self.expression = " 2√ "
        else:
            self.expression = self.expression + " 2√ "
        self.show_input()

    def trig_pressed(self, funct):
        self.lbracket += 1
        if self.expression == "0":
            self.expression = funct
        else:
            self.expression = self.expression + funct
        self.show_input()

    def clear_pressed(self):
        self.expression = "0"
        self.show_input()

    def del_pressed(self):
        numbers = self.expression.split(' ')
        last = len(numbers) - 1
        if numbers[last] == '':
            self.expression = ''
            for i in range(0, last - 1):
                self.expression = self.expression + " " + numbers[i]
        else:
            self.expression = self.expression[:-1]
        if self.expression == '':
            self.expression = "0"
        self.show_input()

