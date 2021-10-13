# File:         CTC.py
# Maintainer:   Eric Trimbur
# Created:      10/12/21
# Last Updated: 10/13/21

# Template code from Alan D Moore, Master PyQt5 Series

import sys
from functools import partial
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtCore as qtc
from PyQt5 import QtGui as qtg
from PyQt5 import uic

Ui_MainGUI, MainBaseClass = uic.loadUiType('UI/MainGUI.ui')
Ui_InputDebug, InputDebugBaseClass = uic.loadUiType('UI/InputsDebug.ui')
Ui_Scheduler, SchedulerBaseClass = uic.loadUiType('UI/SchedulingGUI.ui')

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

        b12state = self.ui.b12o.checkState()
        self.ui.b12o.stateChanged.connect(partial(self.showOccupied, 12))

        b13state = self.ui.b13o.checkState()
        self.ui.b13o.stateChanged.connect(partial(self.showOccupied, 13))

        b14state = self.ui.b14o.checkState()
        self.ui.b14o.stateChanged.connect(partial(self.showOccupied, 14))

        b15state = self.ui.b15o.checkState()
        self.ui.b15o.stateChanged.connect(partial(self.showOccupied, 15))


    def showOccupied(self, block):
        targetBlock = self.parent.blocks[block-1]
        print(targetBlock.palette().color(1).rgb())
        if targetBlock.palette().color(1).rgb() == 0xFF99c1f1:
            targetBlock.setStyleSheet("background-color: orange;")
        else:
            targetBlock.setStyleSheet("background-color: #99c1f1;")



class MainWindow(MainBaseClass):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.ui = Ui_MainGUI()
        self.ui.setupUi(self)

        self.ui.actionInput_Debug.triggered.connect(self.openInputDebug);
        self.ui.actionEdit_Schedule.triggered.connect(self.openScheduling);

        self.blocks = [self.ui.block1, self.ui.block2, self.ui.block3, self.ui.block4, self.ui.block5, self.ui.block6, self.ui.block7, self.ui.block8, self.ui.block9, self.ui.block10, self.ui.block11, self.ui.block12, self.ui.block13, self.ui.block14, self.ui.block15]

        self.InputDebugWin = InputDebugWindow(self)
        self.SchedulerWin = SchedulerWindow(self)

        self.show()

    #def showOccupied(self):
        #self.blocks[0].setStyleSheet("background-color: orange;")
        

    def openInputDebug(self):
        self.InputDebugWin.show()

    def openScheduling(self):
        self.SchedulerWin.show()

if __name__ == '__main__':
    app = qtw.QApplication(sys.argv)
    w = MainWindow()
    sys.exit(app.exec_())
