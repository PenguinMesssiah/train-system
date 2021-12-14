from PyQt5 import QtCore, QtGui, QtWidgets

# Handle high resolution displays:
if hasattr(QtCore.Qt, 'AA_EnableHighDpiScaling'):
    QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)
if hasattr(QtCore.Qt, 'AA_UseHighDpiPixmaps'):
    QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)

class EngineerDisplay(object):
    def setupUI(self, EngineerWindow):
        EngineerWindow.setObjectName("EngineerWindow")
        EngineerWindow.resize(400, 250)
        EngineerWindow.setStyleSheet("background-color: rgb(0, 102, 204);")
        
        self.centralwidget = QtWidgets.QWidget(EngineerWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        self.controllerLabel = QtWidgets.QLabel(self.centralwidget)
        self.controllerLabel.setGeometry(QtCore.QRect(30, 10, 400, 61))
        self.controllerLabel.setStyleSheet("font: 26pt")
        self.controllerLabel.setObjectName("controllerLabel")
        
        self.kpLabel = QtWidgets.QLabel(self.centralwidget)
        self.kpLabel.setGeometry(QtCore.QRect(30, 90, 41, 31))
        self.kpLabel.setStyleSheet("font: 14pt")
        self.kpLabel.setObjectName("kpLabel")
        
        self.kpInput = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.kpInput.setGeometry(QtCore.QRect(75, 90, 81, 31))
        self.kpInput.setTabletTracking(False)
        self.kpInput.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.kpInput.setMaximum(10000)
        self.kpInput.setAlignment(QtCore.Qt.AlignCenter)
        self.kpInput.setObjectName("kpInput")
        
        self.kiLabel = QtWidgets.QLabel(self.centralwidget)
        self.kiLabel.setGeometry(QtCore.QRect(175, 90, 31, 31))
        self.kiLabel.setStyleSheet("font: 14pt")
        self.kiLabel.setObjectName("kiLabel")
        
        self.kiInput = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.kiInput.setGeometry(QtCore.QRect(205, 90, 81, 31))
        self.kiInput.setTabletTracking(False)
        self.kiInput.setMaximum(10000)
        self.kiInput.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.kiInput.setAlignment(QtCore.Qt.AlignCenter)
        self.kiInput.setObjectName("kiInput")

        self.enterButton = QtWidgets.QPushButton(self.centralwidget)
        self.enterButton.setGeometry(QtCore.QRect(120, 140, 100, 31))
        self.enterButton.setStyleSheet("background-color:rgb(224,232,245)")
        self.enterButton.setObjectName("enterButton")

        EngineerWindow.setCentralWidget(self.centralwidget)
        self.retranslateUI(EngineerWindow)

    def retranslateUI(self, EngineerWindow):
        _translate = QtCore.QCoreApplication.translate
        EngineerWindow.setWindowTitle(_translate("EngineerWindow", "EngineerWindow"))
        self.controllerLabel.setText(_translate("EngineerWindow", "Engineer Display"))
        self.kpLabel.setText(_translate("EngineerWindow", "Kp:"))
        self.kiLabel.setText(_translate("EngineerWindow", "Ki:"))
        self.enterButton.setText(_translate("EngineerWindow", "Enter"))
