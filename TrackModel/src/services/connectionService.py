# Imports
import os
import pylightxl as xl
import xlsxwriter
from openpyxl import load_workbook


from PyQt5.QtCore           import pyqtSlot
from models.trackBlock      import trackBlock
from models.station         import station
from models.trackSwitch     import trackSwitch

def retrieveBlockOccupancy(section: str) -> list:
    occupancyList = []
    #Opening Database
    path        = r"C:\Users\willi\eclipse-workspace\train-system\TrackModel\src\database.xlsx"
    assert      os.path.isfile(path) 
    db_workbook = load_workbook(path);
    database    = db_workbook.active;

    index = 0
    for row in database.values:
        index += 1
        if(row[0] == 'Block' and row[2] == section):
            occupancyList.append(row[8])

    db_workbook.save(r'C:\Users\willi\eclipse-workspace\train-system\TrackModel\src\database.xlsx')
    db_workbook.close

    return occupancyList

def setBlockOccupancyHigh(blockNumber: int):
    path        = r"C:\Users\willi\eclipse-workspace\train-system\TrackModel\src\database.xlsx"
    assert      os.path.isfile(path) 
    db_workbook = load_workbook(path);
    database    = db_workbook.active;

    rowIndex = 0
    for row in database.values:
        rowIndex+=1
        if(row[0] == 'Block' and row[3]==blockNumber):
            print('\nSuccessful Writing')
            database.cell(row=rowIndex, column= 8, value=1)
    
    db_workbook.save(r'C:\Users\willi\eclipse-workspace\train-system\TrackModel\src\database.xlsx')
    db_workbook.close

def setBlockOccupancyLow(blockNumber: int):
    path        = r"C:\Users\willi\eclipse-workspace\train-system\TrackModel\src\database.xlsx"
    assert      os.path.isfile(path) 
    db_workbook = load_workbook(path);
    database    = db_workbook.active;

    rowIndex = 0
    for row in database.values:
        rowIndex+=1
        if(row[0] == 'Block' and row[3]==blockNumber):
            database.cell(row=rowIndex, column= 8, value=0)
    
    db_workbook.save(r'C:\Users\willi\eclipse-workspace\train-system\TrackModel\src\database.xlsx')
    db_workbook.close

def setStationOccupancyHigh(name: str):
    path        = r"C:\Users\willi\eclipse-workspace\train-system\TrackModel\src\database.xlsx"
    assert      os.path.isfile(path) 
    db_workbook = load_workbook(path);
    database    = db_workbook.active;

    rowIndex = 0
    for row in database.values:
        rowIndex+=1
        if(row[0] == 'Station' and row[1]==name):
            database.cell(row=rowIndex, column= 2, value=1)
    
    db_workbook.save(r'C:\Users\willi\eclipse-workspace\train-system\TrackModel\src\database.xlsx')
    db_workbook.close

def setStationOccupancyLow(name: str):
    path        = r"C:\Users\willi\eclipse-workspace\train-system\TrackModel\src\database.xlsx"
    assert      os.path.isfile(path) 
    db_workbook = load_workbook(path);
    database    = db_workbook.active;

    rowIndex = 0
    for row in database.values:
        rowIndex+=1
        if(row[0] == 'Station' and row[1]==station):
            database.cell(row=rowIndex, column= 2, value=0)

    db_workbook.save(r'C:\Users\willi\eclipse-workspace\train-system\TrackModel\src\database.xlsx')
    db_workbook.close