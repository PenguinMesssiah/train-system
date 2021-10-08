'''
Last Updated: October 8, 2021
@author: Will Scott
'''

class trackBlock(object):
    # Member Variables: External
    blockId   = None;
    elev      = None; 
    size      = None;
    gradLevel = None;
    envTemp   = None;
    occupancy = None;
    authority = None;
    
    # Member Variables: Positioning
    xPos = None;
    yPos = None;
    
    # Member Variables: Failure States
    failureBR = None;  # Broken Rail Failure
    failurePF = None;  # Power Failure
    failureTC = None;  # Track Circuit Failure
    
    # Member Functions
    def __init__(self, blockId, elev, size, gradLevel, envTemp, 
                 occupancy, xPos, yPos, failureBR, failurePF, failureTC, authority):
        # Constructor
        self.blockId   = blockId;
        self.elev      = elev;
        self.size      = size;
        self.envTemp   = envTemp;
        self.gradLevel = gradLevel;
        self.occupancy = occupancy;
        self.xPos      = xPos;
        self.yPos      = yPos;
        self.failureBR = failureBR;
        self.failurePF = failurePF;
        self.failureTC = failureTC;
        self.authority = authority;