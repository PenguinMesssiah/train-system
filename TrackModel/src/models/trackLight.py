'''
Last Updated: October 8, 2021
@author: william scott
'''

class trackLight(object):
    # Member Variables
    lightId = None;
    xPos    = None;
    yPos    = None;
    state   = None;

    def __init__(self, lightId, xPos, yPos, state):
        # Constructor
        self.lightId = lightId;
        self.xPos    = xPos;
        self.yPos    = yPos;
        self.state   = state;
        