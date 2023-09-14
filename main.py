from PyQt5 import QtWidgets
from PyQt5.QtWidgets import * #QApplication, QWidget, QMainWindow
from PyQt5.QtGui import *
import sys

HI DARLA --> DELETE THIS  --> Just testing my access and commit rights.

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
    print("test!!")
    #birthday_entry = QtWidgets.QTextEdit(window)
    #birthday_entry.move(300, 100)

    window.show()
    sys.exit(app.exec())

window()

