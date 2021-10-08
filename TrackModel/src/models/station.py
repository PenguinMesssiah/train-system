'''
Last Updated: October 8, 2021
@author: Will Scott
'''

class station(object):
    # Member Variable
    
    name      = None;
    xPos      = None;
    yPos      = None;
    occupancy = None;

    def __init__(self, name, xPos, yPos, occupancy):
        # Constructor
        self.name      = name;
        self.xPos      = xPos;
        self.yPos      = xPos;
        self.occupancy = occupancy;