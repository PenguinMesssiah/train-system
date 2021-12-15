from time import sleep
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit, QFileDialog
from PyQt5.QtGui import QIcon
import sys

sys.path.append("..")

from HWTrack.block import Block
from HWTrack.PLCInterpreter import PLCInterpreter


from Shared.connections import *
#from Shared.commmon import *


#implement my wayside controller
class WaysideControllerHW(object):
  """Define my one wayside controller!"""
  def __init__(self):
    self.control = [Block(19),Block(20),Block(21),Block(22),Block(23),Block(24),Block(25),Block(26),Block(27),Block(28),Block(29),Block(30),Block(31),Block(32),Block(33),Block(150)]    # control and listen are set in stone, they can't be modified after instantiation
    self.listen = [Block(17),Block(18),Block(34),Block(35),Block(36)]
    # dictionaries of all values
    self.lights_dict = dict()
    self.switch_dict = dict()
    self.crossing_dict = dict()
    self.occupancyCTC_dict = dict()
    self.commanded_speed_dict = dict()
    self.authority_dict = dict()
    self.suggested_speed_dict = dict()
    self.authority_limit_dict = dict()
    self.occupancy_tm_dict = dict()
    self.plc = PLCInterpreter()
    #controlled blocks indicies:
    # 0  | 19
    # 1  | 20
    # 2  | 21
    # 3  | 22
    # 4  | 23
    # 5  | 24
    # 6  | 25
    # 7  | 26
    # 8  | 27
    # 9  | 28
    # 10 | 29
    # 11 | 30
    # 12 | 31
    # 13 | 32
    # 14 | 33
    # 15 | 150
    # listened blockes indicies:
    # 0  | 17
    # 1  | 18
    # 2  | 34
    # 3  | 35
    # 4  | 36
    # give blocks with switches, crossings, and lights appropriate attributes
    self.control[0].addCrossing()   # Crossing on 19
    self.control[2].addLight()# Lights on 21
    self.control[4].addLight()# Lights on 23
    self.control[10].addSwitch()# Switch on 29
    self.control[10].addLight()# Lights on 29
    self.control[11].addLight()# Lights on 30
    self.control[13].addLight()# Lights on 32
    self.control[15].addLight()# Lights on 150

  # These getters and setters are for blocks under control
  # get blocks with switches
#  def getBlocksWithSwitches(self):
#    for i in range(len(self.control)):
#      if self.control[i].isSwitch():
#        print(self.control.getNumber())

  # get a block's switch position
#  def getBlockSwitchPosition(self, num):
#    return self.control[num].getSwitchPosition()

  # set a block's crossing state
  def setBlockSwitchPosition(self, num, position):
    self.control[num].setSwitchPosition(position)

  # get blocks with crossings
#  def getBlocksWithCrossings(self):
#    for i in range(len(self.control)):
#      if self.control[i].isCrossing():
#        print(self.control.getNumber())

  # get a block's crossing state
#  def getBlockCrossingState(self, num):
#    return self.control[num].getCrossingState()

  # set a block's crossing state
  def setBlockCrossingState(self, num, state):
    self.control[num].setCrossingState(state)

  # get blocks with lights
#  def getBlocksWithLights(self):
#    for i in range(len(self.control)):
#      if self.control[i].isLights():
#        print(self.control.getNumber())

  # get a block's lights state
#  def getBlockLightsState(self, num):
#    return self.control[num].getLightsState()

  # set a block's lights states
  # super green
  def setBlockSuperGreenLights(self, num):
    self.control[num].setSuperGreenLight()

  # green
  def setBlockGreenLights(self, num):
    self.control[num].setGreenLight()

  # Yellow
  def setBlockYellowLights(self, num):
    self.control[num].setYellowLight()

  # Red
  def setBlockRedLights(self, num):
    self.control[num].setRedLight()

  # These getters and setters specify whether they are for ALL blocks (blocks under control and listened to), just controlled blocks, or just listened to blocks
  # get controlled blocks' occupancies_ctc
