import sys
import os
from PyQt5 import QtCore, QtGui, QtWidgets

class viewExperiment(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui(self)

    def init_ui(self, *args):
        self.setWindowTitle("P.O.D.")

        # far down on page, far left on page, width, height
        self.setGeometry(325, 100, 650, 400)

        self.setStyleSheet("background-color:#FFFFFF");
        #98FB98

        # Create new experiment labels
        self.createNewLabel = QtWidgets.QLabel(self)
        self.createNewLabel.setText('View Experiments')
        self.createNewLabel.move(300, 15)
        self.createFont = QtGui.QFont("Times", 24, QtGui.QFont.Bold)
        self.createNewLabel.setFont(self.createFont)
        self.createNewLabel.setStyleSheet("background-color:#FFFFFF")

        # labels
        # Background label
        self.menuLabel = QtWidgets.QLabel(self)
        self.menuLabel.setGeometry(QtCore.QRect(0, 0, 175, 70))
        self.menuLabel.setStyleSheet("background-color:#98FB98")
        # Image logo
        self.podLogo = QtWidgets.QLabel(self)
        self.originalpixmap = QtGui.QPixmap('podLogo1.png')
        self.adjustedPixmap = self.originalpixmap.scaled(150, 150, QtCore.Qt.KeepAspectRatio, QtCore.Qt.FastTransformation)
        self.podLogo.setPixmap(self.adjustedPixmap)
        self.podLogo.setStyleSheet("background-color:#98FB98")
        self.podLogo.move(15, 10)

        self.tableWidget = QtWidgets.QTableWidget(self)
        # set row count
        self.tableWidget.setRowCount(6)
        # set column count
        self.tableWidget.setColumnCount(6)
        self.tableWidget.setHorizontalHeaderLabels(('Experiment Name', 'Group Name', 'POD Number', 'Start Time', 'End Time', 'CSV File'))
        self.tableWidget.move(10, 75)
        self.tableWidget.resize(625, 200)


        self.show()
