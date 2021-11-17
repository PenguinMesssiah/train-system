'''
Last Updated: Oct 12, 2021
@author: Will
'''

# Imports
import sys
from models import trackBlock, trackSwitch
from PyQt5.QtWidgets import QDialog, QApplication
from ui.trackModel_mainPage import Ui_Dialog
from services import formBuilderService, trackBuilderService


# Application Window Definition
class AppWindow(QDialog):
        def __init__(self):
            super().__init__()
            self.ui = Ui_Dialog()
            self.ui.setupUi(self)
            self.show()
            #Connections to Backend
            #Connecting uploadTrackButton to Intializing Form Data
            self.ui.uploadTrackButton.clicked.connect(lambda: self.uploadButtonClicked())
            
            #Connecting Power Failure Buttons
            self.ui.powerFailureButton.clicked.connect(lambda: self.updatePowerFailure())
            self.ui.brokenRailFailureButton.clicked.connect(lambda: self.updateBrokenRailFailure())
            self.ui.trackCircuitFailureButton.clicked.connect(lambda: self.updateTrackCircuitFailure())

            #Connecting Spin Boxes
            self.ui.blockSelectSpinBox.valueChanged['int'].connect(lambda: self.updateGlobalBlock())
            self.ui.swSelectSpinBox.valueChanged['int'].connect(lambda: self.updateGlobalSwitch())
            
        #Intializing Data
        def uploadButtonClicked(self):
            trackBuilderService.readTrackFile()
            formBuilderService.initalizeLCDs(self)
            formBuilderService.updateScrollArea(self)
        
        def updateGlobalBlock(self):
            print('\n\nSelected Block Number Equals: ', self.ui.blockSelectSpinBox.value())
            formBuilderService.updateBlockLCDs(self, self.ui.blockSelectSpinBox.value())

        def updateGlobalSwitch(self):
            print('\n\nSelected Switch Element Id Equals: ', self.ui.swSelectSpinBox.value())
            formBuilderService.updateSwitchLCDs(self, self.ui.swSelectSpinBox.value())

        #Updating Failure States
        def updatePowerFailure(self):
            trackBuilderService.writeFailureState(self.ui.blockSelectSpinBox.value(), 1)
            formBuilderService.updateFailureLCDs(self, self.ui.blockSelectSpinBox.value())
        def updateBrokenRailFailure(self):
            trackBuilderService.writeFailureState(self.ui.blockSelectSpinBox.value(), 0)
            formBuilderService.updateFailureLCDs(self, self.ui.blockSelectSpinBox.value())
        def updateTrackCircuitFailure(self):
            trackBuilderService.writeFailureState(self.ui.blockSelectSpinBox.value(), 2)
            formBuilderService.updateFailureLCDs(self, self.ui.blockSelectSpinBox.value())                  

app    = QApplication(sys.argv)
window = AppWindow()
window.show()

sys.exit(app.exec_())