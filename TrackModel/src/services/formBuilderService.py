'''
Last Updated: Oct 13, 2021
@author: Will Scott
'''
#imports
from models.trackBlock import trackBlock
from models.trackSwitch import trackSwitch
from services import trackBuilderService
from PyQt5.QtWidgets import QDialog, QLCDNumber, QFormLayout, QLabel, QGroupBox,\
    QVBoxLayout, QScrollArea, QWidget
from PyQt5.QtCore import Qt
      
#Service for Updating Form Fields on the UI

def initalizeLCDs(window: QDialog):
    trackList = trackBuilderService.readDatabase()

    #Iterate through all the LCD Numbers
    children = window.findChildren(QLCDNumber)
    for child in children:
        if(child.objectName() == 'lcdBlockSize'):
            child.display(trackList[0].size)
            
        elif(child.objectName() == 'lcdGrad'):
            child.display(trackList[0].gradLevel)   
            
        elif(child.objectName() == 'lcdElev'):
            child.display(trackList[0].elev)
        
        elif(child.objectName() == 'lcdStationOccupancy'):
            child.display(0)

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

#Updating the Switch LCDs
def updateSwitchLCDs(window: QDialog, elementId: int):
    trackList = trackBuilderService.readDatabase()

    #Find the Switch
    startBlock  = 0;   
    endBlockOne = 0;   
    endBlockTwo = 0;   
    position    = 0; 

    for curObject in trackList:
        if(curObject.objType == 'Switch'):
            print('\nCur Object Type = ', curObject.objType)
            print('\nCur Object Element Id = ', curObject.elementId)
            print('\nCur Element Id = ', elementId)
            print('------------------------------')
        
        if(curObject.objType == 'Switch' and curObject.elementId == elementId):
            print('\n\nmade it')    

        if(curObject.objType == 'Switch'):
            startBlock  = curObject.startBlock
            endBlockOne = curObject.endBlockOne
            endBlockTwo = curObject.endBlockTwo
            position    = curObject.position
            

    #Iterate through all the LCD Numbers
    children = window.findChildren(QLCDNumber)
    for child in children:
        if(child.objectName() == 'lcdStartBlock'):
            child.display(startBlock)
            
        elif(child.objectName() == 'lcdEndBlockOne'):
            child.display(endBlockOne)
            
        elif(child.objectName() == 'lcdEndBlockTwo'):
            child.display(endBlockTwo)   
            
        elif(child.objectName() == 'lcdPosition'):
            child.display(position)
    
    return 0

def updateFailureLCDs(window: QDialog, blockNumber:int):
    trackList = trackBuilderService.readDatabase()
    
    #Find the Block
    failureBR = 0
    failureTC = 0
    failurePF  = 0
    for curObject in trackList:
        if(curObject.objType == 'Block' and curObject.blockNumber == blockNumber):
            failureBR = curObject.failureBR
            failureTC = curObject.failureTC
            failurePF = curObject.failurePF

    #Iterate through all the LCD Numbers
    children = window.findChildren(QLCDNumber)
    for child in children:
        if(child.objectName() == 'lcdBrokenRail'):
            child.display(failureBR)
        elif(child.objectName() == 'lcdTrackCircuit'):
            child.display(failureTC)
        elif(child.objectName() == 'lcdPower'):
            child.display(failurePF)

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
        if(child.objectName() == 'scrollAreaWidgetContents'):
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

#Method for Updating Station Occupancy
