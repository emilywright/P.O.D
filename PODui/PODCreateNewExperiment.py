import sys
import os
import csv
from PyQt5 import QtCore, QtGui, QtWidgets
from PODAddGroup import addGroup
# from PyQt5.QtWidgets import QLineEdit
# from PODWelcomePage import Window

class createNew(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui(self)

    def init_ui(self, *args):
        self.setWindowTitle("P.O.D.")

        # far down on page, far left on page, width, height
        self.setGeometry(325, 100, 650, 400)

        # self.setStyleSheet("background-color:#CGCGCG");

        # labels
        # Background label
        self.menuLabel = QtWidgets.QLabel(self)
        self.menuLabel.setGeometry(QtCore.QRect(0, 0, 175, 70))
        self.menuLabel.setStyleSheet("background-color:#98FB98")

        self.podbackLabel = QtWidgets.QLabel(self)
        self.podbackLabel.setGeometry(QtCore.QRect(175, 0, 600, 70))
        self.podbackLabel.setStyleSheet("background-color:#FFFFFF")
        # Image logo
        self.podLogo = QtWidgets.QLabel(self)
        self.originalpixmap = QtGui.QPixmap('podLogo1.png')
        self.adjustedPixmap = self.originalpixmap.scaled(150, 150, QtCore.Qt.KeepAspectRatio, QtCore.Qt.FastTransformation)
        self.podLogo.setPixmap(self.adjustedPixmap)
        self.podLogo.setStyleSheet("background-color:#98FB98")
        self.podLogo.move(15, 10)
        # Create new experiment labels
        self.createNewLabel = QtWidgets.QLabel(self)
        self.createNewLabel.setText('Create New Experiment')
        self.createNewLabel.move(250, 15)
        self.createFont = QtGui.QFont("Times", 24, QtGui.QFont.Bold)
        self.createNewLabel.setFont(self.createFont)
        self.createNewLabel.setStyleSheet("background-color:#FFFFFF")

        self.inputFont = QtGui.QFont("Times", 12, QtGui.QFont.Bold)
        # Experiment name
        self.experimentNameLabel = QtWidgets.QLabel(self)
        self.experimentNameLabel.setText('Experiment Name:')
        self.experimentNameLabel.move(15, 90)
        self.experimentNameLabel.setFont(self.inputFont)
        # experiment name textbox
        self.experimentNameTextBox = QtWidgets.QLineEdit(self)
        self.experimentNameTextBox.move(150, 90)
        self.experimentNameTextBox.resize(150,25)
        self.experimentNameTextBox.setStyleSheet("background-color:#FFFFFF")

        # Group name
        # self.groupNameLabel = QtWidgets.QLabel(self)
        # self.groupNameLabel.setText('Group Name:')
        # self.groupNameLabel.move(15, 120)
        # self.groupNameLabel.setFont(self.inputFont)
        # # group name textbox
        # self.groupNameTextBox = QtWidgets.QLineEdit(self)
        # self.groupNameTextBox.move(150, 120)
        # self.groupNameTextBox.resize(150,25)
        # self.groupNameTextBox.setStyleSheet("background-color:#FFFFFF")

        # POD Number
        self.PODNumLabel = QtWidgets.QLabel(self)
        self.PODNumLabel.setText('P.O.D. Number:')
        self.PODNumLabel.move(15, 120)
        self.PODNumLabel.setFont(self.inputFont)
        # POD number textbox
        self.PODNumberTextBox = QtWidgets.QLineEdit(self)
        self.PODNumberTextBox.move(150, 120)
        self.PODNumberTextBox.resize(150,25)
        self.PODNumberTextBox.setStyleSheet("background-color:#FFFFFF")

        # Start Experiment Time
        self.startTimeLabel = QtWidgets.QLabel(self)
        self.startTimeLabel.setText('Start Time:')
        self.startTimeLabel.move(320, 90)
        self.startTimeLabel.setFont(self.inputFont)
        # End Time
        self.endTimeLabel = QtWidgets.QLabel(self)
        self.endTimeLabel.setText('End Time:')
        self.endTimeLabel.move(320, 120)
        self.endTimeLabel.setFont(self.inputFont)

        # Pictures per day label
        self.endTimeLabel = QtWidgets.QLabel(self)
        self.endTimeLabel.setText('Pictures per day:')
        self.endTimeLabel.move(15, 210)
        self.endTimeLabel.setFont(self.inputFont)

        # Pictures per day
        self.picuresPerDay = QtWidgets.QSpinBox(self)
        self.picuresPerDay.move(140, 210)

        # Button font
        self.buttonFont = QtGui.QFont("Helvetica", 12)

        self.exitButton = QtWidgets.QPushButton(self)
        self.exitButton.setText('Exit')
        self.exitButton.move(70, 300)
        self.exitButton.resize(100, 40);
        self.exitButton.setStyleSheet("background-color:#FFFFFF")
        self.exitButton.setFont(self.buttonFont)
        self.exitButton.clicked.connect(self.close)

        self.createButton = QtWidgets.QPushButton(self)
        self.createButton.setText('Add Group')
        self.createButton.move(270, 300)
        self.createButton.resize(100, 40)
        self.createButton.setStyleSheet("background-color:#FFFFFF")
        self.createButton.setFont(self.buttonFont)
        self.createButton.clicked.connect(self.openAddGroup)

        self.createButton = QtWidgets.QPushButton(self)
        self.createButton.setText('Create')
        self.createButton.move(480, 300)
        self.createButton.resize(100, 40);
        self.createButton.setStyleSheet("background-color:#FFFFFF")
        self.createButton.setFont(self.buttonFont)
        self.createButton.clicked.connect(self.createExperiment)

        self.startDate = QtWidgets.QDateEdit(self)
        self.startDate.setDisplayFormat("MMM d yyyy")
        self.startDate.setDate(QtCore.QDate.currentDate())
        self.startDate.move(420, 90)

        self.startTime = QtWidgets.QTimeEdit(self)
        self.startTime.setDisplayFormat('hh:mm AP')
        self.startTime.move(540, 90)

        self.endDate = QtWidgets.QDateEdit(self)
        self.endDate.setDisplayFormat("MMM d yyyy")
        self.endDate.setDate(QtCore.QDate.currentDate())
        self.endDate.move(420, 120)

        self.endTime = QtWidgets.QTimeEdit(self)
        self.endTime.setDisplayFormat('hh:mm AP')
        self.endTime.move(540, 120)

        # Water Cycle label
        self.waterCycleLabel = QtWidgets.QLabel(self)
        self.waterCycleLabel.setText('Water Cycle (Hours):')
        self.waterCycleLabel.move(15, 150)
        self.waterCycleLabel.setFont(self.inputFont)

        # Watering Time label
        self.waterTimeLabel = QtWidgets.QLabel(self)
        self.waterTimeLabel.setText('Watering Time (Seconds):')
        self.waterTimeLabel.move(15, 180)
        self.waterTimeLabel.setFont(self.inputFont)

        # Water number textbox
        self.waterTime = QtWidgets.QTimeEdit(self)
        self.waterTime.setDisplayFormat('hh')
        self.waterTime.move(200, 150)

        # Water number textbox
        self.wateringTime = QtWidgets.QTimeEdit(self)
        self.wateringTime.setDisplayFormat('ss')
        self.wateringTime.move(200, 180)

        # light label
        self.waterCycleLabel = QtWidgets.QLabel(self)
        self.waterCycleLabel.setText('Input CSV file for Lights:')
        self.waterCycleLabel.move(320, 150)
        self.waterCycleLabel.setFont(self.inputFont)

        self.csvFileTextBox = QtWidgets.QLineEdit(self)
        self.csvFileTextBox.move(405, 180)
        self.csvFileTextBox.resize(180, 25)
        self.csvFileTextBox.setStyleSheet("background-color:#D3D3D3")
        self.csvFileTextBox.setDisabled(True)

        self.browseButton = QtWidgets.QPushButton(self)
        self.browseButton.setText('Browse')
        self.browseButton.move(323, 182)
        self.browseButton.resize(80, 20);
        self.browseButton.setStyleSheet("background-color:#FFFFFF")
        self.browseButton.setFont(self.buttonFont)
        self.browseButton.clicked.connect(self.openCSVFile)

        self.show()

    def openAddGroup(self):
        self.hide()
        self.dialog = addGroup()
        self.dialog.show()

    def openCSVFile(self):
        self.path, _ = QtWidgets.QFileDialog.getOpenFileName(self, 'Open CSV', os.getenv('HOME'), 'CSV(*.csv)')
        self.file = QtCore.QFileInfo(self.path).fileName()
        # print(self.file)
        self.csvFileTextBox.setStyleSheet("background-color:#FFFFFF")
        self.csvFileTextBox.setText(self.file)

    def createExperiment(self):
        with open("currentExperiments/" + self.experimentNameTextBox.text() + ".csv", 'w') as self.f:
            self.f.write(self.experimentNameTextBox.text() + "\n")
            self.f.write("  \n")
            self.f.write(self.PODNumberTextBox.text() + "\n")
            self.f.write(self.waterTime.time().toString("hh") + "\n")
            self.f.write(self.wateringTime.time().toString("ss") + "\n")
            self.f.write(self.startDate.date().toString("MM d yyyy") + "\n")
            self.f.write(self.startTime.time().toString("hh:mm AP") + "\n")
            self.f.write(self.endDate.date().toString("MM d yyyy") + "\n")
            self.f.write(self.endTime.time().toString("hh:mm AP") + "\n")
            self.f.write(self.file)
