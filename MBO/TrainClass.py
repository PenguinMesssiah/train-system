import time
import csv
from BlueLineSet import BlueLine
from PathSet import Path
from TrainDriver import Driver
from GreenLine import GreenLine
import math
class Train(object):

    train_count = 1
    def __init__(self, lineColor):
        
        self.number = Train.train_count
        Train.train_count += 1
        self.position = 0.0
        self.block = 0
        self.yardBool = False
        self.currentSpeed = 0.0
        self.lineCol = lineColor
        if self.lineCol == 'B':
            self.line = BlueLine()
        elif self.lineCol == 'G':
            self.line = GreenLine()
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
        # This section will calculate the total distance between the train and the destination(where the train needs to stop).
        # This section is for trains on the Green Line.
        
        elif self.lineCol == 'G':
            
            # This statement handles distance calculations when the destination is between block 57 and 77.
            # The distance of every block the train does not currently occupy to the destination is added to destX.
            # Finally, to complete the distance addition, the remaining distance on the current block is added to destX.
            # This same algorithm is used for every stretch of the track when the track is unidirectional.
            if self.DestinationBlock > 57 and self.DestinationBlock < 77:
                    for x in range(self.block+1,self.DestinationBlock+1):
                        self.destX += self.line.getBlockLength(x)
                    self.destX += self.line.getBlockLength(self.block) - self.position
            
            # This statement handles distance calculations when the destination is from block 77 to 85, aka on section N
            elif self.DestinationBlock >= 77 and self.DestinationBlock <=85:
                    if self.block < 77:
                        for x in range(self.block+1,self.DestinationBlock+1):
                            self.destX += self.line.getBlockLength(x)
                        self.destX += self.line.getBlockLength(self.block) - self.position
                    elif self.block >=77 and self.block <= 85:
                            for x in range(self.DestinationBlock,self.block):
                                self.destX += self.line.getBlockLength(x)
                            self.destX += self.line.getBlockLength(self.block) - self.position
                    else:
                        for x in range(self.block+1,self.DestinationBlock+1):
                            self.destX += self.line.getBlockLength(x)
                        self.destX += self.line.getBlockLength(self.block) - self.position
                        for x in range(77, 86):
                            self.destX += self.line.getBlockLength(x)
            # This statement handles distance calculations when the destination is between block 85 and 100(inclusive).            
            elif self.DestinationBlock > 85 and self.DestinationBlock <= 100:
                    for x in range(self.block+1,self.DestinationBlock+1):
                        self.destX += self.line.getBlockLength(x)
                    self.destX += self.line.getBlockLength(self.block) - self.position          
                    
            # This statement handles block R to station glenbury coming from U.
            # If the train is still at Mt Lebanon, regard position as 0 at station.
            elif self.DestinationBlock >= 101 and self.DestinationBlock <= 114:
                    if self.block == 77:
                        for x in range(101,self.DestinationBlock+1):
                            self.destX += self.line.getBlockLength(x)
                    else:
                        for x in range(self.block+1,self.DestinationBlock+1):
                            self.destX += self.line.getBlockLength(x)
                        self.destX += self.line.getBlockLength(self.block) - self.position
                        
            # This statement handles station glenbury to the end of block 150, which is the last block of block Z.
            # This whole section of track is unidirectional
            elif self.DestinationBlock > 114 and self.DestinationBlock <= 150:
                    for x in range(self.block+1,self.DestinationBlock+1):
                        self.destX += self.line.getBlockLength(x)
                    self.destX += self.line.getBlockLength(self.block) - self.position

            # This statement handles the bidirectional track starting at section F.
            # It determines which direction the train is coming from, so that the distances can be added properly
            elif self.DestinationBlock > 21 and self.DestinationBlock <=28:
                    if self.block >= 141:
                        for x in range(self.block+1,151):
                            self.destX += self.line.getBlockLength(x)
                        self.destX += self.line.getBlockLength(self.block) - self.position
                        # add distance for F line
                        for x in range(self.DestinationBlock, 28+1):
                            self.destX += self.line.getBlockLength(x)
                    # if train currently is heading up the F section    
                    elif self.block > self.DestinationBlock:
                            for x in range(self.DestinationBlock,self.block):
                                self.destX += self.line.getBlockLength(x)
                            self.destX += self.line.getBlockLength(self.block) - self.position
                    # if train heading towards F section from D-F sections        
                    else:
                        for x in range(self.block+1,self.DestinationBlock+1):
                            self.destX += self.line.getBlockLength(x)
                        self.destX += self.line.getBlockLength(self.block) - self.position
           # This statement handles the E + D + block 21 section.
            elif self.DestinationBlock > 12 and self.DestinationBlock <=21:
                    if self.block >= self.DestinationBlock:
                        for x in range(self.DestinationBlock,self.block):
                                self.destX += self.line.getBlockLength(x)
                        self.destX += self.line.getBlockLength(self.block) - self.position
                    # handles A section in distance calculation to section D        
                    else:
                        if self.block < 3:
                            if self.block == 2:
                                self.destX += self.line.getBlockLength(1)
                            else:
                                self.destX += self.line.getBlockLength(self.block) - self.position 
                        # add distance for D line
                            for x in range(13,self.DestinationBlock+1):
                                self.destX += self.line.getBlockLength(x)
                        else:
                            # regular direction
                            for x in range(self.block+1,self.DestinationBlock+1):
                                self.destX += self.line.getBlockLength(x)
                            self.destX += self.line.getBlockLength(self.block) - self.position
            # This statement handles if the train is in sections C, B, or A.
            elif self.DestinationBlock <=12:
                    for x in range(self.DestinationBlock,self.block):
                        self.destX += self.line.getBlockLength(x)
                    self.destX += self.line.getBlockLength(self.block) - self.position

            # This statement jumps to destinations in line G to end of I. This is the last section of the distance calculations.               
            elif self.DestinationBlock > 28 and self.DestinationBlock <=57:
                    for x in range(self.DestinationBlock,self.block):
                        self.destX += self.line.getBlockLength(x)
                    self.destX += self.line.getBlockLength(self.block) - self.position

                    
        self.safeStoppingDistance =  (0 - self.currentSpeed ** 2)/(2*self.regDecel)

        #--print(self.safeStoppingDistance)
        #--print(self.destX)

        self.Authority = self.destX - self.safeStoppingDistance

        return self.Authority


        
