from PyQt5.Qt import pyqtSignal
from PyQt5.QtCore import QObject
from common import *

class Connections(QObject):

    track_model_update_block_occupancy = pyqtSignal(int, int)

    train_ctrl_train_dispatched = pyqtSignal(Track_Circuit_Data)

    train_model_dispatch_train = pyqtSignal(str, int, list, Track_Circuit_Data)
    train_model_update_kinematics = pyqtSignal(str, int, float)

    train_model_update_ui_int = pyqtSignal(str, int)
    train_model_update_ui_double = pyqtSignal(str, float)
    train_model_update_ui_string = pyqtSignal(str, str)

    train_model_ui_passenger_button_pressed = pyqtSignal(int)
    diagnostics_button_pressed = pyqtSignal(str)
    train_model_receive_passenger_emergencyBrake = pyqtSignal(int, bool)
    train_model_send_emergencyBrake_passenger_UI = pyqtSignal(bool)

    train_model_send_failure = pyqtSignal(str, bool)

connect = Connections()