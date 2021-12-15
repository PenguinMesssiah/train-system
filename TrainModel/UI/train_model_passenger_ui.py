# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'train_model_passenger_ui.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import sys
sys.path.append("..")

from Shared.connections import link

class Passenger_UI(object):
    def setupUi(self, Passenger_UI, currentTrainNum):
        self.currentTrainNum = currentTrainNum
        Passenger_UI.setObjectName("Passenger_UI")
        Passenger_UI.resize(800, 600)
        self.gridLayout_2 = QtWidgets.QGridLayout(Passenger_UI)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 1, 2, 1, 1)
        self.currentTime_label = QtWidgets.QLabel(Passenger_UI)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.currentTime_label.setFont(font)
        self.currentTime_label.setTextFormat(QtCore.Qt.RichText)
        self.currentTime_label.setScaledContents(False)
        self.currentTime_label.setAlignment(QtCore.Qt.AlignCenter)
        self.currentTime_label.setObjectName("currentTime_label")
        self.gridLayout.addWidget(self.currentTime_label, 0, 1, 1, 1)
        self.emergencyBrake_grid = QtWidgets.QGridLayout()
        self.emergencyBrake_grid.setObjectName("emergencyBrake_grid")
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.emergencyBrake_grid.addItem(spacerItem1, 0, 1, 1, 1)
        self.engage_emergencyBrake_button = QtWidgets.QPushButton(Passenger_UI)
        self.engage_emergencyBrake_button.setObjectName("engage_emergencyBrake_button")
        self.emergencyBrake_grid.addWidget(self.engage_emergencyBrake_button, 1, 1, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.emergencyBrake_grid.addItem(spacerItem2, 3, 1, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.emergencyBrake_grid.addItem(spacerItem3, 1, 0, 1, 1)
        self.disengage_emergencyBrake_button = QtWidgets.QPushButton(Passenger_UI)
        self.disengage_emergencyBrake_button.setObjectName("disengage_emergencyBrake_button")
        self.emergencyBrake_grid.addWidget(self.disengage_emergencyBrake_button, 2, 1, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.emergencyBrake_grid.addItem(spacerItem4, 2, 2, 1, 1)
        self.gridLayout.addLayout(self.emergencyBrake_grid, 5, 2, 1, 1)
        self.emergencyBrake_status_label = QtWidgets.QLabel(Passenger_UI)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.emergencyBrake_status_label.setFont(font)
        self.emergencyBrake_status_label.setTextFormat(QtCore.Qt.RichText)
        self.emergencyBrake_status_label.setScaledContents(False)
        self.emergencyBrake_status_label.setAlignment(QtCore.Qt.AlignCenter)
        self.emergencyBrake_status_label.setObjectName("emergencyBrake_status_label")
        self.gridLayout.addWidget(self.emergencyBrake_status_label, 8, 2, 1, 1)
        self.arrivalTime_text = QtWidgets.QTextBrowser(Passenger_UI)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(28)
        self.arrivalTime_text.setFont(font)
        self.arrivalTime_text.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.arrivalTime_text.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.arrivalTime_text.setObjectName("arrivalTime_text")
        self.gridLayout.addWidget(self.arrivalTime_text, 9, 1, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem5, 1, 0, 1, 1)
        self.departureTime_label = QtWidgets.QLabel(Passenger_UI)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.departureTime_label.setFont(font)
        self.departureTime_label.setScaledContents(False)
        self.departureTime_label.setAlignment(QtCore.Qt.AlignCenter)
        self.departureTime_label.setObjectName("departureTime_label")
        self.gridLayout.addWidget(self.departureTime_label, 3, 1, 1, 1)
        self.departureTime_text = QtWidgets.QTextBrowser(Passenger_UI)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(28)
        self.departureTime_text.setFont(font)
        self.departureTime_text.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.departureTime_text.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.departureTime_text.setObjectName("departureTime_text")
        self.gridLayout.addWidget(self.departureTime_text, 5, 1, 1, 1)
        self.arrivalTime_label = QtWidgets.QLabel(Passenger_UI)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.arrivalTime_label.setFont(font)
        self.arrivalTime_label.setTextFormat(QtCore.Qt.RichText)
        self.arrivalTime_label.setScaledContents(False)
        self.arrivalTime_label.setAlignment(QtCore.Qt.AlignCenter)
        self.arrivalTime_label.setObjectName("arrivalTime_label")
        self.gridLayout.addWidget(self.arrivalTime_label, 8, 1, 1, 1)
        self.currentSpeed_label_4 = QtWidgets.QLabel(Passenger_UI)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.currentSpeed_label_4.setFont(font)
        self.currentSpeed_label_4.setTextFormat(QtCore.Qt.RichText)
        self.currentSpeed_label_4.setScaledContents(False)
        self.currentSpeed_label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.currentSpeed_label_4.setObjectName("currentSpeed_label_4")
        self.gridLayout.addWidget(self.currentSpeed_label_4, 3, 2, 1, 1)
        self.currentTime_text = QtWidgets.QTextBrowser(Passenger_UI)
        self.currentTime_text.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.currentTime_text.sizePolicy().hasHeightForWidth())
        self.currentTime_text.setSizePolicy(sizePolicy)
        self.currentTime_text.setMinimumSize(QtCore.QSize(1, 1))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(28)
        self.currentTime_text.setFont(font)
        self.currentTime_text.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.currentTime_text.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.currentTime_text.setObjectName("currentTime_text")
        self.gridLayout.addWidget(self.currentTime_text, 1, 1, 1, 1)
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.gridLayout.addLayout(self.gridLayout_3, 9, 2, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)

        self.retranslateUi(Passenger_UI)
        QtCore.QMetaObject.connectSlotsByName(Passenger_UI)

        self.engage_emergencyBrake_button.pressed.connect(self.engage_emergencyBrake_button_pressed)
        self.disengage_emergencyBrake_button.pressed.connect(self.disengage_emergencyBrake_button_pressed)
        link.train_model_send_emergencyBrake_passenger_UI.connect(self.set_emergencyBrake_status_label)

    def engage_emergencyBrake_button_pressed(self):
        link.train_model_receive_passenger_emergencyBrake.emit(self.currentTrainNum, True)

    def disengage_emergencyBrake_button_pressed(self):
        link.train_model_receive_passenger_emergencyBrake.emit(self.currentTrainNum, False)

    def set_emergencyBrake_status_label(self, status):
        if status:
            self.emergencyBrake_status_label.setText("Currently ENGAGED")
        else:
            self.emergencyBrake_status_label.setText("Currently disengaged")

    def retranslateUi(self, Passenger_UI):
        _translate = QtCore.QCoreApplication.translate
        Passenger_UI.setWindowTitle(_translate("Passenger_UI", "Dialog"))
        self.currentTime_label.setText(_translate("Passenger_UI", "Current Time"))
        self.engage_emergencyBrake_button.setText(_translate("Passenger_UI", "Engage"))
        self.disengage_emergencyBrake_button.setText(_translate("Passenger_UI", "Disengage"))
        self.emergencyBrake_status_label.setText(_translate("Passenger_UI", "Currently Disengaged"))
        self.arrivalTime_text.setHtml(_translate("Passenger_UI", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Arial\'; font-size:28pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:16pt;\">12:00:00</span></p></body></html>"))
        self.departureTime_label.setText(_translate("Passenger_UI", "Departure Time"))
        self.departureTime_text.setHtml(_translate("Passenger_UI", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Arial\'; font-size:28pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:16pt;\">12:00:00</span></p></body></html>"))
        self.arrivalTime_label.setText(_translate("Passenger_UI", "Arrival Time"))
        self.currentSpeed_label_4.setText(_translate("Passenger_UI", "Emergency Brake"))
        self.currentTime_text.setHtml(_translate("Passenger_UI", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Arial\'; font-size:28pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:16pt;\">12:00:00</span></p></body></html>"))


# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     Passenger_UI = QtWidgets.QDialog()
#     ui = Ui_Passenger_UI()
#     ui.setupUi(Passenger_UI)
#     Passenger_UI.show()
#     sys.exit(app.exec_())

