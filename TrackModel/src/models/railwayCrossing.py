'''
Last Updated: October 8, 2021
@author: Will Scott
'''

class railwayCrossing(object):
    # Member Variables
    rId   = None;
    xPos  = None;
    yPos  = None;
    state = None; # Open(0) or Closed(1)

    def __init__(self, rId, xPos, yPos, state):
        # Constructor
        self.rId   = rId;
        self.xPos  = xPos;
        self.yPos  = yPos;
        self.state = state;
        