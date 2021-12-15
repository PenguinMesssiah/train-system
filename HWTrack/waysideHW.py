from time import sleep
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit, QFileDialog
from PyQt5.QtGui import QIcon
import sys
from pyfirmata import ArduinoMega
import numpy as np
import pandas as pd
import re

sys.path.append("..")

from HWTrack.block import Block
from HWTrack.PLCInterpreter import PLCInterpreter


from Shared.connections import *
#from Shared.commmon import *

# Declare board variable
board = ArduinoMega("COM3", baudrate=57600)

# Declare list of all 27 pins that are in use
PINS = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53]

lights_PINS = [4, 5, 6, 7]
switch_PINS = 3
crossing_PINS = 2
authority_PINS = [38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53]
commandedSpeed_PINS = [0, 1, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27]
occupancy_PINS = [8, 9, 10, 11, 12, 13, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37]


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

  def merge_dicts(self):
      # controlled
      for i in range(len(self.control)):
          # These next 6 lines are what make the data come from Elissa, but since that isn't working I assign my own values
#        self.lights_dict.update(self.control[i].lights)
#        self.switch_dict.update(self.control[i].switch)
#        self.crossing_dict.update(self.control[i].crossing)
#        #occupancyCTC_dict.update(self.control[i].occupancy_ctc)
#        self.commanded_speed_dict.update(self.control[i].commanded_speed)
#        self.authority_dict.update(self.control[i].authority)

        # putting my own values to show the hardware works
        self.authority_dict.update({self.control[i].getNumber(): 1})
        self.lights_dict.update({self.control[i].getNumber(): 1})
        self.switch_dict.update({self.control[i].getNumber(): 1})
        self.crossing_dict.update({self.control[i].getNumber(): 1})
        #occupancyCTC_dict.update(self.control[i].occupancy_ctc)
        self.commanded_speed_dict.update({self.control[i].getNumber(): 1})

        self.suggested_speed_dict.update({self.control[i].getNumber(): 0})
        self.authority_limit_dict.update({self.control[i].getNumber(): 0})
        self.occupancyCTC_dict.update({self.control[i].getNumber(): 1})
      # listened
      for i in range(len(self.listen)):
          self.suggested_speed_dict.update({self.listen[i].getNumber(): 0})
          self.authority_limit_dict.update({self.listen[i].getNumber(): 0})
          self.occupancyCTC_dict.update({self.listen[i].getNumber(): 0})
      print(self.lights_dict)
      print(self.switch_dict)
      print(self.crossing_dict)
      #print(self.occupancyCTC_dict)
      print(self.commanded_speed_dict)
      print(self.authority_dict)
      print(self.suggested_speed_dict)
      print(self.authority_limit_dict)
      print(self.occupancyCTC_dict)


  # send info to Elissa
  def send_dicts(self):
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

#    self.suggested_speed_dict = suggested_speed_d
#    self.authority_limit_dict = authority_limit_d
#    self.occupancy_tm_dict = occupancy_tm_d
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


# TEST "INTERFACE" FUNCTION
#make a function that asks for a bunch of inputs and then reflects those inputs on the hardware LEDs
def testInterface():
    # Ask user which kind of test they want to run (keep asking for input until valid one entered)
    while True:
        try:
            in_choiceOfTest = int(input("Enter 1 to change all Inputs, Enter 2 to choose which Input to change: "))
            if in_choiceOfTest == 1 or in_choiceOfTest == 2:
                break
        except Exception as e:
            print("Invalid input type, try again")
    # If the user wanted to change ALL Inputs
    #TODO: ADD TRY-EXCEPT CASES FOR ALLLLLLLLL INPUTS TO ENSURE GOOD INPUT
    if in_choiceOfTest == 1:
        # Authority (keep asking for input until valid one entered)
        while True:
            try:
                in_authority = int(input("Enter Authority Limit (0-1023): "))
                if (in_authority >= 0) and (in_authority <= 1023):
                    set_authority(in_authority)
                    break
            except Exception as e:
                print("Invalid input type, try again")
        # Switch Position from CTC (keep asking for input until valid one entered)
        while True:
            try:
                in_switchPosition_CTC = int(input("Enter Switch Position from CTC (6 or 11): "))
                if in_switchPosition_CTC == 6:
                    set_switchPosition_CTC(1)
                    break
                elif in_switchPosition_CTC == 11:
                    set_switchPosition_CTC(0)
                    break
            except Exception as e:
                print("Invalid input type, try again")
        # Occupancy (keep asking for input until valid one entered)
        while True:
            try:
                in_occupancy = int(input("Enter Occupancy (0-127): "))
                if (in_occupancy >= 0) and (in_occupancy <= 127):
                    set_occupancy(in_occupancy)
                    break
            except Exception as e:
                print("Invalid input type, try again")
