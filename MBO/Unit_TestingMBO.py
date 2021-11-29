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

def main():
    #Call Test One
    unit_test_one()
    #Call Test Two
    unit_test_two()
    #Call Test Three
    unit_test_three()

if __name__ == '__main__':
    main() 

