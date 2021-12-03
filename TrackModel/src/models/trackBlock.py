'''
Last Updated: October 10, 2021
@author: Will Scott
'''

class trackBlock(object):
    # Member Variables: External
    blockNumber = None
    line        = None
    elev        = None
    cumElev     = None 
    size        = None
    section     = None
    gradLevel   = None
    speedLimit  = None
    occupancy   = None
    authority   = None
    
    objType     = None
    
    # Member Variables: Positioning
    xPos = None
    yPos = None
    angle = None
    
    # Member Variables: Failure States
    failureBR = None  # Broken Rail Failure
    failurePF = None  # Power Failure
    failureTC = None   # Track Circuit Failure
    
    # Member Functions 1     2        3            4        5        6           7      8        9      10
    def __init__(self, line, section, blockNumber, size, gradLevel, speedLimit, elev, cumEvel, objType, occupancy):
        # Constructor
        self.line        = line
        self.section     = section
        self.blockNumber = blockNumber
        self.size        = size
        self.gradLevel   = gradLevel
        self.speedLimit  = speedLimit
        self.elev        = elev
        self.cumElev     = cumEvel
        self.objType     = objType
        self.occupancy   = occupancy
        self.failureBR   = 0
        self.failurePF   = 0
        self.failureTC   = 0

    def setFailureStates(self, failureBR: int, failurePF: int, failureTC: int):
        self.failureBR = failureBR
        self.failurePF = failurePF
        self.failureTC = failureTC
