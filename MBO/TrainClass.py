import time
import csv
from BlueLineSet import BlueLine
from PathSet import Path
from TrainDriver import Driver
from GreenLine import GreenLine
from RedLine import RedLine
import math
class Train(object):

    train_count = 0
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
        elif self.lineCol == 'R':
            self.line = RedLine()
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

    def getLineString(self):
        if self.lineCol == 'B':
            return "Blue"
        elif self.lineCol == 'G':
            return "Green"
        else:
            return "Red"

    def setDBlock(self,num):
        self.DestinationBlock = int(num)
        #--self.getAuthority()

    def setCurrentSpeed(self,num):
        self.currentSpeed = num
        #--self.getAuthority()

    def setPosition(self,num):
        self.position = num
        #--self.getAuthority()

    def setBlock(self,num):
        self.block = int(num)
        #--self.getAuthority()

    def setSuggestedSpeed(self):
        self.suggestedSpeed = 0.85*self.line.getSpeedLimit(self.block)
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
                        self.destX += self.line.getBlockLength(29)
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
                if self.block < 60:
                    for x in range(self.DestinationBlock,self.block):
                        self.destX += self.line.getBlockLength(x)
                    self.destX += self.line.getBlockLength(self.block) - self.position
                else:
                    for x in range(self.block+1,self.DestinationBlock+1):
                        self.destX += self.line.getBlockLength(x)
                    self.destX += self.line.getBlockLength(self.block) - self.position
                    for x in range(29,self.DestinationBlock+1):
                        self.destX += self.line.getBlockLength(x)

        # This section will detetmine the distance between the train and its destination in meters.
        # This section is for trains on the Red Line
        
        elif self.lineCol == 'R':
            
            #These section handles the stretch of the track with the loop, sections A-E.
            if self.DestinationBlock < 16:
                if self.block <= self.DestinationBlock:
                    for x in range(self.block+1,self.DestinationBlock+1):
                        self.destX += self.line.getBlockLength(x)
                    self.destX += self.line.getBlockLength(self.block) - self.position
                else:
                    for x in range(self.DestinationBlock,self.block):
                        self.destX += self.line.getBlockLength(x)
                    self.destX += self.line.getBlockLength(self.block) - self.position
            # This section will handle when the destination is Herron Ave.
            # If it is the destination, it needs to be determined which of the three directions it is coming from
            
            elif self.DestinationBlock == 16:

                if self.block <= 7:
                    for x in range(1,self.block):
                        self.destX += self.line.getBlockLength(x)
                    self.destX += self.line.getBlockLength(self.block) - self.position
                    self.destX += self.line.getBlockLength(16)
                    
                elif self.block <=16:
                    for x in range(self.block+1,self.DestinationBlock+1):
                        self.destX += self.line.getBlockLength(x)
                    self.destX += self.line.getBlockLength(self.block) - self.position

                else:
                    for x in range(self.DestinationBlock,self.block):
                        self.destX += self.line.getBlockLength(x)
                    self.destX += self.line.getBlockLength(self.block) - self.position
                    
            # This section covers sections F, G, and the block of H before the station
            elif self.DestinationBlock > 16 and self.DestinationBlock < 25:

                if self.block < self.DestinationBlock:
                    for x in range(self.block+1,self.DestinationBlock+1):
                        self.destX += self.line.getBlockLength(x)
                    self.destX += self.line.getBlockLength(self.block) - self.position

                else:
                    for x in range(self.DestinationBlock,self.block):
                        self.destX += self.line.getBlockLength(x)
                    self.destX += self.line.getBlockLength(self.block) - self.position

            # This section will cover the first station in H, Penn Station, to handle the change if the RST section is taken.
            elif self.DestinationBlock == 25:

                # If the train is coming from the north, add the distance normally.
                if self.block < 25:
                    for x in range(self.block+1,self.DestinationBlock+1):
                        self.destX += self.line.getBlockLength(x)
                    self.destX += self.line.getBlockLength(self.block) - self.position

                # If the train is coming from the South, it depends if it took the extra loop
                else:
                    # If the train is heading north and hasn't crossed the switch yet, assume it is taking the main path.
                    # The safe stopping distance is small enough to cover this discrepancy.
                    if self.block > 32 and self.block <=35:
                        for x in range(self.DestinationBlock,self.block):
                            self.destX += self.line.getBlockLength(x)
                        self.destX += self.line.getBlockLength(self.block) - self.position
                    # This is the same as the previous section. This is when the train took the main path.
                    # It is separate in-case future iterations of this module wanted to take an input signal signaling which path the train will take.
                    elif self.block <= 32:
                        for x in range(self.DestinationBlock,self.block):
                            self.destX += self.line.getBlockLength(x)
                        self.destX += self.line.getBlockLength(self.block) - self.position
                    # This is to update the authority if the train took the alternate route.
                    elif self.block >= 72 and self.block <= 76:
                        for x in range(self.block+1,77):
                            self.destX += self.line.getBlockLength(x)
                        self.destX += self.line.getBlockLength(self.block) - self.position
                        # This adds the 3 blocks that remain after the loop.
                        for x in range(25,28):
                            self.destX += self.line.getBlockLength(x)
                        
            # This section handles if the train wanted to stop at blocks 26 and 27. Would only happen if there is an obstacle in the way.
            elif self.DestinationBlock > 25 and self.DestinationBlock < 28:

                if self.block <= self.DestinationBlock:
                    for x in range(self.block+1,self.DestinationBlock+1):
                        self.destX += self.line.getBlockLength(x)
                    self.destX += self.line.getBlockLength(self.block) - self.position

                else:

                    # If the train is heading north and hasn't crossed the switch yet, assume it is taking the main path.
                    # The safe stopping distance is small enough to cover this discrepancy.
                    if self.block > 32 and self.block <=35:
                        for x in range(self.DestinationBlock,self.block):
                            self.destX += self.line.getBlockLength(x)
                        self.destX += self.line.getBlockLength(self.block) - self.position
                    # This is the same as the previous section. This is when the train took the main path.
                    # It is separate in-case future iterations of this module wanted to take an input signal signaling which path the train will take.
                    elif self.block <= 32:
                        for x in range(self.DestinationBlock,self.block):
                            self.destX += self.line.getBlockLength(x)
                        self.destX += self.line.getBlockLength(self.block) - self.position
                    # This is to update the authority if the train took the alternate route.
                    elif self.block >= 72 and self.block <= 76:
                        for x in range(self.block+1,77):
                            self.destX += self.line.getBlockLength(x)
                        self.destX += self.line.getBlockLength(self.block) - self.position
                        # This adds the 3 blocks that remain after the loop.
                        for x in range(self.DestinationBlock,28):
                            self.destX += self.line.getBlockLength(x)

            # This section handles if the train wanted to stop along the H path between the switches for R and T.
            elif self.DestinationBlock >= 28 and self.DestinationBlock <33:

                # If the train is coming from the north.
                if self.block <= self.DestinationBlock:
                    for x in range(self.block+1,self.DestinationBlock+1):
                        self.destX += self.line.getBlockLength(x)
                    self.destX += self.line.getBlockLength(self.block) - self.position
                    
                # if the train is coming from the south.
                else:
                    for x in range(self.DestinationBlock,self.block):
                        self.destX += self.line.getBlockLength(x)
                    self.destX += self.line.getBlockLength(self.block) - self.position
            # This section handles if the train wanted to stop before the station but after the loop.
            
            elif self.DestinationBlock == 33 or self.DestinationBlock == 34:
                
                # If the train is coming from the south.
                if self.block >= self.DestinationBlock and self.block < 36:
                    for x in range(self.DestinationBlock,self.block):
                        self.destX += self.line.getBlockLength(x)
                    self.destX += self.line.getBlockLength(self.block) - self.position
                    
                # If the train is coming from the north and not in the RST loop.    
                elif self.block < self.DestinationBlock:
                    
                    for x in range(self.block+1,self.DestinationBlock+1):
                        self.destX += self.line.getBlockLength(x)
                    self.destX += self.line.getBlockLength(self.block) - self.position
                # If the train is in the RST loop coming down    
                else:
                    
                    for x in range(72, self.block):
                        self.destX += self.line.getBlockLength(x)
                    self.destX += self.line.getBlockLength(self.block) - self.position
                    for x in range(33, self.DestinationBlock+1):
                        self.destX += self.line.getBlockLength(x)

                        
            # This section handles if the train is headed to STEEL PLAZA.
            # There are 4 possibilities:
            # The train comes from the north, not in the RST loop.
            # The train comes from the north, in the RST loop.
            # The train comes from the south, not in the OPQ loop.
            # The train comes from the south, in the OPQ loop.
            elif self.DestinationBlock == 35:

                # The train comes from the north, not in the RST loop.
                if self.block <= self.DestinationBlock:
                    for x in range(self.block+1,self.DestinationBlock+1):
                        self.destX += self.line.getBlockLength(x)
                    self.destX += self.line.getBlockLength(self.block) - self.position
                    
                # The train comes from the south, not in the OPQ loop.
                elif self.block < 46:
                    for x in range(self.DestinationBlock,self.block):
                        self.destX += self.line.getBlockLength(x)
                    self.destX += self.line.getBlockLength(self.block) - self.position

                # The train comes from the north, in the RST loop.
                elif self.block > 71:
                    for x in range(72, self.block):
                        self.destX += self.line.getBlockLength(x)
                    self.destX += self.line.getBlockLength(self.block) - self.position
                    for x in range(33, self.DestinationBlock+1):
                        self.destX += self.line.getBlockLength(x)
                # The train comes from the south, in the OPQ loop.
                elif self.block > 66:
                    for x in range(self.block+1,72):
                        self.destX += self.line.getBlockLength(x)
                    self.destX += self.line.getBlockLength(self.block) - self.position
                    # This adds the 4 blocks that remain after the loop.
                    for x in range(35,39):
                        self.destX += self.line.getBlockLength(x)
            # This section solves the distance for when the train wants to stop after the station at block 35 and before the switch at the end of 38.
            elif self.DestinationBlock > 35 and self.DestinationBlock < 39:

                # The train comes from the south, not in the OPQ loop.
                if self.block < 46 and self.block > self.DestinationBlock:
                    for x in range(self.DestinationBlock,self.block):
                        self.destX += self.line.getBlockLength(x)
                    self.destX += self.line.getBlockLength(self.block) - self.position
                    
                # The train comes from the north.
                elif self.block <= self.DestinationBlock:
                    for x in range(self.block+1,self.DestinationBlock+1):
                        self.destX += self.line.getBlockLength(x)
                    self.destX += self.line.getBlockLength(self.block) - self.position

                # The train comes from the south, in the OPQ loop.
                elif self.block > 66:
                    for x in range(self.block+1,72):
                        self.destX += self.line.getBlockLength(x)
                    self.destX += self.line.getBlockLength(self.block) - self.position
                    # This adds the blocks that remain after the loop.
                    for x in range(self.DestinationBlock,39):
                        self.destX += self.line.getBlockLength(x)
            # This section accounts for the stretch of section H on the main path instead of the OPQ loop
            elif self.DestinationBlock > 38 and self.DestinationBlock < 44:

                # The train comes from the north.
                if self.block <= self.DestinationBlock:
                    for x in range(self.block+1,self.DestinationBlock+1):
                        self.destX += self.line.getBlockLength(x)
                    self.destX += self.line.getBlockLength(self.block) - self.position
                    
                # The train comes from the south.    
                else:
                    for x in range(self.DestinationBlock,self.block):
                        self.destX += self.line.getBlockLength(x)
                    self.destX += self.line.getBlockLength(self.block) - self.position

            # This section handles if the train wanted to stop before the station but after the loop.
            
            elif self.DestinationBlock == 44:
                
                # If the train is coming from the south.
                if self.block >= self.DestinationBlock and self.block < 46:
                    for x in range(self.DestinationBlock,self.block):
                        self.destX += self.line.getBlockLength(x)
                    self.destX += self.line.getBlockLength(self.block) - self.position
                    
                # If the train is coming from the north and not in the OPQ loop.    
                elif self.block < self.DestinationBlock:
                    
                    for x in range(self.block+1,self.DestinationBlock+1):
                        self.destX += self.line.getBlockLength(x)
                    self.destX += self.line.getBlockLength(self.block) - self.position
                    
                # If the train is in the OPQ loop coming down    
                else:
                    
                    for x in range(67, self.block):
                        self.destX += self.line.getBlockLength(x)
                    self.destX += self.line.getBlockLength(self.block) - self.position
                    self.destX += self.line.getBlockLength(44)

            # This section will handle the station at First Ave.
            elif self.DestinationBlock == 45:

                # If the train is coming from the south
                if self.block >= self.DestinationBlock and self.block < 49:
                    for x in range(self.DestinationBlock,self.block):
                        self.destX += self.line.getBlockLength(x)
                    self.destX += self.line.getBlockLength(self.block) - self.position

                # If the train is coming from the north, no loop taken.
                elif self.block < self.DestinationBlock:                   
                    for x in range(self.block+1,self.DestinationBlock+1):
                        self.destX += self.line.getBlockLength(x)
                    self.destX += self.line.getBlockLength(self.block) - self.position

                # If the train is in the OPQ loop coming down    
                else:
                    for x in range(67, self.block):
                        self.destX += self.line.getBlockLength(x)
                    self.destX += self.line.getBlockLength(self.block) - self.position
                    self.destX += self.line.getBlockLength(44)
                    self.destX += self.line.getBlockLength(45)
                    
            # This section will handle the stretch of track between station's first ave and station square.
            elif self.DestinationBlock > 45 and self.DestinationBlock < 48:
                
                # If the train is coming from the north.
                if self.block <= self.DestinationBlock:
                    for x in range(self.block+1,self.DestinationBlock+1):
                        self.destX += self.line.getBlockLength(x)
                    self.destX += self.line.getBlockLength(self.block) - self.position
                else:
                    for x in range(self.DestinationBlock,self.block):
                        self.destX += self.line.getBlockLength(x)
                    self.destX += self.line.getBlockLength(self.block) - self.position
            # This section will handle station station square.        
            elif self.DestinationBlock == 48:

                # If the train is coming from the north.
                if self.block <= self.DestinationBlock:
                    for x in range(self.block+1,self.DestinationBlock+1):
                        self.destX += self.line.getBlockLength(x)
                    self.destX += self.line.getBlockLength(self.block) - self.position
                # If the train is coming from the south, from L, K, or J.
                elif self.block < 60:
                    for x in range(self.DestinationBlock,self.block):
                        self.destX += self.line.getBlockLength(x)
                    self.destX += self.line.getBlockLength(self.block) - self.position
                # If the train is coming from the south, from M, N.   
                else:
                    for x in range(self.block+1, 67):
                        self.destX += self.line.getBlockLength(x)
                    self.destX += self.line.getBlockLength(self.block) - self.position
                    for x in range(48, 53):
                        self.destX += self.line.getBlockLength(x)
            # This section will handle the stretch from j to the switch on j.        
            elif self.DestinationBlock > 48 and self.DestinationBlock < 53:

                # If the train is coming from the north.
                if self.block <= self.DestinationBlock:
                    for x in range(self.block+1,self.DestinationBlock+1):
                        self.destX += self.line.getBlockLength(x)
                    self.destX += self.line.getBlockLength(self.block) - self.position
                # If the train is coming from the south, from L, K, or J.
                elif self.block < 60:
                    for x in range(self.DestinationBlock,self.block):
                        self.destX += self.line.getBlockLength(x)
                    self.destX += self.line.getBlockLength(self.block) - self.position
                # If the train is coming from the south, from M, N.   
                else:
                    for x in range(self.block+1, 67):
                        self.destX += self.line.getBlockLength(x)
                    self.destX += self.line.getBlockLength(self.block) - self.position
                    for x in range(self.DestinationBlock, 53):
                        self.destX += self.line.getBlockLength(x)
            # This section will cover the stretch of j,k, and L.
            elif self.DestinationBlock >=53 and self.DestinationBlock < 60:

                # If the train is coming from the north.
                if self.block <= self.DestinationBlock:
                    for x in range(self.block+1,self.DestinationBlock+1):
                        self.destX += self.line.getBlockLength(x)
                    self.destX += self.line.getBlockLength(self.block) - self.position
                # If the train is coming from the other direction.
                else:
                    for x in range(self.DestinationBlock,self.block):
                        self.destX += self.line.getBlockLength(x)
                    self.destX += self.line.getBlockLength(self.block) - self.position

            # This section will cover station South Hills Junction to the end of N
            elif self.DestinationBlock >= 60 and self.DestinationBlock <= 66:

                # If the train is coming from the north.
                if self.block <= self.DestinationBlock:
                    for x in range(self.block+1,self.DestinationBlock+1):
                        self.destX += self.line.getBlockLength(x)
                    self.destX += self.line.getBlockLength(self.block) - self.position

                # If the train is coming from the south.
                else:
                    # If the train is on sections M or N
                    if self.block >= 60 and self.block <= 66:
                        for x in range(self.DestinationBlock,self.block):
                            self.destX += self.line.getBlockLength(x)
                        self.destX += self.line.getBlockLength(self.block) - self.position
                    # If the train is still on J or I
                    else:
                        for x in range(self.DestinationBlock, 67):
                            self.destX += self.line.getBlockLength(x)
                        for x in range(self.block+1, 53):
                            self.destX += self.line.getBlockLength(x)
                        self.destX += self.line.getBlockLength(self.block) - self.position

            # This section will cover the OPQ loop, if a train needed to stop there.
            elif self.DestinationBlock > 66 and self.DestinationBlock < 72:

                if self.block < 39:
                    for x in range(self.block+1, 39):
                        self.destX += self.line.getBlockLength(x)
                    self.destX += self.line.getBlockLength(self.block) - self.position
                    for x in range(self.DestinationBlock, 72):
                        self.destX += self.line.getBlockLength(x)

                elif self.block < 46:
                    for x in range(44, self.block):
                        self.destX += self.line.getBlockLength(x)
                    self.destX += self.line.getBlockLength(self.block) - self.position
                    for x in range(67, self.DestinationBlock+1):
                        self.destX += self.line.getBlockLength(x)

                
                elif self.block <= self.DestinationBlock:
                    for x in range(self.block+1,self.DestinationBlock+1):
                        self.destX += self.line.getBlockLength(x)
                    self.destX += self.line.getBlockLength(self.block) - self.position

                else:
                    for x in range(self.DestinationBlock,self.block):
                        self.destX += self.line.getBlockLength(x)
                    self.destX += self.line.getBlockLength(self.block) - self.position

            # This section will cover the RST loop, if a train needed to stop there.
            elif self.DestinationBlock > 71:

                if self.block < 28:
                    for x in range(self.block+1, 28):
                        self.destX += self.line.getBlockLength(x)
                    self.destX += self.line.getBlockLength(self.block) - self.position
                    for x in range(self.DestinationBlock, 77):
                        self.destX += self.line.getBlockLength(x)

                elif self.block < 36:
                    for x in range(33, self.block):
                        self.destX += self.line.getBlockLength(x)
                    self.destX += self.line.getBlockLength(self.block) - self.position
                    for x in range(72, self.DestinationBlock+1):
                        self.destX += self.line.getBlockLength(x)

                
                elif self.block <= self.DestinationBlock:
                    for x in range(self.block+1,self.DestinationBlock+1):
                        self.destX += self.line.getBlockLength(x)
                    self.destX += self.line.getBlockLength(self.block) - self.position

                else:
                    for x in range(self.DestinationBlock,self.block):
                        self.destX += self.line.getBlockLength(x)
                    self.destX += self.line.getBlockLength(self.block) - self.position


                    
        self.safeStoppingDistance =  (0 - self.currentSpeed ** 2)/(2*self.regDecel)

        #--print(self.safeStoppingDistance)
        #--print(self.destX)

        self.Authority = self.destX - self.safeStoppingDistance

        return self.Authority


        
