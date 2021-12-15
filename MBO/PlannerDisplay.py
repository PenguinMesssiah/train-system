from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QTableView, QPushButton, QAction, QLineEdit, QMessageBox
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot




class Display(object):
    def setupUI(self, DisplayWindow):
        DisplayWindow.setObjectName("DisplayWindow")
        DisplayWindow.resize(1500, 1000)
        DisplayWindow.setAutoFillBackground(False)
        DisplayWindow.setStyleSheet("background-color: rgb(216, 216, 162);")
        
        self.centralwidget = QtWidgets.QWidget(DisplayWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        self.displayLabel = QtWidgets.QLabel(self.centralwidget)
        self.displayLabel.setGeometry(QtCore.QRect(100, 40, 181, 61))
        self.displayLabel.setStyleSheet("font: 18pt \"MS Shell Dlg 2\";\nbackground-color:rgb(160, 100, 162)")
        self.displayLabel.setObjectName("displayLabel")
        self.displayLabel.setAlignment(QtCore.Qt.AlignCenter)

        self.trainLabel = QtWidgets.QLabel(self.centralwidget)
        self.trainLabel.setGeometry(QtCore.QRect(500, 300, 300, 61))
        self.trainLabel.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";\nbackground-color:rgb(216, 216, 162)")
        self.trainLabel.setObjectName("trainLabel")
        self.trainLabel.setAlignment(QtCore.Qt.AlignCenter)

        

        self.inputsLabel = QtWidgets.QLabel(self.centralwidget)
        self.inputsLabel.setGeometry(QtCore.QRect(900, 300, 300, 61))
        self.inputsLabel.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";\nbackground-color:rgb(216, 216, 162)")
        self.inputsLabel.setObjectName("inputsLabel")
        self.inputsLabel.setAlignment(QtCore.Qt.AlignCenter)

        self.driversLabel = QtWidgets.QLabel(self.centralwidget)
        self.driversLabel.setGeometry(QtCore.QRect(1200, 300, 300, 61))
        self.driversLabel.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";\nbackground-color:rgb(216, 216, 162)")
        self.driversLabel.setObjectName("driversLabel")
        self.driversLabel.setAlignment(QtCore.Qt.AlignCenter)
        
        self.trainNameOutput1 = QtWidgets.QLineEdit(self.centralwidget)
        self.trainNameOutput1.setGeometry(QtCore.QRect(500, 420, 80, 31))
        self.trainNameOutput1.setStyleSheet("background-color:rgb(224,232,245)")
        self.trainNameOutput1.setText("Green 1")
        self.trainNameOutput1.setAlignment(QtCore.Qt.AlignCenter)
        self.trainNameOutput1.setObjectName("trainNameOutput1")
        self.trainNameOutput1.setReadOnly(True)

        self.trainNameOutput2 = QtWidgets.QLineEdit(self.centralwidget)
        self.trainNameOutput2.setGeometry(QtCore.QRect(500, 460, 80, 31))
        self.trainNameOutput2.setStyleSheet("background-color:rgb(224,232,245)")
        self.trainNameOutput2.setText("Red 1")
        self.trainNameOutput2.setAlignment(QtCore.Qt.AlignCenter)
        self.trainNameOutput2.setObjectName("trainNameOutput2")
        self.trainNameOutput2.setReadOnly(True)

        self.posOutput1 = QtWidgets.QLineEdit(self.centralwidget)
        self.posOutput1.setGeometry(QtCore.QRect(600, 420, 80, 31))
        self.posOutput1.setStyleSheet("background-color:rgb(224,232,245)")
        #-- self.posOutput1.setText("35 m")
        self.posOutput1.setAlignment(QtCore.Qt.AlignCenter)
        self.posOutput1.setObjectName("posOutput1")
        #-- self.posOutput1.setReadOnly(True)

        self.posOutput2 = QtWidgets.QLineEdit(self.centralwidget)
        self.posOutput2.setGeometry(QtCore.QRect(600, 460, 80, 31))
        self.posOutput2.setStyleSheet("background-color:rgb(224,232,245)")
        #-- self.posOutput2.setText("75 m")
        self.posOutput2.setAlignment(QtCore.Qt.AlignCenter)
        self.posOutput2.setObjectName("posOutput2")
        # --self.posOutput2.setReadOnly(True)

        self.blockOutput1 = QtWidgets.QLineEdit(self.centralwidget)
        self.blockOutput1.setGeometry(QtCore.QRect(700, 420, 80, 31))
        self.blockOutput1.setStyleSheet("background-color:rgb(224,232,245)")
        #-- self.blockOutput1.setText("A")
        self.blockOutput1.setAlignment(QtCore.Qt.AlignCenter)
        self.blockOutput1.setObjectName("blockOutput1")
        #-- self.blockOutput1.setReadOnly(True)

        self.blockOutput2 = QtWidgets.QLineEdit(self.centralwidget)
        self.blockOutput2.setGeometry(QtCore.QRect(700, 460, 80, 31))
        self.blockOutput2.setStyleSheet("background-color:rgb(224,232,245)")
        #-- self.blockOutput2.setText("H")
        self.blockOutput2.setAlignment(QtCore.Qt.AlignCenter)
        self.blockOutput2.setObjectName("blockOutput2")
        #-- self.blockOutput2.setReadOnly(True)

        self.trainLabel2 = QtWidgets.QLabel(self.centralwidget)
        self.trainLabel2.setGeometry(QtCore.QRect(500, 380, 100, 31))
        self.trainLabel2.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.trainLabel2.setObjectName("trainLabel2")

        self.blockLabel2 = QtWidgets.QLabel(self.centralwidget)
        self.blockLabel2.setGeometry(QtCore.QRect(600, 380, 100, 31))
        self.blockLabel2.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.blockLabel2.setObjectName("blockLabel2")

        self.posLabel2 = QtWidgets.QLabel(self.centralwidget)
        self.posLabel2.setGeometry(QtCore.QRect(700, 380, 200, 31))
        self.posLabel2.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.posLabel2.setObjectName("posLabel2")

        self.timeLabel = QtWidgets.QLabel(self.centralwidget)
        self.timeLabel.setGeometry(QtCore.QRect(900, 375, 140, 31))
        self.timeLabel.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.timeLabel.setObjectName("timeLabel")
        
        self.timeSelector = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.timeSelector.setGeometry(QtCore.QRect(1050, 375, 111, 31))
        self.timeSelector.setStyleSheet("background-color: rgb(224,232,245);")    
        self.timeSelector.setMaximum(24)
        self.timeSelector.setMinimum(1)
        self.timeSelector.setTabletTracking(False)
        self.timeSelector.setObjectName("timeSelector")

        self.timeLabel = QtWidgets.QLabel(self.centralwidget)
        self.timeLabel.setGeometry(QtCore.QRect(900, 375, 140, 31))
        self.timeLabel.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.timeLabel.setObjectName("timeLabel")
        
        self.timeSelector = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.timeSelector.setGeometry(QtCore.QRect(1050, 375, 111, 31))
        self.timeSelector.setStyleSheet("background-color: rgb(224,232,245);")    
        self.timeSelector.setMaximum(24)
        self.timeSelector.setMinimum(1)
        self.timeSelector.setTabletTracking(False)
        self.timeSelector.setObjectName("timeSelector")

