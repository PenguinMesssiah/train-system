from PyQt5.Qt import pyqtSignal
from PyQt5.QtCore import QObject
from common import *

class Connections(QObject):
    
    #Essential Train Functions Here
    emergBrake = pyqtSignal(bool)
    serviceBrake = pyqtSignal(bool)
    
    modeControl = pyqtSignal()
    speedControl = pyqtSignal(int)
    
    engineControl = pyqtSignal(bool)

    #NonEssential Train Functions Here
    calculatePower = pyqtSignal(float)
    intercomOn = pyqtSignal(bool)
    intercomOff = pyqtSignal(bool)
    
    incTemp = pyqtSignal(bool)
    decTemp = pyqtSignal(bool)
    
    headlights = pyqtSignal(bool)
    cabinlights = pyqtSignal(bool)
    
    leftdoorstatus = pyqtSignal(bool)
    rightdoorstatus = pyqtSignal(bool)
    
    
connect = Connections()