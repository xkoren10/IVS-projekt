## @file: calculator.py
# @brief: Realization of graphical user interface
# @author: Marek Tiss, xtissm00, PyJaMa's
# @date: March/April 2021

from PyQt5.QtGui import QIcon, QFont
from PyQt5.Qt import Qt
from calcules_Ui import Ui_Calculator
from PyQt5.QtWidgets import QMessageBox, QDialog, QPushButton, QLabel, QScrollArea, QWidget, QMainWindow
import calc
import os


## @var history
# Global variable that tracks history of inputs/outputs
history = ''


class CalculatorWindow(QMainWindow, Ui_Calculator):
    ##
    # Variable containing current expression from input
    expression = "0"
    # Variables tracking number of used parentheses
    lparen = 0
    rparen = 0
    # Variable tracking if last action was pressing equals
    equals = 0

    ##
    # @brief Initialization of main window
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()

        ##
        # Setting name and logo of main window
        self.setWindowTitle("Calcules")
        self.setWindowIcon(QIcon('logo.ico'))
        # Showing 0 at input at the start of app
        self.label_input.setText("0 ")

        # Connecting buttons on GUI to the functions
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

        self.pushButton_help.clicked.connect(self.help_window)
        self.pushButton_hist.clicked.connect(self.history_window)

    ##
    # @brief Connecting keys on keyboard to the functions
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

    ##
    # @brief Formatting expression and showing it as input
    def show_input(self):
        # Placing formatted expression to display input
        self.label_input.setText(self.expression.replace(' ', '') + ' ')
        # Making output blank
        self.label_output.setText("")
        # Resetting equals 0
        self.equals = 0

    ##
    # @brief Preparing expression for some functions
    def zero_and_space(self):
        # Setting expression to 0 if last action was pressing equals
        if self.equals == 1:
            self.expression = "0"
        # Adding space if it's missing for creating list
        if self.expression[-1] != " ":
            self.expression = self.expression + " "

    ##
    # @brief Adds operation to expression
    # @param add Which operation should be added
    def add_to_expression(self, add):
        # If expression is "empty", replaces expression 
        if self.expression == "0 ":
            self.expression = add
        # If expression isn't "empty", adds to the end of expression  
        else:
            self.expression = self.expression + add

    ##
    # @brief Adding digit to input
    # @param digit Which digit was pressed
    def digit_pressed(self, digit):
        # Declaration of new blank label
        new_label = ""
        # Splitting expression by space so the last element is number
        numbers = self.expression.split(' ')
        # Getting index of last element of numbers
        last = len(numbers) - 1
        # Checking if new number should replace last or if it should be added
        if numbers[last] == "0" or self.equals == 1:
            new_number = digit
        else:
            new_number = numbers[last] + digit
        # Creating new expression
        if last == 0:
            self.expression = new_number
        else:
            for i in range(0, last):
                new_label = new_label + ' ' + numbers[i]
            self.expression = new_label + ' ' + new_number
        # Displaying input
        self.show_input()

    ##
    # @brief Adding decimal point to input
    def decimal_pressed(self):
        # Setting expression to 0 if last action was pressing equals
        if self.equals == 1:
            self.expression = "0"

        # Splitting expression by space so the last element is number
        numbers = self.expression.split(' ')
        # Getting index of last element of numbers
        last = len(numbers) - 1
        # Checking if last number exists and doesn't already have decimal point
        if (numbers[last] != "") and (numbers[last].find('.') == -1):
            # Adding decimal point and displaying input
            self.expression = self.expression + '.'
            self.show_input()
    
    ##
    # @brief Adding function to input
    # @param funct Which function was pressed
    def function_pressed(self, funct):
        # Adding space if it's missing for creating list
        if self.expression[-1] != " ":
            self.expression = self.expression + " "
        # Adding function and displaying input
        self.expression = self.expression + funct
        self.show_input()

    ##
    # @brief Adding parentheses to input
    # @param paren Which parenthesis was pressed
    def paren_pressed(self, paren):
        # Preparing expression
        self.zero_and_space()
        # Incrementing counter of used parenthesis
        if funct == "( ":
            self.lparen += 1
        else:
            self.rparen += 1
        # Adding parenthesis and displaying input
        self.add_to_expression(paren)
        self.show_input()

    ##
    # @brief Adding root to input
    def root_pressed(self):
        # Preparing expression
        self.zero_and_space()
        # Adding root and displaying input
        self.add_to_expression("2√ ")
        self.show_input()
    
    ##
    # @brief Adding trigonometric function to input
    # @param funct Which function was pressed
    def trig_pressed(self, funct):
        # Incrementing counter of left parenthesis
        self.lparen += 1
        # Preparing expression
        self.zero_and_space()
        # Adding trigonometric function to and displaying input
        self.add_to_expression(funct)
        self.show_input()

    ##
    # @brief Resetting state of calculator
    def clear_pressed(self):
        self.expression = "0"
        self.rparen = 0
        self.lparen = 0
        self.show_input()

    ##
    # @brief Deleting last action
    def del_pressed(self):
        # Splitting expression by space so the last element is number
        numbers = self.expression.split(' ')
        # Geting index of last element of numbers
        last = len(numbers) - 1
        # Decrementing counter of parenthesis if they were used in last action 
        if numbers[last - 1].find('(') != -1:
            self.lparen -= 1
        if numbers[last - 1] == ')':
            self.rparen -= 1

        # Checking if last action wasn't adding digit
        if numbers[last] == '':
            self.expression = ''
            # Adding all but last elements of number
            for i in range(0, last - 1):
                if self.expression == "":
                    self.expression = numbers[i] + " "
                else:
                    self.expression = self.expression + numbers[i] + " "
        # If the last action was adding digit, deleting it
        else:
            self.expression = self.expression[:-1]
        # If the resulting expression was blank, adding 0
        if self.expression == '':
            self.expression = "0"
        # Displaying intput
        self.show_input()

    ##
    # @brief Calculating expression and showing result
    def equals_pressed(self):   
        global history
        # Checking if correct amounts of parentheses are in the expression
        if self.lparen == self.rparen:
            # Calling function to evaluate expression
            result = calc.evaluate(self.expression)
            # Placeing result to display output
            self.label_output.setText(result + " ")
            # Adding expression and result to history
            history += self.expression.replace(' ', '') + '\n' + result + '\n\n'
            # Checking if result isn't error
            if result != "Math Error":
                # Setting result as new expression
                self.expression = result
                self.equals = 1
        # If amounts of parentheses aren't same output is error and history is updated
        else:
            self.label_output.setText("Syntax Error ")
            history += self.expression.replace(' ', '') + '\n' + "Syntax Error" + '\n\n'

    ##
    # @brief Displaying help message
    def help_window(self):
        msg = QMessageBox()
        # Setting help message look
        msg.setWindowTitle("Help")
        msg.setWindowIcon(QIcon('logo.ico'))
        msg.setText("Calcules")
        msg.setIcon(QMessageBox.Information)
        # Adding buttons
        msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Open)
        msg.setDefaultButton(QMessageBox.Ok)
        msg.setEscapeButton(QMessageBox.Ok)
        # Setting info
        msg.setInformativeText("Calcules is a simple calculator.\n"
                               "You can press buttons on screen or on your keyboard to provide input.\n"
                               "On keyboard you can use numbers,\n"
                               ", or . as decimal point,\n"
                               "+ - * / ! ^ for operations,\n"
                               "( ) as parentheses,\n"
                               "Backspace for deleting last input,\n"
                               "C for clearing whole input,\n"
                               "Enter or = for display the result.\n\n"
                               "For more information open manual by clicking open")
        # Displaying help message
        returnValue = msg.exec_()
        # Opening manual if open button was clicked
        if returnValue == QMessageBox.Open:
            # Getting path to the current directory
            dir_path = os.path.dirname(os.path.realpath(__file__))
            # Changing path to User_manual
            dir_path = dir_path[:-3]+"User manual.docx"
            # Opening User_manual
            os.startfile(dir_path)

    ##
    # @brief Displaying history
    def history_window(self):
        his = History()
        his.exec_()
           

