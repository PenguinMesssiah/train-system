import time

class BlueLine(object):

    speedLimitArray = [0, 13.8889, 13.8889, 13.8889, 13.8889, 13.8889, 13.8889, 13.8889, 13.8889, 13.8889, 13.8889, 13.8889, 13.8889, 13.8889, 13.8889, 13.8889]
    blockCount = 15
    blockLengthArray = [0, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50]
    stationToStationBlockCount = 10
    stationToYardBC = 10
    timeFromStationToStation = 1
    timeFromStationToYard = 1
    dwell = 1

    def getSpeedLimit(self,num):

        return self.speedLimitArray[num]

    def getBlockLength(self,num):

        return self.blockLengthArray[num]

    def getDwell(self):
        return dwell

    def getStatTime(self):
        return timeFromStationToStation

    def getYardTime(self):
        return timeFromStationToYard

    def getSBC(self):
        return stationToStationBlockCount

    def getYBC(self):
        return stationToYardBC

    
