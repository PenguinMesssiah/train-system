import time
from PlannerDisplay import Display
from TestUI import TestDisplay
from TrainControllerTest import TrainController
from PyQt5 import QtCore, QtGui, QtWidgets
from TrainDriver import Driver
from TrainClass import Train
from BlueLineSet import BlueLine
from PathSet import Path
from GreenLine import GreenLine
from RedLine import RedLine
import math
import csv
from MBO import MBO
import os

def main():
    count = 0

#Unit Test 1: Adding trains to the system. If properly added, should be 12 trains
def unit_test_one():
    import sys
    app = QtWidgets.QApplication(sys.argv)
    DisplayTestWindow = QtWidgets.QMainWindow()
    DisplayWindow = QtWidgets.QMainWindow()
    
    test_UI = TestDisplay()
    test_UI.setupUI(DisplayTestWindow)
    ##DisplayTestWindow.show()

    main_UI = Display()
    main_UI.setupUI(DisplayWindow)
    ##DisplayWindow.show()

    trainA = Train('B')
    trainB = Train('B')
    trainC = Train('B')
    trainD = Train('B')
    trainE = Train('B')
    trainF = Train('B')
    trainG = Train('B')
    trainH = Train('B')
    trainI = Train('B')
    trainJ = Train('B')
    trainK = Train('B')
    trainL = Train('B')
    MBO1 = MBO(trainA,test_UI,main_UI)
    MBO1.addTrain(trainB)
    MBO1.addTrain(trainC)
    MBO1.addTrain(trainD)
    MBO1.addTrain(trainE)
    MBO1.addTrain(trainF)
    MBO1.addTrain(trainG)
    MBO1.addTrain(trainH)
    MBO1.addTrain(trainI)
    MBO1.addTrain(trainJ)
    MBO1.addTrain(trainK)
    MBO1.addTrain(trainL)
    
    assert    len(MBO1.trainSets) ==  12

    print("\ntest 1 passed")


#Unit Test 2: Set Driver Information for a Train, deactivate driver
def unit_test_two():
    import sys
    app = QtWidgets.QApplication(sys.argv)
    DisplayTestWindow = QtWidgets.QMainWindow()
    DisplayWindow = QtWidgets.QMainWindow()
    
    test_UI = TestDisplay()
    test_UI.setupUI(DisplayTestWindow)
    ##DisplayTestWindow.show()

    main_UI = Display()
    main_UI.setupUI(DisplayWindow)
    ##DisplayWindow.show()

    trainA = Train('B')
    trainB = Train('B')
    trainC = Train('B')
    trainD = Train('B')
    trainE = Train('B')
    trainF = Train('B')
    trainG = Train('B')
    trainH = Train('B')
    trainI = Train('B')
    trainJ = Train('B')
    trainK = Train('B')
    trainL = Train('B')
    MBO1 = MBO(trainA,test_UI,main_UI)
    MBO1.addTrain(trainB)
    MBO1.addTrain(trainC)
    MBO1.addTrain(trainD)
    MBO1.addTrain(trainE)
    MBO1.addTrain(trainF)
    MBO1.addTrain(trainG)
    MBO1.addTrain(trainH)
    MBO1.addTrain(trainI)
    MBO1.addTrain(trainJ)
    MBO1.addTrain(trainK)
    MBO1.addTrain(trainL)

    Joseph = Driver("Joseph Smith",1,1,0,1,1,1,1,1)
    MBO1.trainSets[11].setDriver(Joseph)

    assert MBO1.trainSets[11].driverTrain.getStatus() == True
    MBO1.trainSets[11].driverTrain.deactivateDriver()
    assert MBO1.trainSets[11].driverTrain.getStatus() == False


    print("\ntest 2 passed")

   
##
#Unit Test 3: Generating Schedule. Check schedule was generated properly
    #Runs properly on my machine, might change if run from different location
