'''
Last Updated: Oct 13, 2021
@author: Will Scott
'''
#imports
from models.trackBlock import trackBlock
from services import trackBuilderService
from PyQt5.QtWidgets import QDialog, QLCDNumber, QFormLayout, QLabel, QGroupBox,\
    QVBoxLayout, QScrollArea, QWidget
from PyQt5.QtCore import Qt


def updateBlockSelect(self, paramQWidget):
        trackFile = trackBuilderService.readDatabase()
            
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
        
                
def initalizeLCDs(window: QDialog):
    trackList = trackBuilderService.readDatabase()
    
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

        elif(child.objectName() == 'lcdBrokenRail'):
            child.display(trackList[0].failureBR)
        
        elif(child.objectName() == 'lcdTrackCircuit'):
            child.display(trackList[0].failureTC)
        
        elif(child.objectName() == 'lcdPower'):
            child.display(trackList[0].failurePF)

def updateBlockLCDs(window: QDialog, blockNumber:int):
    trackList = trackBuilderService.readDatabase()

    #Find the Block
    curBlock = trackList[0]
    for curObject in trackList:
        if(curObject.objType == 'Block' and curObject.blockNumber == blockNumber):
            curBlock = curObject

    print("\n\nCurrent Block = ", curBlock.blockNumber)
    #Iterate through all the LCD Numbers
    children = window.findChildren(QLCDNumber)
    for child in children:
        if(child.objectName() == 'lcdBlockSize'):
            child.display(curBlock.size)
            
        elif(child.objectName() == 'lcdEnvTemp'):
            child.display(curBlock.envTemp)
            
        elif(child.objectName() == 'lcdGrad'):
            child.display(curBlock.gradLevel)   
            
        elif(child.objectName() == 'lcdElev'):
            child.display(curBlock.elev)

        elif(child.objectName() == 'lcdBrokenRail'):
            child.display(curBlock.failureBR)
        
        elif(child.objectName() == 'lcdTrackCircuit'):
            child.display(curBlock.failureTC)
        
        elif(child.objectName() == 'lcdPower'):
            child.display(curBlock.failurePF)

def updateSwitchLCDs(window: QDialog, elementId:int):
    trackList = trackBuilderService.readDatabase()
    
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

        elif(child.objectName() == 'lcdBrokenRail'):
            child.display(trackList[0].failureBR)
        
        elif(child.objectName() == 'lcdTrackCircuit'):
            child.display(trackList[0].failureTC)
        
        elif(child.objectName() == 'lcdPower'):
            child.display(trackList[0].failurePF)

def updateScrollArea(window: QDialog):
    trackList = trackBuilderService.readDatabase()
    children1 = window.findChildren(QScrollArea)
    children2 = window.findChildren(QWidget)

    blockVertBlock = QVBoxLayout()
    swVertBlock    = QVBoxLayout()
    signVertBlock  = QVBoxLayout()

    #Adding Track Elements to Widget List
    for curObject in trackList:
        if(curObject.objType == 'Block'):
            object = QLabel(str(curObject.blockNumber))
            blockVertBlock.addWidget(object) 

        elif(curObject.objType == 'Switch'):
            object = QLabel(str(curObject.elementId))
            swVertBlock.addWidget(object) 
        
        elif(curObject.objType == 'Station'):
            object = QLabel(curObject.name)
            signVertBlock.addWidget(object)

    #Parsing Form for the Widget Contents
    for child in children2:
        if(child.objectName() == 'blockScrollAreaWidgetContents'):
            child.setLayout(blockVertBlock)
        elif(child.objectName() == 'swScrollAreaWidgetContents'):         
            child.setLayout(swVertBlock)
        elif(child.objectName() == 'stationListScrollArea'):
            child.setLayout(signVertBlock)
    
    #Parsing Form for the Scroll Area 
    for child in children1:
        if(child.objectName() == 'blockSelScrollArea' or child.objectName() == 'swScrollArea' or child.objectName() == 'signScrollArea'):
            child.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
            child.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
            child.setWidgetResizable(True)