##        self.thimeLabel = QtWidgets.QLabel(self.centralwidget)
##        self.thimeLabel.setGeometry(QtCore.QRect(900, 475, 140, 31))
##        self.thimeLabel.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
##        self.thimeLabel.setObjectName("thimeLabel")
##        
##        self.thimeSelector = QtWidgets.QDoubleSpinBox(self.centralwidget)
##        self.thimeSelector.setGeometry(QtCore.QRect(1050, 475, 111, 31))
##        self.thimeSelector.setStyleSheet("background-color: rgb(224,232,245);")    
##        self.thimeSelector.setMaximum(24)
##        self.thimeSelector.setMinimum(1)
##        self.thimeSelector.setTabletTracking(False)
##        self.thimeSelector.setObjectName("thimeSelector")

        self.throLabel = QtWidgets.QLabel(self.centralwidget)
        self.throLabel.setGeometry(QtCore.QRect(900, 475, 200, 41))
        self.throLabel.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.throLabel.setObjectName("throLabel")
        
        self.throSelector = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.throSelector.setGeometry(QtCore.QRect(1050, 475, 111, 31))
        self.throSelector.setStyleSheet("background-color: rgb(224,232,245);")    
        self.throSelector.setMaximum(10000)
        self.throSelector.setMinimum(10)
        self.throSelector.setSingleStep(10)
        self.throSelector.setTabletTracking(False)
        self.throSelector.setObjectName("throSelector")

        #-- To add

        #-- Schedule Display

        #-- selection for new driver to be added

        #-- input for name, selection of days available

        #-- button to deactivate a driver

        self.addDriverButton = QtWidgets.QPushButton(self.centralwidget)
        self.addDriverButton.setGeometry(QtCore.QRect(1200, 375, 100, 50))
        self.addDriverButton.setStyleSheet("background-color:rgb(224,232,245)")
        self.addDriverButton.setObjectName("addDriverButton")

        #-- button to make schedule
        self.SchedButton = QtWidgets.QPushButton(self.centralwidget)
        self.SchedButton.setGeometry(QtCore.QRect(200, 375, 100, 50))
        self.SchedButton.setStyleSheet("background-color:rgb(224,232,245)")
        self.SchedButton.setObjectName("SchedButton")
         # Create textbox
        self.textbox1 = QtWidgets.QLineEdit(self.centralwidget)
        self.textbox1.move(1350, 500)
        self.textbox1.resize(150,40)

        self.submitNameButton = QtWidgets.QPushButton(self.centralwidget)
        self.submitNameButton.setGeometry(QtCore.QRect(1350, 550, 100, 50))
        self.submitNameButton.setStyleSheet("background-color:rgb(224,232,245)")
        self.submitNameButton.setObjectName("submitNameButton")

        self.nameLabel = QtWidgets.QLabel(self.centralwidget)
        self.nameLabel.setGeometry(QtCore.QRect(1200, 500, 100, 41))
        self.nameLabel.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.nameLabel.setObjectName("nameLabel")

        self.datesLabel = QtWidgets.QLabel(self.centralwidget)
        self.datesLabel.setGeometry(QtCore.QRect(1200, 600, 200, 40))
        self.datesLabel.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.datesLabel.setObjectName("datesLabel")

