from train_functions import Train_Functions
from block import Block
from train import Train
from common import *
from train_model_ui import Ui_TrainModel
from PyQt5 import QtCore
from connections import connect

class test:

    def __init__(self):

        train = Train_Functions(0)

        print("init test")
        connect.diagnostics_button_pressed.connect(self.test3)

    def test1(self):
        print("Test 1")


    def test2(self):
        print("Test 2")

    def test3(self, str):
        print("Test 3")

        # tempBlock1 = Block("A0", 50, 50000, 20, 0.5, "ABC", "beacon1")
        # tempBlock2 = Block("A1", 75, 70000, 10, 0.5, "ABC", "beacon2")
        # tempBlock3 = Block("A2", 60, 40000,  0, 0, 'A', "beacon3")
        # tempList = []
        # tempList.append(tempBlock1)
        # tempList.append(tempBlock2)
        # tempTC = Track_Circuit_Data(60, 70)

        self.blockList = tempList

        self.dispatch_train(5, tempList, tempTC)
        self.update_kinematics(0, 22)
        self.update_kinematics(0, 55)
        self.receive_commandedSpeed(0, 50)

        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.test3())
        self.timer.start(200)


Test = test()
Test.test3("yeet")
connect.diagnostics_button_pressed.connect(Test.test3)