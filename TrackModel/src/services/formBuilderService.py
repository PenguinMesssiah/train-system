'''
Last Updated: Oct 13, 2021
@author: Will Scott
'''
#imports
from services import trackBuilderService
from PyQt5.QtWidgets import QDialog, QLCDNumber, QFormLayout, QLabel, QGroupBox,\
    QVBoxLayout


def updateBlockSelect(self, paramQWidget):
        trackFile = trackBuilderService.readTrackFile()
            
        formLayout = QFormLayout()
        groupBox   = QGroupBox()
        
        for trackObject in trackFile:
            if(trackObject.objType == 'Block'):
                tempObject = QLabel(str(trackObject.blockNumber))
                formLayout.addRow(tempObject)
            
        groupBox.setLayout(formLayout)
        paramQWidget.setWidget(groupBox)
        
        layout = QVBoxLayout()
        layout.addWidget(paramQWidget)
        
                
def updateLCDs(window: QDialog):
    trackList = trackBuilderService.readTrackFile()
    
    #Iterate through all the LCD Numbers
    children = window.findChildren(QLCDNumber)
    for child in children:
        if(child.objectName() == 'lcdBlockSize'):
            child.display(trackList[0].size)
            
        elif(child.objectName() == 'lcdEnvTemp'):
            child.display(trackList[0].envTemp)
            
        elif(child.objectName() == 'lcdGrad'):
            child.display(trackList[0].gradLevel)   
            
        elif(child.objectName() == 'lcdElev'):
            child.display(trackList[0].elev)        