##        self.sundayLabel = QtWidgets.QLabel(self.centralwidget)
##        self.sundayLabel.setGeometry(QtCore.QRect(1400, 640, 100, 40))
##        self.sundayLabel.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")  
##        self.sundayLabel.setObjectName("sundayLabel")

        self.sunCheck = QtWidgets.QCheckBox("Sunday", self.centralwidget)
        self.sunCheck.move(1200,640)
        self.sunCheck.resize(360,40)
        self.sunCheck.setChecked(True)
        self.sunCheck.setObjectName("sunCheck")

##        self.mondayLabel = QtWidgets.QLabel(self.centralwidget)
##        self.mondayLabel.setGeometry(QtCore.QRect(1400, 680, 100, 40))
##        self.mondayLabel.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
##        self.mondayLabel.setObjectName("mondayLabel")

        self.monCheck = QtWidgets.QCheckBox("Monday", self.centralwidget)
        self.monCheck.move(1200,680)
        self.monCheck.resize(360,40)
        self.monCheck.setChecked(True)
        self.monCheck.setObjectName("monCheck")


##        self.tuesdayLabel = QtWidgets.QLabel(self.centralwidget)
##        self.tuesdayLabel.setGeometry(QtCore.QRect(1400, 720, 100, 40))
##        self.tuesdayLabel.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
##        self.tuesdayLabel.setObjectName("tuesdayLabel")
##
        
        self.tuesCheck = QtWidgets.QCheckBox("Tuesday", self.centralwidget)
        self.tuesCheck.move(1200,720)
        self.tuesCheck.resize(360,40)
        self.tuesCheck.setChecked(True)
        self.tuesCheck.setObjectName("tuesCheck")

##
##        self.wednesdayLabel = QtWidgets.QLabel(self.centralwidget)
##        self.wednesdayLabel.setGeometry(QtCore.QRect(1400, 760, 100, 40))
##        self.wednesdayLabel.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
##        self.wednesdayLabel.setObjectName("wednesdayLabel")


        self.wedCheck = QtWidgets.QCheckBox("Wednesday", self.centralwidget)
        self.wedCheck.move(1200,760)
        self.wedCheck.resize(360,40)
        self.wedCheck.setChecked(True)
        self.wedCheck.setObjectName("wedCheck")
        
##        self.thursLabel = QtWidgets.QLabel(self.centralwidget)
##        self.thursLabel.setGeometry(QtCore.QRect(1400, 800, 100, 40))
##        self.thursLabel.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
##        self.thursLabel.setObjectName("thursLabel")

        self.thursCheck = QtWidgets.QCheckBox("Thursday", self.centralwidget)
        self.thursCheck.move(1200,800)
        self.thursCheck.resize(360,40)
        self.thursCheck.setChecked(True)
        self.thursCheck.setObjectName("thursCheck")


##        self.fridayLabel = QtWidgets.QLabel(self.centralwidget)
##        self.fridayLabel.setGeometry(QtCore.QRect(1400, 840, 100, 40))
##        self.fridayLabel.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
##        self.fridayLabel.setObjectName("fridayLabel")

        self.friCheck = QtWidgets.QCheckBox("Friday", self.centralwidget)
        self.friCheck.move(1200,840)
        self.friCheck.resize(360,40)
        self.friCheck.setChecked(True)
        self.friCheck.setObjectName("friCheck")


