from PyQt5 import QtWidgets, QtGui
from PyQt5.Qt import Qt
from calcules_Ui import Ui_Calculator
from PyQt5.QtWidgets import QMessageBox



class CalculatorWindow(QtWidgets.QMainWindow, Ui_Calculator):

    expression = "0"
    lparen = 0
    rparen = 0
    equals = 0

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()
        self.setWindowTitle("Calcules")
        self.setWindowIcon(QtGui.QIcon('logo.ico'))
        self.label_input.setText("0 ")

        self.pushButton_0.clicked.connect(lambda: self.digit_pressed("0"))
        self.pushButton_1.clicked.connect(lambda: self.digit_pressed("1"))
        self.pushButton_2.clicked.connect(lambda: self.digit_pressed("2"))
        self.pushButton_3.clicked.connect(lambda: self.digit_pressed("3"))
        self.pushButton_4.clicked.connect(lambda: self.digit_pressed("4"))
        self.pushButton_5.clicked.connect(lambda: self.digit_pressed("5"))
        self.pushButton_6.clicked.connect(lambda: self.digit_pressed("6"))
        self.pushButton_7.clicked.connect(lambda: self.digit_pressed("7"))
        self.pushButton_8.clicked.connect(lambda: self.digit_pressed("8"))
        self.pushButton_9.clicked.connect(lambda: self.digit_pressed("9"))

        self.pushButton_decimal.clicked.connect(self.decimal_pressed)
        self.pushButton_root.clicked.connect(self.root_pressed)
        self.pushButton_clear.clicked.connect(self.clear_pressed)
        self.pushButton_del.clicked.connect(self.del_pressed)
        self.pushButton_eq.clicked.connect(self.equals_pressed)

        self.pushButton_plus.clicked.connect(lambda: self.function_pressed("+ "))
        self.pushButton_minus.clicked.connect(lambda: self.function_pressed("- "))
        self.pushButton_times.clicked.connect(lambda: self.function_pressed("* "))
        self.pushButton_divide.clicked.connect(lambda: self.function_pressed("/ "))
        self.pushButton_pow.clicked.connect(lambda: self.function_pressed("^ "))
        self.pushButton_nroot.clicked.connect(lambda: self.function_pressed("√ "))
        self.pushButton_factor.clicked.connect(lambda: self.function_pressed("! "))

        self.pushButton_lparen.clicked.connect(lambda: self.paren_pressed("( "))
        self.pushButton_rparen.clicked.connect(lambda: self.paren_pressed(") "))

        self.pushButton_sin.clicked.connect(lambda: self.trig_pressed("sin( "))
        self.pushButton_cos.clicked.connect(lambda: self.trig_pressed("cos( "))
        self.pushButton_tan.clicked.connect(lambda: self.trig_pressed("tan( "))
        self.pushButton_cotan.clicked.connect(lambda: self.trig_pressed("cotan( "))

        self.pushButton_help.clicked.connect(self.help)

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_0:
            self.digit_pressed("0")
        
        elif event.key() == Qt.Key_1:
            self.digit_pressed("1")
        
        elif event.key() == Qt.Key_2:
            self.digit_pressed("2")
        
        elif event.key() == Qt.Key_3:
            self.digit_pressed("3")
        
        elif event.key() == Qt.Key_4:
            self.digit_pressed("4")
        
        elif event.key() == Qt.Key_5:
            self.digit_pressed("5")
        
        elif event.key() == Qt.Key_6:
            self.digit_pressed("6")
        
        elif event.key() == Qt.Key_7:
            self.digit_pressed("7")
        
        elif event.key() == Qt.Key_8:
            self.digit_pressed("8")
        
        elif event.key() == Qt.Key_9:
            self.digit_pressed("9")
        
        elif event.key() == Qt.Key_Plus:
            self.function_pressed("+ ")
        
        elif event.key() == Qt.Key_Minus:
            self.function_pressed("- ")

        elif event.key() == Qt.Key_Slash:
            self.function_pressed("/ ")
        
        elif event.key() == Qt.Key_Asterisk:
            self.function_pressed("* ")

        elif event.key() == Qt.Key_Exclam:
            self.function_pressed("! ")
        
        elif event.key() == Qt.Key_AsciiCircum:
            self.function_pressed("^ ")

        elif event.key() == Qt.Key_ParenLeft:
            self.paren_pressed("( ")

        elif event.key() == Qt.Key_ParenRight:
            self.paren_pressed(") ")
        
        elif event.key() == Qt.Key_Backspace:
            self.del_pressed()
        
        elif event.key() == Qt.Key_C:
            self.clear_pressed()
        
        elif event.key() == Qt.Key_Enter:
            self.equals_pressed()

        elif event.key() == Qt.Key_Return:
            self.equals_pressed()
        
        elif event.key() == Qt.Key_Comma:
            self.decimal_pressed()
        
        elif event.key() == Qt.Key_Period:
            self.decimal_pressed()
        

    def show_input(self):
        self.label_input.setText(self.expression.replace(' ', '') + ' ')
        self.label_output.setText("")
        self.equals = 0
        self.error = 0

    def digit_pressed(self, digit):
        new_label = ""
        numbers = self.expression.split(' ')
        last = len(numbers) - 1
        if numbers[last] == "0" or self.equals == 1:
            new_number = digit
        else:
            new_number = numbers[last] + digit

        if last == 0:
            self.expression = new_number
        else:
            for i in range(0, last):
                new_label = new_label + ' ' + numbers[i]
            self.expression = new_label + ' ' + new_number

        self.show_input()

    def decimal_pressed(self):
        if self.equals == 1:
            self.expression = "0"

        numbers = self.expression.split(' ')
        last = len(numbers) - 1
        if (numbers[last] != "") and (numbers[last].find('.') == -1):
            self.expression = self.expression + '.'
            self.show_input()

    def function_pressed(self, funct):
        if self.expression[-1] != " ":
            self.expression = self.expression + " "
        self.expression = self.expression + funct
        self.show_input()

    def paren_pressed(self, funct):

        if self.equals == 1:
            self.expression = "0"

        if funct == "( ":
            self.lparen += 1
        else:
            self.rparen += 1

        if self.expression[-1] != " ":
            self.expression = self.expression + " "

        if self.expression == "0 ":
            self.expression = funct
        else:
            self.expression = self.expression + funct
        self.show_input()

    def root_pressed(self):
        if self.equals == 1:
            self.expression = "0"

        if self.expression[-1] != " ":
            self.expression = self.expression + " "

        if self.expression == "0 ":
            self.expression = "2√ "
        else:
            self.expression = self.expression + "2√ "
        self.show_input()

    def trig_pressed(self, funct):
        if self.equals == 1:
            self.expression = "0"

        self.lparen += 1
        if self.expression[-1] != " ":
            self.expression = self.expression + " "

        if self.expression == "0 ":
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
                if self.expression == "":
                    self.expression = numbers[i]
                else:
                    self.expression = self.expression + " " + numbers[i]
        else:
            self.expression = self.expression[:-1]
        if self.expression == '':
            self.expression = "0"
        self.show_input()

    def equals_pressed(self):
        error = 0
        if self.lparen == self.rparen:
            result = "PLACEHOLDER"           ## Here sends equation to processing unit
            self.label_output.setText(result + " ")
            error = 1
            if result != "Math Error":
                self.expression = result
                error = 0
        else:
            self.label_output.setText("Syntax Error ")
            error = 1 
        
        if error == 0:
            self.equals = 1

    def help(self):
        msg = QMessageBox()
        msg.setWindowTitle("Help")
        msg.setText("Calcules Manual")
        msg.setIcon(QMessageBox.Information)
        msg.setStandardButtons(QMessageBox.Ok)
        msg.setDefaultButton(QMessageBox.Ok)
        msg.setEscapeButton(QMessageBox.Ok)

        msg.setInformativeText("Calcules is a simple calculator.\n"
                               "You can press buttons on screen or on your keyboard to provide input.\n"
                               "On keyboard you can use numbers,\n"
                               ", or . as decimal point,\n"
                               "+ - * / ! ^ for operations,\n"
                               "( ) as parentheses,\n"
                               "Backspace for deleting last input,\n"
                               "C for clearing whole input,\n"
                               "Enter or = for display the result.\n")
        msg.setDetailedText("ADD MORE DETAILS")          #TODO
        msg.exec_()



