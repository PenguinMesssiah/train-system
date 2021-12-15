import time
import sys
import string
#temp from Controller.TrainController import TrainController
#temp from UI.Driver import DriverDisplay
#temp from UI.Engineer import EngineerDisplay
from PyQt5 import QtCore, QtGui, QtWidgets

sys.path.append("..")

from Shared.connections import *
from Shared.common import *

def send_sw_inputs(): #This links the values entered by the train driver to the SW module.
    link.HWTrainSendsKpTo.emit(Kp);
    link.HWTrainSendsKiTo.emit(Ki);
    
    link.HWTrainSendsTempTo.emit(tempStatus);
    link.HWTrainSendsEngineTo.emit(engineStatus);
    link.HWTrainSendsAnnounceTo.emit(announceStatus);
    
    link.HWTrainSendsRDoorTo.emit(rdoorsOpen);
    link.HWTrainSendsLDoorTo.emit(ldoorsOpen);
    
    link.HWTrainSendsIncSpeedTo.emit(incSpeed);
    link.HWTrainSendsDecSpeedTo.emit(decSpeed);
    
    link.HWTrainSendsCabinLightsTo.emit(cabinlightsOn);
    link.HWTrainSendsHeadLightsTo.emit(headlightsOn);
    
    link.HWTrainSendsAutoModeTo.emit(autoMode);
    link.HWTrainSendsManModeTo.emit(manMode);
    
    link.HWTrainSendsEmergBrakeTo.emit(emergBrake);
    link.HWTrainSendsServBrakeTo.emit(servBrake);
    
def setTrainValues():
    #Gather kp and ki input from Engineer
    print("Welcome Engineer!")
    kp = float(input("Enter kp value: "))
    ki = float(input("Enter ki value: "))
    print("Kp is", kp, "and ki is", ki, ".")
    start(kp, ki)

def start(kp, ki): #Start 1 train at a time. Function can only run a single train on hardware.
    print("Welcome Train Driver!")
    engineStatus = input("Turn engine on? (y/n)")
    #Run RPi display
    if engineStatus == "y":
        print("Engine on.")
        func=input("What would you like to do? (temp/announce/doors/lights/speed/mode/emergbrake/servbrake) ")
        if func=="temp":
            tempStatus=input("Increase or decrease temp? (up/down)")
            if tempStatus=="up":
                incTemp=True
                print("Temperature increased.")
            elif tempStatus=="down":
                decTemp=True;
                print("Temperature decreased.")
            start(kp,ki)
        if func=="announce":
            announceStatus=True
            print("Announcement made.")
            start(kp,ki)
        if func=="doors":
            doorStatus=input("Right doors or left doors?(r/l)")
            if doorStatus=="r":
                openStatus=input("Open or close?(o/c)")
                if openStatus=="o":
                    rdoorsOpen=True;
                    print("Right doors opened.")
                if openStatus=="c":
                    rdoorsOpen=False;
                    print("Right doors closed.")
            if doorStatus=="l":
                openStatus=input("Open or close?(o/c)")
                if openStatus=="o":
                    ldoorsOpen=True;
                    print("Left doors opened.")
                if openStatus=="c":
                    ldoorsOpen=False;
                    print("Left doors closed.")
            start(kp,ki)
        if func=="lights":
            lightStatus=input("Cabin lights or headlights?(c/h)")
            if lightStatus=="c":
                onStatus=input("On or off?(on/off)")
                if onStatus=="on":
                    cabinlightsOn=True;
                    print("Cabin lights on.")
                if onStatus=="off":
                    cabinlightsOn=False;
                    print("Cabin lights off.")
            if lightStatus=="h":
                onStatus=input("On or off?(on/off)")
                if onStatus=="on":
                    headlightsOn=True;
                    print("Headlights on.")
                if onStatus=="off":
                    headlightsOn=False;
                    print("Headlights off.")
            start(kp,ki)
        if func=="speed":
            speedStatus=input("Increase or decrease speed? (up/down")
            if speedStatus=="up":
                incSpeed=True;
                print("Speed increased by 5 mph.")
            if speedStatus=="down":
                decSpeed=True;
                print("Speed decreased by 5 mph.")
            start(kp,ki)
        if func=="mode":
            modeStatus=input("Automatic or manual?(a/m)")
            if modeStatus=="a":
                autoMode=True;
                print("Automatic mode ON.")
            if modeStatus=="m":
                manMode=True;
                print("Manual mode ON.")
            start(kp,ki)
        if func=="emergbrake":
            emergBrake=True;
            print("Emergency brake engaged.")
            start(kp,ki)
        if func=="servbrake":
            servBrake=True;
            print("Service brake engaged.")
            start(kp,ki)
        if func=="quit":
            sys.exit(app.exec_())
    if engineStatus == "n":
        print("Please turn on engine to start train.")
        start(kp,ki)

if __name__ == "__main__":
    import sys
    setTrainValues()
    send_sw_inputs() #send values over to Klaus