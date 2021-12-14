import time

class RedLine(object):

    speedLimitArray1 = [0, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 55, 70, 70, 70, 55, 55, 55, 70, 70, 70, 70, 70, 70, 70, 70, 70, 70, 70, 70, 70, 70, 70, 70, 70, 70, 70, 70, 70, 70, 70, 70, 70, 60, 60, 55, 55, 55, 55, 55, 55, 55, 55, 55, 55, 55, 55, 55, 55, 55, 55, 55, 55, 55, 55, 55, 55, 55, 55, 55, 55]
    blockCount = 150
    speedLimitArray = []
    for k in range(0,77):
        speedLimitArray.append(speedLimitArray1[k]/3.6)
        
    blockLengthArray = [0, 50, 50, 50, 50, 50, 50, 75, 75, 75, 75, 75, 75, 70, 60, 60, 50, 200, 400, 400, 200, 100, 100, 100, 50, 50, 50, 50, 50, 60, 60, 50, 50, 50, 50, 50, 50, 50, 50, 50, 60, 60, 50, 50, 50, 50, 75, 75, 75, 50, 50, 50, 43.2, 50, 50, 75, 75, 75, 75, 75, 75, 75, 75, 75, 75, 75, 75, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50]
    stationIndex = 0
    stationArray = ["GLENBURY", "DORMONT", "MT LEBANON", "POPLAR", "CASTLE SHANNON", "MT LEBANON", "GLENBURY", "OVERBROOK", "INGLEWOOD","CENTRAL", "WHITED", "UNNAMED", "EDGEBROOK", "PIONEER", "UNNAMED", "WHITED", "SOUTH BANK", "CENTRAL", "INGLEWOOD", "OVERBROOK"]
    stationCount = 20
    TimeArray = [75, 45, 165, 90, 100, 185, 175, 100, 85, 85, 175, 60, 60, 60, 40, 70, 80, 50, 55, 55, 55, 30, 30]
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
        if self.stationIndex == 19:
            return self.stationArray[0]
        else:
            return self.stationArray[self.stationIndex + 1]
            

    def incrementIndex(self):
            if self.stationIndex == 19:
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

    