class ScrollLabel(QScrollArea):
    ##
    # @brief Initialization of scrollable part of history
    def __init__(self, *args, **kwargs):
        QScrollArea.__init__(self, *args, **kwargs)
        self.setWidgetResizable(True)
        content = QWidget(self)
        self.setWidget(content)
        self.label = QLabel(content)
        self.label.setTextInteractionFlags(Qt.TextSelectableByMouse)
        self.label.setAlignment(Qt.AlignLeft | Qt.AlignTop)
        self.label.setWordWrap(True)
    
    ##
    # @brief Adding text to scrollable label
    # @param text Text to be added
    def setText(self, text):
        self.label.setText(text)


class History(QDialog):
    ##
    # @brief Initialization of history window
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        # Setting icon and title
        self.setWindowIcon(QIcon('logo.ico'))
        self.setWindowTitle("History")
        # Allowing text to by be copied
        self.setWindowFlags(self.windowFlags() & ~Qt.WindowContextHelpButtonHint)
        self.setFixedSize(1000, 750)
        # Calling function to add widgets and showing history window
        self.UiComponents()
        self.show()
    
    ##
    # @brief Adding widgets to history window
    def UiComponents(self):
        # Adding scrollable label
        self.label = ScrollLabel(self)
        # Adding text from variable history
        self.label.setText(history)
        # Setting font size
        self.label.setStyleSheet("font: 15pt;")
        # Setting size of label to fill whole window
        self.label.setGeometry(0, 0, 1000, 750)
        # Adding button to clear history
        self.clear_button = QPushButton('Clear', self)
        # Setting size and position of button
        self.clear_button.setGeometry(0, 0, 100, 50)
        self.clear_button.move(890, 690)
        # Setting style of buttons text
        font = QFont()
        font.setFamily("Noto Sans")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.clear_button.setFont(font)
        # Setting style of button
        self.clear_button.setStyleSheet("QPushButton   {border: 2px solid #8f8f91;\n    "
                                        "               border-radius: 6px;\n"
                                        "               background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
                                        "               stop: 0 #B3E5FC, stop: 1 #00AFFF);\n"
                                        "               min-width: 80px;\n"
                                        "              }\n"
                                        "QPushButton:pressed   {background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
                                        "                       stop: 0 #00AFFF, stop: 1#B3E5FC);\n"
                                        "                       }\n"
                                        "QPushButton:flat    { border: none}\n"
                                        "QPushButton:default { border-color: navy}")

        # Connecting button to clearing history
        self.clear_button.clicked.connect(self.clear_history)

    ##
    # @brief Clearing history of calculator
    def clear_history(self):
        global history
        history = ''
        # Displaying clear history
        self.label.setText(history)