#  def getControlledBlocksOccupancies_CTC(self):
#    occs = []
#    for i in range(len(self.control)):
#      occs.append(self.control[i].getOccupancy_CTC())
#    return occs

  # set controlled blocks' occupancies_ctc
  # NOTE to self: might be easier to make individual block setters too, so we can just change one value instead of the whole list
  def setControlledBlocksOccupancies_CTC(self, occs):
    # occs is a list of size len(self.control)
    for i in range(len(self.control)):
      self.control[i].setOccupancy_CTC(occs[i])

  # get listened blocks' occupancies_ctc
#  def getListenedBlocksOccupancies_CTC(self):
#    occs = []
#    for i in range(len(self.listen)):
#      occs.append(self.listen[i].getOccupancy_CTC())
#    return occs

  # set listened blocks' occupancies_ctc
  def setListenedBlocksOccupancies_CTC(self, occs):
    # occs is a list of size len(self.control)
    for i in range(len(self.listen)):
      self.listen[i].setOccupancy_CTC(occs[i])


  # get controlled blocks' commanded speeds
#  def getControlledBlocksCommanded_Speeds(self):
#    css = []
#    for i in range(len(self.control)):
#      css.append(self.control[i].getCommanded_Speed())
#    return css

  # set controlled blocks' commanded speeds
  def setControlledBlocksCommanded_Speeds(self, css):
    # css is a list of size len(self.control)
    for i in range(len(self.control)):
      self.control[i].setCommanded_Speed(css[i])

  # get listened blocks' commanded speeds
#  def getListenedBlocksCommanded_Speeds(self):
#    css = []
#    for i in range(len(self.listen)):
#      ccs.append(self.listen[i].getCommanded_Speed())
#    return ccs

  # set listened blocks' commanded speeds
    def setListenedBlocksCommanded_Speeds(self, css):
      # css is a list of size len(self.listen)
      for i in range(len(self.listen)):
        self.listen[i].setCommanded_Speed(css[i])


  # get controlled blocks' authorities
#  def getControlledBlocksAuthorities(self):
#    auths = []
#    for i in range(len(self.control)):
#      auths.append(self.control[i].getAuthorities())
#    return auths

  # set controlled blocks' authorities
  def setControlledBlocksAuthorities(self, auths):
    # auths is a list of size len(self.control)
    for i in range(len(self.control)):
      self.control[i].setAuthority(auths[i])

  # get listened blocks' authorities
#  def getListenedBlocksAuthorities(self):
#    auths = []
#    for i in range(len(self.listen)):
#      auths.append(self.listen[i].getAuthority())
#    return auths

  # set listened blocks' authorities
  def setListenedBlocksAuthorities(self, auths):
    # auths is a list of size len(self.control)
    for i in range(len(self.listen)):
      self.listen[i].setAuthority(auths[i])

  # merge dictionaries and send info to Elissa
  def merge_and_send_dicts(self):
    for i in range(len(self.control)):
      self.lights_dict.update(self.control[i].lights)
      self.switch_dict.update(self.control[i].switch)
      self.crossing_dict.update(self.control[i].crossing)
      #occupancyCTC_dict.update(self.control[i].occupancy_ctc)
      self.commanded_speed_dict.update(self.control[i].commanded_speed)
      self.authority_dict.update(self.control[i].authority)
    print(self.lights_dict)
    print(self.switch_dict)
    print(self.crossing_dict)
    #print(self.occupancyCTC_dict)
    print(self.commanded_speed_dict)
    print(self.authority_dict)

    # send info to Elissa
    link.hw_track_controller_send_lights_switch_crossing_commandedspeed_authority.emit(self.lights_dict, self.switch_dict, self.crossing_dict, self.commanded_speed_dict, self.authority_dict)


  # receive info from Elissa
  def receive(self):
    # receive info
    link.hw_track_controller_receive_suggestedspeed_authoritylimit_occupancyTM.connect(self.update)

  def update(self, suggested_speed_d, authority_limit_d, occupancy_tm_d):
    # update info
