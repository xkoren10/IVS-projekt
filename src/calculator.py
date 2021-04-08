from PyQt5 import QtWidgets
from calcules_Ui import Ui_Calculator


class CalculatorWindow(QtWidgets.QMainWindow, Ui_Calculator):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()

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

        self.pushButton_plus.clicked.connect(lambda: self.function_pressed("+"))
        self.pushButton_minus.clicked.connect(lambda: self.function_pressed("-"))
        self.pushButton_times.clicked.connect(lambda: self.function_pressed("*"))
        self.pushButton_divide.clicked.connect(lambda: self.function_pressed("/"))
        self.pushButton_pow.clicked.connect(lambda: self.function_pressed("^"))
        self.pushButton_root.clicked.connect(lambda: self.function_pressed("√"))
        self.pushButton_factor.clicked.connect(lambda: self.function_pressed("!"))



    def digit_pressed(self):
        button = self.sender()

        new_label = ""
        numbers = self.label_input.text().split(' ')
        last = len(numbers) - 1
        new_number = format(float(numbers[last] + button.text()), '.15g')

        if (last == 0):
            new_label = new_number
        else:
            for i in range(0, last ):
                new_label = new_label + ' ' + numbers[i]
            new_label = new_label + ' ' + new_number

        self.label_input.setText(new_label)

    def decimal_pressed(self):
        # to do: add check if decimal already pressed
        self.label_input.setText(self.label_input.text() + '.')

    def function_pressed(self, funct):
        self.label_input.setText(self.label_input.text() + ' ' + funct + ' ')
