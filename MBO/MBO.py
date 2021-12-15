import time
from PlannerDisplay import Display
from TestUI import TestDisplay
from TrainControllerTest import TrainController
from PyQt5 import QtCore, QtGui, QtWidgets
from TrainDriver import Driver
from TrainClass import Train
from BlueLineSet import BlueLine
from PathSet import Path
from GreenLine import GreenLine
from RedLine import RedLine
import math
import csv
import sys

sys.path.append("..")

from Shared.connections import *
from Shared.common      import *

class MBO(object):


    def __init__(self, train, testyUI, ui):

        self.trainSel = 0
        self.changed = 0
        self.trainSets = [train]
        self.driverSets = []
        self.driverCount = 0
        self.authority = 0
        self.suggestedSpeed = 0.0
        self.throughArray = [2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000]
        self.startTime = 0.00
        self.hourSelect = 0
        self.hourN = 0.00
        self.interval = 1.00
        self.trainsNeeded = 1
        self.tempName = "John Smith"
        self.tempDateArray = [1, 1, 1, 1, 1, 1, 1]
        self.tempActive = 1
        self.tempIndex = 0
        self.driverBool = 0
        self.enterDriverBool = 0
      

        link.train_model_send_gps_velocity_mbo.connect(self.receive_train_inputs)

        self.displayTestUI = testyUI
        self.testWindow()
        self.displayMainUI = ui
        self.showWindow()
        self.addDefaultDrivers()
        
    def testWindow(self):

        #Controls activated[str].connect(self.onChanged
        self.displayTestUI.trainSelector.valueChanged.connect(self.updateTrainSel)
        self.displayTestUI.positionInput.valueChanged.connect(self.updatePosition)
        self.displayTestUI.blockInput.valueChanged.connect(self.updateBlock)
        self.displayTestUI.speedInput.valueChanged.connect(self.updateSpeed)
        self.displayTestUI.destInput.valueChanged.connect(self.updateDest)
       #-- self.displayTestUI.authButton.pressed.connect(self.calculateAuthority)
        
     

        #--self.timer = QtCore.QTimer()
        #--self.timer.timeout.connect(
        #--self.timer.start(100)


    def showWindow(self):

        print("window")
        self.displayMainUI.timeSelector.valueChanged.connect(self.changeStartTime)
       ## self.displayMainUI.thimeSelector.valueChanged.connect(self.changeHourSelect)
        self.displayMainUI.throSelector.valueChanged.connect(self.changeThroughput)
        self.displayMainUI.addDriverButton.pressed.connect(self.makeNewDriver)
        self.displayMainUI.submitNameButton.pressed.connect(self.changeName)
        self.displayMainUI.enterDatesButton.pressed.connect(self.changeDates)
        self.displayMainUI.enterDriverDataButton.pressed.connect(self.addNewDriver)
        self.displayMainUI.setActiveButton.pressed.connect(self.toggleStatus)
        #--self.updateMain()
        
    def updateTrainSel(self):
        
       self.trainSel = self.displayTestUI.trainSelector.value() - 1
       
       print(self.trainSel)
            


    def updatePosition(self):

        self.trainSets[self.trainSel].setPosition(self.displayTestUI.positionInput.value())
        self.authority = self.trainSets[self.trainSel].getAuthority()
        self.displayTestUI.authorityOutput.setText(str(self.authority))
        print(self.trainSets[self.trainSel].getPosition())
        #--self.displayUI.posOutput1.setText(str(self.trainSets[self.trainSel].getPosition()))
        
    def updateBlock(self):

        self.trainSets[self.trainSel].setBlock(self.displayTestUI.blockInput.value())
        self.authority = self.trainSets[self.trainSel].getAuthority()
        self.displayTestUI.authorityOutput.setText(str(self.authority))
        print(self.trainSets[self.trainSel].getBlock())
       #-- self.displayTestUI.authorityOutput.setText(str(self.trainSets[self.trainSel].authority))
        self.suggestedSpeed = self.trainSets[self.trainSel].getSuggestedSpeed()
        self.displayTestUI.speedOutput.setText(str(self.suggestedSpeed))

    def updateSpeed(self):

        self.trainSets[self.trainSel].setCurrentSpeed(self.displayTestUI.speedInput.value())
        self.authority = self.trainSets[self.trainSel].getAuthority()
        self.displayTestUI.authorityOutput.setText(str(self.authority))
       #-- self.displayTestUI.authorityOutput.setText(str(self.trainSets[self.trainSel].authority))
        print(self.trainSets[self.trainSel].getCurrentSpeed())

    def updateDest(self):

        self.trainSets[self.trainSel].setDBlock(self.displayTestUI.destInput.value())
        self.authority = self.trainSets[self.trainSel].getAuthority()
        self.displayTestUI.authorityOutput.setText(str(self.authority))
        #--self.displayTestUI.authorityOutput.setText(str(self.trainSets[self.trainSel].authority))
        print(self.trainSets[self.trainSel].getDBlock())