##        self.satLabel = QtWidgets.QLabel(self.centralwidget)
##        self.satLabel.setGeometry(QtCore.QRect(1400, 880, 100, 40))
##        self.satLabel.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
##        self.satLabel.setObjectName("satLabel")

        self.satCheck = QtWidgets.QCheckBox("Saturday", self.centralwidget)
        self.satCheck.move(1200,880)
        self.satCheck.resize(360,40)
        self.satCheck.setChecked(True)
        self.satCheck.setObjectName("satCheck")
        
        # Toggle Active Status

        self.setActiveButton = QPushButton(self.centralwidget)
        self.setActiveButton.setGeometry(QtCore.QRect(1500, 930, 100, 50))
        self.setActiveButton.setStyleSheet("background-color:rgb(224,232,245)")
        self.setActiveButton.setObjectName("setActiveButton")
        
        # Create a button in the window
        self.enterDriverDataButton = QPushButton(self.centralwidget)
        self.enterDriverDataButton.setGeometry(QtCore.QRect(1300, 930, 100, 50))
        self.enterDriverDataButton.setStyleSheet("background-color:rgb(224,232,245)")
        self.enterDriverDataButton.setObjectName("enterDriverDataButton")

         # Create a button in the window
        self.enterDatesButton = QPushButton(self.centralwidget)
        self.enterDatesButton.setGeometry(QtCore.QRect(1200, 930, 100, 50))
        self.enterDatesButton.setStyleSheet("background-color:rgb(224,232,245)")
        self.enterDatesButton.setObjectName("enterDatesButton")


        self.tableView = QtWidgets.QTableView(self.centralwidget)
        self.tableView.setObjectName("tableView")
        ##        
        ##        col_headers = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
        self.tableView.setGeometry(QtCore.QRect(100, 360, 100, 50))
       ## self.tableView.setHorizontalHeaderLabels(col_headers)
##        table = MyTable(QTableWidget)
##        self.tableView.table.open_sheet()

        



        self.cb = QtWidgets.QComboBox(self.centralwidget)
        self.cb.move(1350, 700)
        self.cb.resize(200,50)
        self.cb.setObjectName("cb")

      
                
        DisplayWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(DisplayWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 768, 26))
        self.menubar.setObjectName("menubar")       

        self.retranslateUi(DisplayWindow)
        QtCore.QMetaObject.connectSlotsByName(DisplayWindow)

    def retranslateUi(self, DisplayWindow):
        _translate = QtCore.QCoreApplication.translate
        DisplayWindow.setWindowTitle(_translate("DisplayWindow", "MainWindow"))
        self.displayLabel.setText(_translate("DisplayWindow", "MBO UI"))
       
        self.inputsLabel.setText(_translate("DisplayWindow", "Inputs"))
        self.driversLabel.setText(_translate("DisplayWindow", "Drivers"))
        
       
        self.trainLabel.setText(_translate("DisplayWindow", "Train, Position and Block"))
         
        self.trainLabel2.setText(_translate("DisplayWindow", "Train"))

        self.blockLabel2.setText(_translate("DisplayWindow", "Position"))

        self.posLabel2.setText(_translate("DisplayWindow", "Block"))
        
        self.timeLabel.setText(_translate("DisplayWindow", "Input Start Time"))

        self.throLabel.setText(_translate("DisplayWindow", "Input Thoughput\ntickets/hr"))

       ## self.thimeLabel.setText(_translate("DisplayWindow", "Select Hour"))
        self.nameLabel.setText(_translate("DisplayWindow", "Input Name:"))
        self.addDriverButton.setText(_translate("DisplayWindow", "Add Driver"))
        self.datesLabel.setText(_translate("DisplayWindow", "Select Available Dates"))
        self.submitNameButton.setText(_translate("DisplayWindow", "Submit Name"))
        self.setActiveButton.setText(_translate("DisplayWindow", "Activate Driver"))
        self.enterDriverDataButton.setText(_translate("DisplayWindow", "Enter Driver"))
        self.enterDatesButton.setText(_translate("DisplayWindow", "Submit Dates"))
        self.SchedButton.setText(_translate("DisplayWindow", "Make Schedule"))
##        self.sundayLabel.setText(_translate("DisplayWindow", "Sunday:"))
##        self.mondayLabel.setText(_translate("DisplayWindow", "Monday:"))
##        self.tuesdayLabel.setText(_translate("DisplayWindow", "Tuesday:"))
##        self.wednesdayLabel.setText(_translate("DisplayWindow", "Wednesday:"))
##        self.thursLabel.setText(_translate("DisplayWindow", "Thursday:"))
##        self.fridayLabel.setText(_translate("DisplayWindow", "Friday:"))
##        self.satLabel.setText(_translate("DisplayWindow", "Saturday:"))
        


