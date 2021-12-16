from PyQt5.Qt import pyqtSignal
from PyQt5.QtCore import QObject
import sys
sys.path.append("..")

from Shared.common import *

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
    train_model_send_failure_ctrl = pyqtSignal(bool,bool,bool)
    train_model_send_velocity_ctrl = pyqtSignal(float)
    train_model_send_lights_ctrl = pyqtSignal(bool, bool)
    train_model_train_dispatched_ctrl = pyqtSignal(Track_Circuit_Data)
    train_model_send_beacon_ctrl = pyqtSignal(Beacon_Data)
    train_model_send_suggestedSpeed_ctrl = pyqtSignal(int, float)

    # Train Controller -> Train Model
    train_model_update_kinematics = pyqtSignal(float, float)
    train_model_receive_temperature = pyqtSignal(int)
    train_model_toggleDoors = pyqtSignal(int, str)

    # Track Model -> Train Model
    train_model_dispatch_train = pyqtSignal(str, int, list, Track_Circuit_Data)
    train_model_receive_blockList = pyqtSignal(list)
    train_model_receive_track_circuit = pyqtSignal(int, list)     # Includes authority and commanded speed
    train_model_receive_beacon = pyqtSignal(int, Beacon_Data)
    train_model_receive_authority = pyqtSignal(int, float)
    train_model_receive_lights = pyqtSignal(int, bool)

    #Track Model -> SW Wayside
    track_model_send_blockOccupancy = pyqtSignal(dict)
    sw_wayside_send_blockList = pyqtSignal(list)

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

    # MBO -> Train Controller
    mbo_send_authority_velocity = pyqtSignal(int, float)

    # Train Controller -> MBO
    TrainControllerSendsBeaconSignal = pyqtSignal(str)

    # HW Train Controller -> SW Train Controller
    HWTrainSendsKpTo = pyqtSignal(float);
    HWTrainSendsKiTo = pyqtSignal(float);

    HWTrainSendsTempTo = pyqtSignal(bool);
    HWTrainSendsEngineTo = pyqtSignal(bool);
    HWTrainSendsAnnounceTo = pyqtSignal(bool);

    HWTrainSendsRDoorTo = pyqtSignal(bool);
    HWTrainSendsLDoorTo = pyqtSignal(bool);

    HWTrainSendsIncSpeedTo = pyqtSignal(bool);
    HWTrainSendsDecSpeedTo = pyqtSignal(bool);

    HWTrainSendsCabinLightsTo = pyqtSignal(bool);
    HWTrainSendsHeadLightsTo = pyqtSignal(bool);

    HWTrainSendsAutoModeTo = pyqtSignal(bool);
    HWTrainSendsManModeTo = pyqtSignal(bool);

    HWTrainSendsEmergBrakeTo = pyqtSignal(bool);
    HWTrainSendsServBrakeTo = pyqtSignal(bool);

    # HW Track Controller -> SW Track Controller
    hw_track_controller_send_lights_switch_crossing_commandedspeed_authority = pyqtSignal(dict, dict, dict, dict, dict)
    hw_track_controller_receive_suggestedspeed_authoritylimit_occupancyTM= pyqtSignal(dict, dict, dict)

    # SW Track Controller -> HW Track Controller
    sw_track_controller_send_suggestedspeed_authoritylimit_occupancyTM= pyqtSignal(dict, dict, dict)

    # SW Track Controller -> CTC

    # SW Track Controller -> Track Model

link = Connections()
