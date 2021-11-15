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
            self.ui.uploadTrackButton.clicked.connect(self.uploadButtonClicked)
           
            self.ui.lcdBlockSize.update(self.updateGlobalBlock(self.ui.blockSelectSpinBox.value))
            #self.ui.Dialog.update.connect(self.updateGlobalSwitch(self.ui.swSelectSpinBox.value))
            
        def uploadButtonClicked(self):
            trackBuilderService.readTrackFile()
            formBuilderService.initalizeLCDs(window)
            formBuilderService.updateScrollArea(window)
        
        def updateGlobalBlock(self, blockNumber: int):
            print('\n\nBlock Number Equals: ', blockNumber)
            #formBuilderService.updateBlockLCDs(blockNumber)

        def updateGlobalSwitch(self, elementId: int):
            formBuilderService.updateSwitchLCDs(elementId)
                    
                    
app    = QApplication(sys.argv)
window = AppWindow()
window.show()

sys.exit(app.exec_())