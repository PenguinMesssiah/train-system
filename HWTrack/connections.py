from PyQt5.Qt import pyqtSignal
from PyQt5.QtCore import QObject
from common import *

class Connections(QObject):


    # Inputs from CTC
    in_authorityLimit = pyqtSignal(bool)
    in_speedLimit = pyqtSignal(bool)
    in_suggestedSpeed = pyqtSignal(bool)
    in_signalStatus = pyqtSignal(bool)
    in_switchPosition = pyqtSignal(bool)

    # Inputs from Track Model
    in_occupancy = pyqtSignal(bool)


    # Outputs to CT
    out_lights = pyqtSignal(bool)
    out_switch = pyqtSignal(bool)
    out_crossing = pyqtSignal(bool)
    out_occupancy = pyqtSignal(bool)


    # Outputs to Track Model
    #out_lights = pyqtSignal(bool)
    #out_switch = pyqtSignal(bool)
    #out_crossing = pyqtSignal(bool)
    out_authority = pyqtSignal(bool)
    out_commandedSpeed = pyqtSignal(bool)


connect = Connections()
