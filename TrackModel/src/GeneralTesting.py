'''
Created on October 11, 2021

File for Testing Track Model Implementation
'''

import os
from services import trackBuilderService

def main():
    count = 0

    #Unit Test 1: Reading the Track File & Writing to the Database
    old_trackList = trackBuilderService.readTrackFile()

    path      = r"C:\Users\willi\eclipse-workspace\train-system\TrackModel\src\database.xlsx"
    assert    os.path.isfile(path) 

    #Unit Test 2: Reading Information from the Database
    new_trackList = trackBuilderService.readDatabase()
    
    for curObject in new_trackList:
        print('\nnew_trackList object type = ', curObject.objType, 
                '\told_trackList object type = ', old_trackList[count].objType)
        
        assert curObject.objType == old_trackList[count].objType
        count += 1

    #Unit Test 3: Generating Random Ticket Sales
    trackBuilderService.generateTicketSales()
    new_trackList = trackBuilderService.readDatabase()

    for curObject in new_trackList:
        if(curObject.objType == 'Station'):
            print('\n', curObject.name, ' Ticket Sales = ', curObject.ticketSales)
            assert curObject.ticketSales != None
            assert curObject.ticketSales != 0

if __name__ == '__main__':
    main()