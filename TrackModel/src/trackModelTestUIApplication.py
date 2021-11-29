'''
Created on Oct 13, 2021
@author: Will Scott
'''

# Imports
import sys
from PyQt5.QtWidgets     import QDialog, QApplication
from ui.testingInterface import Ui_Dialog2

# Application Window Definition
class AppWindow(QDialog):
        def __init__(self):
            super().__init__()
            self.ui = Ui_Dialog2()
            self.ui.setupUi(self)
            self.show()
    

app    = QApplication(sys.argv)
window = AppWindow()
window.show()


sys.exit(app.exec_())