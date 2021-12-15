import time

class GreenLine(object):

    speedLimitArray1 = [0, 45, 45, 45,45, 45, 45,45, 45, 45, 45, 45, 45, 70, 70, 70, 70, 60, 60, 60, 60, 70, 70, 70, 70, 70, 70, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 70, 70, 70, 70, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 70, 70, 70, 70, 70, 70, 70, 70, 70, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 26, 28, 28, 28, 28, 28, 28, 28, 28, 30, 30, 30, 30, 30, 30, 30, 15, 15, 15, 15, 15, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20]                                                                                                               
    blockCount = 150
    speedLimitArray = []
    for k in range(0,151):
        speedLimitArray.append(speedLimitArray1[k]/3.6)
        
    blockLengthArray = [0, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 150, 150, 150, 150, 150, 150, 150, 150, 300, 300, 300, 300, 200, 100, 50, 50, 50, 50, 50 , 50, 50, 50, 50, 50, 50 , 50, 50, 50, 50, 50, 50 , 50, 50, 50, 50, 50, 50 , 50, 50, 50, 50, 50, 50 , 50, 50, 50, 50, 50, 50 , 50,100, 100, 200, 200, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 300, 300, 300,  300, 300, 300,  300, 300, 300, 100, 86.6, 100, 75, 75, 75, 75, 75, 75, 75, 75, 75, 75, 75, 75, 35, 100, 100, 80, 100, 100, 90, 100, 100, 100, 100, 100, 100, 162, 100, 100, 50, 50, 40, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 184, 40, 35]

    stationIndex = 0
    stationArray = ["GLENBURY", "DORMONT", "MT LEBANON", "POPLAR", "CASTLE SHANNON", "MT LEBANON", "DORMONT", "GLENBURY", "OVERBROOK", "INGLEWOOD","CENTRAL", "WHITED", "UNNAMED", "EDGEBROOK", "PIONEER", "UNNAMED", "WHITED", "SOUTH BANK", "CENTRAL", "INGLEWOOD", "OVERBROOK"]
    stationCount = 21
    TimeArray = [75, 45, 165, 90, 100, 55, 120, 175, 100, 85, 85, 175, 60, 60, 60, 40, 70, 80, 50, 55, 55, 55, 30, 30]
    stationToStationBlockCount = 10
    stationToYardBC = 10
    timeFromStationToStation = 1
    timeFromStationToYard = 1
    dwell = .5
## total time 1865 seconds w/o yard
    ## plus 30*20 = 600 seconds for dwell
    ## 2465 - 2457 - 2455 - 2451 - 
    ## need to get down to 2400
    def getBlockCount(self):
        return len(self.blockLengthArray)

    def getSpeedCount(self):
        return len(self.speedLimitArray)
    
    def getSpeedLimit(self,num):

        return self.speedLimitArray[num]

    def getBlockLength(self,num):

        return self.blockLengthArray[num]

    def getDwell(self):
        return self.dwell

    def getCurrentStation(self):
        return self.stationArray[self.stationIndex]

    def getNextStation(self):
        if self.stationIndex == 20:
            return self.stationArray[0]
        else:
            return self.stationArray[self.stationIndex + 1]

    def setStationIndex(self,num):
        self.stationIndex = num

    def incrementIndex(self):
            if self.stationIndex == 20:
                self.stationIndex = 0
            else:
                self.stationIndex = self.stationIndex + 1
                
    def getTime(self):
        return self.TimeArray[self.stationIndex]
                

    def getStatTime(self):
        return timeFromStationToStation

    def getYardTime(self):
        return timeFromStationToYard

    def getSBC(self):
        return stationToStationBlockCount

    def getYBC(self):
        return stationToYardBC

    
