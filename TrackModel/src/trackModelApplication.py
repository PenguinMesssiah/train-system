'''
Last Updated: Oct 12, 2021
@author: Will
'''

# Imports
import sys, time
from models          import trackBlock, trackSwitch
from PyQt5.QtWidgets import QDialog, QApplication, QLineEdit
from PyQt5.QtCore    import pyqtSlot
from ui.trackModel_mainPage import Ui_Dialog
from services        import formBuilderService, trackBuilderService, connectionService

#Importing Connections Class
sys.path.append("..\Shared")
from connections import link

# Application Window Definition
class AppWindow(QDialog):
        def __init__(self):
            super().__init__()
            self.ui = Ui_Dialog()
            self.ui.setupUi(self)
            self.show()

            self.blockList = []
            self.trackHeater = 0
            #Connections to Backend
            #Connecting uploadTrackButton to Intializing Form Data
            self.ui.uploadTrackButton.clicked.connect(lambda: self.uploadButtonClicked())
            self.ui.stationButton.clicked.connect(lambda: self.updateStationOccupancy())
            
            #Connecting Power Failure Buttons
            self.ui.powerFailureButton.clicked.connect(lambda: self.updatePowerFailure())
            self.ui.brokenRailFailureButton.clicked.connect(lambda: self.updateBrokenRailFailure())
            self.ui.trackCircuitFailureButton.clicked.connect(lambda: self.updateTrackCircuitFailure())

            #Connecting Spin Boxes
            self.ui.blockSelectSpinBox.valueChanged['int'].connect(lambda: self.updateGlobalBlock())
            self.ui.swSelectSpinBox.valueChanged['int'].connect(lambda: self.updateGlobalSwitch())

            #Connecting Line Edit
            self.ui.envTempLineEdit.returnPressed.connect(lambda: self.enableHeater(self, self.ui.envTempLineEdit.text()))
                
            
        #Intializing Data
        def uploadButtonClicked(self):
            trackBuilderService.readTrackFile()
            formBuilderService.initalizeLCDs(self)
            formBuilderService.updateScrollArea(self)

            #Connecting to Train Model
            #link.train_model_dispatch_train()         Comes from the CTC Office
            link.train_model_receive_track_circuit.emit(0 , trackBuilderService.readDatabase())
            link.train_model_receive_blockList.emit(connectionService.retrieveBlockList()) 
            print('\n\nSuccessfully Transmitted Data to Train Model')

            #Connecting to SW Hard Wayside Controller
            link.sw_wayside_send_blockList.connect(lambda: self.receiveBlockList(self, self.blockList))
            link.track_model_send_blockOccupancy.emit(connectionService.retrieveBlockOccupancy(self.blockList))
            print('\nSuccessfully Transmitted Data to SW Hayside Controller')
        
        def updateGlobalBlock(self):
            print('\nSelected Block Number Equals: ', self.ui.blockSelectSpinBox.value())
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

        def receiveBlockList(self, pBlockList: list):
            self.blockList = pBlockList;
        
        def updateStationOccupancy(self):
            occupancy = trackBuilderService.generateTicketSales()
            self.ui.lcdStationOccupancy.display(occupancy)

        def enableHeater(self, QLineEdit: QLineEdit, lineEditValue: str):       
            if(float(lineEditValue) < 40):
                self.trackHeater = 1
                self.ui.lcdTrackHeater.display(self.trackHeater)
                print('\nTrack Heater Enabled')
            else:
                self.trackHeater = 0
                self.ui.lcdTrackHeater.display(self.trackHeater)
                print("\nTrack Heater Disabled")
            

app    = QApplication(sys.argv)
window = AppWindow()
window.show()

sys.exit(app.exec_())