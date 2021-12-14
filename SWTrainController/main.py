import time
from Controller.TrainController import TrainController
from UI.Driver import DriverDisplay
from UI.Engineer import EngineerDisplay
from PyQt5 import QtCore, QtGui, QtWidgets

def setTrainValues():
    kp = Engineer_UI.kpInput.value()
    ki = Engineer_UI.kiInput.value()
    EngineerWindow.close()
    start(kp, ki)

def start(kp, ki):

    train1_DriverWindow = QtWidgets.QMainWindow()
    train1_UI = DriverDisplay()
    train1_UI.setupUI(train1_DriverWindow, 1)
    train1_DriverWindow.show()
    train1 = TrainController(1, kp, ki, train1_UI)

    #train2_DriverWindow = QtWidgets.QMainWindow()
    #train2_UI = DriverDisplay()
    #train2_UI.setupUI(train2_DriverWindow, 2)
    #train2_DriverWindow.show()
    #train2 = TrainController(2, kp, ki, train2_UI)

    #train3_DriverWindow = QtWidgets.QMainWindow()
    #train3_UI = DriverDisplay()
    #train3_UI.setupUI(train3_DriverWindow, 3)
    #train3_DriverWindow.show()
    #train3 = TrainController(3, kp, ki, train3_UI)

    #train4_DriverWindow = QtWidgets.QMainWindow()
    #train4_UI = DriverDisplay()
    #train4_UI.setupUI(train4_DriverWindow, 4)
    #train4_DriverWindow.show()
    #train4 = TrainController(4, kp, ki, train4_UI)

    #train5_DriverWindow = QtWidgets.QMainWindow()
    #train5_UI = DriverDisplay()
    #train5_UI.setupUI(train5_DriverWindow, 5)
    #train5_DriverWindow.show()
    #train5 = TrainController(5, kp, ki, train5_UI)

    #train6_DriverWindow = QtWidgets.QMainWindow()
    #train6_UI = DriverDisplay()
    #train6_UI.setupUI(train6_DriverWindow, 6)
    #train6_DriverWindow.show()
    #train6 = TrainController(6, kp, ki, train6_UI)

    #train7_DriverWindow = QtWidgets.QMainWindow()
    #train7_UI = DriverDisplay()
    #train7_UI.setupUI(train7_DriverWindow, 7)
    #train7_DriverWindow.show()
    #train7 = TrainController(7, kp, ki, train7_UI)

    #train8_DisplayWindow = QtWidgets.QMainWindow()
    #train8_UI = DriverDisplay()
    #train8_UI.setupUI(train8_DisplayWindow, 8)
    #train8_DisplayWindow.show()
    #train8 = TrainController(8, kp, ki, train8_UI)

    #train9_DriverWindow = QtWidgets.QMainWindow()
    #train9_UI = DriverDisplay()
    #train9_UI.setupUI(train9_DriverWindow, 9)
    #train9_DriverWindow.show()
    #train9 = TrainController(9, kp, ki, train9_UI)

    #train10_DriverWindow = QtWidgets.QMainWindow()
    #train10_UI = DriverDisplay()
    #train10_UI.setupUI(train10_DriverWindow, 10)
    #train10_DriverWindow.show()
    #train10 = TrainController(10, kp, ki, train10_UI)
    
    sys.exit(app.exec_())

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    
    EngineerWindow = QtWidgets.QMainWindow()
    Engineer_UI = EngineerDisplay()
    Engineer_UI.setupUI(EngineerWindow)
    EngineerWindow.show()
    Engineer_UI.enterButton.clicked.connect(setTrainValues)





















    
