#block class


class Block(object):
    """Our Block class that holds all attributes of a block"""
    def __init__(self, number):
        self.number = number
        self.switch = None
        self.crossing = None
        self.lights = None
        self.occupancy_ctc = 0
        self.commanded_speed = 0
        self.authority = 0


    # Block number methods
    def getNumber(self):
        return self.number

    def setNumber(self, num):
        self.number = num


    # Switch methods
    # switch will be an int representing current position, defaults to 0 when switch exists
    # None = no switch, number = goes from this Block to Block(number)
    def isSwitch(self):
        if self.switch is None:
            return False
        else:
            return True

    def addSwitch(self):
        self.switch = 0

    def getSwitchPosition(self):
        if isSwitch(self):
            return self.switch

    def setSwitchPosition(self, position):
        if isSwitch(self):
            self.switch = position


    # Crossing methods
    # None = no crossing, 0 = not enabled, 1 = enabled
    def isCrossing(self):
        if self.crossing is None:
            return False
        else:
            return True

    def addCrossing(self):
        self.crossing = 0

    def getCrossingState(self):
        if isCrossing(self):
            return self.crossing

    def setCrossinghState(self, state):
        if isCrossing(self):
            self.crossing = state


    # Lights methods
    # None = no lights, list 0001 = superGreen, 0010 = green, 0100 = yellow, 1000 = red
    def isLights(self):
        if self.lights is None:
            return False
        else:
            return True

    def addLights(self):
        self.lights = [0,0,0,0] #default all off

    def getLightsState(self):
        if isLights(self):
            return self.lights

    def setLightsState(self, state):
        if isLights(self):
            if state == 'r':
                self.lights = [1,0,0,0]     # red
            elif state == 'y':
                self.lights = [0,1,0,0]     # yellow
            elif state == 'g':
                self.lights = [0,0,1,0]     # green
            elif state == 's':
                self.lights = [0,0,0,1]     # supergreen
            else:
                print("not a valid state, enter r y g or s")


    # Occupancy (output to CTC) methods
    # 0 = occupied, 1 = free
    def getOccupancy_CTC(self):
        return self.occupancy_ctc

    def setOccupancy_CTC(self, occ):
        self.occupancy_ctc = occ


    # Commanded Speed methods
    # 0 = send 0 speed, 1 = send suggested speed
    def getCommanded_Speed(self):
        return self.commanded_speed

    def setCommanded_Speed(self, cs):
        self.commanded_speed = cs

    # Authority methods
     # 0 = not authorized, 1 = authoized
    def getAuthority(self):
        return self.authority

    def setAuthority(self, auth):
        self.authority = auth
