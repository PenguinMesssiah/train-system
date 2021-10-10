'''
Last Updated: October 10, 2021
@author: Will Scott
'''

class trackSwitch(object):
    #Member Variables
    
    elementId   = None
    startBlock  = None
    endBlockOne = None
    endBlockTwo = None
    position    = None

    def __init__(self, elementId, startBlock, endBlockOne, endBlockTwo, position):
        # Constructor
        self.elementId   = elementId
        self.startBlock  = startBlock
        self.endBlockOne = endBlockOne
        self.endBlockTwo = endBlockTwo
        self.position    = position
        