##    def updateMain(self):
##
##        self.displayUI.trainNameOutput1.setText(str(self.trainSets[0].driverTrain.getName()))

    def addTrain(self,train):
        self.trainSets.append(train)


    def changeHourSelect(self):
        self.hourSelect = self.displayMainUI.thimeSelector.value()
        print("Hour toggled is: ", int(self.hourSelect), ":00")
        
##    def changeThroughput(self):
##        self.throughArray[self.hourSelect] = self.displayMainUI.throSelector.value()
##        print("New Throughput for hour", int(self.hourSelect), "is: ", int(self.throughArray[self.hourSelect]), "tickets/hr")

    def changeStartTime(self):
        self.startTime = self.displayMainUI.timeSelector.value()
        print("New Start Time is: ", int(self.startTime), ":00 ")
        ## self.makeScheduleGreen()

    def changeThroughput(self):
        self.throughput = self.displayMainUI.throSelector.value()
        print("The new throughput is: ", int(self.throughput)," tickets/hr")

    def makeNewDriver(self):
        if self.driverBool == 0:
            self.driverBool = 1
            self.tempName = "Josh Smith"
            self.displayMainUI.addDriverButton.setText("ADDING DRIVER")
            self.displayMainUI.addDriverButton.setStyleSheet("background-color:rgb(0, 255, 0)")
            for k in range(0,7):
                self.tempDateArray[k] = 1
            self.tempActive = 1
            print("Im in if and The current driver bool is: ", int(self.driverBool))
        else:
            print("Im in else and The current driver bool is: ", int(self.driverBool))


    def changeName(self):
        self.tempName = self.displayMainUI.textbox1.text()
        print("The inputted name is: ", self.tempName)
        self.displayMainUI.submitNameButton.setStyleSheet("background-color:rgb(0, 255, 0)")

    def changeDates(self):
        if self.displayMainUI.sunCheck.isChecked() == True:
            self.tempDateArray[0] = 1
        else:
            self.tempDateArray[0] = 0
            
        if self.displayMainUI.monCheck.isChecked() == True:
            self.tempDateArray[1] = 1
        else:
            self.tempDateArray[1] = 0
            
        if self.displayMainUI.tuesCheck.isChecked() == True:
            self.tempDateArray[2] = 1
        else:
            self.tempDateArray[2] = 0
            
        if self.displayMainUI.wedCheck.isChecked() == True:
            self.tempDateArray[3] = 1
        else:
            self.tempDateArray[3] = 0
            
        if self.displayMainUI.thursCheck.isChecked() == True:
            self.tempDateArray[4] = 1
        else:
            self.tempDateArray[4] = 0

        if self.displayMainUI.friCheck.isChecked() == True:
            self.tempDateArray[5] = 1
        else:
            self.tempDateArray[5] = 0

        if self.displayMainUI.satCheck.isChecked() == True:
            self.tempDateArray[6] = 1
        else:
            self.tempDateArray[6] = 0

        self.displayMainUI.enterDatesButton.setStyleSheet("background-color:rgb(0, 255, 0)")

        
        for k in range(0,7):
            print("The status for date: ", int(k), " is: ", self.tempDateArray[k], "\n")

    def addDefaultDrivers(self):
        self.driverSets.append(Driver("Roger Smith",1,1,1,1,1,1,1,0))
        self.displayMainUI.cb.addItem(self.driverSets[self.driverCount].getName())
        self.driverCount = self.driverCount + 1
        self.driverSets.append(Driver("David Johnson",1,1,1,1,1,1,1,1))
        self.displayMainUI.cb.addItem(self.driverSets[self.driverCount].getName())
        self.driverCount = self.driverCount + 1
        self.driverSets.append(Driver("Peter Davis",1,1,1,1,1,1,1,2))
        self.displayMainUI.cb.addItem(self.driverSets[self.driverCount].getName())
        self.driverCount = self.driverCount + 1
        self.driverSets.append(Driver("Joseph Clark",1,1,1,1,1,1,1,3))
        self.displayMainUI.cb.addItem(self.driverSets[self.driverCount].getName())
        self.driverCount = self.driverCount + 1
        self.driverSets.append(Driver("Joseph Clark",1,1,1,1,1,1,1,3))
        self.displayMainUI.cb.addItem(self.driverSets[self.driverCount].getName())
        self.driverCount = self.driverCount + 1
        self.driverSets.append(Driver("Joseph Clark",1,1,1,1,1,1,1,3))
        self.displayMainUI.cb.addItem(self.driverSets[self.driverCount].getName())
        self.driverCount = self.driverCount + 1
        self.driverSets.append(Driver("Joseph Clark",1,1,1,1,1,1,1,3))
        self.displayMainUI.cb.addItem(self.driverSets[self.driverCount].getName())
        self.driverCount = self.driverCount + 1

    def addNewDriver(self):
        if self.driverBool == 1:
            
            self.driverSets.append(Driver(self.tempName, self.tempDateArray[0], self.tempDateArray[1], self.tempDateArray[2], self.tempDateArray[3], self.tempDateArray[4], self.tempDateArray[5], self.tempDateArray[6], self.driverCount))
            self.displayMainUI.cb.addItem(self.driverSets[self.driverCount].getName())
            print("The driver's ID number is: ", self.driverSets[self.driverCount].getIDNumber(),"\n")
            print("The driver's name is: ", self.driverSets[self.driverCount].getName(),"\n")
            self.driverCount = self.driverCount + 1
            print("The new number of drivers is: ", self.driverCount, "\n")
            self.driverBool = 0
            self.displayMainUI.addDriverButton.setText("Add Driver")
            self.displayMainUI.addDriverButton.setStyleSheet("background-color:rgb(255, 0, 0)")
            self.displayMainUI.submitNameButton.setStyleSheet("background-color:rgb(255, 0, 0)")
            self.displayMainUI.enterDatesButton.setStyleSheet("background-color:rgb(255, 0, 0)")


        else:
            print("Not in add mode\n")
            
    def toggleStatus(self):
        if self.driverCount > 0:
            self.tempIndex = self.displayMainUI.cb.currentIndex()
        if self.driverSets[self.tempIndex].getStatus() == True:
            self.driverSets[self.tempIndex].deactivateDriver()
        else:
            self.driverSets[self.tempIndex].activateDriver()

        print("The driver,", self.driverSets[self.tempIndex].getName(),"'s status is now: ",self.driverSets[self.tempIndex].getStatus(), "\n")
        
        
