'''
Last Updated: Oct 12, 2021
@author: willi
'''

# Imports
import sys
from PyQt5.QtWidgets import QDialog, QApplication
from ui.trackModel_mainPage import Ui_Dialog


# Application Window Definition
class AppWindow(QDialog):
        def __init__(self):
            super().__init__()
            self.ui = Ui_Dialog()
            self.ui.setupUi(self)
            self.show()
    

app    = QApplication(sys.argv)
window = AppWindow()
window.show()
sys.exit(app.exec_())