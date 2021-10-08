'''
Last Updated: October 8, 2021
@author: Will Scott
'''

class trackBlock(object):
    # Member Variables: External
    blockId    = None;
    line       = None;
    elev       = None; 
    size       = None;
    gradLevel  = None;
    envTemp    = None;
    speedLimit = None;
    occupancy  = None;
    authority  = None;
    
    # Member Variables: Positioning
    xPos = None;
    yPos = None;
    angle = None;
    
    # Member Variables: Failure States
    failureBR = None;  # Broken Rail Failure
    failurePF = None;  # Power Failure
    failureTC = None;  # Track Circuit Failure
    
    # Member Functions
    def __init__(self, blockId, line, elev, size, gradLevel, envTemp, speedLimit, 
                 occupancy, xPos, yPos, angle, failureBR, failurePF, failureTC, authority):
        # Constructor
        self.blockId    = blockId;
        self.line       = line;
        self.elev       = elev;
        self.size       = size;
        self.envTemp    = envTemp;
        self.speedLimit = speedLimit;
        self.gradLevel  = gradLevel;
        self.occupancy  = occupancy;
        self.xPos       = xPos;
        self.yPos       = yPos;
        self.angle      = angle;
        self.failureBR  = failureBR;
        self.failurePF  = failurePF;
        self.failureTC  = failureTC;
        self.authority  = authority;