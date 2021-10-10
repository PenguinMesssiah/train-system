import time
from DriverDisplay import Display
from TrainModelTest import TrainModel
from PyQt5 import QtCore, QtGui, QtWidgets

class TrainController(object):

    #---------------------- Constructor where train number is assigned and variables are assigned -------------------------
    def __init__(self, number, ui, model):
        self.speed = 0.0
        self.currentVelocity = 0.0
        self.temperature = 70
        self.nextStation = 'NONE'
        self.headlightStatus = False
        self.cabinlightStatus = False
        self.doorStatus = False
        self.kp = 9000.0
        self.ki = 100.0
        self.faultStatus = 'NONE'
        self.faultStatusHold = 0
        self.mode = 'AUTOMATIC'
        self.engineStatus = True
        self.serviceBrake = False
        self.emergencyBrake = False
        self.intercom = False
        self.automaticMode = False
        self.commanded = 0.0
        self.authority = 0.0
        self.speedLimit = 0.0
        self.power = 0.0
        self.startTime = time.time()
        self.beaconMessage = "NONE"
        self.announcement = "NONE"
        self.maxPower = 150000
        
        self.trainNumber = number
        self.trainModel = model
        self.displayUI = ui
        self.driverWindow()
        self.engineControlOff()



    #----------------------- Driver Display ----------------------------------
    def driverWindow(self):

        #Control links
        self.displayUI.speedInput.valueChanged.connect(self.speedControl)
        self.displayUI.temperatureInput.valueChanged.connect(self.tempControl)
        self.displayUI.headlightOnButton.clicked.connect(self.headlightControlOn)
        self.displayUI.headlightOffButton.clicked.connect(self.headlightControlOff)
        self.displayUI.cabinlightOnButton.clicked.connect(self.cabinlightControlOn)
        self.displayUI.cabinlightOffButton.clicked.connect(self.cabinlightControlOff)
        self.displayUI.doorOpenButton.clicked.connect(self.doorControlOpen)
        self.displayUI.doorCloseButton.clicked.connect(self.doorControlClose)
        self.displayUI.engineOnButton.clicked.connect(self.engineControlOn)
        self.displayUI.engineOffButton.clicked.connect(self.engineControlOff)
        self.displayUI.servicebrakeButton.pressed.connect(self.serviceBrakeControl)
        self.displayUI.emergencybrakeButton.pressed.connect(self.serviceBrakeControl)
        self.displayUI.announcementButton.pressed.connect(self.intercomControl)
        self.displayUI.automaticModeButton.pressed.connect(self.automaticControl)

        #Timer to refresh inputs every half second
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.getTrainModelInputs)
        self.timer.start(100)

        


    #------------------- Functions for Train Model to receive outputs -------------------------
    def getPower(self):
        return self.power

    def getTemperature(self):
        return self.temperature

    def getHeadlightStatus(self):
        return self.headlightStatus

    def getCabinLightStatus(self):
        return self.cabinlightStatus

    def getDoorStatus(self):
        return self.doorStatus

    def getEmergencyBrake(self):
        return self.emergencyBrake

    def getServiceBrake(self):
        return self.serviceBrake

    def getKp(self):
        return self.kp
        
    def getAnnouncement(self):
        return self.announcement

    def getSetSpeed(self):
        return self.speed
    



    #------------------------ Get inputs from train model -------------------------------
    def getTrainModelInputs(self):
        if self.engineStatus:
            self.authority = self.trainModel.getAuthority(self.trainNumber)
            self.currentVelocity = self.trainModel.getVelocity(self.trainNumber)
            self.beaconMessage = self.trainModel.getBeacon(self.trainNumber)
            self.commanded = self.trainModel.getCommanded(self.trainNumber)
            self.speedLimit = self.trainModel.getSpeedLimit(self.trainNumber)
            self.displayUI.nextstationOutput.setText(self.beaconMessage)
            self.displayUI.actualSpeed.setText(str(self.currentVelocity))
            print('inputs received from train model')

    


    #-------------------- Function to calculate Power -------------------------
    lastTime = 0.0
    timeChange = 0.0
    errSum = 0.0
    previous_errSum = 0.0
    error = 0.0
    previous_error = 0.0
    def calculatePower(self):
        #time since last calculation
        self.currentTime = time.time()
        self.timeChange = self.currentTime - self.startTime

        #Compute working error variables
        self.error = self.speed - self.currentVelocity
        if self.power < self.maxPower:
            self.errSum = self.previous_errSum + (self.timeChange/2)*(self.error + self.previous_error)
        else:
            self.errSum = self.previous_errSum

        #Compute PID power output
        self.power = (self.kp * self.error) + (self.ki * self.errSum)

        self.displayUI.powerOutput.setText(str(round(self.power,2)))

        self.startTime = self.currentTime
        self.previous_error = self.error
        self.previous_errSum = self.errSum



    #--------------------------- Emergency Brake Control --------------------------------------------
    def emergencyBrakeControl(self):
        if self.engineStatus:
            if self.emergencyBrake == False:
                self.emergencyBrake = True
            else:
                self.emergencyBrake = False
                
            while(self.emergencyBrake == True and self.speed > 0):
                self.speed = self.speed - .0001
                self.calculatePower()
                self.displayUI.speedInput.setValue(self.speed)


    #------------------------ Service Brake Control -----------------------------------
    def serviceBrakeControl(self):
        if self.engineStatus:
            if self.serviceBrake == False:
                self.serviceBrake = True
            else:
                self.serviceBrake = False
            while(self.serviceBrake == True and self.speed > 0):
                self.speed = self.speed - .0001
                self.calculatePower()
                self.displayUI.speedInput.setValue(self.speed)



    #--------------------------- Announcement Control ------------------------
    def intercomControl(self):
        if self.engineStatus:
            self.getTrainModelInputs()
            self.announcement = "We have arrived at " + self.beaconMessage + " station."
            print(self.announcement)



    #---------------------------- Automatic/Manual Control --------------------------
    def automaticControl(self):
        if self.engineStatus:
            if self.automaticMode == False:
                self.automaticMode = True
                self.mode = "AUTOMATIC"
                self.displayUI.modeOutput.setText(self.mode)
                self.displayUI.automaticModeButton.setText("SWITCH TO\nMANUAL\nMODE")
                self.displayUI.speedInput.setReadOnly(True)
                if self.commanded <= self.speedLimit:
                    self.speed = self.commanded
                    self.displayUI.speedInput.setValue(self.speed)
                    self.calculatePower()
                else:
                    self.speed = self.speedLimit
                    self.displayUI.speedInput.setValue(self.speed)
                    self.calculatePower()
            else:
                self.automaticMode = False
                self.mode = "MANUAL"
                self.displayUI.modeOutput.setText(self.mode)
                self.displayUI.automaticModeButton.setText("SWITCH TO\nAUTOMATIC\nMODE")
                self.displayUI.speedInput.setReadOnly(False)

            if self.authority == 0:
                self.serviceBrakeControl()



    #----------------------------- Kp and Ki Control ---------------------------------
    def kiControl(self):
        if self.engineStatus:
            self.ki = self.engineerUI.kiInput.value()
            print(self.ki)

    def kpControl(self):
        if self.engineStatus:
            self.kp = self.engineerUI.kpInput.value()
            print(self.kp)
        


    #---------------------------- Speed Control ------------------------------------
    def speedControl(self):
        if self.engineStatus:
            if self.automaticMode == False:
                self.speed = self.displayUI.speedInput.value()
                if self.authority == 0:
                    self.serviceBrakeControl()
                if self.speed >= self.commanded:
                    self.speed = self.commanded
                    self.displayUI.speedInput.setValue(self.speed)
                if self.speed >= self.speedLimit:
                    self.speed = self.speedLimit
                    self.displayUI.speedInput.setValue(self.speed)
            self.calculatePower()



    #--------------------------- Temperature Control --------------------------------------
    def tempControl(self):
        if self.engineStatus:
            self.temperature = self.displayUI.temperatureInput.value()


    #----------------------- Headlight Control -------------------------------------------
    def headlightControlOn(self):
        if self.engineStatus:
            self.displayUI.headlightOnButton.setStyleSheet("background-color:rgb(0, 255, 0)")
            self.displayUI.headlightOffButton.setStyleSheet("background-color:rgb(216, 216, 162)")
            self.headlightStatus = True

    def headlightControlOff(self):
        if self.engineStatus:
            self.displayUI.headlightOffButton.setStyleSheet("background-color:rgb(0, 255, 0)")
            self.displayUI.headlightOnButton.setStyleSheet("background-color:rgb(216, 216, 162)")
            self.headlightStatus = False



    #------------------------------------ Cabinlight Control -----------------------------------
    def cabinlightControlOn(self):
        if self.engineStatus:
            self.displayUI.cabinlightOnButton.setStyleSheet("background-color:rgb(0, 255, 0)")
            self.displayUI.cabinlightOffButton.setStyleSheet("background-color:rgb(216, 216, 162)")
            self.cabinlightStatus = True

    def cabinlightControlOff(self):
        if self.engineStatus:
            self.displayUI.cabinlightOffButton.setStyleSheet("background-color:rgb(0, 255, 0)")
            self.displayUI.cabinlightOnButton.setStyleSheet("background-color:rgb(216, 216, 162)")
            self.cabinlightStatus = False



    #-------------------------------- Door Control ----------------------------
    def doorControlOpen(self):
        if self.engineStatus:
            if self.currentVelocity > 0:
                return
            self.displayUI.doorOpenButton.setStyleSheet("background-color:rgb(0, 255, 0)")
            self.displayUI.doorCloseButton.setStyleSheet("background-color:rgb(216, 216, 162)")
            self.doorStatus = True

    def doorControlClose(self):
        if self.engineStatus:
            if self.currentVelocity > 0:
                return
            self.displayUI.doorCloseButton.setStyleSheet("background-color:rgb(0, 255, 0)")
            self.displayUI.doorOpenButton.setStyleSheet("background-color:rgb(216, 216, 162)")
            self.doorStatus = False

    
    #---------------------------------------- Engine control ----------------------------------------
    def engineControlOn(self):
        self.displayUI.engineOnButton.setStyleSheet("background-color:rgb(0, 255, 0)")
        self.displayUI.engineOffButton.setStyleSheet("background-color:rgb(216, 216, 162)")
        self.engineStatus = True
        self.displayUI.automaticModeButton.setText("SWITCH TO\nAUTOMATIC\nMODE")
        self.automaticMode = False
        self.doorControlClose()
        self.cabinlightControlOff()
        self.headlightControlOff()
        
        self.displayUI.nextstationOutput.setText(self.nextStation)
        self.displayUI.faultStatusOutput.setText(self.faultStatus)
        self.displayUI.modeOutput.setText("MANUAL")
        self.displayUI.kiInput.setText(str(self.ki))
        self.displayUI.kpInput.setText(str(self.kp))
        self.displayUI.temperatureInput.setValue(self.temperature)

    def engineControlOff(self):
        self.displayUI.engineOffButton.setStyleSheet("background-color:rgb(0, 255, 0)")
        self.displayUI.engineOnButton.setStyleSheet("background-color:rgb(216, 216, 162)")
        self.engineStatus = False
        self.displayUI.doorCloseButton.setStyleSheet("background-color:rgb(216, 216, 162)")
        self.displayUI.doorOpenButton.setStyleSheet("background-color:rgb(216, 216, 162)")
        self.doorStatus = False
        self.displayUI.cabinlightOffButton.setStyleSheet("background-color:rgb(216, 216, 162)")
        self.displayUI.cabinlightOnButton.setStyleSheet("background-color:rgb(216, 216, 162)")
        self.cabinlightStatus = False
        self.displayUI.headlightOffButton.setStyleSheet("background-color:rgb(216, 216, 162)")
        self.displayUI.headlightOnButton.setStyleSheet("background-color:rgb(216, 216, 162)")
        self.headlightStatus = False
        
        self.displayUI.nextstationOutput.setText("")
        self.displayUI.faultStatusOutput.setText("")
        self.displayUI.modeOutput.setText("")
        self.displayUI.kiInput.setText("")
        self.displayUI.kpInput.setText("")
        self.displayUI.temperatureInput.setValue(0.0)
        self.displayUI.speedInput.setValue(0.0)
        self.displayUI.powerOutput.setText("")
        self.displayUI.actualSpeed.setText("")



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    DisplayWindow = QtWidgets.QMainWindow()
    
    train1_UI = Display()
    train1_UI.setupUI(DisplayWindow)
    DisplayWindow.show()

    train1_model = TrainModel()
    train = TrainController(1, train1_UI, train1_model)
    
    sys.exit(app.exec_())





















    