def unit_test_three():
    import sys
    app = QtWidgets.QApplication(sys.argv)
    DisplayTestWindow = QtWidgets.QMainWindow()
    DisplayWindow = QtWidgets.QMainWindow()
    
    test_UI = TestDisplay()
    test_UI.setupUI(DisplayTestWindow)
    

    main_UI = Display()
    main_UI.setupUI(DisplayWindow)
    

    trainA = Train('B')
    trainB = Train('B')
    trainC = Train('B')
    trainD = Train('B')
    trainE = Train('B')
    trainF = Train('B')
    trainG = Train('B')
    trainH = Train('B')
    trainI = Train('B')
    trainJ = Train('B')
    trainK = Train('B')
    trainL = Train('B')
    MBO1 = MBO(trainA,test_UI,main_UI)
    MBO1.addTrain(trainB)
    MBO1.addTrain(trainC)
    MBO1.addTrain(trainD)
    MBO1.addTrain(trainE)
    MBO1.addTrain(trainF)
    MBO1.addTrain(trainG)
    MBO1.addTrain(trainH)
    MBO1.addTrain(trainI)
    MBO1.addTrain(trainJ)
    MBO1.addTrain(trainK)
    MBO1.addTrain(trainL)
    John = Driver("John Smith",1,1,1,1,1,1,1,1)
    MBO1.trainSets[0].setDriver(John)
    Roger = Driver("Roger Smith",1,1,1,1,1,1,1,1)
    MBO1.trainSets[1].setDriver(Roger)
    David = Driver("David Smith",1,1,1,1,1,1,1,1)
    MBO1.trainSets[2].setDriver(David)
    Timmy = Driver("Timmy Smith",1,1,1,1,1,1,1,1)
    MBO1.trainSets[3].setDriver(Timmy)
    Max = Driver("Max Smith",1,1,1,1,1,1,1,1)
    MBO1.trainSets[4].setDriver(Max)
    Jack = Driver("Jack Smith",1,1,1,1,1,1,1,1)
    MBO1.trainSets[5].setDriver(Jack)
    Joel = Driver("Joel Smith",1,1,1,1,1,1,1,1)
    MBO1.trainSets[6].setDriver(Joel)
    Eli = Driver("Eli Smith",1,1,1,1,1,1,1,1)
    MBO1.trainSets[7].setDriver(Eli)
    Zach = Driver("Zach Smith",1,1,1,1,1,1,1,1)
    MBO1.trainSets[8].setDriver(Zach)
    Alex = Driver("Alex Smith",1,1,1,1,1,1,1,1)
    MBO1.trainSets[9].setDriver(Alex)
    Gabe = Driver("Gabe Smith",1,1,1,1,1,1,1,1)
    MBO1.trainSets[10].setDriver(Gabe)
    Joseph = Driver("Joseph Smith",1,1,1,1,1,1,1,1)
    MBO1.trainSets[11].setDriver(Joseph)
    MBO1.makeScheduleGreen()

    path      = r"F:\train-system\MBO\schedule.csv"
    assert    os.path.isfile(path)
    print("\ntest 3 passed")

