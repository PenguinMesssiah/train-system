from PyQt5.Qt import pyqtSignal
from PyQt5.QtCore import QObject
import common

class Connections(QObject):

    track_model_update_block_occupancy = pyqtSignal(int, int)

    train_ctrl_train_dispatched = pyqtSignal(common.Track_Circuit_Data)

    train_model_update_ui = pyqtSignal(str, int)


connect = Connections()