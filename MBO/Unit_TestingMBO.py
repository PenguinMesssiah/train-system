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
    assert    trainA.getAuthority() > 742 and trainA.getAuthority() < 743

    print("\ntest 4 passed")

    trainA.setBlock(66)
    trainA.controlSpeed()
    trainA.setPosition(50)
    # move the train 50 meters down the block to see updated authority
    print("Authority Calculated as")
    print(trainA.getAuthority())
    assert    trainA.getAuthority() > 692 and trainA.getAuthority() < 693

    print("\ntest 5 passed")

    # The train has moved to the station Edgebrook and is headed towards Pioneer
    trainA.setBlock(9)
    trainA.setDBlock(2)
    trainA.controlSpeed()
    trainA.setPosition(100)

    print("Authority Calculated as")
    print(trainA.getAuthority())
    # the total distance should be 700
    # speed lim is 12.5 m/s
    # safe stopping distance is 65.10m
    # authority should be 700 - 65.10 = 634.896m
    assert    trainA.getAuthority() > 634 and trainA.getAuthority() < 635

    print("\ntest 6 passed")

    # the train just finished at station central underground. Next dest is WHITED in section F
    trainA.setBlock(141)
    trainA.setDBlock(22)
    trainA.controlSpeed()
    trainA.setPosition(50)

    print("Authority Calculated as")
    print(trainA.getAuthority())
    # the total distance should be 1859m
    # speed lim in block 141 is 5.55 m/s
    # safe stopping distance is 12.86m
    # authority should be 1859 - 12.86 = 1846.14m
    assert    trainA.getAuthority() > 1846 and trainA.getAuthority() < 1847

    print("\ntest 7 passed")

    # the train just moved to block 28, section F, still heading towards WHITED
    trainA.setBlock(28)
    trainA.controlSpeed()
    trainA.setPosition(20)

    print("Authority Calculated as")
    print(trainA.getAuthority())
    # the total distance should be 1280m
    # speed lim in block 28 is 8.33 m/s
    # safe stopping distance is 28.94m
    # authority should be 1280m - 28.94m = 1251.06m
    assert    trainA.getAuthority() > 1251 and trainA.getAuthority() < 1252

    print("\ntest 8 passed")

def main():
    #Call Test One
    #unit_test_one()
    #Call Test Two
    #unit_test_two()
    #Call Test Three
    #unit_test_three()
    #Call Test Four
    unit_test_four()
    

if __name__ == '__main__':
    main() 