#Unit Test 4: Properly checking Authority Calculations for the Green Line
def unit_test_four():
    import sys
    app = QtWidgets.QApplication(sys.argv)
    DisplayTestWindow = QtWidgets.QMainWindow()
    DisplayWindow = QtWidgets.QMainWindow()
    
    test_UI = TestDisplay()
    test_UI.setupUI(DisplayTestWindow)
    ##DisplayTestWindow.show()

    main_UI = Display()
    main_UI.setupUI(DisplayWindow)
    ##DisplayWindow.show()

    trainA = Train('G')

    # first test will be from station glenbury to station dormont
    trainA.setBlock(65)
    trainA.setDBlock(73)
    trainA.controlSpeed()
    trainA.setPosition(200)
    print("Authority Calculated as")
    print(trainA.getAuthority())
    assert    trainA.getAuthority() > 786 and trainA.getAuthority() < 787

    print("\ntest 4 passed")

    trainA.setBlock(66)
    trainA.controlSpeed()
    trainA.setPosition(50)
    # move the train 50 meters down the block to see updated authority
    # safe stopping distance is 113.8197m
    # authority is 850 - 113.8197m = 736.18m
    print("Authority Calculated as")
    print(trainA.getAuthority())
    assert    trainA.getAuthority() > 736 and trainA.getAuthority() < 737

    print("\ntest 5 passed")

    # The train has moved to the station Edgebrook and is headed towards Pioneer
    trainA.setBlock(9)
    trainA.setDBlock(2)
    trainA.controlSpeed()
    trainA.setPosition(100)

    print("Authority Calculated as")
    print(trainA.getAuthority())
    # the total distance should be 700
    # speed lim is 12.5 m/s -> 10.625 m/s
    # safe stopping distance is 47.038m
    # authority should be 700 - 47.038 = 652.96m
    assert    trainA.getAuthority() > 652 and trainA.getAuthority() < 653

    print("\ntest 6 passed")

    # the train just finished at station central underground. Next dest is WHITED in section F
    trainA.setBlock(141)
    trainA.setDBlock(22)
    trainA.controlSpeed()
    trainA.setPosition(50)

    print("Authority Calculated as")
    print(trainA.getAuthority())
    # the total distance should be 1859m
    # speed lim in block 141 is 5.55 m/s -> 4.722m/s
    # safe stopping distance is 9.29m
    # authority should be 1859 - 9.29m = 1849.71m
    assert    trainA.getAuthority() > 1849 and trainA.getAuthority() < 1850

    print("\ntest 7 passed")

    # the train just moved to block 28, section F, still heading towards WHITED
    trainA.setBlock(28)
    trainA.controlSpeed()
    trainA.setPosition(20)

    print("Authority Calculated as")
    print(trainA.getAuthority())
    # the total distance should be 1280m
    # speed lim in block 28 is 8.33 m/s -> 7.083
    # safe stopping distance is 20.901m
    # authority should be 1280m - 20.906m = 1259.09m
    assert    trainA.getAuthority() > 1259 and trainA.getAuthority() < 1260

    print("\ntest 8 passed")
    
#Unit Test 5: Confirming that the Red Line track layout is stored properly in the classes
# if not, all vital calculations will fail
def unit_test_five():
    import sys
    app = QtWidgets.QApplication(sys.argv)
    DisplayTestWindow = QtWidgets.QMainWindow()
    DisplayWindow = QtWidgets.QMainWindow()
    
    test_UI = TestDisplay()
    test_UI.setupUI(DisplayTestWindow)
    ##DisplayTestWindow.show()

    main_UI = Display()
    main_UI.setupUI(DisplayWindow)
    ##DisplayWindow.show()

    red = RedLine()
    # there are 76 blocks, plus 1 for the yard in position 0 = 77 speeds
    assert    red.getSpeedCount() ==  77

    print("\n Speed count is correct")
    # check that speed limit at various blocks is correct after conversion
    # first block 1
    assert  red.getSpeedLimit(1) > 11 and red.getSpeedLimit(1) < 11.20

    print("\nSpeed Limit at Block 1 is correct")

    # block 17 - 55 km/hr to 15.2777 m/s
    assert  red.getSpeedLimit(17) > 15.20 and red.getSpeedLimit(17) < 15.30

    print("\nSpeed Limit at Block 17 is correct")

    # block 48 - 70 km/hr to 19.44m/s
    assert  red.getSpeedLimit(48) > 19.40 and red.getSpeedLimit(48) < 19.50

    print("\nSpeed Limit at Block 48 is correct")

    # block 49 - first block in long stretch not to be 70 km/hr. 60 km/hr to 16.667 m/s
    assert  red.getSpeedLimit(49) > 16.60 and red.getSpeedLimit(49) < 16.70

    print("\nSpeed Limit at Block 49 is correct")

    # block 51 - first of 55 km/hr blocks. the rest are also 55 km/hr. Should be 15.278 m/s
    assert  red.getSpeedLimit(51) > 15.270 and red.getSpeedLimit(51) < 15.280

    print("\nSpeed Limit at Block 51 is correct")

    # block 76 - final block. Should be 15.278 m/s
    assert  red.getSpeedLimit(76) > 15.270 and red.getSpeedLimit(76) < 15.280

    print("\nSpeed Limit at Block 76 is correct")

    print("This is the block count for the red line:")
    print(red.getBlockCount())
    # make sure every block is accounted for
    assert red.getBlockCount() == 77

    print("\n There are lengths for all 76 blocks in the Red Line and 1 for the yard")


