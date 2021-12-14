from PyQt5 import QtCore, QtGui, QtWidgets

# Handle high resolution displays:
if hasattr(QtCore.Qt, 'AA_EnableHighDpiScaling'):
    QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)
if hasattr(QtCore.Qt, 'AA_UseHighDpiPixmaps'):
    QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)

class DriverDisplay(object):
    def setupUI(self, DisplayWindow, number):
        DisplayWindow.setObjectName("DisplayWindow")
        DisplayWindow.resize(1000, 750)
        DisplayWindow.setAutoFillBackground(False)
        DisplayWindow.setStyleSheet("background-color: rgb(0, 102, 204);")
        
        self.centralwidget = QtWidgets.QWidget(DisplayWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        self.displayLabel = QtWidgets.QLabel(self.centralwidget)
        self.displayLabel.setGeometry(QtCore.QRect(300, 25, 500, 50))
        self.displayLabel.setStyleSheet("font: 25pt")
        self.displayLabel.setObjectName("displayLabel")
        
        self.actualSpeedLabel = QtWidgets.QLabel(self.centralwidget)
        self.actualSpeedLabel.setGeometry(QtCore.QRect(75, 120, 115, 25))
        self.actualSpeedLabel.setStyleSheet("font: 14pt")
        self.actualSpeedLabel.setObjectName("actualSpeedLabel")

        self.actualSpeedInput = QtWidgets.QLineEdit(self.centralwidget)
        self.actualSpeedInput.setGeometry(QtCore.QRect(200, 120, 115, 25))
        self.actualSpeedInput.setStyleSheet("background-color:rgb(255,255,255)")
        self.actualSpeedInput.setText("")
        self.actualSpeedInput.setAlignment(QtCore.Qt.AlignCenter)
        self.actualSpeedInput.setObjectName("actualSpeedInput")
        self.actualSpeedInput.setReadOnly(True)
        self.actualSpeedInput.setMaxLength(5)

        self.setSpeedLabel = QtWidgets.QLabel(self.centralwidget)
        self.setSpeedLabel.setGeometry(QtCore.QRect(75, 80, 100, 25))
        self.setSpeedLabel.setStyleSheet("font: 14pt")
        self.setSpeedLabel.setObjectName("setSpeedLabel")

        self.setSpeedInput = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.setSpeedInput.setGeometry(QtCore.QRect(200, 80, 115, 25))
        self.setSpeedInput.setTabletTracking(False)
        self.setSpeedInput.setStyleSheet("background-color: rgb(255,255,255);")
        self.setSpeedInput.setAlignment(QtCore.Qt.AlignCenter)
        self.setSpeedInput.setObjectName("setSpeedInput")
        
        self.cabinlightLabel = QtWidgets.QLabel(self.centralwidget)
        self.cabinlightLabel.setGeometry(QtCore.QRect(380, 200, 125, 25))
        self.cabinlightLabel.setStyleSheet("font: 14pt")
        self.cabinlightLabel.setObjectName("cabinlightLabel")

        self.cabinlightOnButton = QtWidgets.QPushButton(self.centralwidget)
        self.cabinlightOnButton.setGeometry(QtCore.QRect(550, 200, 50, 25))
        self.cabinlightOnButton.setStyleSheet("background-color:rgb(255,255,255)")
        self.cabinlightOnButton.setObjectName("cabinlightOnButton")

        self.cabinlightOffButton = QtWidgets.QPushButton(self.centralwidget)
        self.cabinlightOffButton.setGeometry(QtCore.QRect(610, 200, 50, 25))
        self.cabinlightOffButton.setStyleSheet("background-color:rgb(255,255,255)")
        self.cabinlightOffButton.setObjectName("cabinlightOffButton")
        
        self.engineFaultLabel = QtWidgets.QLabel(self.centralwidget)
        self.engineFaultLabel.setGeometry(QtCore.QRect(75, 280, 125, 25))
        self.engineFaultLabel.setStyleSheet("font: 14pt")
        self.engineFaultLabel.setObjectName("engineFaultLabel")
        
        self.engineFaultOutput = QtWidgets.QLineEdit(self.centralwidget)
        self.engineFaultOutput.setGeometry(QtCore.QRect(200, 280, 110, 25))
        self.engineFaultOutput.setStyleSheet("background-color:rgb(255,255,255)")
        self.engineFaultOutput.setText("")
        self.engineFaultOutput.setAlignment(QtCore.Qt.AlignCenter)
        self.engineFaultOutput.setReadOnly(True)
        self.engineFaultOutput.setObjectName("engineFaultOutput")

        self.brakeFaultLabel = QtWidgets.QLabel(self.centralwidget)
        self.brakeFaultLabel.setGeometry(QtCore.QRect(75, 320, 125, 25))
        self.brakeFaultLabel.setStyleSheet("font: 14pt")
        self.brakeFaultLabel.setObjectName("brakeFaultLabel")
        
        self.brakeFaultOutput = QtWidgets.QLineEdit(self.centralwidget)
        self.brakeFaultOutput.setGeometry(QtCore.QRect(200, 320, 110, 25))
        self.brakeFaultOutput.setStyleSheet("background-color:rgb(255,255,255)")
        self.brakeFaultOutput.setText("")
        self.brakeFaultOutput.setAlignment(QtCore.Qt.AlignCenter)
        self.brakeFaultOutput.setReadOnly(True)
        self.brakeFaultOutput.setObjectName("brakeFaultOutput")

        self.signalFaultLabel = QtWidgets.QLabel(self.centralwidget)
        self.signalFaultLabel.setGeometry(QtCore.QRect(75, 360, 125, 25))
        self.signalFaultLabel.setStyleSheet("font: 14pt")
        self.signalFaultLabel.setObjectName("engineFaultLabel")
        
        self.signalFaultOutput = QtWidgets.QLineEdit(self.centralwidget)
        self.signalFaultOutput.setGeometry(QtCore.QRect(200, 360, 110, 25))
        self.signalFaultOutput.setStyleSheet("background-color:rgb(255,255,255)")
        self.signalFaultOutput.setText("")
        self.signalFaultOutput.setAlignment(QtCore.Qt.AlignCenter)
        self.signalFaultOutput.setReadOnly(True)
        self.signalFaultOutput.setObjectName("signalFaultOutput")

        self.rightDoorStatusLabel = QtWidgets.QLabel(self.centralwidget)
        self.rightDoorStatusLabel.setGeometry(QtCore.QRect(380, 80, 160, 25))
        self.rightDoorStatusLabel.setStyleSheet("font: 14pt")
        self.rightDoorStatusLabel.setObjectName("rightDoorStatusLabel")

        self.rightDoorOpenButton = QtWidgets.QPushButton(self.centralwidget)
        self.rightDoorOpenButton.setGeometry(QtCore.QRect(550, 80, 50, 25))
        self.rightDoorOpenButton.setStyleSheet("background-color:rgb(255,255,255)")
        self.rightDoorOpenButton.setObjectName("rightDoorOpenButton")
        
        self.rightDoorCloseButton = QtWidgets.QPushButton(self.centralwidget)
        self.rightDoorCloseButton.setGeometry(QtCore.QRect(610, 80, 50, 25))
        self.rightDoorCloseButton.setStyleSheet("background-color:rgb(255,255,255)")
        self.rightDoorCloseButton.setObjectName("rightDoorCloseButton")

        self.leftDoorStatusLabel = QtWidgets.QLabel(self.centralwidget)
        self.leftDoorStatusLabel.setGeometry(QtCore.QRect(380, 120, 150, 25))
        self.leftDoorStatusLabel.setStyleSheet("font: 14pt")
        self.leftDoorStatusLabel.setObjectName("leftDoorStatusLabel")

        self.leftDoorOpenButton = QtWidgets.QPushButton(self.centralwidget)
        self.leftDoorOpenButton.setGeometry(QtCore.QRect(550, 120, 50, 25))
        self.leftDoorOpenButton.setStyleSheet("background-color:rgb(255,255,255)")
        self.leftDoorOpenButton.setObjectName("leftDoorOpenButton")
        
        self.leftDoorCloseButton = QtWidgets.QPushButton(self.centralwidget)
        self.leftDoorCloseButton.setGeometry(QtCore.QRect(610, 120, 50, 25))
        self.leftDoorCloseButton.setStyleSheet("background-color:rgb(255,255,255)")
        self.leftDoorCloseButton.setObjectName("leftDoorCloseButton")

        self.temperatureLabel = QtWidgets.QLabel(self.centralwidget)
        self.temperatureLabel.setGeometry(QtCore.QRect(380, 160, 150, 25))
        self.temperatureLabel.setStyleSheet("font: 14pt")
        self.temperatureLabel.setObjectName("temperatureLabel")
        
        self.temperatureInput = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.temperatureInput.setGeometry(QtCore.QRect(550, 160, 110, 25))
        self.temperatureInput.setTabletTracking(False)
        self.temperatureInput.setStyleSheet("background-color: rgb(255,255,255);")
        self.temperatureInput.setAlignment(QtCore.Qt.AlignCenter)
        self.temperatureInput.setObjectName("temperatureInput")

        self.powerLabel = QtWidgets.QLabel(self.centralwidget)
        self.powerLabel.setGeometry(QtCore.QRect(75, 240, 75, 25))
        self.powerLabel.setStyleSheet("font: 14pt")
        self.powerLabel.setObjectName("powerLabel")

        self.powerOutput = QtWidgets.QLineEdit(self.centralwidget)
        self.powerOutput.setGeometry(QtCore.QRect(200, 240, 75, 25))
        self.powerOutput.setStyleSheet("background-color:rgb(255,255,255)")
        self.powerOutput.setText("")
        self.powerOutput.setAlignment(QtCore.Qt.AlignCenter)
        self.powerOutput.setObjectName("powerOutput")
        self.powerOutput.setReadOnly(True)

        self.beaconLabel = QtWidgets.QLabel(self.centralwidget)
        self.beaconLabel.setGeometry(QtCore.QRect(380, 280, 125, 25))
        self.beaconLabel.setStyleSheet("font: 14pt")
        self.beaconLabel.setObjectName("beaconLabel")

        self.beaconOutput = QtWidgets.QLineEdit(self.centralwidget)
        self.beaconOutput.setGeometry(QtCore.QRect(550,  280, 115, 25))
        self.beaconOutput.setStyleSheet("background-color:rgb(255,255,255)")
        self.beaconOutput.setText("")
        self.beaconOutput.setReadOnly(True)
        self.beaconOutput.setAlignment(QtCore.Qt.AlignCenter)
        self.beaconOutput.setObjectName("beaconOutput")

        self.enginestatusLabel = QtWidgets.QLabel(self.centralwidget)
        self.enginestatusLabel.setGeometry(QtCore.QRect(380, 320, 150, 25))
        self.enginestatusLabel.setStyleSheet("font: 14pt")
        self.enginestatusLabel.setObjectName("enginestatusLabel")
        
        self.engineOnButton = QtWidgets.QPushButton(self.centralwidget)
        self.engineOnButton.setGeometry(QtCore.QRect(550, 320, 50, 25))
        self.engineOnButton.setStyleSheet("background-color:rgb(255,255,255)")
        self.engineOnButton.setObjectName("engineOnButton")
        
        self.engineOffButton = QtWidgets.QPushButton(self.centralwidget)
        self.engineOffButton.setGeometry(QtCore.QRect(610, 320, 50, 25))
        self.engineOffButton.setStyleSheet("background-color:rgb(255,255,255)")
        self.engineOffButton.setObjectName("engineOffButton")
        
        self.kpLabel = QtWidgets.QLabel(self.centralwidget)
        self.kpLabel.setGeometry(QtCore.QRect(75, 160, 50, 25))
        self.kpLabel.setStyleSheet("font: 14pt")
        self.kpLabel.setObjectName("kpLabel")
        
        self.kpInput = QtWidgets.QLineEdit(self.centralwidget)
        self.kpInput.setGeometry(QtCore.QRect(200, 160, 75, 25))
        self.kpInput.setStyleSheet("background-color:rgb(255,255,255)")
        self.kpInput.setReadOnly(True)
        self.kpInput.setAlignment(QtCore.Qt.AlignCenter)
        self.kpInput.setObjectName("kpInput")
        
        self.kiLabel = QtWidgets.QLabel(self.centralwidget)
        self.kiLabel.setGeometry(QtCore.QRect(75, 200, 50, 25))
        self.kiLabel.setStyleSheet("font: 14pt")
        self.kiLabel.setObjectName("kiLabel")
        
        self.kiInput = QtWidgets.QLineEdit(self.centralwidget)
        self.kiInput.setGeometry(QtCore.QRect(200, 200, 75, 25))
        self.kiInput.setStyleSheet("background-color: rgb(255,255,255);")
        self.kiInput.setReadOnly(True)
        self.kiInput.setAlignment(QtCore.Qt.AlignCenter)
        self.kiInput.setObjectName("kiInput")
        
        self.servicebrakeButton = QtWidgets.QPushButton(self.centralwidget)
        self.servicebrakeButton.setGeometry(QtCore.QRect(150, 415, 125, 40))
        self.servicebrakeButton.setStyleSheet("background-color:rgb(255,255,255)")
        self.servicebrakeButton.setObjectName("servicebrakeButton")
        
        self.emergencybrakeButton = QtWidgets.QPushButton(self.centralwidget)
        self.emergencybrakeButton.setGeometry(QtCore.QRect(300, 415, 125, 40))
        self.emergencybrakeButton.setStyleSheet("background-color: rgb(255, 23, 2);")
        self.emergencybrakeButton.setObjectName("emergencybrakeButton")
        
        self.announcementButton = QtWidgets.QPushButton(self.centralwidget)
        self.announcementButton.setGeometry(QtCore.QRect(450, 415, 125, 40))
        self.announcementButton.setStyleSheet("background-color:rgb(255,255,255)")
        self.announcementButton.setObjectName("announcementButton")

        self.modeLabel = QtWidgets.QLabel(self.centralwidget)
        self.modeLabel.setGeometry(QtCore.QRect(380, 360, 75, 25))
        self.modeLabel.setStyleSheet("font: 14pt")
        self.modeLabel.setObjectName("modeLabel")

        self.automaticButton = QtWidgets.QPushButton(self.centralwidget)
        self.automaticButton.setGeometry(QtCore.QRect(550, 360, 60, 25))
        self.automaticButton.setStyleSheet("background-color:rgb(255,255,255)")
        self.automaticButton.setObjectName("automaticButton")
        
        self.manualButton = QtWidgets.QPushButton(self.centralwidget)
        self.manualButton.setGeometry(QtCore.QRect(620, 360, 60, 25))
        self.manualButton.setStyleSheet("background-color:rgb(255,255,255)")
        self.manualButton.setObjectName("manualButton")

        self.headlightsLabel = QtWidgets.QLabel(self.centralwidget)
        self.headlightsLabel.setGeometry(QtCore.QRect(380, 240, 125, 25))
        self.headlightsLabel.setStyleSheet("font: 14pt")
        self.headlightsLabel.setObjectName("headlightsLabel")
        
        self.headlightOnButton = QtWidgets.QPushButton(self.centralwidget)
        self.headlightOnButton.setGeometry(QtCore.QRect(550, 240, 50, 25))
        self.headlightOnButton.setStyleSheet("background-color:rgb(255,255,255)")
        self.headlightOnButton.setObjectName("headlightOnButton")
        
        self.headlightOffButton = QtWidgets.QPushButton(self.centralwidget)
        self.headlightOffButton.setGeometry(QtCore.QRect(610, 240, 50, 25))
        self.headlightOffButton.setStyleSheet("background-color:rgb(255,255,255)")
        self.headlightOffButton.setObjectName("headlightOffButton")
        
        DisplayWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(DisplayWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 775, 26))
        self.menubar.setObjectName("menubar")       

        self.retranslateUi(DisplayWindow, number)
        QtCore.QMetaObject.connectSlotsByName(DisplayWindow)

    def retranslateUi(self, DisplayWindow, number):
        _translate = QtCore.QCoreApplication.translate
        DisplayWindow.setWindowTitle(_translate("DisplayWindow", "Train " + str(number) + " Window"))
        self.displayLabel.setText(_translate("DisplayWindow", "Train - " + str(number)))
        self.setSpeedLabel.setText(_translate("DisplayWindow", "Set Speed:"))
        self.actualSpeedLabel.setText(_translate("DisplayWindow", "Actual Speed:"))
        self.beaconLabel.setText(_translate("DisplayWindow", "Next Station:"))
        self.temperatureLabel.setText(_translate("DisplayWindow", "Temperature:"))
        self.headlightsLabel.setText(_translate("DisplayWindow", "Headlights: "))
        self.cabinlightLabel.setText(_translate("DisplayWindow", "Cabin Lights:"))
        self.leftDoorStatusLabel.setText(_translate("DisplayWindow", "Left Door Status:"))
        self.rightDoorStatusLabel.setText(_translate("DisplayWindow", "Right Door Status:"))
        self.engineFaultLabel.setText(_translate("DisplayWindow", "Engine Fault:"))
        self.brakeFaultLabel.setText(_translate("DisplayWindow", "Brake Fault:"))
        self.signalFaultLabel.setText(_translate("DisplayWindow", "Signal Fault:"))
        self.modeLabel.setText(_translate("DisplayWindow", "Mode:"))
        self.manualButton.setText(_translate("DisplayWindow", "Manual"))
        self.automaticButton.setText(_translate("DisplayWindow", "Automatic"))
        self.headlightOnButton.setText(_translate("DisplayWindow", "ON"))
        self.headlightOffButton.setText(_translate("DisplayWindow", "OFF"))
        self.cabinlightOnButton.setText(_translate("DisplayWindow", "ON"))
        self.cabinlightOffButton.setText(_translate("DisplayWindow", "OFF"))
        self.leftDoorOpenButton.setText(_translate("DisplayWindow", "OPEN"))
        self.leftDoorCloseButton.setText(_translate("DisplayWindow", "CLOSE"))
        self.rightDoorOpenButton.setText(_translate("DisplayWindow", "OPEN"))
        self.rightDoorCloseButton.setText(_translate("DisplayWindow", "CLOSE"))
        self.kpLabel.setText(_translate("DisplayWindow", "Kp:"))
        self.kiLabel.setText(_translate("DisplayWindow", "Ki:"))
        self.powerLabel.setText(_translate("DisplayWindow", "Power:"))
        self.servicebrakeButton.setText(_translate("DisplayWindow", "SERVICE\nBRAKE"))
        self.emergencybrakeButton.setText(_translate("DisplayWindow", "EMERGENCY\nBRAKE"))
        self.announcementButton.setText(_translate("DisplayWindow", "MAKE\nANNOUNCEMENT"))
        self.enginestatusLabel.setText(_translate("DisplayWindow", "Engine Status:"))
        self.engineOnButton.setText(_translate("DisplayWindow", "ON"))
        self.engineOffButton.setText(_translate("DisplayWindow", "OFF"))
