# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'train_model_diagnostics_ui.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import sys
sys.path.append("..")

from Shared.connections import link

class Diagnostics_UI(object):
    def setupUi(self, Diagnostics_UI, currentTrainNum):
        self.currentTrainNum = currentTrainNum
        Diagnostics_UI.setObjectName("Diagnostics_UI")
        Diagnostics_UI.resize(800, 600)
        self.gridLayout_2 = QtWidgets.QGridLayout(Diagnostics_UI)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.diagnostics_grid = QtWidgets.QGridLayout()
        self.diagnostics_grid.setObjectName("diagnostics_grid")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.diagnostics_grid.addItem(spacerItem, 7, 0, 1, 1)
        self.toggleSignalPickupFailure_button = QtWidgets.QPushButton(Diagnostics_UI)
        self.toggleSignalPickupFailure_button.setObjectName("toggleSignalPickupFailure_button")
        self.diagnostics_grid.addWidget(self.toggleSignalPickupFailure_button, 6, 0, 1, 1)
        self.failureStatus_label = QtWidgets.QLabel(Diagnostics_UI)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.failureStatus_label.setFont(font)
        self.failureStatus_label.setAlignment(QtCore.Qt.AlignCenter)
        self.failureStatus_label.setObjectName("failureStatus_label")
        self.diagnostics_grid.addWidget(self.failureStatus_label, 2, 1, 1, 1)
        self.diagnostics_label = QtWidgets.QLabel(Diagnostics_UI)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.diagnostics_label.sizePolicy().hasHeightForWidth())
        self.diagnostics_label.setSizePolicy(sizePolicy)
        self.diagnostics_label.setMinimumSize(QtCore.QSize(1, 1))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.diagnostics_label.setFont(font)
        self.diagnostics_label.setAlignment(QtCore.Qt.AlignCenter)
        self.diagnostics_label.setObjectName("diagnostics_label")
        self.diagnostics_grid.addWidget(self.diagnostics_label, 2, 0, 1, 1)
        self.toggleBrakeFailure_button = QtWidgets.QPushButton(Diagnostics_UI)
        self.toggleBrakeFailure_button.setObjectName("toggleBrakeFailure_button")
        self.diagnostics_grid.addWidget(self.toggleBrakeFailure_button, 5, 0, 1, 1)
        self.toggleEngineFailure_button = QtWidgets.QPushButton(Diagnostics_UI)
        self.toggleEngineFailure_button.setObjectName("toggleEngineFailure_button")
        self.diagnostics_grid.addWidget(self.toggleEngineFailure_button, 4, 0, 1, 1)
        self.signalPickupStatus = QtWidgets.QLabel(Diagnostics_UI)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.signalPickupStatus.setFont(font)
        self.signalPickupStatus.setAlignment(QtCore.Qt.AlignCenter)
        self.signalPickupStatus.setObjectName("signalPickupStatus")
        self.diagnostics_grid.addWidget(self.signalPickupStatus, 6, 1, 1, 1)
        self.brakeStatus = QtWidgets.QLabel(Diagnostics_UI)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.brakeStatus.setFont(font)
        self.brakeStatus.setAlignment(QtCore.Qt.AlignCenter)
        self.brakeStatus.setObjectName("brakeStatus")
        self.diagnostics_grid.addWidget(self.brakeStatus, 5, 1, 1, 1)
        self.engineStatus = QtWidgets.QLabel(Diagnostics_UI)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.engineStatus.setFont(font)
        self.engineStatus.setAlignment(QtCore.Qt.AlignCenter)
        self.engineStatus.setObjectName("engineStatus")
        self.diagnostics_grid.addWidget(self.engineStatus, 4, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.diagnostics_grid.addItem(spacerItem1, 1, 1, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.diagnostics_grid.addItem(spacerItem2, 3, 0, 1, 1)
        self.gridLayout_2.addLayout(self.diagnostics_grid, 0, 0, 1, 1)

        self.retranslateUi(Diagnostics_UI)
        QtCore.QMetaObject.connectSlotsByName(Diagnostics_UI)

        self.toggleEngineFailure_button.pressed.connect(self.toggleEngineFailure)
        self.toggleBrakeFailure_button.pressed.connect(self.toggleBrakeFailure)
        self.toggleSignalPickupFailure_button.pressed.connect(self.toggleSignalPickupFailure)
        #connect.train_model_send_emergencyBrake_passenger_UI.connect(self.set_emergencyBrake_status_label)

    def toggleEngineFailure(self):
        link.train_model_diagnostics_toggleEngineFailure.emit(self.currentTrainNum)

    def toggleBrakeFailure(self):
        link.train_model_diagnostics_toggleBrakeFailure.emit(self.currentTrainNum)

    def toggleSignalPickupFailure(self):
        link.train_model_diagnostics_toggleSignalPickupFailure.emit(self.currentTrainNum)

    def retranslateUi(self, Diagnostics_UI):
        _translate = QtCore.QCoreApplication.translate
        Diagnostics_UI.setWindowTitle(_translate("Diagnostics_UI", "Dialog"))
        self.toggleSignalPickupFailure_button.setText(_translate("Diagnostics_UI", "Toggle Signal Pickup Failure"))
        self.failureStatus_label.setText(_translate("Diagnostics_UI", "Failure Status"))
        self.diagnostics_label.setText(_translate("Diagnostics_UI", "Diagnostics"))
        self.toggleBrakeFailure_button.setText(_translate("Diagnostics_UI", "Toggle Brake Failure"))
        self.toggleEngineFailure_button.setText(_translate("Diagnostics_UI", "Toggle Engine Failure"))
        self.signalPickupStatus.setText(_translate("Diagnostics_UI", "Signal Pickup Status"))
        self.brakeStatus.setText(_translate("Diagnostics_UI", "Brake Status"))
        self.engineStatus.setText(_translate("Diagnostics_UI", "Engine Status"))


# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     Diagnostics_UI = QtWidgets.QDialog()
#     ui = Ui_Diagnostics_UI()
#     ui.setupUi(Diagnostics_UI)
#     Diagnostics_UI.show()
#     sys.exit(app.exec_())

