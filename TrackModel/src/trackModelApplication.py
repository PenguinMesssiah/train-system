'''
Last Updated: Oct 12, 2021
@author: Will
'''

# Imports
import sys
from PyQt5.QtWidgets import QDialog, QApplication,QPushButton
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
            
        def uploadButtonClicked(self):
            trackBuilderService.readTrackFile()
            formBuilderService.updateLCDs(window)
            formBuilderService.updateScrollArea(window)
                    
                    
app    = QApplication(sys.argv)
window = AppWindow()
window.show()

sys.exit(app.exec_())