#block class


class Block(object):
  """Our Block class that holds all attributes of a block"""
  def __init__(self, num):
    self.number = num
    self.switch = dict()
    self.crossing = dict()
    self.lights = dict()
    self.occupancy_ctc = dict({self.number: 0})
    self.commanded_speed = dict({self.number: 0})
    self.authority = dict({self.number: 0})


  # Block number methods
  def getNumber(self):
    return self.number

  def setNumber(self, num):
    self.number = num


  # Switch methods
  # switch will be an int representing current position, defaults to 0 when switch exists
  # None = no switch, number = goes from this Block to Block(number)
#  def isSwitch(self):
#    if self.switch is None:
#      return False
#    else:
#      return True

  def addSwitch(self):
    self.switch.update({self.number: 0})
    print(self.switch)

#  def getSwitchPosition(self):
#    return self.switch

  def setSwitchPosition(self, position):
    self.switch.update({self.number: position})
    print(self.switch)


  # Crossing methods
  # None = no crossing, 0 = not enabled, 1 = enabled
#  def isCrossing(self):
#    if self.crossing is None:
#      return False
#    else:
#      return True

  def addCrossing(self):
    self.crossing.update({self.number: 0})

#  def getCrossingState(self):
#    if isCrossing(self):
#      return self.crossing

  def setCrossingState(self, state):
    self.crossing.update({self.number: state})


  # Lights methods
  # None = no lights, list 0001 = superGreen, 0010 = green, 0100 = yellow, 1000 = red
#  def isLights(self):
#    if self.lights is None:
#      return False
#    else:
#      return True

  def addLight(self):
    self.lights.update({self.number :[0, 0, 0, 0]})
    print(self.lights)

  def setSuperGreenLight(self):
    self.lights.update({self.number: [0, 0, 0, 1]})
    print(self.lights)

  def setGreenLight(self):
    self.lights.update({self.number: [0, 0, 1, 0]})
    print(self.lights)

  def setYellowLight(self):
    self.lights.update({self.number: [0, 1, 0, 0]})
    print(self.lights)

  def setRedLight(self):
    self.lights.update({self.number: [1, 0, 0, 0]})
    print(self.lights)

#  def getLightsState(self):
#    if isLights(self):
#      return self.lights

  # Occupancy (output to CTC) methods
  # 0 = occupied, 1 = free
#  def getOccupancy_CTC(self):
#    return self.occupancy_ctc

  def setOccupancy_CTC(self, occ):
    self.occupancy_ctc.update({self.number: occ})
    print(self.occupancy_CTC)


  # Commanded Speed methods
  # 0 = send 0 speed, 1 = send suggested speed
#  def getCommanded_Speed(self):
#    return self.commanded_speed

  def setCommanded_Speed(self, cs):
    self.commanded_speed.update({self.number: cs})
    print(self.commanded_speed)


  # Authority methods
   # 0 = not authorized, 1 = authoized
#  def getAuthority(self):
#    return self.authority

  def setAuthority(self, auth):
    self.authority.update({self.number: auth})
    print(self.authority)