#    # If the user wanted to specify which Input to change
    elif in_choiceOfTest == 2:
        # Ask the user which Input they would like to change (keep asking until valid input received)
        while True:
            try:
                in_choiceOfInput = int(input("Enter the number of the Input you would like to test (Lights - 1, Switch - 2, Crossing - 3, Authority - 4, Commanded Speed - 5, Occupancy - 6): "))
                if (in_choiceOfInput >= 1) and (in_choiceOfInput <= 7):
                    break
            except Exception as e:
                print("Invalid input type, try again")
        if in_choiceOfInput == 1:
            # Lights (keep asking for input until valid one entered)
            while True:
                try:
                    in_lights = int(input("Enter Lights state (0-1): "))
                    if (in_lights >= 0) and (in_lights <= 1):
                        set_lights(in_lights)
                        break
                except Exception as e:
                    print("Invalid input type, try again")
        elif in_choiceOfInput == 2:
            # Switch (keep asking for input until valid one entered)
            while True:
                try:
                    in_switch = int(input("Enter Switch state (0-1): "))
                    if (in_switch >= 0) and (in_switch <= 1):
                        set_switch(in_switch)
                        break
                except Exception as e:
                    print("Invalid input type, try again")
        elif in_choiceOfInput == 3:
            # Crossing (keep asking for input until valid one entered)
            while True:
                try:
                    in_crossing = int(input("Enter Crossing state (0-1): "))
                    if (in_crossing >= 0) and (in_crossing <= 1):
                        set_crossing(in_crossing)
                        break
                except Exception as e:
                    print("Invalid input type, try again")
        elif in_choiceOfInput == 4:
            # Authority (keep asking for input until valid one entered)
            while True:
                try:
                    in_authority = int(input("Enter Authority (0-1023): "))
                    if (in_authority >= 0) and (in_authority <= 7):
                        set_authority(in_authority)
                        break
                except Exception as e:
                    print("Invalid input type, try again")
        elif in_choiceOfInput == 5:
            # Commanded Speed (keep asking for input until valid one entered)
            while True:
                try:
                    in_commandedSpeed = int(input("Enter Commanded Speed (0-15): "))
                    if (in_commandedSpeed >= 0) and (in_commandedSpeed <= 127):
                        set_commandedSpeed(in_commandedSpeed)
                        break
                except Exception as e:
                    print("Invalid input type, try again")
        elif in_choiceOfInput == 6:
            # Occupancy (keep asking for input until valid one entered)
            while True:
                try:
                    in_occupancy = int(input("Enter Occupancy (0-1023): "))
                    if (in_occupancy >= 0) and (in_occupancy <= 7):
                        set_occupancy(in_occupancy)
                        break
                except Exception as e:
                    print("Invalid input type, try again")
    # Ask the user if they would like to continue testing
    while True:
        try:
            in_continueTesting = input("Continue Testing? (y/n): ")
            if in_continueTesting == 'y' or in_continueTesting == 'Y':
                # Go back to the start of the method
                break
            elif in_continueTesting == 'n' or in_continueTesting == 'N':
                # Exit the method
                return None
                break
        except Exception as e:
            print("Invalid input type, try again")



# Arduino stuff

