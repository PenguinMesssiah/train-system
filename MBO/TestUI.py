from PyQt5 import QtCore, QtGui, QtWidgets

class TestDisplay(object):
    def setupUI(self, TestDisplayWindow):
        TestDisplayWindow.setObjectName("TestDisplayWindow")
        TestDisplayWindow.resize(2000, 2000)
        TestDisplayWindow.setAutoFillBackground(False)
        TestDisplayWindow.setStyleSheet("background-color: rgb(240, 240, 180);")

        self.centralwidget = QtWidgets.QWidget(TestDisplayWindow)
        self.centralwidget.setObjectName("centralwidget")
        

        self.testLabel = QtWidgets.QLabel(self.centralwidget)
        self.testLabel.setGeometry(QtCore.QRect(90, 80, 200, 31))
        self.testLabel.setStyleSheet("font: 20pt \"MS Shell Dlg 2\";")
        self.testLabel.setObjectName("testLabel")

        self.trainSelector = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.trainSelector.setGeometry(QtCore.QRect(300, 120, 111, 31))
        self.trainSelector.setStyleSheet("background-color: rgb(224,232,245);")    
        self.trainSelector.setMaximum(12)
        self.trainSelector.setMinimum(1)
        self.trainSelector.setTabletTracking(False)
        self.trainSelector.setObjectName("trainSelector")

        self.trainSelectorLabel = QtWidgets.QLabel(self.centralwidget)
        self.trainSelectorLabel.setGeometry(QtCore.QRect(90, 120, 111, 31))
        self.trainSelectorLabel.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.trainSelectorLabel.setObjectName("trainSelectorLabel")

        self.positionInput = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.positionInput.setGeometry(QtCore.QRect(300, 180, 111, 31))
        self.positionInput.setTabletTracking(False)
        self.positionInput.setStyleSheet("background-color: rgb(224,232,245);")
        #--self.positionInput.setAlignment(QtCore.Qt.AlignCenter)
        self.positionInput.setObjectName("positionInput")
        self.positionInput.setMaximum(300)
        self.positionInput.setMinimum(0)

        self.positionLabel = QtWidgets.QLabel(self.centralwidget)
        self.positionLabel.setGeometry(QtCore.QRect(90, 180, 111, 31))
        self.positionLabel.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.positionLabel.setObjectName("positionLabel")


        self.blockInput = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.blockInput.setGeometry(QtCore.QRect(300, 220, 111, 31))
        self.blockInput.setTabletTracking(False)
        self.blockInput.setStyleSheet("background-color: rgb(224,232,245);")
        self.blockInput.setAlignment(QtCore.Qt.AlignCenter)
        self.blockInput.setObjectName("blockInput")
        self.blockInput.setMaximum(150)
        self.blockInput.setMinimum(1)

        self.blockLabel = QtWidgets.QLabel(self.centralwidget)
        self.blockLabel.setGeometry(QtCore.QRect(90, 220, 111, 31))
        self.blockLabel.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.blockLabel.setObjectName("blockLabel")


        self.destInput = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.destInput.setGeometry(QtCore.QRect(300, 260, 111, 31))
        self.destInput.setTabletTracking(False)
        self.destInput.setStyleSheet("background-color: rgb(224,232,245);")
        self.destInput.setAlignment(QtCore.Qt.AlignCenter)
        self.destInput.setObjectName("destInput")
        self.destInput.setMaximum(150)
        self.destInput.setMinimum(1)

        self.destLabel = QtWidgets.QLabel(self.centralwidget)
        self.destLabel.setGeometry(QtCore.QRect(90, 260, 200, 31))
        self.destLabel.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.destLabel.setObjectName("destLabel")

        self.speedInput = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.speedInput.setGeometry(QtCore.QRect(300, 300, 111, 31))
        self.speedInput.setTabletTracking(False)
        self.speedInput.setStyleSheet("background-color: rgb(224,232,245);")
        self.speedInput.setAlignment(QtCore.Qt.AlignCenter)
        self.speedInput.setObjectName("speedInput")
        self.speedInput.setMaximum(25)
        self.speedInput.setMinimum(0)

        self.speedLabel = QtWidgets.QLabel(self.centralwidget)
        self.speedLabel.setGeometry(QtCore.QRect(90, 300, 200, 31))
        self.speedLabel.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.speedLabel.setObjectName("speedLabel")


        self.authorityOutput = QtWidgets.QLineEdit(self.centralwidget)
        self.authorityOutput.setGeometry(QtCore.QRect(300, 380, 150, 31))
        self.authorityOutput.setStyleSheet("background-color:rgb(224,232,245)")
        self.authorityOutput.setText("")
        self.authorityOutput.setAlignment(QtCore.Qt.AlignCenter)
        self.authorityOutput.setObjectName("authorityOutput")
        self.authorityOutput.setReadOnly(True)

        self.authLabel = QtWidgets.QLabel(self.centralwidget)
        self.authLabel.setGeometry(QtCore.QRect(90, 380, 200, 31))
        self.authLabel.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.authLabel.setObjectName("authLabel")

        self.speedOutput = QtWidgets.QLineEdit(self.centralwidget)
        self.speedOutput.setGeometry(QtCore.QRect(300, 440, 150, 31))
        self.speedOutput.setStyleSheet("background-color:rgb(224,232,245)")
        self.speedOutput.setText("")
        self.speedOutput.setAlignment(QtCore.Qt.AlignCenter)
        self.speedOutput.setObjectName("speedOutput")
        self.speedOutput.setReadOnly(True)

        self.speedLabel2 = QtWidgets.QLabel(self.centralwidget)
        self.speedLabel2.setGeometry(QtCore.QRect(90, 440, 200, 31))
        self.speedLabel2.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.speedLabel2.setObjectName("speedLabel2")

        #-- button to make authority
        self.AuthButton = QtWidgets.QPushButton(self.centralwidget)
        self.AuthButton.setGeometry(QtCore.QRect(500, 375, 100, 50))
        self.AuthButton.setStyleSheet("background-color:rgb(224,232,245)")
        self.AuthButton.setObjectName("AuthButton")
        
        TestDisplayWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(TestDisplayWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 768, 26))
        self.menubar.setObjectName("menubar")       

        self.retranslateUi(TestDisplayWindow)
        QtCore.QMetaObject.connectSlotsByName(TestDisplayWindow)
        
        
        

    def retranslateUi(self,TestDisplayWindow):
        _translate = QtCore.QCoreApplication.translate
        TestDisplayWindow.setWindowTitle(_translate("TestDisplayWindow", "Test Window"))

        self.testLabel.setText(_translate("TestDisplayWindow", "Test UI"))
        self.trainSelectorLabel.setText(_translate("TestDisplayWindow", "Select Train"))
        self.positionLabel.setText(_translate("TestDisplayWindow", "Input Position"))

        self.blockLabel.setText(_translate("TestDisplayWindow", "Input Block"))

        self.destLabel.setText(_translate("TestDisplayWindow", "Input Destination Block"))

        self.speedLabel.setText(_translate("TestDisplayWindow", "Input Train Speed (m/s)"))

        self.authLabel.setText(_translate("TestDisplayWindow", "Authority (m)"))

        self.speedLabel2.setText(_translate("TestDisplayWindow", "Suggested Speed (m/s)"))

        self.AuthButton.setText(_translate("TestDisplayWindow", "Calculate Authority"))
       #-- self.authButton.setText(_translate("TestDisplayWindow", "CALCULATE AUTHORITY"))
        

        
        
