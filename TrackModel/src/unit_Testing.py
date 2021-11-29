'''
Created on October 11, 2021

File for Testing Track Model Implementation
'''

import os
from services import trackBuilderService

#Unit Test 1: Reading the Track File & Writing to the Database
def unit_test_one():
    old_trackList = trackBuilderService.readTrackFile()

    path      = r"C:\Users\willi\eclipse-workspace\train-system\TrackModel\src\database.xlsx"
    assert    os.path.isfile(path) 

#Unit Test 2: Reading Information from the Database
def unit_test_two():
    count = 0
    old_trackList = trackBuilderService.readTrackFile()

    new_trackList = trackBuilderService.readDatabase()
    
    for curObject in new_trackList:
        print('\nnew_trackList object type = ', curObject.objType, 
                '\told_trackList object type = ', old_trackList[count].objType)
        
        assert curObject.objType == old_trackList[count].objType
        count += 1

#Unit Test 3: Generating Random Ticket Sales
def unit_test_three():
    trackBuilderService.generateTicketSales()
    new_trackList = trackBuilderService.readDatabase()

    for curObject in new_trackList:
        if(curObject.objType == 'Station'):
            print('\n', curObject.name, ' Ticket Sales = ', curObject.ticketSales)
            assert curObject.ticketSales != None
            assert curObject.ticketSales != 0

def main():
    #Call Test One
    unit_test_one()
    #Call Test Two
    unit_test_two()
    #Call Test Three
    unit_test_three()

if __name__ == '__main__':
    main()