# Set Authority
def set_authority(ctrl):
    board.digital[authority_PINS[0]].write(ctrl.authority_dict.get(ctrl.control[0].number))
    board.digital[authority_PINS[1]].write(ctrl.authority_dict.get(ctrl.control[1].number))
    board.digital[authority_PINS[2]].write(ctrl.authority_dict.get(ctrl.control[2].number))
    board.digital[authority_PINS[3]].write(ctrl.authority_dict.get(ctrl.control[3].number))
    board.digital[authority_PINS[4]].write(ctrl.authority_dict.get(ctrl.control[4].number))
    board.digital[authority_PINS[5]].write(ctrl.authority_dict.get(ctrl.control[5].number))
    board.digital[authority_PINS[6]].write(ctrl.authority_dict.get(ctrl.control[6].number))
    board.digital[authority_PINS[7]].write(ctrl.authority_dict.get(ctrl.control[7].number))
    board.digital[authority_PINS[8]].write(ctrl.authority_dict.get(ctrl.control[8].number))
    board.digital[authority_PINS[9]].write(ctrl.authority_dict.get(ctrl.control[9].number))
    board.digital[authority_PINS[10]].write(ctrl.authority_dict.get(ctrl.control[10].number))
    board.digital[authority_PINS[11]].write(ctrl.authority_dict.get(ctrl.control[11].number))
    board.digital[authority_PINS[12]].write(ctrl.authority_dict.get(ctrl.control[12].number))
    board.digital[authority_PINS[13]].write(ctrl.authority_dict.get(ctrl.control[13].number))
    board.digital[authority_PINS[14]].write(ctrl.authority_dict.get(ctrl.control[14].number))
    board.digital[authority_PINS[15]].write(ctrl.authority_dict.get(ctrl.control[15].number))

# Set Commanded Speed
def set_commandedSpeed(ctrl):
    # cannot use these pins as digital using firmata
    #board.digital[commandedSpeed_PINS[0]].write(ctrl.commanded_speed_dict.get(ctrl.control[0].number))
    #board.digital[commandedSpeed_PINS[1]].write(ctrl.commanded_speed_dict.get(ctrl.control[1].number))
    #board.digital[commandedSpeed_PINS[2]].write(ctrl.commanded_speed_dict.get(ctrl.control[2].number))
    #board.digital[commandedSpeed_PINS[3]].write(ctrl.commanded_speed_dict.get(ctrl.control[3].number))
    #board.digital[commandedSpeed_PINS[4]].write(ctrl.commanded_speed_dict.get(ctrl.control[4].number))
    #board.digital[commandedSpeed_PINS[5]].write(ctrl.commanded_speed_dict.get(ctrl.control[5].number))
    #board.digital[commandedSpeed_PINS[6]].write(ctrl.commanded_speed_dict.get(ctrl.control[6].number))
    #board.digital[commandedSpeed_PINS[7]].write(ctrl.commanded_speed_dict.get(ctrl.control[7].number))
    #board.digital[commandedSpeed_PINS[8]].write(ctrl.commanded_speed_dict.get(ctrl.control[8].number))
    #board.digital[commandedSpeed_PINS[9]].write(ctrl.commanded_speed_dict.get(ctrl.control[9].number))
    # can use these pins as digital using firmata
    board.digital[commandedSpeed_PINS[10]].write(ctrl.commanded_speed_dict.get(ctrl.control[10].number))
    board.digital[commandedSpeed_PINS[11]].write(ctrl.commanded_speed_dict.get(ctrl.control[11].number))
    board.digital[commandedSpeed_PINS[12]].write(ctrl.commanded_speed_dict.get(ctrl.control[12].number))
    board.digital[commandedSpeed_PINS[13]].write(ctrl.commanded_speed_dict.get(ctrl.control[13].number))
    board.digital[commandedSpeed_PINS[14]].write(ctrl.commanded_speed_dict.get(ctrl.control[14].number))
    board.digital[commandedSpeed_PINS[15]].write(ctrl.commanded_speed_dict.get(ctrl.control[15].number))

