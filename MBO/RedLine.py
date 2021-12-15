import time

class RedLine(object):

    speedLimitArray1 = [0, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 55, 70, 70, 70, 55, 55, 55, 70, 70, 70, 70, 70, 70, 70, 70, 70, 70, 70, 70, 70, 70, 70, 70, 70, 70, 70, 70, 70, 70, 70, 70, 70, 60, 60, 55, 55, 55, 55, 55, 55, 55, 55, 55, 55, 55, 55, 55, 55, 55, 55, 55, 55, 55, 55, 55, 55, 55, 55, 55, 55]
    blockCount = 76
    speedLimitArray = []
    for k in range(0,77):
        speedLimitArray.append(speedLimitArray1[k]/3.6)
        
    blockLengthArray = [0, 50, 50, 50, 50, 50, 50, 75, 75, 75, 75, 75, 75, 70, 60, 60, 50, 200, 400, 400, 200, 100, 100, 100, 50, 50, 50, 50, 50, 60, 60, 50, 50, 50, 50, 50, 50, 50, 50, 50, 60, 60, 50, 50, 50, 50, 75, 75, 75, 50, 50, 50, 43.2, 50, 50, 75, 75, 75, 75, 75, 75, 75, 75, 75, 75, 75, 75, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50]
    stationIndex = 0
    stationArray = ["SHADYSIDE", "HERRON AVE", "SWISSVALE", "PENN STATION", "STEEL PLAZA", "FIRST AVE", "STATION SQUARE", "SOUTH HILLS JUNCTION", "STATION SQUARE","FIRST AVE", "STEEL PLAZA", "PENN STATION", "SWISSVALE", "HERRON AVE"]
    stationCount = 14
    TimeArray = [35, 75, 20, 30, 30, 15, 55, 50, 15, 30, 30, 25, 75, 60, 30, 30]
    stationToStationBlockCount = 10
    stationToYardBC = 10
    timeFromStationToStation = 1
    timeFromStationToYard = 1
    dwell = .5
## total time 1865 seconds w/o yard
    ## plus 30*20 = 600 seconds for dwell
    ## 2465 - 2457 - 2455 - 2451 - 
    ## need to get down to 2400

    # Total time around track no dwell is 545 seconds
    # dwell 14*30 = 420
    # total time = 965
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
        if self.stationIndex == 13:
            return self.stationArray[0]
        else:
            return self.stationArray[self.stationIndex + 1]
            

    def setStationIndex(self,num):
        self.stationIndex = num

    def incrementIndex(self):
            if self.stationIndex == 13:
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

    
