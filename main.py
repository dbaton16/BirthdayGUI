from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import * 
from PyQt5.QtGui import *
from PyQt5.QtCore import QDate, QTime, QDateTime, Qt
import sys

# Function for the main window
def window():
    # application
    app = QApplication(sys.argv)

    # creating the window
    window = QMainWindow()
    #window.setStyleSheet("background-color: grey;")
    # variables for window width and height
    Wwidth, Wheight = 500, 500
    window.setWindowTitle("Birthday GUI")
    window.setGeometry(500, 100, Wwidth, Wheight)

    # divide into top and bottom subframe here
    # maybe try to make frame hidden until user enters info
    
    # creating the welcome to label
    welcome_label = QtWidgets.QLabel(window)
    welcome_label.setText("Welcome to a...")
    welcome_label.setFont(QFont('Arial', 12))
    welcome_label.adjustSize()
    welcome_label.move(200, 10)

    # creating the title label
    birthday_label = QtWidgets.QLabel(window)
    birthday_label.setText("BIRTHDAY GUI")
    birthday_label.setFont(QFont('Arial', 20))
    birthday_label.adjustSize()
    birthday_label.move(160, 30)


    # creating the entry box for entering birthday
    birthday_instruction = QtWidgets.QLabel(window)
    birthday_instruction.setText("Please enter your date of birth: ")
    birthday_instruction.setFont(QFont('Arial', 12))
    birthday_instruction.adjustSize()
    birthday_instruction.move(80, 100)
    datetimeedit = QDateTimeEdit(window)
    datetimeedit.setGeometry(100, 100, 150, 35)
    datetimeedit.setDisplayFormat("dd/MM/yyyyy")
    #birthday_entry = QtWidgets.QTextEdit(window)
    #birthday_entry.move(300, 100)

    #handle keypress for user entry
    def keyPressEvent(key):
        if key.key() == Qt.Key_enter:
            app.close()

    #NEXT STEP: create a frame underneath, use connect method to connect widgets to functions and use alerts for zodiac

    window.show()
    sys.exit(app.exec())

window()

