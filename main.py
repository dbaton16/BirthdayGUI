from PyQt6 import QtWidgets, QtCore
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtCore import QDate, QTime, QDateTime, Qt
import sys
import dateutil
from dateutil import relativedelta
from datetime import datetime, date
import csv

#print(birthdayPicker.dateTime().toString())

entries = 0
#print((now.tostring(Qt.ISODate)))
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
        QTabBar::tab:selected {background: #9c9c9c;}
        QTabWidget>QWidget>QWidget{background: #e6e8e8;}
        """
    tab.setStyleSheet(stylesheet)

    # Makes tabs using for loop
    tab_pages = ['Years', 'Months', 'Days', 'Hours', 'Minutes', 'Seconds']
    labels = []
    tab_layouts = []
    layouts = []
    for i in tab_pages:
        name = i.lower()
        namePage = QWidget(tab)
        tab_layouts.append(namePage)
        namePage_layout = QVBoxLayout()
        namePage.setLayout(namePage_layout)
        namePage.Label = QLabel()
        labels.append(namePage.Label)
        tab.addTab(namePage, f"{name.upper()}")

    tab.show()

    with open('Birthdays Entered.csv', 'w') as csvfile:
        columns = ["Entry Number", "Birthdate"]

        # create the DictWriter object
        csv_writer = csv.DictWriter(csvfile, fieldnames=columns, delimiter=';')
        csv_writer.writeheader()



    # FUNCTIONS
    def calcAge():
        global entries
        birthday_dict = {}
        entries += 1
        birthday_dict['Entry Number'] = f"{entries}"
        birthday_dict['Birthdate'] = f"{birthdayPicker.date().toString()}"

        with open('Birthdays Entered.csv', 'a') as csvfile:
            dictwriter_object = csv.DictWriter(csvfile, fieldnames=columns, delimiter=';')
            dictwriter_object.writerow(birthday_dict)

        # Prints user entry into console and adds it to csv file
        user_birthday = birthdayPicker.date().toString()
        print(f"Birthday Entered: {user_birthday}")

        #Assigns the current date and the birthdate entered to variables
        now = QDate.currentDate()
        birthday = birthdayPicker.date()

        start_date = datetime.strptime(birthday.toString("dd/MM/yyyy"), "%d/%m/%Y")
        end_date = datetime.strptime(now.toString("dd/MM/yyyy"), "%d/%m/%Y")
        delta = relativedelta.relativedelta(end_date, start_date)

        ageDays = birthday.daysTo(now)
        ageMonths = delta.months + (delta.years * 12)
        ageYears = int(ageDays/365.2425)
        ageHours = ageDays * 24
        ageMinutes = ageHours * 60
        ageSeconds = ageMinutes * 60
        """
        zodiac = ""
        if birthday
        """
        labels[0].setText(f"You are {ageYears} years old!")
        labels[1].setText(f"You are {ageMonths} months old!")
        labels[2].setText(f"You are {ageDays} days old!")
        labels[3].setText(f"You are {ageHours} hours old!")
        labels[4].setText(f"You are {ageMinutes} minutes old!")
        labels[5].setText(f"You are {ageSeconds} seconds old!")

        for x in range(6) :
            labels[x].setFont(QFont('Arial', 28))
            labels[x].setGeometry(100, 50, 200, 150)
            labels[x].adjustSize()
            tab_layouts[x].layout().addWidget(labels[x])


        # Zodiac Sign Check (start date, sign)
        #Takes current year
        z_year = now.year()
        z_birthday = birthday.toPyDate().replace(year=z_year)
        print(z_birthday)

        # Checks if birthday is Jan 1st, if so alerts about cool birthday
        if str(z_birthday)== (f"{z_year}-01-01"):
            newYearAlert = QMessageBox()
            newYearAlert.setText(f"Wow, you were born on the very\nfirst day of the year!\nThat's pretty cool!")
            newYearAlert.adjustSize()
            retval = newYearAlert.exec()


        z_signs = [(date(month=1, day=1, year=z_year), "Capricorn"), (date(month=1, day=20, year=z_year), "Aquarius"),
                   (date(month=2, day=18, year=z_year), "Pisces"), (date(month=3, day=21,year=z_year), "Aries"),
                   (date(month=4, day=20, year=z_year), "Taurus"), (date(month=5, day=21, year=z_year), "Gemini"),
                   (date(month=6, day=22, year=z_year), "Cancer"), (date(month=7, day=23, year=z_year), "Leo"),
                   (date(month=8, day=23, year=z_year), "Virgo"), (date(month=9, day=23, year=z_year), "Libra"),
                   (date(month=10, day=24, year=z_year), "Scorpio"), (date(month=11, day=22, year=z_year), "Sagittarius"),
                   (date(month=12, day=22, year=z_year), "Capricorn")]
        user_sign = None
        for sign in z_signs:
            if sign[0] <= z_birthday:
                user_sign = sign[1]
        print(user_sign)


        # Alert box/ Message box with zodiac sign
        zodiacAlert = QMessageBox()
        zodiacAlert.setText(f"Your Zodiac sign is... {user_sign.upper()}")
        zodiacAlert.adjustSize()
        retval = zodiacAlert.exec()

        # Shows the bottom frame
        bframe.show()

    # creating the welcome to label
    welcome_label = QtWidgets.QLabel(window)
    welcome_label.setText("Welcome to a...")
    welcome_label.setFont(QFont('Arial', 16))
    welcome_label.adjustSize()
    welcome_label.move(200, 15)

    # creating the title label using a picture
    pixmap = QPixmap('assets/title.png')
    pixmap_resized = pixmap.scaled(400, 150, QtCore.Qt.AspectRatioMode.KeepAspectRatio)
    birthday_label = QtWidgets.QLabel(window)
    #birthday_label.setText("BIRTHDAY CALCULATOR!")
    #birthday_label.setFont(QFont('Arial', 20))
    birthday_label.setPixmap(pixmap_resized)
    birthday_label.resize(400, 100)
    birthday_label.move(50, 10)

    # cake pictures
    cake_pixmap = QPixmap('assets/cake.png').scaled(300, 80, QtCore.Qt.AspectRatioMode.KeepAspectRatio)
    cake1_label = QtWidgets.QLabel(window)
    cake1_label.setPixmap(cake_pixmap)
    cake1_label.resize(300, 100)
    cake1_label.move(10, 10)

    cake_pixmap = QPixmap('assets/cake.png').scaled(300, 80, QtCore.Qt.AspectRatioMode.KeepAspectRatio)
    cake2_label = QtWidgets.QLabel(window)
    cake2_label.setPixmap(cake_pixmap)
    cake2_label.resize(300, 100)
    cake2_label.move(440, 10)


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




    window.show()
    sys.exit(app.exec())


window()
