from train_functions import Train_Functions
from block import Block
from train import Train
from common import *
from train_model_ui import Ui_TrainModel
from PyQt5 import QtCore
from connections import connect
import time

class TrainModel_UnitTests:

    def __init__(self):

        tempBlock1 = Block("A1", 50, 0.25, 0.5, "", "")
        tempBlock2 = Block("A2", 50, 0.5, 1, "", "")
        tempBlock3 = Block("A3", 50, 0.75, 1.5, "", "")
        tempBlock4 = Block("B4", 50, 1, 2, "", "")
        tempBlock5 = Block("B5", 50, 0.75, 1.5, "", "")
        tempBlock6 = Block("B6", 50, 0.5, 1, "", "")
        tempBlock7 = Block("C7", 75, 0.38, 0.5, "Shadyside", "arrived_at_station")
        tempBlock8 = Block("C8", 75, 0, 0 ,"", "")

        self.tempList = []
        self.tempList.append(tempBlock1)
        self.tempList.append(tempBlock2)
        self.tempList.append(tempBlock3)
        self.tempList.append(tempBlock4)
        self.tempList.append(tempBlock5)
        self.tempList.append(tempBlock6)
        self.tempList.append(tempBlock7)
        self.tempList.append(tempBlock8)
        self.tempList2 = self.tempList.copy()

        self.tempTrackCircuit = Track_Circuit_Data(450, 40)

        self.unit_test_1()
        self.unit_test_2()
        self.unit_test_3()


    def unit_test_1(self):
        # Test kinematics and moving from block to block
        print("Unit Test 1 running...")

        train = Train_Functions(0, False)

        train.dispatch_train("Shadyside", self.tempList, self.tempTrackCircuit)
        train.update_continuously(0, 5)

        assert train.trainList[0].destination == "Shadyside", "Destination is incorrect, should be Shadyside"
        assert train.trainList[0].power == 5000, "Power is incorrect, should be 5000"
        assert train.trainList[0].position == 75, "End position is incorrect, should be 75"
        assert train.destination_reached, "Train destination not reached"
        
        print("Unit Test 1 complete")


    def unit_test_2(self):
        # Test station functions
        print("Unit Test 2 running...")

        train = Train_Functions(0, False)

        train.dispatch_train("Shadyside", self.tempList, self.tempTrackCircuit)
        train.receive_lights(0, True)
        train.receive_door(0, "left")
        train.receive_serviceBrake(0)
        train.receive_temperature(0, 70.5)
        train.receive_beacon(0, "Shadyside")

        assert train.trainList[0].lights, "Lights are incorrect, should be true"
        assert train.trainList[0].doors == [True, False], "Doors are incorrect, left should be open (true, false)"
        assert train.trainList[0].serviceBrake, "Service brake is incorrect, should be engaged (true)"
        assert train.trainList[0].temperature == 70.5, "Temperature is incorrect, should be 70.5"
        assert train.trainList[0].beacon == "Shadyside", "Beacon is incorrect, should be Shadyside"

        print("Unit Test 2 complete")


    def unit_test_3(self):
        # Test failures
        print("Unit Test 3 running...")
        
        train = Train_Functions(0, False)

        train.dispatch_train("Shadyside", self.tempList2, self.tempTrackCircuit)
        train.receive_engineFailure(0)
        train.update_kinematics(0, 5)

        assert train.trainList[0].power == 0, "Power is incorrect, should be 0"
        assert train.trainList[0].position == 0, "Position is incorrect, should be 0"
        assert train.trainList[0].currentSpeed == 0, "Current Speed is incorrect, should be 0"

        train.receive_engineFailure(0)
        train.update_kinematics(0, 5)

        assert train.trainList[0].power == 5000, "Power is incorrect, should be 5000"
        assert train.trainList[0].position > 0, "Position is incorrect, should be >0"
        assert train.trainList[0].currentSpeed > 0, "Current Speed is incorrect, should be >0"

        train.receive_brakeFailure(0)
        train.receive_serviceBrake(0)
        
        assert train.trainList[0].serviceBrake == False, "Service brake is incorrect, should be false"

        print("Unit Test 3 complete")


test = TrainModel_UnitTests()