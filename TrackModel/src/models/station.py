'''
Last Updated: October 10, 2021
@author: Will Scott
'''

class station(object):
    # Member Variable
    
    name      = None
    xPos      = None
    yPos      = None
    occupancy = None
    objType   = None

    def __init__(self, name, xPos, yPos, occupancy, objType):
        # Constructor
        self.name      = name
        self.xPos      = xPos
        self.yPos      = xPos
        self.occupancy = occupancy
        self.objType   = objType