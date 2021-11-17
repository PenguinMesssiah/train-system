import time

class BlueLine(object):

    speedLimitArray = [50 50 50 50 50 50 50 50 50 50 50 50 50 50 50]
    blockCount = 15
    blockLengthArray = [50 50 50 50 50 50 50 50 50 50 50 50 50 50 50]

    def getSpeedLimit(self,num)

        return speedLimitArray[num-1]

    def getBlockLength(self,num)

        return blockLengthArray[num-1]

    
