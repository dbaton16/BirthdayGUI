from PyQt6 import QtWidgets, QtCore
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtCore import QDate, QTime, QDateTime, Qt
import sys
import dateutil
from dateutil import relativedelta
from datetime import datetime

#print(birthdayPicker.dateTime().toString())
"""
# Zodiac dates
# Aries : Mar 21 - Apr 19
ariesS = QtCore.QDate.fromString("04-21", "yyyy-MM-dd")
ariesF = QtCore.QDate.fromString("05-19", "yyyy-MM-dd")
print(ariesS, ariesF)
# Taurus : Apr 20 - May 20
# Gemini : May 21 - Jun 21
# Cancer : Jun 22 - Jul 22
# Leo : July 23 - August 22
# Virgo : August 23 - Sept 22
# Libra : Sept 23 - Oct 23
# Scorpio : Oct 24 - Nov 21
# Sagittarius : Nov 22 - Dec 21
# Capricorn : Dec 22 - Jan 19
# Aquarius : Jan 20 - Feb 18
# Pisces : Feb 19 - Mar 20
"""
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
    # Fixes the size of the window
    window.setFixedSize(Wwidth,Wheight)

    # bottom subframe here
    bframe = QFrame(window)
    #bframe.setFrameShape(QFrame.StyledPanel)
    bframe.setGeometry(0, 220, 500, 300)
    bframe.setStyleSheet("background-color: #e6e8e8;")
    bframe.hide() #hides frame until user enters info

    # Tabs for bottom frame
    tab = QTabWidget(bframe)
    tab.resize(500, 300)
    layout = QFormLayout()
    layout.addWidget(tab)
    #Styles tabs
    stylesheet = """ 
        QTabBar::tab:selected {background: #000000;}
        QTabWidget>QWidget>QWidget{background: #e6e8e8;}
        """
    tab.setStyleSheet(stylesheet)
    #Creates year tab widget
    yearpage = QWidget(tab)
    yearpage_layout = QVBoxLayout()
    yearpage.setLayout(yearpage_layout)
    #Creates month tab widget
    monthpage = QWidget(tab)
    monthpage_layout = QVBoxLayout()
    monthpage.setLayout(monthpage_layout)
    #Creates day tab widget
    daypage = QWidget(tab)
    daypage_layout = QVBoxLayout()
    daypage.setLayout(daypage_layout)

    #Adds the tab widgets to the QTabWidget
    tab.addTab(yearpage, "Years")
    tab.addTab(monthpage, "Months")
    tab.addTab(daypage, "Days")

    tab.show()

    # FUNCTIONS
    def calcAge():
        # Prints user entry into console
        print(f"Birthday Entered: {birthdayPicker.date().toString()}")

        #Assigns the current date and the birthdate entered to variables
        now = QDate.currentDate()
        birthday = birthdayPicker.date()

        start_date = datetime.strptime(birthday.toString("dd/MM/yyyy"), "%d/%m/%Y")
        end_date = datetime.strptime(now.toString("dd/MM/yyyy"), "%d/%m/%Y")
        delta = relativedelta.relativedelta(end_date, start_date)

        ageDays = birthday.daysTo(now)
        ageMonths = delta.months + (delta.years * 12)
        ageYears = int(ageDays/365)
        """
        zodiac = ""
        if birthday
        """
        #Adds year label to the Years tab
        yrsoldlabel = QLabel()
        yrsoldlabel.setText(f"You are {ageYears} years old!")
        yrsoldlabel.setFont(QFont('Arial', 12))
        yrsoldlabel.setGeometry(100, 30, 150, 15)
        yrsoldlabel.adjustSize()
        yearpage.layout().addWidget(yrsoldlabel)

        #Adds month label to the Months tab
        monthsoldlabel = QLabel()
        monthsoldlabel.setText(f"You are {ageMonths} months old!")
        monthpage.setLayout(monthpage_layout)
        monthpage.layout().addWidget(monthsoldlabel)

        #Adds day label to the Days tab
        daysoldlabel = QLabel()
        daysoldlabel.setText(f"You are {ageDays} days old!")
        daypage.layout().addWidget(daysoldlabel)
        daysoldlabel.setFont(QFont('Arial', 12))
        daysoldlabel.setGeometry(170, 50, 150, 15)
        daysoldlabel.adjustSize()
        #print(ageDays, ageYears)



        # Alert box/ Message box with zodiac sign
        zodiacAlert = QMessageBox()
        #zodiacAlert.setStyle("Zodiac Sign")
        #zodiacAlert.setIcon(QMessageBox.Information)
        zodiacAlert.setText("Your Zodiac sign is..")
        #zodiacAlert.setStandardButtons(QMessageBox.Ok)
        #zodiacAlert.setInformativeText(sign)
        zodiacAlert.adjustSize()
        retval = zodiacAlert.exec()

        # Shows the bottom frame
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
