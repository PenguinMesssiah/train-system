# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'train_model_testing_ui.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import sys
sys.path.append("..")

from Shared.connections import link

class Testing_UI(object):
    def setupUi(self, Test, currentTrainNum):
        self.currentTrainNum = currentTrainNum

        Test.setObjectName("Test")
        Test.resize(795, 600)
        self.gridLayout = QtWidgets.QGridLayout(Test)
        self.gridLayout.setObjectName("gridLayout")
        self.test_grid = QtWidgets.QGridLayout()
        self.test_grid.setObjectName("test_grid")
        self.setPower_text = QtWidgets.QPlainTextEdit(Test)
        self.setPower_text.setObjectName("setPower_text")
        self.test_grid.addWidget(self.setPower_text, 14, 1, 1, 1)
        self.setPassengers_label = QtWidgets.QLabel(Test)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.setPassengers_label.setFont(font)
        self.setPassengers_label.setAlignment(QtCore.Qt.AlignCenter)
        self.setPassengers_label.setObjectName("setPassengers_label")
        self.test_grid.addWidget(self.setPassengers_label, 7, 0, 1, 1)
        self.setPower_label = QtWidgets.QLabel(Test)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.setPower_label.setFont(font)
        self.setPower_label.setAlignment(QtCore.Qt.AlignCenter)
        self.setPower_label.setObjectName("setPower_label")
        self.test_grid.addWidget(self.setPower_label, 11, 1, 1, 1)
        self.setCommandedSpeed_label = QtWidgets.QLabel(Test)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.setCommandedSpeed_label.setFont(font)
        self.setCommandedSpeed_label.setAlignment(QtCore.Qt.AlignCenter)
        self.setCommandedSpeed_label.setObjectName("setCommandedSpeed_label")
        self.test_grid.addWidget(self.setCommandedSpeed_label, 7, 1, 1, 1)
        self.setSpeedLimit_label = QtWidgets.QLabel(Test)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.setSpeedLimit_label.setFont(font)
        self.setSpeedLimit_label.setAlignment(QtCore.Qt.AlignCenter)
        self.setSpeedLimit_label.setObjectName("setSpeedLimit_label")
        self.test_grid.addWidget(self.setSpeedLimit_label, 9, 1, 1, 1)
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setObjectName("gridLayout_4")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem, 1, 0, 1, 1)
        self.setValues_button = QtWidgets.QPushButton(Test)
        self.setValues_button.setObjectName("setValues_button")
        self.gridLayout_4.addWidget(self.setValues_button, 1, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_4.addItem(spacerItem1, 0, 1, 1, 1)
        self.stopTest_button = QtWidgets.QPushButton(Test)
        self.stopTest_button.setObjectName("stopTest_button")
        self.gridLayout_4.addWidget(self.stopTest_button, 1, 2, 1, 1)
        self.test_grid.addLayout(self.gridLayout_4, 14, 2, 1, 1)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.toggleEmergencyBrakes_button = QtWidgets.QPushButton(Test)
        self.toggleEmergencyBrakes_button.setObjectName("toggleEmergencyBrakes_button")
        self.gridLayout_2.addWidget(self.toggleEmergencyBrakes_button, 2, 0, 1, 1)
        self.toggleServiceBrakes_button = QtWidgets.QPushButton(Test)
        self.toggleServiceBrakes_button.setObjectName("toggleServiceBrakes_button")
        self.gridLayout_2.addWidget(self.toggleServiceBrakes_button, 1, 0, 1, 1)
        self.test_grid.addLayout(self.gridLayout_2, 3, 0, 1, 1)
        self.toggleDoors_label = QtWidgets.QLabel(Test)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.toggleDoors_label.setFont(font)
        self.toggleDoors_label.setAlignment(QtCore.Qt.AlignCenter)
        self.toggleDoors_label.setObjectName("toggleDoors_label")
        self.test_grid.addWidget(self.toggleDoors_label, 11, 0, 1, 1)
        self.setTemperature_label = QtWidgets.QLabel(Test)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.setTemperature_label.setFont(font)
        self.setTemperature_label.setAlignment(QtCore.Qt.AlignCenter)
        self.setTemperature_label.setObjectName("setTemperature_label")
        self.test_grid.addWidget(self.setTemperature_label, 9, 0, 1, 1)
        self.setSpeedLimit_text = QtWidgets.QPlainTextEdit(Test)
        self.setSpeedLimit_text.setObjectName("setSpeedLimit_text")
        self.test_grid.addWidget(self.setSpeedLimit_text, 10, 1, 1, 1)
        self.setBrakes_label = QtWidgets.QLabel(Test)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.setBrakes_label.setFont(font)
        self.setBrakes_label.setAlignment(QtCore.Qt.AlignCenter)
        self.setBrakes_label.setObjectName("setBrakes_label")
        self.test_grid.addWidget(self.setBrakes_label, 2, 0, 1, 1)
        self.setCommandedSpeed_text = QtWidgets.QPlainTextEdit(Test)
        self.setCommandedSpeed_text.setObjectName("setCommandedSpeed_text")
        self.test_grid.addWidget(self.setCommandedSpeed_text, 8, 1, 1, 1)
        self.setTemperature_text = QtWidgets.QPlainTextEdit(Test)
        self.setTemperature_text.setObjectName("setTemperature_text")
        self.test_grid.addWidget(self.setTemperature_text, 10, 0, 1, 1)
        self.setPassengers_text = QtWidgets.QPlainTextEdit(Test)
        self.setPassengers_text.setObjectName("setPassengers_text")
        self.test_grid.addWidget(self.setPassengers_text, 8, 0, 1, 1)
        self.setSuggestSpeed_text = QtWidgets.QPlainTextEdit(Test)
        self.setSuggestSpeed_text.setObjectName("setSuggestSpeed_text")
        self.test_grid.addWidget(self.setSuggestSpeed_text, 3, 1, 1, 1)
        self.setSuggestSpeed_label = QtWidgets.QLabel(Test)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.setSuggestSpeed_label.setFont(font)
        self.setSuggestSpeed_label.setAlignment(QtCore.Qt.AlignCenter)
        self.setSuggestSpeed_label.setObjectName("setSuggestSpeed_label")
        self.test_grid.addWidget(self.setSuggestSpeed_label, 2, 1, 1, 1)
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.toggleLeftDoor_button = QtWidgets.QPushButton(Test)
        self.toggleLeftDoor_button.setObjectName("toggleLeftDoor_button")
        self.gridLayout_3.addWidget(self.toggleLeftDoor_button, 0, 0, 1, 1)
        self.toggleRightDoor_button = QtWidgets.QPushButton(Test)
        self.toggleRightDoor_button.setObjectName("toggleRightDoor_button")
        self.gridLayout_3.addWidget(self.toggleRightDoor_button, 1, 0, 1, 1)
        self.test_grid.addLayout(self.gridLayout_3, 14, 0, 1, 1)
        self.gridLayout.addLayout(self.test_grid, 0, 1, 1, 1)

        self.retranslateUi(Test)
        QtCore.QMetaObject.connectSlotsByName(Test)

        self.numPressed = 0

        self.toggleServiceBrakes_button.pressed.connect(self.toggleServiceBrakes)
        self.toggleEmergencyBrakes_button.pressed.connect(self.toggleEmergencyBrakes)     
        self.setValues_button.pressed.connect(self.setValues)
        self.stopTest_button.pressed.connect(self.stopRun)
        self.toggleLeftDoor_button.pressed.connect(self.toggleLeftDoor)
        self.toggleRightDoor_button.pressed.connect(self.toggleRightDoor)

    def toggleServiceBrakes(self):
        link.train_model_testing_send_serviceBrake.emit(self.currentTrainNum)


    def toggleEmergencyBrakes(self):
        self.numPressed += 1

        if (self.numPressed % 2) == 0:
            link.train_model_receive_passenger_emergencyBrake.emit(self.currentTrainNum, False)     # temp for iteration 2, reusing passenger function
        else:
            link.train_model_receive_passenger_emergencyBrake.emit(self.currentTrainNum, True)


    def toggleLeftDoor(self):
        link.train_model_toggleDoors.emit(self.currentTrainNum, "left")


    def toggleRightDoor(self):
        link.train_model_toggleDoors.emit(self.currentTrainNum, "right")

    
    def stopRun(self):
        link.train_model_stop_run.emit()


    def setValues(self):
        passengers = int(self.setPassengers_text.toPlainText())
        temperature = float(self.setTemperature_text.toPlainText())
        suggestedSpeed = float(self.setSuggestSpeed_text.toPlainText())
        commandedSpeed = float(self.setCommandedSpeed_text.toPlainText())
        speedLimit = float(self.setSpeedLimit_text.toPlainText())
        power = float(self.setPower_text.toPlainText())
        link.train_model_send_testing_values.emit(self.currentTrainNum, passengers, temperature, suggestedSpeed, commandedSpeed, speedLimit, power)


    def set_to_zero_if_empty(self, text):
        if not text:
            return '0'
        else:
            return text


    def retranslateUi(self, Test):
        _translate = QtCore.QCoreApplication.translate
        Test.setWindowTitle(_translate("Test", "Dialog"))
        self.setPassengers_label.setText(_translate("Test", "Set Passengers"))
        self.setPower_label.setText(_translate("Test", "Set Power"))
        self.setCommandedSpeed_label.setText(_translate("Test", "Set Commanded Speed"))
        self.setSpeedLimit_label.setText(_translate("Test", "Set Speed Limit"))
        self.setValues_button.setText(_translate("Test", "Set Values"))
        self.stopTest_button.setText(_translate("Test", "Stop Test"))
        self.toggleEmergencyBrakes_button.setText(_translate("Test", "Toggle Emergency Brakes"))
        self.toggleServiceBrakes_button.setText(_translate("Test", "Toggle Service Brakes"))
        self.toggleDoors_label.setText(_translate("Test", "Set Doors"))
        self.setTemperature_label.setText(_translate("Test", "Set Temperature"))
        self.setBrakes_label.setText(_translate("Test", "Set Brakes"))
        self.setSuggestSpeed_label.setText(_translate("Test", "Set Suggested Speed"))
        self.toggleLeftDoor_button.setText(_translate("Test", "Toggle Left Door"))
        self.toggleRightDoor_button.setText(_translate("Test", "Toggle Right Door"))


# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     Test = QtWidgets.QDialog()
#     ui = Ui_Test()
#     ui.setupUi(Test)
#     Test.show()
#     sys.exit(app.exec_())

