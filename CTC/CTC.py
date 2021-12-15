# File:         CTC.py
# Maintainer:   Eric Trimbur
# Created:      10/12/21
# Last Updated: 11/17/21

# Template code from Alan D Moore, Master PyQt5 Series

import sys, os

from functools import partial
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtCore as qtc
from PyQt5 import QtGui as qtg
from PyQt5 import uic

sys.path.append("..")

from Shared.common import *
from Shared.connections import *
from TrainModel.Models.block import *

Ui_MainGUI, MainBaseClass = uic.loadUiType('UI/MainGUI.ui')
Ui_InputDebug, InputDebugBaseClass = uic.loadUiType('UI/InputsDebug.ui')
Ui_Scheduler, SchedulerBaseClass = uic.loadUiType('UI/SchedulingGUI.ui')

# TODO Seperate each class into its own file
class Block:

    def __init__(self, block_number, station, crossing):
        self.block_number = block_number
        self.maintenance = False
        # Station is 'none' if no station
        self.station = station
        # Crossing is -1 if no crossing
        self.crossingState = crossing

    def getBlockNumber(self):
        return self.block_number

    def getStation(self):
        return self.station

    def getCrossing(self):
        return self.crossing
    
    def setStation(self, station):
        self.station = station

class Train:

    def __init__(self, trainID, name):
        self.trainID = trainID
        self.name = name
        self.current_block = -1
        self.suggested_speed = 0
        self.authority = [0]

    def getTrainID(self):
        return self.trainID

    def getName(self):
        return self.name

    def getCurrentBlock(self):
        return self.current_block

    def setSuggestedSpeed(self, speed):
        self.suggested_speed = speed

    def setAuthority(self, authority):
        self.authority = authority

class TrainList:

    def __init__(self):
        self.trains = []

    def addTrain(self, train):
        self.trains[train.getTrainID, "train"]

    def getTrain(self, trainID):
        return self.trains[trainID]

    def setSuggestedSpeed(self, speed, trainID):
        trains[trainID].setSuggestedSpeed(speed)

    def setAuthority(self, authority, trainID):
        trains[trainID].setAuthority(authority)

class ScheduleItem:

    def __init__(self, trainID, time, target):
        self.trainID = trainID
        self.time = time
        self.target = target

    def getTrainID(self):
        return self.trainID

    def getTime(self):
        return self.time

    def getTarget(self):
        return target

class Schedule:

    def __init__(self):
        self.queue = []

    def getNextStop(self, trainID):
        for item in self.queue:
            if item.getTrainID == trainID:
                return item.getTime, item.getTarget

    def addTrainStop(self, trainID, time, target):
        self.queue.append(ScheduleItem(trainID, time, target))

class WaysidePacket:
    
    def __init__(self, packetDestination, suggestedSpeed, authority):
        self.packetDestination = packetDestination
        self.suggestedSpeed = suggestedSpeed
        self.authority = authority

class GreenLine:

    def __init__(self):
        self.trackLayout = [];
        # Sequential sections of track
        for blockNum in range(149):
            trackLoaout[blockNum] = blockNum+1


        # Yard
        trackLayout[0] = 63

        # Switches
        trackLayout[1] = {2, 13}
        trackLayout[150] = 28
        trackLayout[57] = [58, -1]
        trackLayout[77] = [78, 101]
        trackLayout[100] = 85;

#####PYQT STUFF#####
class SchedulerWindow(SchedulerBaseClass):
    
    def __init__(self, parent):
        super().__init__()

        self.parent = parent

        self.ui = Ui_Scheduler()
        self.ui.setupUi(self)

