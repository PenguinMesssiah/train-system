import time
import RPi.GPIO as GPIO
import wiringpi

class essential(object):

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

    #----------------------- Driver Display ----------------------------------
    def driverWindow(self):   


    #------------------- Accessor functions for train model -------------------------

    def getEmergencyBrake(self):
        return self.emergencyBrake

    def getServiceBrake(self):
        return self.serviceBrake

    def getSetSpeed(self):
        return self.setSpeed


    #--------------------------- Emergency Brake Control --------------------------------------------
    def emergencyBrakeOn(self):
        if self.engineStatus:
            self.emergencyBrake = True
            
    def emergencyBrakeOff(self):
        if self.engineStatus:
            self.emergencyBrake = False


    #------------------------ Service Brake Control -----------------------------------
    def serviceBrakeOn(self):
        if self.engineStatus:
            self.serviceBrake = True
    def serviceBrakeOff(self):
        if self.engineStatus:
            self.serviceBrake = False

    #---------------------------- Automatic/Manual Control --------------------------
    def modeControl(self):
        if self.engineStatus:
            if self.automaticMode == False:
                self.automaticMode = True
                self.mode = "AUTOMATIC"
                print("Automatic mode engaged.")
                
                if self.commanded <= self.speedLimit:
                    self.setSpeed = self.commanded 
                else:
                    self.setSpeed = self.speedLimit
            else:
                self.automaticMode = False
                self.mode = "MANUAL"
                print("Manual mode engaged.")

            if self.authority == 0:
                self.serviceBrakeControl()
                print("Service brake engaged.")

    #---------------------------- Speed Control ------------------------------------
    def speedControl(self):
        if self.engineStatus:
            if self.automaticMode == False:
                if self.authority == 0:
                    self.serviceBrakeControl()
                    print("Service brake engaged.")
                if self.setSpeed >= self.commanded:
                    self.setSpeed = self.commanded
                    self.actualSpeed = self.commanded
                    print("Speed adjusted to commanded speed.")
                if self.setSpeed >= self.speedLimit:
                    self.setSpeed = self.speedLimit
                    self.actualSpeed = self.speedLimit
                    print("Above speed limit. Speed decreased.")
    
    #---------------------------------------- Engine control ----------------------------------------
    def engineControlOn(self):
        self.engineStatus = True
        self.automaticMode = False
        self.doorControlClose()
        self.cabinlightControlOff()
        self.headlightControlOff()
        print("The engine is turned on.")


    def engineControlOff(self):
        self.engineStatus = False
        self.doorStatus = False
        self.cabinlightStatus = False
        self.headlightStatus = False
        print("The engine is turned off.")
    

if __name__ == "__main__":
    import sys
    sys.exit(app.exec_())