# Set Occupancy
def set_occupancy(ctrl):
    board.digital[occupancy_PINS[0]].write(ctrl.occupancyCTC_dict.get(ctrl.control[0].number))
    board.digital[occupancy_PINS[1]].write(ctrl.occupancyCTC_dict.get(ctrl.control[1].number))
    board.digital[occupancy_PINS[2]].write(ctrl.occupancyCTC_dict.get(ctrl.control[2].number))
    board.digital[occupancy_PINS[3]].write(ctrl.occupancyCTC_dict.get(ctrl.control[3].number))
    board.digital[occupancy_PINS[4]].write(ctrl.occupancyCTC_dict.get(ctrl.control[4].number))
    board.digital[occupancy_PINS[5]].write(ctrl.occupancyCTC_dict.get(ctrl.control[5].number))
    board.digital[occupancy_PINS[6]].write(ctrl.occupancyCTC_dict.get(ctrl.control[6].number))
    board.digital[occupancy_PINS[7]].write(ctrl.occupancyCTC_dict.get(ctrl.control[7].number))
    board.digital[occupancy_PINS[8]].write(ctrl.occupancyCTC_dict.get(ctrl.control[8].number))
    board.digital[occupancy_PINS[9]].write(ctrl.occupancyCTC_dict.get(ctrl.control[9].number))
    board.digital[occupancy_PINS[10]].write(ctrl.occupancyCTC_dict.get(ctrl.control[10].number))
    board.digital[occupancy_PINS[11]].write(ctrl.occupancyCTC_dict.get(ctrl.control[11].number))
    board.digital[occupancy_PINS[12]].write(ctrl.occupancyCTC_dict.get(ctrl.control[12].number))
    board.digital[occupancy_PINS[13]].write(ctrl.occupancyCTC_dict.get(ctrl.control[13].number))
    board.digital[occupancy_PINS[14]].write(ctrl.occupancyCTC_dict.get(ctrl.control[14].number))
    board.digital[occupancy_PINS[15]].write(ctrl.occupancyCTC_dict.get(ctrl.control[15].number))

# Set lights on 21
def set_lights(ctrl):
    board.digital[lights_PINS[0]].write(1)#(ctrl.lights_dict.get(ctrl.control[2].number)[0])
    board.digital[lights_PINS[1]].write(1)#(ctrl.lights_dict.get(ctrl.control[2].number)[1])
    board.digital[lights_PINS[2]].write(1)#(ctrl.lights_dict.get(ctrl.control[2].number)[2])
    board.digital[lights_PINS[3]].write(1)#(ctrl.lights_dict.get(ctrl.control[2].number)[3])

# Set Switch Position
def set_switch(ctrl):
    board.digital[switch_PINS].write(ctrl.switch_dict.get(ctrl.control[10].number))

# Set crossing
def set_crossing(ctrl):
    board.digital[crossing_PINS].write(ctrl.crossing_dict.get(ctrl.control[0].number))

# Reset all pins to LOW
def reset_pins():
    for i in PINS:
        board.digital[i].write(0)

# Main function
if __name__ == "__main__":

  # Instantiate controller, first list is controlled blocks second list is listened blocks
  wayside = WaysideControllerHW()

  # all pins low
  reset_pins()


  # receive info from Elissa, calls update automatically
  wayside.receive()

  wayside.merge_dicts()


  # Instantiate PLC
  plc = PLCInterpreter()

  # Choose PLC
  while True:
      try:
          in_plcChoice = int(input("Enter 1 to use the default hardware PLC, enter 2 to enter your own filepath: "))
          if (in_plcChoice >= 1) and (in_plcChoice <= 2):
              break
      except Exception as e:
          print("Invalid input, try again")

  # run PLC with correct path
  if (in_plcChoice == 1):
    plc.runPLC(r"C:\Users\Mike\Documents\GitHub\train-system\HWTrack\hwPLC.txt", wayside)
  elif (in_plcChoice == 2):
    while True:
        try:
            in_path = int(input("Enter COMPLETE filepath of PLC as a string: "))
            if (type(in_path) == str):
                break
        except Exception as e:
            print("Invalid input type, try again")

  # merge dictionaries
  wayside.merge_dicts()


  # send info to elissa
  wayside.send_dicts()


  # set LEDs according to data
  set_authority(wayside)
  set_commandedSpeed(wayside)
  set_occupancy(wayside)
  set_lights(wayside)
  set_switch(wayside)
  set_crossing(wayside)


  sleep(10)
  reset_pins()


  while True:
      try:
          in_test = int(input("Enter 1 to test, enter 2 to quit: "))
          if (in_test >= 1) and (in_test <= 2):
              break
      except Exception as e:
          print("Invalid input, try again")

  if (in_test == 1):
    while True:
      testInterface()

  # merging my info and sending to Elissa
  #wayside.merge_and_send_dicts()
