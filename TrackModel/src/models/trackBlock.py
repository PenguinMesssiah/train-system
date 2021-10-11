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
    envTemp     = None
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
    
    # Member Functions
    def __init__(self, line, section, blockNumber, size, gradLevel, speedLimit, elev, cumEvel, objType):
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
        