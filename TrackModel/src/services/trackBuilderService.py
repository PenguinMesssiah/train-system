'''
Last Updated: October 10, 2021
@author: Will Scott
'''

# Imports
import pylightxl as xl

from models.trackBlock      import trackBlock
from models.station         import station
from models.trackSwitch     import trackSwitch


# Method for Reading the Excel File containing the Track Layout
def readTrackFile() -> list:
    # Defined Variables
    trackLayout      = []
    count, rowlength = 0, 17;
    
    # Opening & Reading Excel File
    database = xl.readxl(fn='C:/Users/willi/Documents/School/SystemsProjectEngineering/TrackLayoutVehicleDatavF2.xlsx')
    
    for row in database.ws(ws='Blue Line').rows:
        # Skipping first row to avoid the section headers
        count += 1
        if(count == 1):
            continue
        elif(count == rowlength):
            break;
        
        # Saving Block Information
        curTrackBlock = trackBlock(row[0], row[1], int(row[2]), int(row[3]), int(row[4]), int(row[5]), int(row [8]), int(row[9]), 'Block')
        trackLayout.append(curTrackBlock)
        
        print('\n----------------------------Added Block----------------------')
        print("\nLine = ", curTrackBlock.line)
        print("\nSection = ", curTrackBlock.section)    
        print("\nBlockNumber = ", curTrackBlock.blockNumber)
        print("\nBlockLength = ", curTrackBlock.size)    
        print("\nBlockGrade = ", curTrackBlock.gradLevel)
        print("\nSpeedLimit = ", curTrackBlock.speedLimit)    
        print("\nElevation = ", curTrackBlock.elev)
        print("\nCum. Elevation = ", curTrackBlock.cumElev)    
        
        #Check & Adding Any Infrastructure
        if(row[6] != ''):
            infraStr = row[6].replace(' ','')
            ## Checking & Adding Switch
            if(infraStr.find('Switch') != -1):
                infraStr = infraStr.replace('Switch', '')
                infraStr = infraStr[1 : len(infraStr)-1]
                
                swPosOne, swPosTwo = infraStr.rsplit(";");
                
                startBlock, endBlockOne = swPosOne.rsplit('-')
                endBlockTwo = swPosTwo.rsplit('-')[1]
                
                print("\n------------------------Added Switch---------------------------------") 
                print("\nSwitch Start Block = ", int(startBlock))
                print("\nEndBlockOne       = ", endBlockOne)
                print("\nEndBlockTwo       = ", endBlockTwo)
                
                curSwitch = trackSwitch('', int(startBlock), int(endBlockOne), int(endBlockTwo), 0, 'Switch')
                trackLayout.append(curSwitch)
            
            ## Checking & Adding Station    
            elif(infraStr.find('Station') != -1):
                infraStr = infraStr.replace('Station', '')
                
                curStation = station(infraStr, '', '', 0, row[1], 'Station')
                trackLayout.append(curStation)
                print("\n---------------------Added Station: Station ", curStation.name,"-------------------")  
        
     
    print("\nSuccessfully Finished Reading the Track Layout File")
    return trackLayout

# Method for Adding Cartesian Grid Data for View Finder
def generatePositioningData(trackLayout: list) -> list:
    # Variables 
    nextX = None
    nextY = None
    
    for curObject in trackLayout:
        #Loading Starting Coordinates
        if(curObject == trackLayout[0]):
            curObject.xPos = 0;
            curObject.yPos = 0;
            
            nextX = curObject.xPos + curObject.size
            print('\nnextX= ', nextX)
            nextY = curObject.yPos
            continue
        
        #Skipping Any Switches: No Positioning Need
        if(curObject.objType == 'Switch'):
            continue
        
        if(curObject.objType == 'Station'):
            curObject.xPos = nextX
            curObject.yPos = nextY
            continue
        
        if(curObject.section == 'A'):
            curObject.xPos = nextX
            curObject.yPos = nextY
             
        elif(curObject.section == 'B'):
            curObject.xPos = nextX
            curObject.yPos = nextY + 25
                
            if(curObject.objType == 'Block'):
                curObject.angle = 15
                
        elif(curObject.section == 'C'):
            if(curObject.blockNumber == 11):
                nextX = 250;
                nextY = 0;
                
            curObject.xPos = nextX
            curObject.yPos = nextY - 25
                
            if(curObject.objType == 'Block'):
                curObject.angle = -15
                
        nextX = curObject.xPos + curObject.size
        nextY = curObject.yPos
            
    return trackLayout;

if __name__ == '__readTrackFile__':
    readTrackFile()