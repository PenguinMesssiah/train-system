# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\wayside_sw.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class WaysideUi(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(804, 515)
        self.TimeBox = QtWidgets.QGroupBox(Form)
        self.TimeBox.setGeometry(QtCore.QRect(10, 10, 241, 51))
        self.TimeBox.setObjectName("TimeBox")
        self.time = QtWidgets.QTimeEdit(self.TimeBox)
        self.time.setGeometry(QtCore.QRect(20, 20, 118, 22))
        self.time.setObjectName("time")
        self.SpeedBox = QtWidgets.QGroupBox(Form)
        self.SpeedBox.setGeometry(QtCore.QRect(520, 10, 271, 241))
        self.SpeedBox.setObjectName("SpeedBox")
        self.speedTxt = QtWidgets.QTextEdit(self.SpeedBox)
        self.speedTxt.setGeometry(QtCore.QRect(10, 20, 251, 211))
        self.speedTxt.setObjectName("speedTxt")
        self.TrackOccBox = QtWidgets.QGroupBox(Form)
        self.TrackOccBox.setGeometry(QtCore.QRect(20, 60, 241, 321))
        self.TrackOccBox.setObjectName("TrackOccBox")
        self.trackOccTxt = QtWidgets.QTextEdit(self.TrackOccBox)
        self.trackOccTxt.setGeometry(QtCore.QRect(10, 20, 161, 261))
        self.trackOccTxt.setObjectName("trackOccTxt")
        self.checkBox10 = QtWidgets.QCheckBox(self.TrackOccBox)
        self.checkBox10.setGeometry(QtCore.QRect(180, 190, 31, 16))
        self.checkBox10.setText("")
        self.checkBox10.setObjectName("checkBox10")
        self.checkBox11 = QtWidgets.QCheckBox(self.TrackOccBox)
        self.checkBox11.setGeometry(QtCore.QRect(180, 210, 31, 16))
        self.checkBox11.setText("")
        self.checkBox11.setObjectName("checkBox11")
        self.checkBox12 = QtWidgets.QCheckBox(self.TrackOccBox)
        self.checkBox12.setGeometry(QtCore.QRect(180, 230, 31, 16))
        self.checkBox12.setText("")
        self.checkBox12.setObjectName("checkBox12")
        self.checkBox13 = QtWidgets.QCheckBox(self.TrackOccBox)
        self.checkBox13.setGeometry(QtCore.QRect(180, 250, 31, 16))
        self.checkBox13.setText("")
        self.checkBox13.setObjectName("checkBox13")
        self.checkBox14 = QtWidgets.QCheckBox(self.TrackOccBox)
        self.checkBox14.setGeometry(QtCore.QRect(180, 270, 31, 16))
        self.checkBox14.setText("")
        self.checkBox14.setObjectName("checkBox14")
        self.checkBox9 = QtWidgets.QCheckBox(self.TrackOccBox)
        self.checkBox9.setGeometry(QtCore.QRect(180, 170, 31, 16))
        self.checkBox9.setText("")
        self.checkBox9.setObjectName("checkBox9")
        self.checkBox15 = QtWidgets.QCheckBox(self.TrackOccBox)
        self.checkBox15.setGeometry(QtCore.QRect(180, 290, 31, 16))
        self.checkBox15.setText("")
        self.checkBox15.setObjectName("checkBox15")
        self.checkBox8 = QtWidgets.QCheckBox(self.TrackOccBox)
        self.checkBox8.setGeometry(QtCore.QRect(180, 150, 31, 16))
        self.checkBox8.setText("")
        self.checkBox8.setObjectName("checkBox8")
        self.checkBox1 = QtWidgets.QCheckBox(self.TrackOccBox)
        self.checkBox1.setGeometry(QtCore.QRect(180, 10, 31, 16))
        self.checkBox1.setObjectName("checkBox1")
        self.checkBox3 = QtWidgets.QCheckBox(self.TrackOccBox)
        self.checkBox3.setGeometry(QtCore.QRect(180, 50, 31, 16))
        self.checkBox3.setObjectName("checkBox3")
        self.checkBox2 = QtWidgets.QCheckBox(self.TrackOccBox)
        self.checkBox2.setGeometry(QtCore.QRect(180, 30, 31, 16))
        self.checkBox2.setObjectName("checkBox2")
        self.checkBox5 = QtWidgets.QCheckBox(self.TrackOccBox)
        self.checkBox5.setGeometry(QtCore.QRect(180, 90, 31, 16))
        self.checkBox5.setObjectName("checkBox5")
        self.checkBox4 = QtWidgets.QCheckBox(self.TrackOccBox)
        self.checkBox4.setGeometry(QtCore.QRect(180, 70, 31, 16))
        self.checkBox4.setObjectName("checkBox4")
        self.checkBox7 = QtWidgets.QCheckBox(self.TrackOccBox)
        self.checkBox7.setGeometry(QtCore.QRect(180, 130, 31, 16))
        self.checkBox7.setObjectName("checkBox7")
        self.checkBox6 = QtWidgets.QCheckBox(self.TrackOccBox)
        self.checkBox6.setGeometry(QtCore.QRect(180, 110, 31, 16))
        self.checkBox6.setObjectName("checkBox6")
        self.switchBox = QtWidgets.QGroupBox(Form)
        self.switchBox.setGeometry(QtCore.QRect(270, 10, 241, 181))
        self.switchBox.setObjectName("switchBox")
        self.switchTxt = QtWidgets.QTextEdit(self.switchBox)
        self.switchTxt.setGeometry(QtCore.QRect(0, 20, 141, 151))
        self.switchTxt.setObjectName("switchTxt")
        self.radioButton = QtWidgets.QRadioButton(self.switchBox)
        self.radioButton.setGeometry(QtCore.QRect(150, 40, 69, 15))
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(self.switchBox)
        self.radioButton_2.setGeometry(QtCore.QRect(150, 60, 69, 15))
        self.radioButton_2.setObjectName("radioButton_2")
        self.CrossingBox = QtWidgets.QGroupBox(Form)
        self.CrossingBox.setGeometry(QtCore.QRect(270, 190, 241, 81))
        self.CrossingBox.setObjectName("CrossingBox")
        self.textEdit_2 = QtWidgets.QTextEdit(self.CrossingBox)
        self.textEdit_2.setGeometry(QtCore.QRect(10, 20, 131, 51))
        self.textEdit_2.setObjectName("textEdit_2")
        self.LightsBox = QtWidgets.QGroupBox(Form)
        self.LightsBox.setGeometry(QtCore.QRect(270, 280, 241, 101))
        self.LightsBox.setObjectName("LightsBox")
        self.textEdit_3 = QtWidgets.QTextEdit(self.LightsBox)
        self.textEdit_3.setGeometry(QtCore.QRect(10, 20, 131, 71))
        self.textEdit_3.setObjectName("textEdit_3")
        self.OperationBox = QtWidgets.QGroupBox(Form)
        self.OperationBox.setGeometry(QtCore.QRect(230, 390, 281, 111))
        self.OperationBox.setObjectName("OperationBox")
        self.autoButton = QtWidgets.QPushButton(self.OperationBox)
        self.autoButton.setGeometry(QtCore.QRect(50, 30, 81, 51))
        self.autoButton.setObjectName("autoButton")
        self.testingButton = QtWidgets.QPushButton(self.OperationBox)
        self.testingButton.setGeometry(QtCore.QRect(150, 30, 81, 51))
        self.testingButton.setObjectName("testingButton")
        self.AuthBox = QtWidgets.QGroupBox(Form)
        self.AuthBox.setGeometry(QtCore.QRect(520, 260, 271, 241))
        self.AuthBox.setObjectName("AuthBox")
        self.authorityTxt = QtWidgets.QTextEdit(self.AuthBox)
        self.authorityTxt.setGeometry(QtCore.QRect(10, 20, 251, 211))
        self.authorityTxt.setObjectName("authorityTxt")
        self.PLCBox = QtWidgets.QGroupBox(Form)
        self.PLCBox.setGeometry(QtCore.QRect(20, 390, 191, 111))
        self.PLCBox.setObjectName("PLCBox")
        self.uploadPLC = QtWidgets.QPushButton(self.PLCBox)
        self.uploadPLC.setGeometry(QtCore.QRect(120, 40, 62, 31))
        self.uploadPLC.setObjectName("uploadPLC")
        self.textEdit = QtWidgets.QTextEdit(self.PLCBox)
        self.textEdit.setGeometry(QtCore.QRect(10, 20, 104, 81))
        self.textEdit.setObjectName("textEdit")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.TimeBox.setTitle(_translate("Form", "Time (EST)"))
        self.SpeedBox.setTitle(_translate("Form", "Commanded Speed (km/hr)"))
        self.TrackOccBox.setTitle(_translate("Form", "Track Occupancy"))
        self.checkBox1.setText(_translate("Form", "0"))
        self.checkBox3.setText(_translate("Form", "62"))
        self.checkBox2.setText(_translate("Form", "61"))
        self.checkBox5.setText(_translate("Form", "64"))
        self.checkBox4.setText(_translate("Form", "63"))
        self.checkBox7.setText(_translate("Form", "66"))
        self.checkBox6.setText(_translate("Form", "65"))
        self.switchBox.setTitle(_translate("Form", "Switch Control"))
        self.radioButton.setText(_translate("Form", "62-63"))
        self.radioButton_2.setText(_translate("Form", "Yard-63"))
        self.CrossingBox.setTitle(_translate("Form", "Crossing Control"))
        self.textEdit_2.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.1pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.LightsBox.setTitle(_translate("Form", "Lights Control"))
        self.textEdit_3.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.1pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.OperationBox.setTitle(_translate("Form", "Operation Mode"))
        self.autoButton.setText(_translate("Form", "Automatic"))
        self.testingButton.setText(_translate("Form", "Testing"))
        self.AuthBox.setTitle(_translate("Form", "Authority (m)"))
        self.PLCBox.setTitle(_translate("Form", "Load PLC"))
        self.uploadPLC.setText(_translate("Form", "Upload PLC"))
        self.textEdit.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.1pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Enter filepath to PLC</p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
