from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import QDate, QTime, QDateTime, Qt
import sys
"""
# Functions for calculations
def calcAgeYears:
    bframe.show()
    currentDateTime = QDateTime.currentDateTime()
    print((currentDateTime.tostring(Qt.ISODate)))
"""
# Function for the main window
def window():
    # application
    app = QApplication(sys.argv)

    # creating the window
    window = QMainWindow()
    # window.setStyleSheet("background-color: grey;")
    # variables for window width and height
    Wwidth, Wheight = 500, 500
    window.setWindowTitle("Birthday GUI")
    window.setGeometry(500, 100, Wwidth, Wheight)

    # bottom subframe here
    bframe = QFrame(window)
    bframe.setFrameShape(QFrame.StyledPanel)
    bframe.setGeometry(0, 250, 500, 250)
    bframe.setStyleSheet("background-color: #c0c7d1;")
    bframe.hide() #hides frame until user enters info

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
    birthdayPicker = QDateTimeEdit(window)
    birthdayPicker.setGeometry(300, 90, 150, 35)
    birthdayPicker.setDisplayFormat("yyyy/MM/dd")

    #work in progress, maybe just use button
    #birthdayPicker.dateTimeChanged.connect()
    user_birthday = QLabel(window)
    user_birthday.setText("Date Chosen: " + str(birthdayPicker.dateTime))
    #user_birthday.setText(f"Date Chosen: {birthdayPicker.get}")
    user_birthday.setGeometry(300, 120, 150, 35)




    # NEXT STEP: use connect method to connect widgets to functions and use alerts for zodiac

    window.show()
    sys.exit(app.exec())


window()
