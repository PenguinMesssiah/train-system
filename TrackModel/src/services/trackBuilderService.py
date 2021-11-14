'''
Last Updated: October 11, 2021
@author: Will Scott
'''

# Imports
import pylightxl as xl
import xlsxwriter
from openpyxl import load_workbook

from PyQt5.QtCore           import pyqtSlot
from models.trackBlock      import trackBlock
from models.station         import station
from models.trackSwitch     import trackSwitch


# Method for Reading the Excel File containing the Track Layout
def readTrackFile() -> list:
    # Defined Variables
    trackLayout      = []
    count, rowlength = 0, 17;
    switchCount = 0;
    
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
        curTrackBlock = trackBlock(row[0], row[1], int(row[2]), int(row[3]), int(row[4]), int(row[5]), int(row [8]), int(row[9]), 'Block', 72)
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
                
                curSwitch = trackSwitch(str(switchCount), int(startBlock), int(endBlockOne), int(endBlockTwo), 0, 'Switch')
                trackLayout.append(curSwitch)
                switchCount+=1;
                
            ## Checking & Adding Station    
            elif(infraStr.find('Station') != -1):
                infraStr = infraStr.replace('Station', '')
                
                curStation = station(infraStr, 0, row[1], 'Station')
                trackLayout.append(curStation)
                print("\n---------------------Added Station: Station ", curStation.name,"-------------------")  
        
     
    print("\nSuccessfully Finished Reading the Track Layout File")
    
    # Write to Database File & Return
    writeDatabase(trackLayout);
    return trackLayout;

# Method for Writing to the Database
def writeDatabase(trackLayout: list):
    rowIndex = 0;
    
    database  = xlsxwriter.Workbook(r'C:\Users\willi\eclipse-workspace\train-system\TrackModel\src\database.xlsx');
    worksheet = database.add_worksheet();

    for curObject in trackLayout:
        if(curObject.objType == 'Block'):
        
        #Writing All of the Block Info Into Single Row
            #Track Object Specific 
            worksheet.write(rowIndex, 0, curObject.objType);    
            worksheet.write(rowIndex, 1, curObject.line);    
            worksheet.write(rowIndex, 2, curObject.section);
            worksheet.write(rowIndex, 3, curObject.blockNumber);    
            worksheet.write(rowIndex, 4, curObject.size);    
            worksheet.write(rowIndex, 5, curObject.gradLevel);    
            worksheet.write(rowIndex, 6, curObject.speedLimit);    
            worksheet.write(rowIndex, 7, curObject.elev);
            worksheet.write(rowIndex, 8, curObject.envTemp);
            #Failure States
            worksheet.write(rowIndex, 9, curObject.failureBR);
            worksheet.write(rowIndex, 10, curObject.failurePF);
            worksheet.write(rowIndex, 11, curObject.failureTC);
            #Positioning Data
            worksheet.write(rowIndex, 12, curObject.xPos);
            worksheet.write(rowIndex, 13, curObject.yPos);
            worksheet.write(rowIndex, 14, curObject.angle);

            rowIndex += 1;        
            
        elif(curObject.objType == 'Switch'):
            #Track Object Specific 
            worksheet.write(rowIndex, 0, curObject.objType);    
            worksheet.write(rowIndex, 1, curObject.elementId);    
            worksheet.write(rowIndex, 2, curObject.startBlock);
            worksheet.write(rowIndex, 3, curObject.endBlockOne);    
            worksheet.write(rowIndex, 4, curObject.endBlockTwo);    
            worksheet.write(rowIndex, 5, curObject.position);     

            rowIndex += 1;   
        
        elif(curObject.objType == 'Station'):
            #Track Object Specific 
            worksheet.write(rowIndex, 0, curObject.objType); 
            worksheet.write(rowIndex, 1, curObject.name);
            worksheet.write(rowIndex, 2, curObject.occupancy);
            worksheet.write(rowIndex, 3, curObject.section);   

            #Positioning Data
            worksheet.write(rowIndex, 12, curObject.xPos);
            worksheet.write(rowIndex, 13, curObject.yPos);  
            rowIndex += 1;   
        
    database.close();


# Method for Reading the Database
def readDatabase() -> list:
    tracklayout = [];

    db_workbook = load_workbook(r'C:\Users\willi\eclipse-workspace\train-system\TrackModel\src\database.xlsx');
    database    = db_workbook.active;
    database.title = "Track Layout Information";

    print('\n\n--------Activating Database Stream--------')
    print('\nDatabase Sheet Name = ', db_workbook.sheetnames);
    
    #Reading Database File
    for row in database.values:
        if(row[0] == 'Block'):
            curTrackBlock = trackBlock(row[1], row[2], int(row[3]), int(row[4]), int(row[5]), int(row[6]), int(row [7]), int(row[8]), row[0], 72);
            tracklayout.append(curTrackBlock);

        elif(row[0] == 'Switch'):
            curTrackSwitch = trackSwitch(row[1], int(row[2]), int(row[3]), int(row[4]), int(row[5]), row[0]);
            tracklayout.append(curTrackSwitch);

        elif(row[0] == 'Station'):
            curStation = station(row[1], int(row[2]), row[3], 'Station')
            tracklayout.append(curStation)

    print('\n--------Closing Database Stream--------')

    return tracklayout;

# Method for Adding Cartesian Grid Data for View Finder
def generatePositioningData_blueLine(trackLayout: list):
    # Variables 
    nextX = None
    nextY = None
    
    for curObject in trackLayout:
        #Loading Starting Coordinates
        if(curObject == trackLayout[0]):
            curObject.xPos = 0;
            curObject.yPos = 0;
            
            nextX = curObject.xPos + curObject.size
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
            
    writeDatabase(trackLayout); 