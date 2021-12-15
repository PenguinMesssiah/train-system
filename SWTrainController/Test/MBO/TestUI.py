from PyQt5 import QtCore, QtGui, QtWidgets

# Handle high resolution displays:
if hasattr(QtCore.Qt, 'AA_EnableHighDpiScaling'):
    QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)
if hasattr(QtCore.Qt, 'AA_UseHighDpiPixmaps'):
    QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)

class MBODisplay(object):
    def setupUI(self, MBOWindow):
        MBOWindow.setObjectName("MBOTestInterface")
        MBOWindow.resize(500, 750)
        MBOWindow.setStyleSheet("background-color: rgb(0, 102, 204);")
        
        self.centralwidget = QtWidgets.QWidget(MBOWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        self.testLabel = QtWidgets.QLabel(self.centralwidget)
        self.testLabel.setGeometry(QtCore.QRect(30, 10, 500, 60))
        self.testLabel.setStyleSheet("font: 26pt")
        self.testLabel.setObjectName("testLabel")
        
        self.trainNumberLabel = QtWidgets.QLabel(self.centralwidget)
        self.trainNumberLabel.setGeometry(QtCore.QRect(30, 90, 150, 30))
        self.trainNumberLabel.setStyleSheet("font: 14pt")
        self.trainNumberLabel.setObjectName("trainNumberLabel")
        
        self.trainNumberInput = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.trainNumberInput.setGeometry(QtCore.QRect(225, 90, 75, 30))
        self.trainNumberInput.setTabletTracking(False)
        self.trainNumberInput.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.trainNumberInput.setMaximum(1)
        self.trainNumberInput.setMinimum(1)
        self.trainNumberInput.setAlignment(QtCore.Qt.AlignCenter)
        self.trainNumberInput.setObjectName("trainNumberInput")
        
        self.authorityLabel = QtWidgets.QLabel(self.centralwidget)
        self.authorityLabel.setGeometry(QtCore.QRect(30, 130, 100, 30))
        self.authorityLabel.setStyleSheet("font: 14pt")
        self.authorityLabel.setObjectName("authorityLabel")
        
        self.authorityInput = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.authorityInput.setGeometry(QtCore.QRect(225, 130, 75, 30))
        self.authorityInput.setTabletTracking(False)
        self.authorityInput.setMaximum(10000)
        self.authorityInput.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.authorityInput.setAlignment(QtCore.Qt.AlignCenter)
        self.authorityInput.setObjectName("authorityInput")

        self.suggestedSpeedLabel = QtWidgets.QLabel(self.centralwidget)
        self.suggestedSpeedLabel.setGeometry(QtCore.QRect(30, 170, 175, 30))
        self.suggestedSpeedLabel.setStyleSheet("font: 14pt")
        self.suggestedSpeedLabel.setObjectName("suggestedSpeedLabel")
        
        self.suggestedSpeedInput = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.suggestedSpeedInput.setGeometry(QtCore.QRect(225, 170, 75, 30))
        self.suggestedSpeedInput.setTabletTracking(False)
        self.suggestedSpeedInput.setMaximum(10000)
        self.suggestedSpeedInput.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.suggestedSpeedInput.setAlignment(QtCore.Qt.AlignCenter)
        self.suggestedSpeedInput.setObjectName("suggestedSpeedInput")

        self.enterButton = QtWidgets.QPushButton(self.centralwidget)
        self.enterButton.setGeometry(QtCore.QRect(120, 210, 100, 31))
        self.enterButton.setStyleSheet("background-color:rgb(224,232,245)")
        self.enterButton.setObjectName("enterButton")

        MBOWindow.setCentralWidget(self.centralwidget)
        self.retranslateUI(MBOWindow)

    def retranslateUI(self, MBOWindow):
        _translate = QtCore.QCoreApplication.translate
        MBOWindow.setWindowTitle(_translate("MBOWindow", "MBOWindow"))
        self.testLabel.setText(_translate("MBOWindow", "MBO Test Interface"))
        self.trainNumberLabel.setText(_translate("MBOWindow", "Train Number:"))
        self.authorityLabel.setText(_translate("MBOWindow", "Authority:"))
        self.suggestedSpeedLabel.setText(_translate("MBOWindow", "Suggested Speed:"))
        self.enterButton.setText(_translate("MBOWindow", "Enter"))