#Unit Test 6: Properly checking Authority Calculations for the Red Line
def unit_test_six():
    import sys
    app = QtWidgets.QApplication(sys.argv)
    DisplayTestWindow = QtWidgets.QMainWindow()
    DisplayWindow = QtWidgets.QMainWindow()
    
    test_UI = TestDisplay()
    test_UI.setupUI(DisplayTestWindow)
    ##DisplayTestWindow.show()

    main_UI = Display()
    main_UI.setupUI(DisplayWindow)
    ##DisplayWindow.show()

    trainA = Train('R')

    # first test will be from a block on section E to station shadyside
    trainA.setBlock(15)
    trainA.setDBlock(7)
    trainA.controlSpeed()
    trainA.setPosition(20)
    print("Authority Calculated as")
    print(trainA.getAuthority())
    # The distance should be 620
    # At the suggested speed = 9.444 m/s
    # authority should be 620 - 37.166 m = 582.834m
    assert    trainA.getAuthority() > 582 and trainA.getAuthority() < 583

    print("\nAuthority Red Line Test 1 passed")

    
    
    
    trainA.setPosition(40)
    # move the train 20 meters down the block to see updated authority
    print("Authority Calculated as")
    print(trainA.getAuthority())
    assert    trainA.getAuthority() > 562 and trainA.getAuthority() < 563

    print("\nAuthority Red Line Test 2 passed")

    # The train has moved to the station Shadyside and is headed towards Herron Ave.
    trainA.setBlock(7)
    trainA.setDBlock(16)
    trainA.controlSpeed()
    trainA.setPosition(75)

    print("Authority Calculated as")
    print(trainA.getAuthority())
    # the total distance should be 350
    # speed sugg is 9.44
    # safe stopping distance is 37.166m
    # authority should be 350 - 37.166 = 312.834m
    assert    trainA.getAuthority() > 312 and trainA.getAuthority() < 313

    print("\nAuthority Red Line Test 3 passed")

    # the train is in the RST loop heading south to station STEEL PLAZA
    trainA.setBlock(76)
    trainA.setDBlock(35)
    trainA.controlSpeed()
    trainA.setPosition(10)

    print("Authority Calculated as")
    print(trainA.getAuthority())
    # the total distance should be 390m
    # speed lim in block 76 is 12.986
    # safe stopping distance is 70.27m
    # authority should be 390 - 70.27 = 319.73m
    assert    trainA.getAuthority() > 319 and trainA.getAuthority() < 320

    print("\nAuthority Red Line Test 4 passed")

    # the train just moved to section M after the station in section L.It is heading towards STATION SQUARE
    trainA.setBlock(61)
    trainA.setDBlock(48)
    trainA.controlSpeed()
    trainA.setPosition(0)

    print("Authority Calculated as")
    print(trainA.getAuthority())
    # the total distance should be 718.2m
    # speed lim in block 61 is 15.278 m/s -> suggested = 12.986
    # safe stopping distance is 70.266m
    # authority should be 718.2m - 70.266m = 647.934m
    assert    trainA.getAuthority() > 647 and trainA.getAuthority() < 648

    print("\nAuthority Red Line Test 5 passed")

def main():
    #Call Test One
    #unit_test_one()
    #Call Test Two
    #unit_test_two()
    #Call Test Three
    #unit_test_three()
    #Call Test Four
    unit_test_four()
    #unit_test_five()
    unit_test_six()

if __name__ == '__main__':
    main() 

