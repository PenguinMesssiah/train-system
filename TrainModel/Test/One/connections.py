from PyQt5.Qt import pyqtSignal
from PyQt5.QtCore import QObject
from common import *

class Connections(QObject):

    track_model_update_block_occupancy = pyqtSignal(int, int)

    # Train Model UI signals
    train_model_update_ui_int = pyqtSignal(str, int)
    train_model_update_ui_double = pyqtSignal(str, float)
    train_model_update_ui_string = pyqtSignal(str, str)

    train_model_update_UI_serviceBrake = pyqtSignal(bool)

    train_model_ui_passenger_button_pressed = pyqtSignal(int)
    train_model_ui_diagnostics_button_pressed = pyqtSignal(int)
    train_model_ui_testing_button_pressed = pyqtSignal(int)

    # Train Model -> Train Controller
    train_model_send_failure_ctrl = pyqtSignal(str, bool)
    train_model_send_velocity_ctrl = pyqtSignal(int, bool)
    train_model_send_lights_ctrl = pyqtSignal(int, bool)
    train_model_train_dispatched_ctrl = pyqtSignal(Track_Circuit_Data)
    train_model_send_beacon_ctrl = pyqtSignal(int, Beacon_Data)

    # Train Controller -> Train Model
    train_model_update_kinematics = pyqtSignal(str, int, float)
    train_model_receive_temperature = pyqtSignal(int, float)
    train_model_toggleDoors = pyqtSignal(int, str)

    # Track Model -> Train Model
    train_model_dispatch_train = pyqtSignal(str, int, list, Track_Circuit_Data)
    train_model_receive_blockList = pyqtSignal(list)
    train_model_receive_track_circuit = pyqtSignal(int, Track_Circuit_Data)     # Includes authority and commanded speed
    train_model_receive_beacon = pyqtSignal(int, Beacon_Data)
    train_model_receive_authority = pyqtSignal(int, float)
    train_model_receive_lights = pyqtSignal(int, bool)

     # Diagnostics / Murphy interactive signals
    train_model_diagnostics_toggleEngineFailure = pyqtSignal(int)
    train_model_diagnostics_toggleBrakeFailure = pyqtSignal(int)
    train_model_diagnostics_toggleSignalPickupFailure = pyqtSignal(int)

    # Passenger interactive signals
    train_model_receive_passenger_emergencyBrake = pyqtSignal(int, bool)
    train_model_send_emergencyBrake_passenger_UI = pyqtSignal(bool)

    # Testing interactive signals
    train_model_testing_send_serviceBrake = pyqtSignal(int)
    train_model_stop_run = pyqtSignal()
    train_model_send_testing_values = pyqtSignal(int, int, float, float, float, float, float)

    # Train Model -> MBO
    train_model_send_gps_velocity_mbo = pyqtSignal(int, float, int, float)


connect = Connections()