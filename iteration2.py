from pyfirmata import ArduinoMega
from time import sleep
import numpy as np

# Declare board variable
board = ArduinoMega("COM3", baudrate=57600)

# Declare list of all 27 pins that are in use
PINS = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53]

# Declare lists/variables of pins for each key input/output, from MSB-->LSB
authorityLimit = [53, 52, 51]
speedLimit = [8, 7, 6, 5, 4, 3]
suggestedSpeed = [50, 13, 12, 11, 10, 9]
switchPosition_CTC = 49
occupancy = [48, 47, 46, 45, 44, 43, 42]
switchPosition_TrackModel = 41
railFailure = 40
trackCircuitFailure = 39
powerFailure = 38

# Reset all pins to LOW
def reset_pins():
    for i in PINS:
        board.digital[i].write(0)

# Setting methods all I/O's
# Set Authority Limit
def set_authorityLimit(lim):
    binLim = np.binary_repr(lim, width=3)
    board.digital[authorityLimit[0]].write(int(binLim[0]))
    board.digital[authorityLimit[1]].write(int(binLim[1]))
    board.digital[authorityLimit[2]].write(int(binLim[2]))

# Set Speed Limit
def set_speedLimit(lim):
    binLim = np.binary_repr(lim, width=6)
    board.digital[speedLimit[0]].write(int(binLim[0]))
    board.digital[speedLimit[1]].write(int(binLim[1]))
    board.digital[speedLimit[2]].write(int(binLim[2]))
    board.digital[speedLimit[3]].write(int(binLim[3]))
    board.digital[speedLimit[4]].write(int(binLim[4]))
    board.digital[speedLimit[5]].write(int(binLim[5]))

# Set Suggested Speed
def set_suggestedSpeed(sug):
    binSug = np.binary_repr(sug, width=6)
    board.digital[suggestedSpeed[0]].write(int(binSug[0]))
    board.digital[suggestedSpeed[1]].write(int(binSug[1]))
    board.digital[suggestedSpeed[2]].write(int(binSug[2]))
    board.digital[suggestedSpeed[3]].write(int(binSug[3]))
    board.digital[suggestedSpeed[4]].write(int(binSug[4]))
    board.digital[suggestedSpeed[5]].write(int(binSug[5]))

# Set Switch Position from CTC
def set_switchPosition_CTC(pos):
    binPos = np.binary_repr(pos, width=1)
    board.digital[switchPosition_CTC].write(int(binPos[0]))

# Set Occupancy
def set_occupancy(occ):
    binOcc = np.binary_repr(occ, width=7)
    board.digital[occupancy[0]].write(int(binOcc[0]))
    board.digital[occupancy[1]].write(int(binOcc[1]))
    board.digital[occupancy[2]].write(int(binOcc[2]))
    board.digital[occupancy[3]].write(int(binOcc[3]))
    board.digital[occupancy[4]].write(int(binOcc[4]))
    board.digital[occupancy[5]].write(int(binOcc[5]))
    board.digital[occupancy[6]].write(int(binOcc[6]))


# Set Switch Position from Track Model
def set_switchPosition_TrackModel(pos):
    binPos = np.binary_repr(pos, width=1)
    board.digital[switchPosition_TrackModel].write(int(binPos[0]))

# Set Rail Failure
def set_railFailure(fail):
    binFail = np.binary_repr(fail, width=1)
    board.digital[railFailure].write(int(binFail[0]))

# Set Track Circuit Failure
def set_trackCircuitFailure(fail):
    binFail = np.binary_repr(fail, width=1)
    board.digital[trackCircuitFailure].write(int(binFail[0]))

# Set Power Failure
def set_powerFailure(fail):
    binFail = np.binary_repr(fail, width=1)
    board.digital[powerFailure].write(int(binFail[0]))


# TEST "INTERFACE" FUNCTION
#make a function that asks for a bunch of inputs and then reflects those inputs on the hardware LEDs


# Continuous while-loop
while True:
    # SIMULATING INPUT FROM CTC OFFICE
    # For Blue Line, Speed Limit is always 50 km/hr = 110010
    set_speedLimit(50)
    # come up with a loop that simulates a bit of time at this station, maybe a couple hours but running at 10x speed?
    # then insert the different values and change them as time goes on
    set_authorityLimit(2)
    set_suggestedSpeed(47)
    set_switchPosition_CTC(1)
    # SIMULATING INPUT FROM TRACK MODEL
    set_occupancy(109)
    set_switchPosition_TrackModel(1)
    set_railFailure(1)
    set_trackCircuitFailure(1)
    set_powerFailure(1)
    #sleep
    sleep(1)
