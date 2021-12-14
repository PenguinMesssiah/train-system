from PyQt5 import QtCore, QtGui, QtWidgets

# Handle high resolution displays:
if hasattr(QtCore.Qt, 'AA_EnableHighDpiScaling'):
    QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)
if hasattr(QtCore.Qt, 'AA_UseHighDpiPixmaps'):
    QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)

class TrainModelDisplay(object):
    def setupUI(self, TrainModelWindow):
        TrainModelWindow.setObjectName("TrainModelTestInterface")
        TrainModelWindow.resize(500, 1000)
        TrainModelWindow.setStyleSheet("background-color: rgb(0, 102, 204);")
        
        self.centralwidget = QtWidgets.QWidget(TrainModelWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        self.testLabel = QtWidgets.QLabel(self.centralwidget)
        self.testLabel.setGeometry(QtCore.QRect(30, 50, 500, 60))
        self.testLabel.setStyleSheet("font: 26pt")
        self.testLabel.setObjectName("testLabel")
        
        self.trainNumberLabel = QtWidgets.QLabel(self.centralwidget)
        self.trainNumberLabel.setGeometry(QtCore.QRect(30, 130, 150, 30))
        self.trainNumberLabel.setStyleSheet("font: 14pt")
        self.trainNumberLabel.setObjectName("trainNumberLabel")
        
        self.trainNumberInput = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.trainNumberInput.setGeometry(QtCore.QRect(225, 130, 75, 30))
        self.trainNumberInput.setTabletTracking(False)
        self.trainNumberInput.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.trainNumberInput.setMaximum(1)
        self.trainNumberInput.setMinimum(1)
        self.trainNumberInput.setAlignment(QtCore.Qt.AlignCenter)
        self.trainNumberInput.setObjectName("trainNumberInput")

        self.beaconLabel = QtWidgets.QLabel(self.centralwidget)
        self.beaconLabel.setGeometry(QtCore.QRect(30, 170, 150, 30))
        self.beaconLabel.setStyleSheet("font: 14pt")
        self.beaconLabel.setObjectName("authorityLabel")
        
        self.beaconInput = QtWidgets.QLineEdit(self.centralwidget)
        self.beaconInput.setGeometry(QtCore.QRect(225, 170, 200, 30))
        self.beaconInput.setTabletTracking(False)
        self.beaconInput.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.beaconInput.setAlignment(QtCore.Qt.AlignCenter)
        self.beaconInput.setObjectName("beaconInput")

        self.commandedSpeedLabel = QtWidgets.QLabel(self.centralwidget)
        self.commandedSpeedLabel.setGeometry(QtCore.QRect(30, 210, 175, 30))
        self.commandedSpeedLabel.setStyleSheet("font: 14pt")
        self.commandedSpeedLabel.setObjectName("commandedSpeedLabel")
        
        self.commandedSpeedInput = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.commandedSpeedInput.setGeometry(QtCore.QRect(225, 210, 75, 30))
        self.commandedSpeedInput.setTabletTracking(False)
        self.commandedSpeedInput.setMaximum(10000)
        self.commandedSpeedInput.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.commandedSpeedInput.setAlignment(QtCore.Qt.AlignCenter)
        self.commandedSpeedInput.setObjectName("commandedSpeedInput")

        self.speedLimitLabel = QtWidgets.QLabel(self.centralwidget)
        self.speedLimitLabel.setGeometry(QtCore.QRect(30, 250, 175, 30))
        self.speedLimitLabel.setStyleSheet("font: 14pt")
        self.speedLimitLabel.setObjectName("authorityLabel")
        
        self.speedLimitInput = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.speedLimitInput.setGeometry(QtCore.QRect(225, 250, 75, 30))
        self.speedLimitInput.setTabletTracking(False)
        self.speedLimitInput.setMaximum(10000)
        self.speedLimitInput.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.speedLimitInput.setAlignment(QtCore.Qt.AlignCenter)
        self.speedLimitInput.setObjectName("authorityInput")

        self.actualSpeedLabel = QtWidgets.QLabel(self.centralwidget)
        self.actualSpeedLabel.setGeometry(QtCore.QRect(30, 290, 175, 30))
        self.actualSpeedLabel.setStyleSheet("font: 14pt")
        self.actualSpeedLabel.setObjectName("authorityLabel")
        
        self.actualSpeedInput = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.actualSpeedInput.setGeometry(QtCore.QRect(225, 290, 75, 30))
        self.actualSpeedInput.setTabletTracking(False)
        self.actualSpeedInput.setMaximum(10000)
        self.actualSpeedInput.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.actualSpeedInput.setAlignment(QtCore.Qt.AlignCenter)
        self.actualSpeedInput.setObjectName("actualSpeedInput")

        self.engineFaultLabel = QtWidgets.QLabel(self.centralwidget)
        self.engineFaultLabel.setGeometry(QtCore.QRect(30, 330, 175, 30))
        self.engineFaultLabel.setStyleSheet("font: 14pt")
        self.engineFaultLabel.setObjectName("engineFaultLabel")

        self.engineFaultTrueButton = QtWidgets.QPushButton(self.centralwidget)
        self.engineFaultTrueButton.setGeometry(QtCore.QRect(225, 330, 50, 25))
        self.engineFaultTrueButton.setStyleSheet("background-color:rgb(255,255,255)")
        self.engineFaultTrueButton.setObjectName("engineFaultTrueButton")

        self.engineFaultFalseButton = QtWidgets.QPushButton(self.centralwidget)
        self.engineFaultFalseButton.setGeometry(QtCore.QRect(285, 330, 50, 25))
        self.engineFaultFalseButton.setStyleSheet("background-color:rgb(255,255,255)")
        self.engineFaultFalseButton.setObjectName("engineFaultFalseButton")

        self.brakeFaultLabel = QtWidgets.QLabel(self.centralwidget)
        self.brakeFaultLabel.setGeometry(QtCore.QRect(30, 370, 175, 30))
        self.brakeFaultLabel.setStyleSheet("font: 14pt")
        self.brakeFaultLabel.setObjectName("brakeFaultLabel")

        self.brakeFaultTrueButton = QtWidgets.QPushButton(self.centralwidget)
        self.brakeFaultTrueButton.setGeometry(QtCore.QRect(225, 370, 50, 25))
        self.brakeFaultTrueButton.setStyleSheet("background-color:rgb(255,255,255)")
        self.brakeFaultTrueButton.setObjectName("brakeFaultTrueButton")

        self.brakeFaultFalseButton = QtWidgets.QPushButton(self.centralwidget)
        self.brakeFaultFalseButton.setGeometry(QtCore.QRect(285, 370, 50, 25))
        self.brakeFaultFalseButton.setStyleSheet("background-color:rgb(255,255,255)")
        self.brakeFaultFalseButton.setObjectName("brakeFaultFalseButton")

        self.signalFaultLabel = QtWidgets.QLabel(self.centralwidget)
        self.signalFaultLabel.setGeometry(QtCore.QRect(30, 410, 175, 30))
        self.signalFaultLabel.setStyleSheet("font: 14pt")
        self.signalFaultLabel.setObjectName("signalFaultLabel")

        self.signalFaultTrueButton = QtWidgets.QPushButton(self.centralwidget)
        self.signalFaultTrueButton.setGeometry(QtCore.QRect(225, 410, 50, 25))
        self.signalFaultTrueButton.setStyleSheet("background-color:rgb(255,255,255)")
        self.signalFaultTrueButton.setObjectName("signalFaultTrueButton")

        self.signalFaultFalseButton = QtWidgets.QPushButton(self.centralwidget)
        self.signalFaultFalseButton.setGeometry(QtCore.QRect(285, 410, 50, 25))
        self.signalFaultFalseButton.setStyleSheet("background-color:rgb(255,255,255)")
        self.signalFaultFalseButton.setObjectName("signalFaultFalseButton")

        self.enterButton = QtWidgets.QPushButton(self.centralwidget)
        self.enterButton.setGeometry(QtCore.QRect(120, 450, 100, 31))
        self.enterButton.setStyleSheet("background-color:rgb(224,232,245)")
        self.enterButton.setObjectName("enterButton")

        TrainModelWindow.setCentralWidget(self.centralwidget)
        self.retranslateUI(TrainModelWindow)

    def retranslateUI(self, TrainModelWindow):
        _translate = QtCore.QCoreApplication.translate
        TrainModelWindow.setWindowTitle(_translate("TrainModelWindow", "TrainModelWindow"))
        self.testLabel.setText(_translate("TrainModelWindow", "Train Model Test Interface"))
        self.trainNumberLabel.setText(_translate("TrainModelWindow", "Train Number:"))
        self.beaconLabel.setText(_translate("TrainModelWindow", "Beacon Message:"))
        self.commandedSpeedLabel.setText(_translate("TrainModelWindow", "Commanded Speed:"))
        self.speedLimitLabel.setText(_translate("TrainModelWindow", "Speed Limit:"))
        self.actualSpeedLabel.setText(_translate("TrainModelWindow", "Actual Speed:"))
        self.engineFaultLabel.setText(_translate("TrainModelWindow", "Engine Fault:"))
        self.engineFaultTrueButton.setText(_translate("TrainModelWindow", "Yes"))
        self.engineFaultFalseButton.setText(_translate("TrainModelWindow", "No"))
        self.brakeFaultLabel.setText(_translate("TrainModelWindow", "Brake Fault:"))
        self.brakeFaultTrueButton.setText(_translate("TrainModelWindow", "Yes"))
        self.brakeFaultFalseButton.setText(_translate("TrainModelWindow", "No"))
        self.signalFaultLabel.setText(_translate("TrainModelWindow", "Signal Fault:"))
        self.signalFaultTrueButton.setText(_translate("TrainModelWindow", "Yes"))
        self.signalFaultFalseButton.setText(_translate("TrainModelWindow", "No"))
        self.enterButton.setText(_translate("TrainModelWindow", "Enter"))
