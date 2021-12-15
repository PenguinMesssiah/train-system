import time
import os
import json
import csv
from PyQt5 import QtCore, QtGui, QtWidgets

class TrainController(object):

    #---------------------- Constructor where train number is assigned and variables are assigned -------------------------
    def __init__(self, number, kp, ki, ui):
        self.setSpeed = 0.0
        self.temperature = 70
        self.beacon = 'NONE'
        self.headlightStatus = False
        self.cabinlightStatus = False
        self.leftDoorStatus = False
        self.rightDoorStatus = False
        self.engineFaultStatus = False
        self.brakeFaultStatus = False
        self.signalFaultStatus = False
        self.engineStatus = True
        self.serviceBrake = False
        self.emergencyBrake = False
        self.intercom = False
        self.automaticMode = False
        self.commandedSpeed = 0.0
        self.authority = 0.0
        self.speedLimit = 0.0
        self.announcement = 'NONE'
        self.actualSpeed = 0.0
        self.suggestedSpeed = 0.0
        self.Track_Circuit_Data = False

        self.power = 0.0
        self.maxPower = 150000
        self.kp = kp
        self.ki = ki
        self.errorSum = 0.0
        self.previous_errorSum = 0.0
        self.error = 0.0
        self.previous_error = 0.0

        self.refresh_rate = 1000
        self.trainNumber = number
        self.displayUI = ui
        self.driverWindow()
        self.engineControlOff()



    #----------------------- Driver Display ----------------------------------
    def driverWindow(self):

        #Control links
        self.displayUI.setSpeedInput.valueChanged.connect(self.speedControl)
        self.displayUI.temperatureInput.valueChanged.connect(self.temperatureControl)
        self.displayUI.headlightOnButton.clicked.connect(self.headlightControlOn)
        self.displayUI.headlightOffButton.clicked.connect(self.headlightControlOff)
        self.displayUI.cabinlightOnButton.clicked.connect(self.cabinlightControlOn)
        self.displayUI.cabinlightOffButton.clicked.connect(self.cabinlightControlOff)
        self.displayUI.leftDoorOpenButton.clicked.connect(self.leftDoorControlOpen)
        self.displayUI.leftDoorCloseButton.clicked.connect(self.leftDoorControlClose)
        self.displayUI.rightDoorOpenButton.clicked.connect(self.rightDoorControlOpen)
        self.displayUI.rightDoorCloseButton.clicked.connect(self.rightDoorControlClose)
        self.displayUI.engineOnButton.clicked.connect(self.engineControlOn)
        self.displayUI.engineOffButton.clicked.connect(self.engineControlOff)
        self.displayUI.servicebrakeButton.pressed.connect(self.serviceBrakeControl)
        self.displayUI.emergencybrakeButton.pressed.connect(self.emergencyBrakeControl)
        self.displayUI.announcementButton.pressed.connect(self.intercomControl)
        self.displayUI.manualButton.pressed.connect(self.manual)
        self.displayUI.automaticButton.pressed.connect(self.automatic)

        #Timer to refresh inputs every half second
        self.timer1 = QtCore.QTimer()
        self.timer1.timeout.connect(self.getTrainModelInputs)
        self.timer1.start(self.refresh_rate)

        #Timer to refresh inputs every half second
        self.timer2 = QtCore.QTimer()
        self.timer2.timeout.connect(self.getMBOInputs)
        self.timer2.start(self.refresh_rate)

        #Timer to refresh inputs every half second
        self.timer3 = QtCore.QTimer()
        self.timer3.timeout.connect(self.checkFaults)
        self.timer3.start(self.refresh_rate)


    #------------------- Functions for Train Model to receive outputs -------------------------
    def getPower(self):
        return self.power

    def getTemperature(self):
        return self.temperature

    def getHeadlightStatus(self):
        return self.headlightStatus

    def getCabinLightStatus(self):
        return self.cabinlightStatus

    def getLeftDoorStatus(self):
        return self.leftDoorStatus

    def getRightDoorStatus(self):
        return self.rightDoorStatus

    def getEmergencyBrake(self):
        return self.emergencyBrake

    def getServiceBrake(self):
        return self.serviceBrake

    def getKp(self):
        return self.kp

    def getKi(self):
        return self.ki
        
    def getAnnouncement(self):
        return self.announcement

    def getSetSpeed(self):
        return self.setSpeed
    

    #------------------------ Get inputs from MBO ---------------------------
    def getMBOInputs(self):
        if self.engineStatus:
            path = os.getcwd()
            path = os.path.abspath(os.path.join(path, 'Test\MBO\TestValues.json'))
            file = open(path, 'r')
            data = json.load(file)

            self.authority = float(data['authority'])
            self.suggestedSpeed = float(data['suggestedSpeed'])

            self.displayUI.suggestedSpeedInput.setText(str(self.suggestedSpeed))
            
            print('inputs received from MBO')


    #------------------------ Get inputs from train model -------------------------------
    def getTrainModelInputs(self):
        if self.engineStatus:
            path = os.getcwd()
            path = os.path.abspath(os.path.join(path, 'Test\TrainModel\TestValues.json'))
            file = open(path, 'r')
            data = json.load(file)
            
            self.commandedSpeed = float(data['commandedSpeed'])
            self.speedLimit = float(data['speedLimit'])
            self.beacon = str(data['beacon'])
            self.actualSpeed = float(data['actualSpeed'])
            self.engineFaultStatus = bool(data['engineFault'])
            self.brakeFaultStatus = bool(data['brakeFault'])
            self.signalFaultStatus = bool(data['signalFault'])
            
            self.displayUI.commandedSpeedInput.setText(str(self.commandedSpeed))
            self.displayUI.actualSpeedInput.setText(str(self.actualSpeed))
            self.displayUI.beaconOutput.setText(self.beacon)
            self.displayUI.engineFaultOutput.setText(str(self.engineFaultStatus))
            self.displayUI.brakeFaultOutput.setText(str(self.brakeFaultStatus))
            self.displayUI.signalFaultOutput.setText(str(self.signalFaultStatus))

            self.calculatePower()
            
            print('inputs received from train model')


    #---------- checking for faulta -----------------------
    def checkFaults(self):
        if (self.engineFaultStatus):
                self.emergencyBrakeControl()
        if (self.brakeFaultStatus):
                self.emergencyBrakeControl()        
        if (self.signalFaultStatus):
                self.emergencyBrakeControl()

        if (self.authority == 0.0):
            self.serviceBrakeControl()
    


    #-------------------- Function to calculate Power -------------------------
    def calculatePower(self):
        self.error = self.setSpeed - self.actualSpeed

        if self.power < self.maxPower:
            self.errorSum = self.previous_errorSum + (self.refresh_rate/(2*1000))*(self.error + self.previous_error)
        else:
            self.errorSum = self.previous_errorSum

        self.power = (self.kp * self.error) + (self.ki * self.errorSum)
        self.previous_error = self.error
        self.previous_errorSum = self.errorSum

        self.displayUI.powerOutput.setText(str(round(self.power,2)))
        print("power changed to " + str(round(self.power,2)) + " watts")



    #--------------------------- Emergency Brake Control --------------------------------------------
    def emergencyBrakeControl(self):
        if self.engineStatus:
            self.emergencyBrake = True
            print("emergency brake applied")
            self.setSpeed = 0.0
            self.displayUI.setSpeedInput.setValue(self.setSpeed)
            while (self.actualSpeed > 0.0):
                self.getTrainModelInputs()
                time.sleep(self.refresh_rate/1000)
            self.emergencyBrake = False
            self.manual()
            self.calculatePower()


    #------------------------ Service Brake Control -----------------------------------
    def serviceBrakeControl(self):
        if self.engineStatus:
            self.serviceBrake = True
            print("service brake applied")
            self.setSpeed = 0.0
            self.displayUI.setSpeedInput.setValue(self.setSpeed)
            while (self.actualSpeed > 0.0):
                self.getTrainModelInputs()
                time.sleep(self.refresh_rate/1000)
            self.serviceBrake = False
            self.manual()
            self.calculatePower()

    #--------------------------- Announcement Control ------------------------
    def intercomControl(self):
        if self.engineStatus:
            self.announcement = "We have arrived at " + self.beacon + " station."
            self.displayUI.consoleOutput.setText(self.announcement)
            print(self.announcement)



    #---------------------------- Automatic/Manual Control --------------------------
    def manual(self):
        if self.engineStatus:
            self.displayUI.manualButton.setStyleSheet("background-color:rgb(0, 255, 0)")
            self.displayUI.automaticButton.setStyleSheet("background-color:rgb(255,255,255)")
            self.automaticMode = False
            print("switched to manual mode")
            self.displayUI.setSpeedInput.setReadOnly(False)
    
    def automatic(self):
        if self.engineStatus:
            self.displayUI.automaticButton.setStyleSheet("background-color:rgb(0, 255, 0)")
            self.displayUI.manualButton.setStyleSheet("background-color:rgb(255,255,255)")
            print("switched to automatic mode")
            self.displayUI.setSpeedInput.setReadOnly(True)
            if self.commandedSpeed <= self.speedLimit:
                self.setSpeed = self.commandedSpeed
            else:
                self.setSpeed = self.speedLimit
            self.displayUI.setSpeedInput.setValue(self.setSpeed)
            self.calculatePower()



    #---------------------------- Speed Control ------------------------------------
    def speedControl(self):
        if self.engineStatus:
            if self.automaticMode == False:
                self.setSpeed = self.displayUI.setSpeedInput.value()
                if self.setSpeed >= self.speedLimit:
                    self.setSpeed = self.speedLimit

                self.displayUI.setSpeedInput.setValue(self.setSpeed)
                self.calculatePower()
            print("speed changed to " + str(self.setSpeed) + " km/h")
        



    #--------------------------- Temperature Control --------------------------------------
    def temperatureControl(self):
        if self.engineStatus:
            self.temperature = self.displayUI.temperatureInput.value()
            print("temperature changed to " + str(self.temperature) + " degrees")


    #----------------------- Headlight Control -------------------------------------------
    def headlightControlOn(self):
        if self.engineStatus:
            self.displayUI.headlightOnButton.setStyleSheet("background-color:rgb(0, 255, 0)")
            self.displayUI.headlightOffButton.setStyleSheet("background-color:rgb(255,255,255)")
            self.headlightStatus = True
            print("head lights turned on")

    def headlightControlOff(self):
        if self.engineStatus:
            self.displayUI.headlightOffButton.setStyleSheet("background-color:rgb(0, 255, 0)")
            self.displayUI.headlightOnButton.setStyleSheet("background-color:rgb(255,255,255)")
            self.headlightStatus = False
            print("head lights turned off")



    #------------------------------------ Cabinlight Control -----------------------------------
    def cabinlightControlOn(self):
        if self.engineStatus:
            self.displayUI.cabinlightOnButton.setStyleSheet("background-color:rgb(0, 255, 0)")
            self.displayUI.cabinlightOffButton.setStyleSheet("background-color:rgb(255,255,255)")
            self.cabinlightStatus = True
            print("cabin lights turned on")

    def cabinlightControlOff(self):
        if self.engineStatus:
            self.displayUI.cabinlightOffButton.setStyleSheet("background-color:rgb(0, 255, 0)")
            self.displayUI.cabinlightOnButton.setStyleSheet("background-color:rgb(255,255,255)")
            self.cabinlightStatus = False
            print("cabin lights turned off")



    #-------------------------------- Door Control ----------------------------
    def leftDoorControlOpen(self):
        if self.engineStatus:
            if self.actualSpeed > 0:
                return
            self.displayUI.leftDoorOpenButton.setStyleSheet("background-color:rgb(0, 255, 0)")
            self.displayUI.leftDoorCloseButton.setStyleSheet("background-color:rgb(255,255,255)")
            self.leftDoorStatus = True
            print("left door open")

    def leftDoorControlClose(self):
        if self.engineStatus:
            if self.actualSpeed > 0:
                return
            self.displayUI.leftDoorCloseButton.setStyleSheet("background-color:rgb(0, 255, 0)")
            self.displayUI.leftDoorOpenButton.setStyleSheet("background-color:rgb(255,255,255)")
            self.leftDoorStatus = False
            print("left door close")


    def rightDoorControlOpen(self):
        if self.engineStatus:
            if self.actualSpeed > 0:
                return
            self.displayUI.rightDoorOpenButton.setStyleSheet("background-color:rgb(0, 255, 0)")
            self.displayUI.rightDoorCloseButton.setStyleSheet("background-color:rgb(255,255,255)")
            self.rightDoorStatus = True
            print("right door open")

    def rightDoorControlClose(self):
        if self.engineStatus:
            if self.actualSpeed > 0:
                return
            self.displayUI.rightDoorCloseButton.setStyleSheet("background-color:rgb(0, 255, 0)")
            self.displayUI.rightDoorOpenButton.setStyleSheet("background-color:rgb(255,255,255)")
            self.rightDoorStatus = False
            print("right door closed")

    
    #---------------------------------------- Engine control ----------------------------------------
    def engineControlOn(self):
        self.getTrainModelInputs()
        
        self.displayUI.engineOnButton.setStyleSheet("background-color:rgb(0, 255, 0)")
        self.displayUI.engineOffButton.setStyleSheet("background-color:rgb(255,255,255)")
        self.engineStatus = True
        self.automaticMode = False
        self.leftDoorControlClose()
        self.rightDoorControlClose()
        self.cabinlightControlOff()
        self.headlightControlOff()
        self.manual()

        self.displayUI.beaconOutput.setText(self.beacon)
        self.displayUI.engineFaultOutput.setText(str(self.engineFaultStatus))
        self.displayUI.brakeFaultOutput.setText(str(self.brakeFaultStatus))
        self.displayUI.signalFaultOutput.setText(str(self.signalFaultStatus))
        self.displayUI.kiInput.setText(str(self.ki))
        self.displayUI.kpInput.setText(str(self.kp))
        self.displayUI.temperatureInput.setValue(self.temperature)
        self.displayUI.setSpeedInput.setValue(self.setSpeed)
        self.displayUI.actualSpeedInput.setText(str(self.actualSpeed))
        self.displayUI.commandedSpeedInput.setText(str(self.commandedSpeed))
        self.displayUI.suggestedSpeedInput.setText(str(self.suggestedSpeed))
        self.displayUI.powerOutput.setText((str(self.power)))
        print("engine on")

    def engineControlOff(self):
        self.getTrainModelInputs()
        
        self.engineStatus = False
        self.power = 0.0
        self.errorSum = 0.0
        self.previous_errorSum = 0.0
        self.error = 0.0
        self.previous_error = 0.0
        self.setSpeed = 0.0
        
        self.displayUI.engineOffButton.setStyleSheet("background-color:rgb(0, 255, 0)")
        self.displayUI.engineOnButton.setStyleSheet("background-color:rgb(255,255,255)")
        self.displayUI.leftDoorCloseButton.setStyleSheet("background-color:rgb(255,255,255)")
        self.displayUI.leftDoorOpenButton.setStyleSheet("background-color:rgb(255,255,255)")
        self.displayUI.rightDoorCloseButton.setStyleSheet("background-color:rgb(255,255,255)")
        self.displayUI.rightDoorOpenButton.setStyleSheet("background-color:rgb(255,255,255)")
        self.displayUI.cabinlightOffButton.setStyleSheet("background-color:rgb(255,255,255)")
        self.displayUI.cabinlightOnButton.setStyleSheet("background-color:rgb(255,255,255)")
        self.displayUI.headlightOffButton.setStyleSheet("background-color:rgb(255,255,255)")
        self.displayUI.headlightOnButton.setStyleSheet("background-color:rgb(255,255,255)")
        self.displayUI.manualButton.setStyleSheet("background-color:rgb(255,255,255)")
        self.displayUI.automaticButton.setStyleSheet("background-color:rgb(255,255,255)")

        self.leftDoorControlClose()
        self.rightDoorControlClose()
        self.cabinlightControlOff()
        self.headlightControlOff()
        self.emergencyBrakeControl()
        self.manual()
        
        self.displayUI.beaconOutput.setText("")
        self.displayUI.engineFaultOutput.setText("")
        self.displayUI.brakeFaultOutput.setText("")
        self.displayUI.signalFaultOutput.setText("")
        self.displayUI.kiInput.setText("")
        self.displayUI.kpInput.setText("")
        self.displayUI.temperatureInput.setValue(0.0)
        self.displayUI.setSpeedInput.setValue(0.0)
        self.displayUI.actualSpeedInput.setText("")
        self.displayUI.commandedSpeedInput.setText("")
        self.displayUI.suggestedSpeedInput.setText("")
        self.displayUI.powerOutput.setText("")

        print("engine off")