##    def howManyTrains(self,index):
##        if self.throughArray[index] > 6600:
##            self.trainsNeeded = 2
##        else
##            self.trainsNeeded = 1


#-- variables to make the schedule
    
    def makeShiftGreen(self, startTH, startTS, startTM, trainNum):
        
        timeNowS = startTH*60*60 + startTM*60 + startTS
        nextTime = 0.0
        nextTimeS = 0.0
        hourT = 0
        hourTN = 0
        minuteTN = 0.0
        minuteT = 0.0
        secondTN = 0.0
        secondT = 0.0
        timeTemp = 0.0
        hourString = ""
        minuteString = ""
        secondString = ""
        timeString = ""
        hourString2 = ""
        minuteString2 = ""
        secondString2 = ""
        timeString2 = ""
        green = GreenLine()
        nextTimeS = timeNowS + 30
        ##print(nextTimeS)
        hourT = math.floor(nextTimeS/3600)
        minuteT = (math.floor((nextTimeS-hourT*3600)/60))
        ##print(minuteT)
        ##minuteT = minuteT/100
        secondT = (nextTimeS - hourT*3600 - minuteT*60)
        hourTN = math.floor(timeNowS/3600)
        minuteTN = math.floor((timeNowS-hourTN*3600)/60)
        secondTN = (timeNowS - hourTN*3600 - minuteTN*60)
        hourString = str(hourT)
        minuteString = str(minuteT)
        secondString = str(secondT)
        timeString = hourString + ":" + minuteString + ":" + secondString + " UTC"
        hourString2 = str(hourTN)
        minuteString2 = str(minuteTN)
        secondString2 = str(secondTN)
        timeString2 = hourString2 + ":" + minuteString2 + ":" + secondString2 + " UTC"
        tempPath = Path(timeString2, timeString,  green.getCurrentStation(), "The Yard")
        self.trainSets[trainNum].addPath(tempPath)
        timeNowS = nextTimeS + 30
        for z in range(0,6):
            for y in range(0,21):
                timeTemp = green.getTime()
                nextTimeS = timeNowS + timeTemp
                ##print(nextTimeS)
                hourT = math.floor(nextTimeS/3600)
                minuteT = (math.floor((nextTimeS-hourT*3600)/60))
                ##print(minuteT)
                ##minuteT = minuteT/100
                secondT = (nextTimeS - hourT*3600 - minuteT*60)
                hourTN = math.floor(timeNowS/3600)
                minuteTN = math.floor((timeNowS-hourTN*3600)/60)
                secondTN = (timeNowS - hourTN*3600 - minuteTN*60)
                ##minuteTN = minuteTN/100
                hourString = str(hourT)
                minuteString = str(minuteT)
                secondString = str(secondT)
                timeString = hourString + ":" + minuteString + ":" + secondString + " UTC"
                hourString2 = str(hourTN)
                minuteString2 = str(minuteTN)
                secondString2 = str(secondTN)
                timeString2 = hourString2 + ":" + minuteString2 + ":" + secondString2 + " UTC"
                tempPath = Path(timeString2, timeString, green.getNextStation(), green.getCurrentStation())
                self.trainSets[trainNum].addPath(tempPath)
                green.incrementIndex()
                if green.stationIndex == 17:
                    if z == 5:
                        break
                timeNowS = nextTimeS + 30
                
        timeNowS = nextTimeS + 30        
        nextTimeS = timeNowS + 120
        ##print(nextTimeS)
        hourT = math.floor(nextTimeS/3600)
        minuteT = (math.floor((nextTimeS-hourT*3600)/60))
        ##print(minuteT)
        ##minuteT = minuteT/100
        secondT = (nextTimeS - hourT*3600 - minuteT*60)
        hourTN = math.floor(timeNowS/3600)
        minuteTN = math.floor((timeNowS-hourTN*3600)/60)
        secondTN = (timeNowS - hourTN*3600 - minuteTN*60)
        hourString = str(hourT)
        minuteString = str(minuteT)
        secondString = str(secondT)
        timeString = hourString + ":" + minuteString + ":" + secondString + " UTC"
        hourString2 = str(hourTN)
        minuteString2 = str(minuteTN)
        secondString2 = str(secondTN)
        timeString2 = hourString2 + ":" + minuteString2 + ":" + secondString2 + " UTC"
        # green.setStationIndex(0)
        tempPath = Path(timeString2, timeString, "The Yard", green.getCurrentStation())
        self.trainSets[trainNum].addPath(tempPath)
        timeNowS = nextTimeS
               
        timeNowS = timeNowS + 30*60

        nextTimeS = timeNowS + 30
        ##print(nextTimeS)
        hourT = math.floor(nextTimeS/3600)
        minuteT = (math.floor((nextTimeS-hourT*3600)/60))
        ##print(minuteT)
        ##minuteT = minuteT/100
        secondT = (nextTimeS - hourT*3600 - minuteT*60)
        hourTN = math.floor(timeNowS/3600)
        minuteTN = math.floor((timeNowS-hourTN*3600)/60)
        secondTN = (timeNowS - hourTN*3600 - minuteTN*60)
        hourString = str(hourT)
        minuteString = str(minuteT)
        secondString = str(secondT)
        timeString = hourString + ":" + minuteString + ":" + secondString + " UTC"
        hourString2 = str(hourTN)
        minuteString2 = str(minuteTN)
        secondString2 = str(secondTN)
        timeString2 = hourString2 + ":" + minuteString2 + ":" + secondString2 + " UTC"
        green.setStationIndex(0)
        tempPath = Path(timeString2, timeString, green.getCurrentStation(),"The Yard")
        
        self.trainSets[trainNum].addPath(tempPath)
        green.setStationIndex(0)
        timeNowS = nextTimeS + 30
        for a in range(0,6):
            for b in range(0,21):
                timeTemp = green.getTime()
                nextTimeS = timeNowS + timeTemp
                ##print(nextTimeS)
                hourT = math.floor(nextTimeS/3600)
                minuteT = (math.floor((nextTimeS-hourT*3600)/60))
                ##print(minuteT)
                ##minuteT = minuteT/100
                secondT = (nextTimeS - hourT*3600 - minuteT*60)
                hourTN = math.floor(timeNowS/3600)
                minuteTN = math.floor((timeNowS-hourTN*3600)/60)
                secondTN = (timeNowS - hourTN*3600 - minuteTN*60)
                ##minuteTN = minuteTN/100
                hourString = str(hourT)
                minuteString = str(minuteT)
                secondString = str(secondT)
                timeString = hourString + ":" + minuteString + ":" + secondString + " UTC"
                hourString2 = str(hourTN)
                minuteString2 = str(minuteTN)
                secondString2 = str(secondTN)
                timeString2 = hourString2 + ":" + minuteString2 + ":" + secondString2 + " UTC"
                tempPath = Path(timeString2, timeString,  green.getNextStation(),green.getCurrentStation())
                self.trainSets[trainNum].addPath(tempPath)
                green.incrementIndex()
                if green.stationIndex == 17:
                    if a == 5:
                        break
                timeNowS = nextTimeS+30
        #self.trainSets[trainNum].displayTrainsRouteList()
        timeNowS = nextTimeS + 30        
        nextTimeS = timeNowS + 120
        ##print(nextTimeS)
        hourT = math.floor(nextTimeS/3600)
        minuteT = (math.floor((nextTimeS-hourT*3600)/60))
        ##print(minuteT)
        ##minuteT = minuteT/100
        secondT = (nextTimeS - hourT*3600 - minuteT*60)
        hourTN = math.floor(timeNowS/3600)
        minuteTN = math.floor((timeNowS-hourTN*3600)/60)
        secondTN = (timeNowS - hourTN*3600 - minuteTN*60)
        hourString = str(hourT)
        minuteString = str(minuteT)
        secondString = str(secondT)
        timeString = hourString + ":" + minuteString + ":" + secondString + " UTC"
        hourString2 = str(hourTN)
        minuteString2 = str(minuteTN)
        secondString2 = str(secondTN)
        timeString2 = hourString2 + ":" + minuteString2 + ":" + secondString2 + " UTC"
        # green.setStationIndex(0)
        tempPath = Path(timeString2, timeString, "The Yard", green.getCurrentStation())
        self.trainSets[trainNum].addPath(tempPath)

    def makeScheduleGreen(self):
        
        self.makeShiftGreen(self.startTime, 0, 0, 0)
        #self.makeShiftGreen(self.startTime, 0, 15, 1)
        
       # self.makeShiftGreen(self.startTime + 9, 0, 0, 4)
