import time

class GreenLine(object):

    speedLimitArray = [0, 13.8889, 13.8889, 13.8889, 13.8889, 13.8889, 13.8889, 13.8889, 13.8889, 13.8889, 13.8889, 13.8889, 13.8889, 13.8889, 13.8889, 13.8889]
    blockCount = 15
    blockLengthArray = [0, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50]
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
    def getSpeedLimit(self,num):

        return self.speedLimitArray[num]

    def getBlockLength(self,num):

        return self.blockLengthArray[num]

    def getDwell(self):
        return dwell

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

    
