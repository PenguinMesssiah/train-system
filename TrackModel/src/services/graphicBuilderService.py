'''
Last Updated: Oct 12, 2021
@author: Will Scott
'''

# Imports
from PyQt5 import QtCore, QtGui, QtWidgets, Qt
from PyQt5.QtGui import QPen, QColor, QBrush
from PyQt5.QtWidgets import QGraphicsScene

from services import trackBuilderService

#Service for Updating the Track Display on the UI

#Used for More Efficient Looping
def varied_step_range(start,stop,stepiter):
    step = iter(stepiter)
    while start < stop:
        yield start
        start += next(step)
        
def insertGridLines(graphicsScene: QGraphicsScene):
    cBrush = QBrush(QColor(0, 0, 255))
    cBrush = QPen(cBrush, 1.0)
        
    #Adding X Grid Lines 
    for i in range(25):
        lineMarker = i *25 
        graphicsScene.addLine(lineMarker,0,lineMarker,1250, cBrush)
        
    #Adding Y Grid Lines
    for y in range(15):
        lineMarker = y *25
        graphicsScene.addLine(0,lineMarker,750,lineMarker, cBrush)
        
    print('\nFinished Adding Grid lines')