'''
Last Updated: October 10, 2021
@author: Will Scott
'''

class station(object):
    # Member Variable
    
    name       = None
    xPos       = None
    yPos       = None
    occupancy  = None
    section    = None
    objType    = None
    underground = None
 
    def __init__(self, name, occupancy, section, objType, underground):
        # Constructor
        self.name       = name
        self.occupancy  = occupancy
        self.section    = section
        self.objType    = objType
        self.underGound = underground