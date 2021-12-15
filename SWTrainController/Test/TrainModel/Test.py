import time
import json
from PyQt5 import QtCore, QtGui, QtWidgets
from TestUI import TrainModelDisplay

trainNumber = 0.0
beacon = ""
commandedSpeed = 0.0
actualSpeed = 0.0
speedLimit = 0.0
engineFaultStatus = False
brakeFaultStatus = False
signalFaultStatus = False

def engineFaultTrue():
    global engineFaultStatus
    engineFaultStatus = True
    TrainModel_UI.engineFaultTrueButton.setStyleSheet("background-color:rgb(0, 255, 0)")
    TrainModel_UI.engineFaultFalseButton.setStyleSheet("background-color:rgb(255,255,255)")

def engineFaultFalse():
    global engineFaultStatus
    engineFaultStatus = False
    TrainModel_UI.engineFaultFalseButton.setStyleSheet("background-color:rgb(0, 255, 0)")
    TrainModel_UI.engineFaultTrueButton.setStyleSheet("background-color:rgb(255,255,255)")

def brakeFaultTrue():
    global brakeFaultStatus
    brakeFaultStatus = True
    TrainModel_UI.brakeFaultTrueButton.setStyleSheet("background-color:rgb(0, 255, 0)")
    TrainModel_UI.brakeFaultFalseButton.setStyleSheet("background-color:rgb(255,255,255)")

def brakeFaultFalse():
    global brakeFaultStatus
    brakeFaultStatus = False
    TrainModel_UI.brakeFaultFalseButton.setStyleSheet("background-color:rgb(0, 255, 0)")
    TrainModel_UI.brakeFaultTrueButton.setStyleSheet("background-color:rgb(255,255,255)")

def signalFaultTrue():
    global signalFaultStatus
    signalFaultStatus = True
    TrainModel_UI.signalFaultTrueButton.setStyleSheet("background-color:rgb(0, 255, 0)")
    TrainModel_UI.signalFaultFalseButton.setStyleSheet("background-color:rgb(255,255,255)")

def signalFaultFalse():
    global signalFaultStatus
    signalFaultStatus = False
    TrainModel_UI.signalFaultFalseButton.setStyleSheet("background-color:rgb(0, 255, 0)")
    TrainModel_UI.signalFaultTrueButton.setStyleSheet("background-color:rgb(255,255,255)")

def setTrainValues():
    trainNumber = TrainModel_UI.trainNumberInput.value()
    beacon = TrainModel_UI.beaconInput.text()
    commandedSpeed = TrainModel_UI.commandedSpeedInput.value()
    speedLimit = TrainModel_UI.speedLimitInput.value()
    actualSpeed = TrainModel_UI.actualSpeedInput.value()

    #writing values to json
    trainModel_data = {"trainNumber":trainNumber,
                       "beacon":beacon,
                       "commandedSpeed":commandedSpeed,
                       "speedLimit":speedLimit,
                       "actualSpeed":actualSpeed,
                       "engineFault":engineFaultStatus,
                       "brakeFault":brakeFaultStatus,
                       "signalFault":signalFaultStatus}
    file = open('TestValues.json', 'w')
    json.dump(trainModel_data, file)
    

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    
    TrainModelWindow = QtWidgets.QMainWindow()
    TrainModel_UI = TrainModelDisplay()
    TrainModel_UI.setupUI(TrainModelWindow)
    TrainModelWindow.show()

    engineFaultFalse()
    TrainModel_UI.engineFaultTrueButton.clicked.connect(engineFaultTrue)
    TrainModel_UI.engineFaultFalseButton.clicked.connect(engineFaultFalse)
    brakeFaultFalse()
    TrainModel_UI.brakeFaultTrueButton.clicked.connect(brakeFaultTrue)
    TrainModel_UI.brakeFaultFalseButton.clicked.connect(brakeFaultFalse)
    signalFaultFalse()
    TrainModel_UI.signalFaultTrueButton.clicked.connect(signalFaultTrue)
    TrainModel_UI.signalFaultFalseButton.clicked.connect(signalFaultFalse)

    TrainModel_UI.enterButton.clicked.connect(setTrainValues)
