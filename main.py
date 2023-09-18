from PyQt6 import QtWidgets, QtCore
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtCore import QDate, QTime, QDateTime, Qt
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
    #bframe.setFrameShape(QFrame.StyledPanel)
    bframe.setGeometry(0, 250, 500, 250)
    bframe.setStyleSheet("background-color: #c0c7d1;")
    bframe.hide() #hides frame until user enters info

    # FUNCTIONS
    def calcAge():
        print(f"Birthday Entered: {birthdayPicker.date().toString()}")
        now = QDate.currentDate()
        birthday = birthdayPicker.date()

        ageDays = birthday.daysTo(now)
        ageYears = int(ageDays/365)

        zodiac = ""
        print(ageDays, ageYears)

        # Alert box/ Message box with zodiac sign
        zodiacAlert = QMessageBox("Information")
        #zodiacAlert.setTitle("Zodiac Sign")
        #zodiacAlert.setIcon(QMessageBox.Information)
        zodiacAlert.setText("Your Zodiac sign is..")
        #zodiacAlert.setStandardButtons(QMessageBox.Ok)
        #zodiacAlert.setInformativeText(sign)

        zodiacAlert.show()

        # Adds age info to frame, then show it
        yearslabel = QtWidgets.QLabel(bframe)
        yearslabel.setText(f"You are {ageYears} years old.")
        yearslabel.setFont(QFont('Arial', 12))
        yearslabel.setGeometry(100, 30, 150, 15)

        dayslabel = QtWidgets.QLabel(bframe)
        dayslabel.setText(f"You are {ageDays} days old.")
        dayslabel.setFont(QFont('Arial', 12))
        dayslabel.setGeometry(170, 50, 150, 15)

        bframe.show()

        #add alert here to say zodiac


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
    birthdayPicker = QDateEdit(window)
    #birthdayPicker = QDateTimeEdit(window)
    birthdayPicker.setGeometry(300, 90, 150, 35)
    birthdayPicker.setDisplayFormat("yyyy/MM/dd")



    birthday = QtWidgets.QPushButton(window)
    birthday.setText("Enter Birthday")
    birthday.setGeometry(295, 125, 150, 35)
    birthday.clicked.connect(calcAge)






    # NEXT STEP: calculate age in years, use alerts for zodiac

    window.show()
    sys.exit(app.exec())


window()
