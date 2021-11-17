from pyfirmata import ArduinoMega
from time import sleep
import numpy as np
import pandas as pd
import re

# Declare board variable
board = ArduinoMega("COM3", baudrate=57600)

# Declare list of all 27 pins that are in use
PINS = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53]

# Declare lists/variables of pins for each key input/output, from MSB-->LSB
#speedLimit = [8, 7, 6, 5, 4, 3]
#suggestedSpeed = [50, 13, 12, 11, 10, 9]
#switchPosition_TrackModel = 41
#railFailure = 40
#trackCircuitFailure = 39
#powerFailure = 38

lights = 40
switch = 39
crossing = 38
authority = [4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
commandedSpeed = [53, 52, 51, 50]
occupancy = [49, 48, 47, 46, 45, 44, 43, 42, 41, 3]

# Declare booleans/tokens
switchOn = True

# Declare counters
demoTrainCounter = 0

# Declare input variables as values that will not allow the test interface to continue
in_switchPosition_CTC = 0
in_switchPosition_TrackModel = 0





# Setting methods all I/O's
# Set Authority Limit
#def set_authorityLimit(lim):
#    binLim = np.binary_repr(lim, width=3)
#    board.digital[authorityLimit[0]].write(int(binLim[0]))
#    board.digital[authorityLimit[1]].write(int(binLim[1]))
#    board.digital[authorityLimit[2]].write(int(binLim[2]))

# Set Speed Limit
#def set_speedLimit(lim):
#    binLim = np.binary_repr(lim, width=6)
#    board.digital[speedLimit[0]].write(int(binLim[0]))
#    board.digital[speedLimit[1]].write(int(binLim[1]))
#    board.digital[speedLimit[2]].write(int(binLim[2]))
#    board.digital[speedLimit[3]].write(int(binLim[3]))
#    board.digital[speedLimit[4]].write(int(binLim[4]))
#    board.digital[speedLimit[5]].write(int(binLim[5]))

# Set Suggested Speed
#def set_suggestedSpeed(sug):
#    binSug = np.binary_repr(sug, width=6)
#    board.digital[suggestedSpeed[0]].write(int(binSug[0]))
#    board.digital[suggestedSpeed[1]].write(int(binSug[1]))
#    board.digital[suggestedSpeed[2]].write(int(binSug[2]))
#    board.digital[suggestedSpeed[3]].write(int(binSug[3]))
#    board.digital[suggestedSpeed[4]].write(int(binSug[4]))
#    board.digital[suggestedSpeed[5]].write(int(binSug[5]))

# Set Switch Position from Track Model
#def set_switchPosition_TrackModel(pos):
#    binPos = np.binary_repr(pos, width=1)
#    board.digital[switchPosition_TrackModel].write(int(binPos[0]))

# Set Rail Failure
#def set_railFailure(fail):
#    binFail = np.binary_repr(fail, width=1)
#    board.digital[railFailure].write(int(binFail[0]))

# Set Track Circuit Failure
#def set_trackCircuitFailure(fail):
#    binFail = np.binary_repr(fail, width=1)
#    board.digital[trackCircuitFailure].write(int(binFail[0]))

# Set Power Failure
#def set_powerFailure(fail):
#    binFail = np.binary_repr(fail, width=1)
#    board.digital[powerFailure].write(int(binFail[0]))



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
        # Authority Limit (keep asking for input until valid one entered)
        while True:
            try:
                in_authorityLimit = int(input("Enter Authority Limit (0-7): "))
                if (in_authorityLimit >= 0) and (in_authorityLimit <= 7):
                    set_authorityLimit(in_authorityLimit)
                    break
            except Exception as e:
                print("Invalid input type, try again")
        # Speed Limit (keep asking for input until valid one entered)
        while True:
            try:
                in_speedLimit = int(input("Enter Speed Limit (0-63): "))
                if (in_speedLimit >= 0) and (in_speedLimit <= 63):
                    set_speedLimit(in_speedLimit)
                    break
            except Exception as e:
                print("Invalid input type, try again")
        # Suggested Speed (keep asking for input until valid one entered)
        while True:
            try:
                in_suggestedSpeed = int(input("Enter Suggested Speed (0-63): "))
                if (in_suggestedSpeed >= 0) and (in_suggestedSpeed <= 63):
                    set_suggestedSpeed(in_suggestedSpeed)
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
        # Switch Position from Track Model (keep asking for input until valid one entered)
        while True:
            try:
                in_switchPosition_TrackModel = int(input("Enter Switch Position from Track Model (6 or 11): "))
                if in_switchPosition_TrackModel == 6:
                    set_switchPosition_TrackModel(1)
                    break
                elif in_switchPosition_TrackModel == 11:
                    set_switchPosition_TrackModel(0)
                    break
            except Exception as e:
                print("Invalid input type, try again")
        # Rail Failure (keep asking for input until valid one entered)
        while True:
            try:
                in_railFailure = input("Rail Failure? (y/n): ")
                if in_railFailure == 'y' or in_railFailure == 'Y':
                    set_railFailure(1)
                    break
                elif in_railFailure == 'n' or in_railFailure == 'N':
                    set_railFailure(0)
                    break
            except Exception as e:
                print("Invalid input type, try again")
        # Track Circuit Failure (keep asking for input until valid one entered)
        while True:
            try:
                in_trackCircuitFailure = input("Track Circuit Failure? (y/n): ")
                if in_trackCircuitFailure == 'y' or in_trackCircuitFailure == 'Y':
                    set_trackCircuitFailure(1)
                    break
                elif in_trackCircuitFailure == 'n' or in_trackCircuitFailure == 'N':
                    set_trackCircuitFailure(0)
                    break
            except Exception as e:
                print("Invalid input type, try again")
        # Power Failure (keep asking for input until valid one entered)
        while True:
            try:
                in_powerFailure = input("Power Failure? (y/n): ")
                if in_powerFailure == 'y' or in_powerFailure == 'Y':
                    set_powerFailure(1)
                    break
                elif in_powerFailure == 'n' or in_powerFailure == 'N':
                    set_powerFailure(0)
                    break
            except Exception as e:
                print("Invalid input type, try again")
        sleep(10)
    # If the user wanted to specify which Input to change
    elif in_choiceOfTest == 2:
        # Ask the user which Input they would like to change (keep asking until valid input received)
        while True:
            try:
                in_choiceOfInput = int(input("Enter the number of the Input you would like to test (Authority Limit - 1, Speed Limit - 2, Suggested Speed - 3, Switch Position from CTC - 4, Occupancy - 5, Switch Position from Track Model - 6, Failures - 7): "))
                if (in_choiceOfInput >= 1) and (in_choiceOfInput <= 7):
                    break
            except Exception as e:
                print("Invalid input type, try again")
        if in_choiceOfInput == 1:
            # Authority Limit (keep asking for input until valid one entered)
            while True:
                try:
                    in_authorityLimit = int(input("Enter Authority Limit (0-7): "))
                    if (in_authorityLimit >= 0) and (in_authorityLimit <= 7):
                        set_authorityLimit(in_authorityLimit)
                        break
                except Exception as e:
                    print("Invalid input type, try again")
        elif in_choiceOfInput == 2:
            # Speed Limit (keep asking for input until valid one entered)
            while True:
                try:
                    in_speedLimit = int(input("Enter Speed Limit (0-63): "))
                    if (in_speedLimit >= 0) and (in_speedLimit <= 63):
                        set_speedLimit(in_speedLimit)
                        break
                except Exception as e:
                    print("Invalid input type, try again")
        elif in_choiceOfInput == 3:
            # Suggested Speed (keep asking for input until valid one entered)
            while True:
                try:
                    in_suggestedSpeed = int(input("Enter Suggested Speed (0-63): "))
                    if (in_suggestedSpeed >= 0) and (in_suggestedSpeed <= 63):
                        set_suggestedSpeed(in_suggestedSpeed)
                        break
                except Exception as e:
                    print("Invalid input type, try again")
        elif in_choiceOfInput == 4:
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
        elif in_choiceOfInput == 5:
            # Occupancy (keep asking for input until valid one entered)
            while True:
                try:
                    in_occupancy = int(input("Enter Occupancy (0-127): "))
                    if (in_occupancy >= 0) and (in_occupancy <= 127):
                        set_occupancy(in_occupancy)
                        break
                except Exception as e:
                    print("Invalid input type, try again")
        elif in_choiceOfInput == 6:
            # Switch Position from Track Model (keep asking for input until valid one entered)
            while True:
                try:
                    in_switchPosition_TrackModel = int(input("Enter Switch Position from Track Model (6 or 11): "))
                    if in_switchPosition_TrackModel == 6:
                        set_switchPosition_TrackModel(1)
                        break
                    elif in_switchPosition_TrackModel == 11:
                        set_switchPosition_TrackModel(0)
                        break
                except Exception as e:
                    print("Invalid input type, try again")
        elif in_choiceOfInput == 7:
            # Rail Failure (keep asking for input until valid one entered)
            while True:
                try:
                    in_railFailure = input("Rail Failure? (y/n): ")
                    if in_railFailure == 'y' or in_railFailure == 'Y':
                        set_railFailure(1)
                        break
                    elif in_railFailure == 'n' or in_railFailure == 'N':
                        set_railFailure(0)
                        break
                except Exception as e:
                    print("Invalid input type, try again")
            # Track Circuit Failure (keep asking for input until valid one entered)
            while True:
                try:
                    in_trackCircuitFailure = input("Track Circuit Failure? (y/n): ")
                    if in_trackCircuitFailure == 'y' or in_trackCircuitFailure == 'Y':
                        set_trackCircuitFailure(1)
                        break
                    elif in_trackCircuitFailure == 'n' or in_trackCircuitFailure == 'N':
                        set_trackCircuitFailure(0)
                        break
                except Exception as e:
                    print("Invalid input type, try again")
            # Power Failure (keep asking for input until valid one entered)
            while True:
                try:
                    in_powerFailure = input("Power Failure? (y/n): ")
                    if in_powerFailure == 'y' or in_powerFailure == 'Y':
                        set_powerFailure(1)
                        break
                    elif in_powerFailure == 'n' or in_powerFailure == 'N':
                        set_powerFailure(0)
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



# Reset all pins to LOW
def reset_pins():
    for i in PINS:
        board.digital[i].write(0)

# Set lights
def set_lights(lit):
    binLit = np.binary_repr(lit, width=1)
    board.digital[lights].write(int(binLit[0]))

# Set Switch Position
def set_switch(pos):
    binPos = np.binary_repr(pos, width=1)
    board.digital[switch].write(int(binPos[0]))

# Set crossing
def set_crossing(cro):
    binCro = np.binary_repr(cro, width=1)
    board.digital[crossing].write(int(binCro[0]))

# Set Authority
def set_authority(aut):
    binAut = np.binary_repr(aut, width=10)
    board.digital[authority[0]].write(int(binAut[0]))
    board.digital[authority[1]].write(int(binAut[1]))
    board.digital[authority[2]].write(int(binAut[2]))
    board.digital[authority[3]].write(int(binAut[3]))
    board.digital[authority[4]].write(int(binAut[4]))
    board.digital[authority[5]].write(int(binAut[5]))
    board.digital[authority[6]].write(int(binAut[6]))
    board.digital[authority[7]].write(int(binAut[7]))
    board.digital[authority[8]].write(int(binAut[8]))
    board.digital[authority[9]].write(int(binAut[9]))

# Set Commanded Speed
def set_commandedSpeed(com):
    binCom = np.binary_repr(com, width=4)
    board.digital[commandedSpeed[0]].write(int(binCom[0]))
    board.digital[commandedSpeed[1]].write(int(binCom[1]))
    board.digital[commandedSpeed[2]].write(int(binCom[2]))
    board.digital[commandedSpeed[3]].write(int(binCom[3]))

# Set Occupancy
def set_occupancy(occ):
    binOcc = np.binary_repr(occ, width=10)
    board.digital[occupancy[0]].write(int(binOcc[0]))
    board.digital[occupancy[1]].write(int(binOcc[1]))
    board.digital[occupancy[2]].write(int(binOcc[2]))
    board.digital[occupancy[3]].write(int(binOcc[3]))
    board.digital[occupancy[4]].write(int(binOcc[4]))
    board.digital[occupancy[5]].write(int(binOcc[5]))
    board.digital[occupancy[6]].write(int(binOcc[6]))
    board.digital[occupancy[7]].write(int(binOcc[7]))
    board.digital[occupancy[8]].write(int(binOcc[8]))
    board.digital[occupancy[9]].write(int(binOcc[9]))


# Continuous while-loop
while True:
    sample_authorityLimit = [1,1,1,1,1,1,1,0,0,0]
    sample_occupancy = [1,1,1,1,1,1,1,1,1,1]
    #PLC parsing
    with open('wayside2_PLC.txt') as file:
        file_contents = file.read()
    #set authority based on authorityLimit and occupancy
    # Train enters my Area of Control
    set_authority(1016)
    sleep(1)
    #Train occupies first block
    set_authority(504)
    sleep(1)
    set_authority(248)
    sleep(1)
    set_authority(120)
    sleep(1)
    set_authority(56)
    sleep(1)
    set_authority(24)
    sleep(1)
    set_authority(8)
    sleep(1)
    # arrived at station
    set_lights(1)
    set_authority(0)
    sleep(100000)



#    # SIMULATING INPUT FROM CTC OFFICE
#    # For Blue Line, Speed Limit is always 50 km/hr = 110010
#    set_speedLimit(50)
#    #For Demo purposes, assume this wayside controller is alongside block 5
#    #It is in charge of the track along blocks 4, 5, 6, and 11, so it controls the switch at block 5
#    # Therefore, highest authority this controller can give is 2 blocks
#    # Stage 1: New Train enters block 4
#    demoTrainCounter = demoTrainCounter + 1
#    # Authority = 2 to get to the end of this wayside's controlled area
#    set_authorityLimit(2)
#    # Suggested Speed = speed limit on block 4
#    set_suggestedSpeed(50)
#    # SIMULATING INPUT FROM TRACK MODEL
#    # Find a random 7-bit number for occupancy
#    set_occupancy(np.random.randint(0,128))
#    # No failures in Demo, they will just come from test interface
#    set_railFailure(0)
#    set_trackCircuitFailure(0)
#    set_powerFailure(0)
#    # Goes through this segment in 4 seconds
#    ####sleep(4)
#    # Stage 2: Train enters block 5
#    # Authority limit can only be 1 now to get to the end of this wayside's area
#    set_authorityLimit(1)
#    # Suggested Speed = slower than speed limit for smooth travel over switch
#    #  (Really just to demo that suggested speed can change)
#    set_suggestedSpeed(45)
#    # Set switch position based on switchOn boolean, then invert switchOn
#    # switchPosition = 1 --> 5-->6 position, switchPosition = 0 --> 5-->11 position
#    if switchOn:
#        set_switchPosition_CTC(1)
#        set_switchPosition_TrackModel(1)
#        switchOn = False
#    else:
#        set_switchPosition_CTC(0)
#        set_switchPosition_TrackModel(0)
#        switchOn = True
#    # Occupancy stays the same
#    # No failures
#    # Goes through this segment in 4 seconds
#    ####sleep(4)
#    # Stage 3: Train enters block 6 or block 11
#    # Authority limit must be 0 now to get to the end of this wayside's area
#    set_authorityLimit(0)
#    # Suggested Speed can go back up to the speed limit
#    set_suggestedSpeed(50)
#    # No failures, other I/O's remain the same
#    # Goes through this segment in 4 seconds, then loop starts over so a "new" train enters area of control
#    ####sleep(4)
#    # If (10) trains have gone through the wayside's area of control, begin test interface demo
#    if demoTrainCounter == 10:
#        # Repeat testInterface() test over and over for demo purposes
        while True:
            testInterface()