##        self.makeShiftGreen(self.startTime + 9, 0, 15, 5)
##        self.makeShiftGreen(self.startTime + 9, 0, 30, 6)
##        self.makeShiftGreen(self.startTime + 9, 0, 45, 7)
        
##        self.makeShiftGreen(self.startTime + 18, 0, 0, 8)
##        self.makeShiftGreen(self.startTime + 18, 0, 15, 9)
##        self.makeShiftGreen(self.startTime + 18, 0, 30, 10)
##        self.makeShiftGreen(self.startTime + 18, 0, 45, 11)

        self.makeCSV()
        
    def makeShiftRed(self, startTH, startTS, startTM, trainNum):
        
        timeNowS = startTH*60*60 + startTM*60 + startTS
        nextTime = 0.0
        nextTimeS = 0.0
        hourT = 0
        hourTN = 0
        minuteTN = 0.0
        minuteT = 0.0
        secondTN = 0.0
        secondT = 0.0
        timeTemp = 0.0
        hourString = ""
        minuteString = ""
        secondString = ""
        timeString = ""
        hourString2 = ""
        minuteString2 = ""
        secondString2 = ""
        timeString2 = ""
        red = RedLine()
        nextTimeS = timeNowS + 30
        ##print(nextTimeS)
        hourT = math.floor(nextTimeS/3600)
        minuteT = (math.floor((nextTimeS-hourT*3600)/60))
        ##print(minuteT)
        ##minuteT = minuteT/100
        secondT = (nextTimeS - hourT*3600 - minuteT*60)
        hourTN = math.floor(timeNowS/3600)
        minuteTN = math.floor((timeNowS-hourTN*3600)/60)
        secondTN = (timeNowS - hourTN*3600 - minuteTN*60)
        hourString = str(hourT)
        minuteString = str(minuteT)
        secondString = str(secondT)
        timeString = hourString + ":" + minuteString + ":" + secondString + " UTC"
        hourString2 = str(hourTN)
        minuteString2 = str(minuteTN)
        secondString2 = str(secondTN)
        timeString2 = hourString2 + ":" + minuteString2 + ":" + secondString2 + " UTC"
        tempPath = Path(timeString2, timeString,  green.getCurrentStation(), "The Yard")
        self.trainSets[trainNum].addPath(tempPath)
        timeNowS = nextTimeS + 30
        for z in range(0,6):
            for y in range(0,21):
                timeTemp = green.getTime()
                nextTimeS = timeNowS + timeTemp
                ##print(nextTimeS)
                hourT = math.floor(nextTimeS/3600)
                minuteT = (math.floor((nextTimeS-hourT*3600)/60))
                ##print(minuteT)
                ##minuteT = minuteT/100
                secondT = (nextTimeS - hourT*3600 - minuteT*60)
                hourTN = math.floor(timeNowS/3600)
                minuteTN = math.floor((timeNowS-hourTN*3600)/60)
                secondTN = (timeNowS - hourTN*3600 - minuteTN*60)
                ##minuteTN = minuteTN/100
                hourString = str(hourT)
                minuteString = str(minuteT)
                secondString = str(secondT)
                timeString = hourString + ":" + minuteString + ":" + secondString + " UTC"
                hourString2 = str(hourTN)
                minuteString2 = str(minuteTN)
                secondString2 = str(secondTN)
                timeString2 = hourString2 + ":" + minuteString2 + ":" + secondString2 + " UTC"
                tempPath = Path(timeString2, timeString, green.getNextStation(), green.getCurrentStation())
                self.trainSets[trainNum].addPath(tempPath)
                green.incrementIndex()
                if green.stationIndex == 17:
                    if z == 5:
                        break
                timeNowS = nextTimeS + 30
                
        timeNowS = nextTimeS + 30        
        nextTimeS = timeNowS + 120
        ##print(nextTimeS)
        hourT = math.floor(nextTimeS/3600)
        minuteT = (math.floor((nextTimeS-hourT*3600)/60))
        ##print(minuteT)
        ##minuteT = minuteT/100
        secondT = (nextTimeS - hourT*3600 - minuteT*60)
        hourTN = math.floor(timeNowS/3600)
        minuteTN = math.floor((timeNowS-hourTN*3600)/60)
        secondTN = (timeNowS - hourTN*3600 - minuteTN*60)
        hourString = str(hourT)
        minuteString = str(minuteT)
        secondString = str(secondT)
        timeString = hourString + ":" + minuteString + ":" + secondString + " UTC"
        hourString2 = str(hourTN)
        minuteString2 = str(minuteTN)
        secondString2 = str(secondTN)
        timeString2 = hourString2 + ":" + minuteString2 + ":" + secondString2 + " UTC"
        # green.setStationIndex(0)
        tempPath = Path(timeString2, timeString, "The Yard", green.getCurrentStation())
        self.trainSets[trainNum].addPath(tempPath)
        timeNowS = nextTimeS
               
        timeNowS = timeNowS + 30*60

        nextTimeS = timeNowS + 30
        ##print(nextTimeS)
        hourT = math.floor(nextTimeS/3600)
        minuteT = (math.floor((nextTimeS-hourT*3600)/60))
        ##print(minuteT)
        ##minuteT = minuteT/100
        secondT = (nextTimeS - hourT*3600 - minuteT*60)
        hourTN = math.floor(timeNowS/3600)
        minuteTN = math.floor((timeNowS-hourTN*3600)/60)
        secondTN = (timeNowS - hourTN*3600 - minuteTN*60)
        hourString = str(hourT)
        minuteString = str(minuteT)
        secondString = str(secondT)
        timeString = hourString + ":" + minuteString + ":" + secondString + " UTC"
        hourString2 = str(hourTN)
        minuteString2 = str(minuteTN)
        secondString2 = str(secondTN)
        timeString2 = hourString2 + ":" + minuteString2 + ":" + secondString2 + " UTC"
        green.setStationIndex(0)
        tempPath = Path(timeString2, timeString, green.getCurrentStation(),"The Yard")
        
        self.trainSets[trainNum].addPath(tempPath)
        green.setStationIndex(0)
        timeNowS = nextTimeS + 30
        for a in range(0,6):
            for b in range(0,21):
                timeTemp = green.getTime()
                nextTimeS = timeNowS + timeTemp
                ##print(nextTimeS)
                hourT = math.floor(nextTimeS/3600)
                minuteT = (math.floor((nextTimeS-hourT*3600)/60))
                ##print(minuteT)
                ##minuteT = minuteT/100
                secondT = (nextTimeS - hourT*3600 - minuteT*60)
                hourTN = math.floor(timeNowS/3600)
                minuteTN = math.floor((timeNowS-hourTN*3600)/60)
                secondTN = (timeNowS - hourTN*3600 - minuteTN*60)
                ##minuteTN = minuteTN/100
                hourString = str(hourT)
                minuteString = str(minuteT)
                secondString = str(secondT)
                timeString = hourString + ":" + minuteString + ":" + secondString + " UTC"
                hourString2 = str(hourTN)
                minuteString2 = str(minuteTN)
                secondString2 = str(secondTN)
                timeString2 = hourString2 + ":" + minuteString2 + ":" + secondString2 + " UTC"
                tempPath = Path(timeString2, timeString,  green.getNextStation(),green.getCurrentStation())
                self.trainSets[trainNum].addPath(tempPath)
                green.incrementIndex()
                if green.stationIndex == 17:
                    if a == 5:
                        break
                timeNowS = nextTimeS+30
        #self.trainSets[trainNum].displayTrainsRouteList()
        timeNowS = nextTimeS + 30        
        nextTimeS = timeNowS + 120
        ##print(nextTimeS)
        hourT = math.floor(nextTimeS/3600)
        minuteT = (math.floor((nextTimeS-hourT*3600)/60))
        ##print(minuteT)
        ##minuteT = minuteT/100
        secondT = (nextTimeS - hourT*3600 - minuteT*60)
        hourTN = math.floor(timeNowS/3600)
        minuteTN = math.floor((timeNowS-hourTN*3600)/60)
        secondTN = (timeNowS - hourTN*3600 - minuteTN*60)
        hourString = str(hourT)
        minuteString = str(minuteT)
        secondString = str(secondT)
        timeString = hourString + ":" + minuteString + ":" + secondString + " UTC"
        hourString2 = str(hourTN)
        minuteString2 = str(minuteTN)
        secondString2 = str(secondTN)
        timeString2 = hourString2 + ":" + minuteString2 + ":" + secondString2 + " UTC"
        # green.setStationIndex(0)
        tempPath = Path(timeString2, timeString, "The Yard", green.getCurrentStation())
        self.trainSets[trainNum].addPath(tempPath)

        

    def makeCSV(self):
       

        with open('schedule.csv', mode='w') as schedule:
            schedule_writer = csv.writer(schedule, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

            schedule_writer.writerow(['Line', 'Train', 'Driver', 'Depart Station', 'Arrival Station', 'Departure Time', 'Arrival Time'])
            for x in range(0, len(self.trainSets)):
                for y in range(0, self.trainSets[x].pathLength):
                    schedule_writer.writerow(['Green', str(x), self.trainSets[x].driverTrain.getName(), self.trainSets[x].pathArray[y].getDepartB(), self.trainSets[x].pathArray[y].getDestB(), self.trainSets[x].pathArray[y].getDepartTime(),self.trainSets[x].pathArray[y].getArrivalTime()])

    def receive_train_inputs(self, numb, pos, blockNum, Velo):
        self.trainSets[numb].setBlock(blockNum)
        self.trainSets[numb].setCurrentSpeed(Velo)
        self.trainSets[numb].setPosition(pos)

        print(self.trainSets[numb].getAuthority())
        link.mbo_send_authority_velocity_tc.emit(numb, self.trainSets[numb].getAuthority(), self.trainSets[numb].getSuggestedSpeed())
        

# This function is used to make the schedule for the blue line.
# The blue line is not a part of the final iteration so it has been commented out.
##    def makeSchedule(self):
##        self.currentTime = self.startTime
##        #--train1 = Train('B')
##        #--self.addTrain(train1)
##        John = Driver("John Smith")
##        self.trainSets[0].driverTrain = John
##        q = 0
##        for j in range(0,4):
##           
##            while self.currentTime < self.startTime+0.60+j:
##                    
##
##                ## --print(self.trainSets[0].getDBlock())
##                if self.trainSets[0].getDBlock() == 0:
##                    tempPath = Path(self.currentTime, self.currentTime + .01, 10, 1)
##                    self.trainSets[0].addPath(tempPath)
##                    if self.currentTime >= self.startTime + 3.56:
##                        self.trainSets[0].setDBlock(1)
##                        self.currentTime += .02
##                    else:
##                        self.trainSets[0].setDBlock(10)
##                        self.currentTime += .02
##                elif self.trainSets[0].getDBlock() == 10 :
##                    tempPath = Path(self.currentTime, self.currentTime + .01, 15, 10)
##                    self.trainSets[0].addPath(tempPath)
##                    if self.currentTime >= self.startTime + 3.56:
##                        self.trainSets[0].setDBlock(1)
##                        self.currentTime += .02
##                    else:
##                        self.trainSets[0].setDBlock(15)
##                        self.currentTime += .02
##                elif self.trainSets[0].getDBlock() == 1 :
##                    tempPath = Path(self.currentTime, self.currentTime + .01, 1, 10)
##                    self.trainSets[0].addPath(tempPath)
##                    if self.currentTime >= self.startTime + 3.56:
##                        self.trainSets[0].setDBlock(1)
##                        self.currentTime += .02
##                    else:
##                        self.trainSets[0].setDBlock(15)
##                        self.currentTime += .02
##                else:
##                    tempPath = Path(self.currentTime, self.currentTime + .01, 10, 15)
##                    self.trainSets[0].addPath(tempPath)
##                    if self.currentTime >= self.startTime + 3.56:
##                        self.trainSets[0].setDBlock(1)
##                        self.currentTime += .02
##                    else:
##                        self.trainSets[0].setDBlock(10)
##                        self.currentTime += .02
##
##            q+=1
####        for j in range(int(self.startTime), 23):
####            self.hourN = j
####            while self.currentTime < j+1:
##                
##        self.trainSets[0].displayTrainsRouteList()
##        
##        ## repeat 30 minutes later
##        ## start 2nd driver 30-31 minutes after the first starts, or if there is a high throughput hour >6660 tickets/hr
##        ## dwell is 1 min, takes about ~45 seconds from station to station
##        ## 222 passengers is occupancy
##        ## about 30 transports in an hour
##        ## if more than 6660 tickets are sold (or expected to be sold) for the hour, requires at least two trains
##        ## would scale for larger lines

## ALGORITHM to walk through drivers
        ## input day
        ## check if each driver is available
        ## if available, add to schedule set
        ## keep going until each shift is covered
        ## if no one is available, hire a new driver
        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    DisplayTestWindow = QtWidgets.QMainWindow()
    DisplayWindow = QtWidgets.QMainWindow()
    
    test_UI = TestDisplay()
    test_UI.setupUI(DisplayTestWindow)
    DisplayTestWindow.show()

    main_UI = Display()
    main_UI.setupUI(DisplayWindow)
    DisplayWindow.show()

    trainA = Train('G')
##    trainB = Train('B')
##    trainC = Train('B')
##    trainD = Train('B')
##    trainE = Train('B')
##    trainF = Train('B')
##    trainG = Train('B')
##    trainH = Train('B')
##    trainI = Train('B')
##    trainJ = Train('B')
##    trainK = Train('B')
##    trainL = Train('B')
    MBO1 = MBO(trainA,test_UI,main_UI)
##    MBO1.addTrain(trainB)
##    MBO1.addTrain(trainC)
##    MBO1.addTrain(trainD)
##    MBO1.addTrain(trainE)
##    MBO1.addTrain(trainF)
##    MBO1.addTrain(trainG)
##    MBO1.addTrain(trainH)
##    MBO1.addTrain(trainI)
##    MBO1.addTrain(trainJ)
##    MBO1.addTrain(trainK)
##    MBO1.addTrain(trainL)
    John = Driver("John Smith",1,1,1,1,1,1,1,1)
    MBO1.trainSets[0].setDriver(John)
##    Roger = Driver("Roger Smith",1,1,1,1,1,1,1,1)
##    MBO1.trainSets[1].setDriver(Roger)
##    David = Driver("David Smith",1,1,1,1,1,1,1,1)
##    MBO1.trainSets[2].setDriver(David)
##    Timmy = Driver("Timmy Smith",1,1,1,1,1,1,1,1)
##    MBO1.trainSets[3].setDriver(Timmy)
##    Max = Driver("Max Smith",1,1,1,1,1,1,1,1)
##    MBO1.trainSets[4].setDriver(Max)
##    Jack = Driver("Jack Smith",1,1,1,1,1,1,1,1)
##    MBO1.trainSets[5].setDriver(Jack)
##    Joel = Driver("Joel Smith",1,1,1,1,1,1,1,1)
##    MBO1.trainSets[6].setDriver(Joel)
##    Eli = Driver("Eli Smith",1,1,1,1,1,1,1,1)
##    MBO1.trainSets[7].setDriver(Eli)
##    Zach = Driver("Zach Smith",1,1,1,1,1,1,1,1)
##    MBO1.trainSets[8].setDriver(Zach)
##    Alex = Driver("Alex Smith",1,1,1,1,1,1,1,1)
##    MBO1.trainSets[9].setDriver(Alex)
##    Gabe = Driver("Gabe Smith",1,1,1,1,1,1,1,1)
##    MBO1.trainSets[10].setDriver(Gabe)
##    Joseph = Driver("Joseph Smith",1,1,1,1,1,1,1,1)
##    MBO1.trainSets[11].setDriver(Joseph)
    MBO1.makeScheduleGreen()

    conv = Conversion()
    # print(conv.kmh_to_ms(40))

    MBO1.trainSets[0].setDBlock(73)

   
    
    ## --- MBO1.makeSchedule()

##    self.tableView = QtGui.QTableView(self.centralwidget)
##    self.tableView.setObjectName(_fromUtf8("tableView"))
##    
##    col_headers = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
##    self.tableView.setGeometry(QtCore.QRect(100, 930, 100, 50))
##    self.tableView.setHorizontalHeaderLabels(col_headers)
##    table = MyTable(QTableWidget)
##    self.tableView.table.open_sheet()
##
    sys.exit(app.exec_())
