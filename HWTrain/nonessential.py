import time
import RPi.GPIO as GPIO
import wiringpi

class nonessential(object):

    #---------------------- Initialization constructor, same as SW -------------------------
    def __init__(self, number, ui, model):
        self.setSpeed = 0.0
        self.temperature = 70
        self.nextStation = 'NONE'
        self.headlightStatus = False
        self.cabinlightStatus = False
        self.ldoorStatus = False
        self.rdoorStatus= False
        self.kp = 9000.0
        self.ki = 100.0
        self.faultStatus = 'NONE'
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
        self.actualSpeed = 0.0
        
        self.trainNumber = number
        self.trainModel = model
        self.displayUI = ui
        self.driverWindow()
        self.engineControlOff()
        
    # -------- train model inputs -----------------
    def getKp(self):
        return self.kp

    def getKi(self):
        return self.ki
        
    def getAnnouncement(self):
        return self.announcement
    
    def getPower(self):
        return self.power

    def getTemperature(self):
        return self.temperature

    def getHeadlightStatus(self):
        return self.headlightStatus

    def getCabinLightStatus(self):
        return self.cabinlightStatus

    def getRightDoorStatus(self):
        return self.rdoorStatus
    
    def getLeftDoorStatus(self):
        return self.rdoorStatus
    
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
        self.error = self.setSpeed - self.actualSpeed
        if self.power < self.maxPower:
            self.errSum = self.previous_errSum + (self.timeChange/2)*(self.error + self.previous_error)
        else:
            self.errSum = self.previous_errSum

        #Compute PID power output
        self.power = (self.kp * self.error) + (self.ki * self.errSum)

        #self.displayUI.powerOutput.setText(str(round(self.power,2)))
        print(self.power)

        self.startTime = self.currentTime
        self.previous_error = self.error
        self.previous_errSum = self.errSum
        
    #--------------------------- Announcement Control ------------------------
    def intercomControl(self):
        if self.engineStatus:
            self.getTrainModelInputs()
            self.announcement = "We have arrived at " + self.beaconMessage + " station."
            print(self.announcement)
            
    #----------------------------- Kp and Ki Control ---------------------------------
    def kiControl(self):
        if self.engineStatus:
            self.ki = self.engineerUI.kiInput.value()
            print(self.ki)

    def kpControl(self):
        if self.engineStatus:
            self.kp = self.engineerUI.kpInput.value()
            print(self.kp)
            
    #--------------------------- temperature --------------------------------------
    def temperatureControl(self):
        if self.engineStatus:
           #read temperature from the train model and inc/dec


    #----------------------- headlights -------------------------------------------
    def headlightControlOn(self):
        if self.engineStatus:
            self.headlightStatus = True


    def headlightControlOff(self):
        if self.engineStatus:
            self.headlightStatus = False



    #------------------------------------ cabin lights-----------------------------------
    def cabinlightControlOn(self):
        if self.engineStatus:
            self.cabinlightStatus = True

    def cabinlightControlOff(self):
        if self.engineStatus:
            self.cabinlightStatus = False



    #-------------------------------- Door Control ----------------------------
    def leftDoorControlOpen(self):
        if self.engineStatus:
            if self.actualSpeed > 0:
                return
            self.ldoorStatus = True

    def leftDoorControlClose(self):
        if self.engineStatus:
            if self.actualSpeed > 0:
                return
            self.ldoorStatus = False
            
    def rightDoorControlOpen(self):
        if self.engineStatus:
            if self.actualSpeed > 0:
                return
            self.rdoorStatus = True

    def rightDoorControlClose(self):
        if self.engineStatus:
            if self.actualSpeed > 0:
                return
            self.rdoorStatus = False
            
            
if __name__ == "__main__":
    import sys
    sys.exit(app.exec_())