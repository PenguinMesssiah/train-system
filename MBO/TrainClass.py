import time
import csv
from BlueLineSet import BlueLine
from PathSet import Path
from TrainDriver import Driver

import math
class Train(object):

    train_count = 1
    def __init__(self, lineColor):
        
        self.number = Train.train_count
        Train.train_count += 1
        self.position = 0.0
        self.block = 0
        self.currentSpeed = 0.0
        self.lineCol = lineColor
        if self.lineCol == 'B':
            self.line = BlueLine()
        self.authority = 0.0
        self.suggestedSpeed = self.line.getSpeedLimit(self.block)
        self.DestinationBlock = 0
        self.regDecel = -1.2
        self.emergDecel = -2.73
        self.pathArray = []
        self.pathLength = 0
        self.driverTrain = Driver("Default",1,1,1,1,1,1,1,1)

        self.currentX = 0.0
        self.destX = 0.0
        self.deltaX = 0.0
        self.safeStoppingDistance = 0.0
        
        
    def setDriver(self,Driverr):
        self.driverTrain = Driverr


    def getPosition(self):
        return self.position

    def addPath(self,path):
        self.pathArray.append(path)
        self.pathLength += 1

    def displayTrainsRouteList(self):
        for x in range(0, self.pathLength):
            print("Train ", str(self.number), "is driven by ", self.driverTrain.getName(), ", and departs Station ", str(self.pathArray[x].getDepartB()), "at time ", str(self.pathArray[x].getDepartTime()), "and arrives at Station ", str(self.pathArray[x].getDestB()), "at time ", str(self.pathArray[x].getArrivalTime()))

    

    def getBlock(self):
        return self.block

    def getDBlock(self):
        return self.DestinationBlock

    def getCurrentSpeed(self):
        return self.currentSpeed

    def getLine(self):
        return self.line

    def getLineCol(self):
        return self.lineCol

    def setDBlock(self,num):
        self.DestinationBlock = int(num)
        #--self.getAuthority()

    def setCurrentSpeed(self,num):
        self.currentSpeed = num
        #--self.getAuthority()

    def setPosition(self,num):
        self.position = num
        self.getAuthority()

    def setBlock(self,num):
        self.block = int(num)
        #--self.getAuthority()

    def setSuggestedSpeed(self):
        self.suggestedSpeed = self.line.getSpeedLimit(self.block)
        #--self.getAuthority()
    
    def getSuggestedSpeed(self):
        self.setSuggestedSpeed()
        return self.suggestedSpeed

    def getTrainNumber(self):
        return self.number
    
    def controlSpeed(self):
        self.currentSpeed = self.getSuggestedSpeed()
       #-- self.getAuthority()
        
    def getAuthority(self):
        self.destX = 0;
        if self.lineCol == 'B':
            if self.DestinationBlock > 10:
                if self.block > 10:
                    
                    for x in range(self.block+1,self.DestinationBlock+1):
                        self.destX += self.line.getBlockLength(x)

                    self.destX += self.line.getBlockLength(self.block) - self.position

                elif self.block > 5 and self.block < 11:
                    for x in range(11,self.DestinationBlock+1):
                        self.destX += self.line.getBlockLength(x)

                    if self.block == 6:
                        self.destX += self.position
                    else:
                        for x in range(6,self.block):
                            self.destX += self.line.getBlockLength(x)

                        self.destX += self.position

                else:
                    
                    self.destX += self.line.getBlockLength(self.block) - self.position
                    
                    for x in range(self.block+1,5+1):
                        self.destX += self.line.getBlockLength(x)
                        

                    for x in range(11,self.DestinationBlock+1):
                        self.destX += self.line.getBlockLength(x)
                       

            elif self.DestinationBlock > 5:
                
                if self.block > 5 and self.block <11:
                    #--print("am i here")
                    for x in range(self.block+1,self.DestinationBlock+1):
                        self.destX += self.line.getBlockLength(x)

                    self.destX += self.line.getBlockLength(self.block) - self.position

                elif self.block > 11:
                    #--print("Im here")
                    for x in range(6,self.DestinationBlock+1):
                        self.destX += self.line.getBlockLength(x)

                    if self.block == 11:
                        self.destX += self.position
                    else:
                        for x in range(11,self.block):
                            self.destX += self.line.getBlockLength(x)

                        self.destX += self.position

                else:
                    #--print("or am i here")
                    self.destX += self.line.getBlockLength(self.block) - self.position 
                    for x in range(self.block+1,5+1):
                        self.destX += self.line.getBlockLength(x)

                    for x in range(6,self.DestinationBlock+1):
                        self.destX += self.line.getBlockLength(x)
                        
            else:
                if self.block > 5 and self.block <11:
                    for x in range(self.DestinationBlock,self.block):
                        self.destX += self.line.getBlockLength(x)

                    self.destX += self.position

                elif self.block > 11:
                    for x in range(self.DestinationBlock,5+1):
                        self.destX += self.line.getBlockLength(x)

                    if self.block == 11:
                        self.destX += self.position
                    else:
                        for x in range(11,self.block):
                            self.destX += self.line.getBlockLength(x)

                        self.destX += self.position

                else:
                    self.destX += self.position 
                    for x in range(self.DestinationBlock,self.block):
                        self.destX+= self.line.getBlockLength(x)

        self.safeStoppingDistance =  (0 - self.currentSpeed ** 2)/(2*self.regDecel)

        #--print(self.safeStoppingDistance)
        #--print(self.destX)

        self.Authority = self.destX - self.safeStoppingDistance

        return self.Authority


        
