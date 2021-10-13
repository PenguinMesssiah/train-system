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

    train_model_send_suggestedSpeed_ctrl = pyqtSignal(int, float)

    train_model_ui_passenger_button_pressed = pyqtSignal(int)
    train_model_ui_diagnostics_button_pressed = pyqtSignal(int)

    train_model_ui_testing_button_pressed = pyqtSignal(int)


    train_model_receive_passengers = pyqtSignal(int, int)

    train_model_stop_run = pyqtSignal()


    train_model_send_testing_values = pyqtSignal(int, int, float, float, float, float, float)
    train_model_receive_blockList = pyqtSignal(list)


    train_model_diagnostics_toggleEngineFailure = pyqtSignal(int)
    train_model_diagnostics_toggleBrakeFailure = pyqtSignal(int)
    train_model_diagnostics_toggleSignalPickupFailure = pyqtSignal(int)

    diagnostics_button_pressed = pyqtSignal(str)
    train_model_receive_passenger_emergencyBrake = pyqtSignal(int, bool)
    train_model_send_emergencyBrake_passenger_UI = pyqtSignal(bool)
    train_model_update_UI_serviceBrake = pyqtSignal(bool)   # not implemented for iteraton 2
    train_model_testing_send_serviceBrake = pyqtSignal(int)

    train_model_send_failure = pyqtSignal(str, bool)

connect = Connections()