class InputDebugWindow(InputDebugBaseClass):

    def __init__(self, parent):
        super().__init__()

        self.parent = parent

        self.ui = Ui_InputDebug()
        self.ui.setupUi(self)

        b1state = self.ui.b1o.checkState()
        self.ui.b1o.stateChanged.connect(partial(self.showOccupied, 1))

        b2state = self.ui.b2o.checkState()
        self.ui.b2o.stateChanged.connect(partial(self.showOccupied, 2))
        
        b2state = self.ui.b2o.checkState()
        self.ui.b2o.stateChanged.connect(partial(self.showOccupied, 2))

        b3state = self.ui.b3o.checkState()
        self.ui.b3o.stateChanged.connect(partial(self.showOccupied, 3))

        b4state = self.ui.b4o.checkState()
        self.ui.b4o.stateChanged.connect(partial(self.showOccupied, 4))

        b5state = self.ui.b5o.checkState()
        self.ui.b5o.stateChanged.connect(partial(self.showOccupied, 5))

        b6state = self.ui.b6o.checkState()
        self.ui.b6o.stateChanged.connect(partial(self.showOccupied, 6))

        b7state = self.ui.b7o.checkState()
        self.ui.b7o.stateChanged.connect(partial(self.showOccupied, 7))

        b8state = self.ui.b8o.checkState()
        self.ui.b8o.stateChanged.connect(partial(self.showOccupied, 8))

        b9state = self.ui.b9o.checkState()
        self.ui.b9o.stateChanged.connect(partial(self.showOccupied, 9))

        b10state = self.ui.b10o.checkState()
        self.ui.b10o.stateChanged.connect(partial(self.showOccupied, 10))

        b11state = self.ui.b11o.checkState()
        self.ui.b11o.stateChanged.connect(partial(self.showOccupied, 11))

    def showOccupied(self, block):
        targetBlock = self.parent.vis_blocks[block-1]
        print(targetBlock.palette().color(1).rgb())
        if targetBlock.palette().color(1).rgb() == 0xFF99c1f1:
            targetBlock.setStyleSheet("background-color: orange;")
        else:
            targetBlock.setStyleSheet("background-color: #99c1f1;")

def deployTrain(block, route, trackCircut):

    tempTC = Track_Circuit_Data(450, 40)

    link.train_model_dispatch_train.emit("Overbrook", block, route, tempTC) 

def parseCommand(inputString):
    command = list(map(int, inputString.split()))

    #dispatch
    temp_data = [63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74]
    if command[0] == 0:
        deployTrain(63, temp_data, 0);


class MainWindow(MainBaseClass):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.ui = Ui_MainGUI()
        self.ui.setupUi(self)

        tempList = []
        block = Block("A1", 50, 0.25)
        tempList.append(block)

        self.ui.actionInput_Debug.triggered.connect(self.openInputDebug)
        self.ui.actionEdit_Schedule.triggered.connect(self.openScheduling)
        self.ui.actionDEPLOY_TRAIN.triggered.connect(lambda: deployTrain(63, tempList, 0))

        #define real blocks
        #self.blocks = []
        #for i in range(63,74):
        #    self.blocks.append(Block(i, "", ""))

        #self.blocks[65-63].setStation("Glenbury")
        #self.blocks[73-63].setStation("Dormont")

        #define visual blocks
        #self.vis_blocks = [self.ui.vis_block_63, self.ui.vis_block_64, self.ui.vis_block_64, self.ui.vis_block_66, self.ui.vis_block_67, self.ui.vis_block_68, self.ui.vis_block_69, self.ui.vis_block_70, self.ui.vis_block_71, self.ui.vis_block_72, self.ui.vis_block_73]
        
#        for i in range(63, 74):
#           self.vis_blocks[i-63].linkActivated.connect(self.updateTableInfo(i))

        self.InputDebugWin = InputDebugWindow(self)
        self.SchedulerWin = SchedulerWindow(self)

        self.show()


        #self.ui.properties_table.setItem(2, 1, qtw.QTableWidgetItem(blockNum))

    #def showOccupied(self):
        #self.blocks[0].setStyleSheet("background-color: orange;")
        
    #def updateTableInfo(self, blockNum):
        #self.ui.properties_table.setItem(2, 1, qtw.QTableWidgetItem(blockNum))
        #self.ui.properties_table.setItem(2, 3, qtw.QTableWidgetItem(self.blocks[blockNum-63].getStation()))

    def openInputDebug(self):
        self.InputDebugWin.show()

    def openScheduling(self):
        self.SchedulerWin.show()

if __name__ == '__main__':
    app = qtw.QApplication(sys.argv)
    w = MainWindow()
    sys.exit(app.exec_())