#    self.lights_dict = lights_d
#    self.switch_dict = switch_d
#    self.crossing_dict = crossing_d
#    #self.occupancyCTC_dict
#    self.commanded_speed_dict = commanded_speed_d
#    self.authority_dict = authority_d

    self.plc.runPLC("hwPLC.txt", self)

    self.suggested_speed_dict = suggested_speed_d
    self.authority_limit_dict = authority_limit_d
    self.occupancy_tm_dict = occupancy_tm_d
    print(self.suggested_speed_dict)
    print(self.authority_limit_dict)
    print(self.occupancy_tm_dict)

    # Lights
    #block 21
#    if self.lights_dict.get(21) == [0, 0, 0, 1]:
#      self.setSuperGreenLight(2)
#    elif self.lights_dict.get(21) == [0, 0, 1, 0]:
#      self.setBlockGreenLights(2)
#    elif self.lights_dict.get(21) == [0, 1, 0, 0]:
#      self.setBlockYellowLights(2)
#    elif self.lights_dict.get(21) == [1, 0, 0, 0]:
#      self.setBlockRedLights(2)

    #block 23
#    if self.lights_dict.get(23) == [0, 0, 0, 1]:
#      self.setBlockSuperGreenLights(4)
#    elif self.lights_dict.get(23) == [0, 0, 1, 0]:
#      self.setBlockGreenLights(4)
#    elif self.lights_dict.get(23) == [0, 1, 0, 0]:
#      self.setBlockYellowLights(4)
#    elif self.lights_dict.get(23) == [1, 0, 0, 0]:
#      self.setBlockRedLights(4)

    #block 29
#    if self.lights_dict.get(29) == [0, 0, 0, 1]:
#      self.setBlockSuperGreenLights(10)
#    elif self.lights_dict.get(29) == [0, 0, 1, 0]:
#      self.setBlockGreenLights(10)
#    elif self.lights_dict.get(29) == [0, 1, 0, 0]:
#      self.setBlockYellowLights(10)
#    elif self.lights_dict.get(29) == [1, 0, 0, 0]:
#      self.setBlockRedLights(10)

    #block 30
#    if self.lights_dict.get(30) == [0, 0, 0, 1]:
#      self.setBlockSuperGreenLights(11)
#    elif self.lights_dict.get(30) == [0, 0, 1, 0]:
#      self.setBlockGreenLights(11)
#    elif self.lights_dict.get(30) == [0, 1, 0, 0]:
#      self.setBlockYellowLights(11)
#    elif self.lights_dict.get(30) == [1, 0, 0, 0]:
#      self.setBlockRedLights(11)

    #block 32
#    if self.lights_dict.get(32) == [0, 0, 0, 1]:
#      self.setBlockSuperGreenLights(13)
#    elif self.lights_dict.get(32) == [0, 0, 1, 0]:
#      self.setBlockGreenLights(13)
#    elif self.lights_dict.get(32) == [0, 1, 0, 0]:
#      self.setBlockYellowLights(13)
#    elif self.lights_dict.get(32) == [1, 0, 0, 0]:
#      self.setBlockRedLights(13)

    #block 150
#    if self.lights_dict.get(150) == [0, 0, 0, 1]:
#      self.setBlockSuperGreenLights(15)
#    elif self.lights_dict.get(150) == [0, 0, 1, 0]:
#      self.setBlockGreenLights(15)
#    elif self.lights_dict.get(150) == [0, 1, 0, 0]:
#      self.setBlockYellowLights(15)
#    elif self.lights_dict.get(150) == [1, 0, 0, 0]:
#      self.setBlockRedLights(15)

    # Crossings
    #block 19
#    self.control[0].setBlockCrossingState(0, self.crossing_dict.get(19))   # Crossing on 19

    # Switch





    #self.control[10].addSwitch()# Switch on 29






# Main function
if __name__ == "__main__":
  # Instantiate controller, first list is controlled blocks second list is listened blocks
  wayside = WaysideControllerHW()
  # Choose PLC
  # enter name of PLC file

  sleep(9)

  # receive info from Elissa, calls update automatically
  wayside.receive()


  # merging my info and sending to Elissa
  wayside.merge_and_send_dicts()
