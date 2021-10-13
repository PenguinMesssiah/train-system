# ECE 1140 Train Model Functions
# Daniel Uebelacker

from PyQt5 import QtCore, QtGui, QtWidgets
import math
from train import Train
from block import Block
from train_model_mainpage_ui import Ui_TrainModel
from train_model_passenger_ui import Passenger_UI
from datetime import datetime
from common import Track_Circuit_Data
from connections import connect

class Train_Functions:

    # trainNum is temporary for iteration 2, needed a quick way to get functionality
    def __init__(self, trainNum):

        connect.train_model_update_kinematics.connect(self.update_kinematics)
        connect.train_model_dispatch_train.connect(self.dispatch_train)
        connect.train_model_ui_passenger_button_pressed.connect(self.open_passenger_dialog)
        connect.train_model_receive_passenger_emergencyBrake.connect(self.receive_emergencyBrake)

        import sys

        #for i in range(len(trainList)):
        app = QtWidgets.QApplication(sys.argv)
        TrainModel = QtWidgets.QMainWindow()
        self.ui = Ui_TrainModel()
        self.ui.setupUi(TrainModel, trainNum)       # this trainNum should be temporary too
        TrainModel.show()

        self.FRICTION = 0.4
        self.GRAVITY_ACC = 9.80665               # m/s^2

        self.POWER_LIMIT = 120000                # W
        self.VELOCITY_LIMIT = 19.4444            # km/h = 70
        self.ACCELERATION_LIMIT = 0.5            # m/s^2
        self.DECELERATION_REGULAR_BRAKE = 1.2    # m/s^2
        self.DECELERATION_EMERGENCY_BRAKE = 2.73 # m/s^2

        self.PASSENGER_LIMIT = 148

        self.trainList = []
        self.blockList = []

        tempBlock1 = Block("A0", 50, 50000, 20, 0.5, "ABC", "beacon1")
        tempBlock2 = Block("A1", 75, 70000, 10, 0.5, "ABC", "beacon2")
        tempBlock3 = Block("A2", 60, 40000,  0, 0, 'A', "beacon3")
        tempList = []
        tempList.append(tempBlock1)
        tempList.append(tempBlock2)
        tempTC = Track_Circuit_Data(60, 70)
        self.dispatch_train(5, tempList, tempTC)


        #self.update_UI()

        sys.exit(app.exec_())


    def open_passenger_dialog(self, trainNum):
        print("yeezy")
        self.TM = QtWidgets.QDialog()
        self.w = Passenger_UI()
        self.w.setupUi(self.TM, trainNum)
        self.TM.show()
        #sys.exit(app.exec_())


    def dispatch_train(self, destination, blockRoute, trackCircuitInput):

        dispatchedTrain = Train(destination, blockRoute)

        self.trainList.append(dispatchedTrain)

        connect.train_ctrl_train_dispatched.emit(trackCircuitInput)


    def update_kinematics(self, trainNum, power):
        
        if power > self.POWER_LIMIT:
            power = self.POWER_LIMIT

        if self.trainList[trainNum].engineFailure:
            power = 0

        # From train class
        commandedSpeed = self.trainList[trainNum].commandedSpeed
        currentSpeed = self.trainList[trainNum].currentSpeed
        prevPosition = self.trainList[trainNum].position
        prevAcceleration = self.trainList[trainNum].acceleration
        mass = self.trainList[trainNum].mass
        brake = self.trainList[trainNum].brakeEngaged
        emergencyBrake = self.trainList[trainNum].emergencyBrake
        currentBlockNum = self.trainList[trainNum].currentBlock

        currentBlock = self.blockList[currentBlockNum]

        # From track class
        currentBlockLength = currentBlock.blockLength
        speedLimit = currentBlock.speedLimit
        slope = currentBlock.slope

        # For calculations
        timePeriod = 0.2

        # --------------------- FORCE CALCULATIONS ---------------------
        # --------------------------------------------------------------
        if (currentSpeed == 0):
            if (brake or emergencyBrake):
                force = 0
            else:
                force = self.FRICTION * mass * self.GRAVITY_ACC * math.cos(slope)
        else:
            force = power / currentSpeed - (self.FRICTION + mass * self.GRAVITY_ACC + math.cos(slope))

        if (force < 0):
            force = 0
    
        # --------------------- ACCELERATION CALCULATIONS ---------------------
        # ---------------------------------------------------------------------
        acceleration = force / mass

        if (acceleration > self.ACCELERATION_LIMIT and not brake and not emergencyBrake):
            acceleration = self.ACCELERATION_LIMIT
        elif (brake and not emergencyBrake):
            acceleration = self.DECELERATION_REGULAR_BRAKE
        elif (emergencyBrake):
            # Note, the emergency brake takes priority over regular
            acceleration = self.DECELERATION_EMERGENCY_BRAKE

        # --------------------- VELOCITY CALCULATIONS ---------------------
        # -----------------------------------------------------------------
        velocity = currentSpeed + ( (timePeriod / 2) * (acceleration + prevAcceleration) )

        if (velocity > self.VELOCITY_LIMIT):
            velocity = self.VELOCITY_LIMIT
        elif (velocity < 0):
            velocity = 0
            
        # --------------------- POSITION CALCULATIONS ---------------------
        # -----------------------------------------------------------------
        position = prevPosition + (velocity * timePeriod)

        # Move position to next block on track
        if (position > currentBlockLength):

            # Fix block length
            position -= currentBlockLength

            # Remove traveled block from list and update current block
            self.trainList[trainNum].pop(0)
            self.trainList[trainNum].currentBlock = self.blockList[0]
            currentBlock = self.blockList[0]

            # Send block occupancy to track model
            connect.track_model_update_block_occupancy.emit(trainNum, currentBlock)
        
        # Update rest of values
        self.trainList[trainNum].position = position
        self.trainList[trainNum].power = power
        self.trainList[trainNum].currentSpeed = velocity
        self.trainList[trainNum].acceleration = acceleration
        
        # Update UI
        # connect.train_model_update_ui.emit("position", position)
        # connect.train_model_update_ui.emit("power", power)
        # connect.train_model_update_ui.emit("velocity", velocity)
        # connect.train_model_update_ui.emit("acceleration", acceleration)
        # connect.train_model_update_ui.emit("blockName", currentBlock.name)

        self.ui.power_text.setText(str(power))
        self.ui.currentSpeed_text.setText(str(velocity))
        #self.ui.currentSpeed_text.setText(str(acceleration))
        self.ui.block_text.setText(str(currentBlock.name))
        
# ---------------------------------------------------------------------------------------------
# -------------------------------- INPUTS FROM TRACK MODEL ------------------------------------
# ---------------------------------------------------------------------------------------------
    # Receives acceleration limit from the Track Model
    def receive_accelerationLimit(self, train, accelerationLimit):
        self.trainList[train].accelerationLimit = accelerationLimit
        self.ui.accLimit_text.setText(str(accelerationLimit))

    # Receives authority from the Track Model
    def receive_authority(self, train, authority):
        self.trainList[train].authority = authority
        self.ui.authority_text.setText(str(authority))

    # Receives beacon from the Track Model
    def receive_beacon(self, train, beacon):
        self.trainList[train].beacon = beacon

    # Receive commanded speed from the Track Model
    def receive_commandedSpeed(self, train, commandedSpeed):
        self.trainList[train].commandedSpeed = commandedSpeed
        self.ui.commandedSpeed_text.setText(str(commandedSpeed))

    # Receive deceleration limit from the Track Model
    def receive_decelerationLimit(self, train, decelerationLimit):
        self.trainList[train].decelerationLimit = decelerationLimit
        self.ui.decelerationLimit_text.setText(str(decelerationLimit))

    # Receives light toggle from the Track Model
    def receive_lights(self, train, lights):
        self.trainList[train].lights = lights
        #self.ui.lightToggle.set(lights)

    # Receive speed limit from the Track Model
    def receive_speedLimit(self, train, speedLimit):
        self.trainList[train].speedLimit = speedLimit
        self.ui.speedLimit_text.setText(str(speedLimit))

    def receive_blockList(self, blockList):
        self.blockList = blockList

# ---------------------------------------------------------------------------------------------
# ----------------------------- INPUTS FROM TRAIN CONTROLLER ----------------------------------
# ---------------------------------------------------------------------------------------------

    # Receive brake command from the Train Controller
    def receive_brake(self, train, brake):
        self.trainList[train].brake = brake
        self.ui.serviceBrake_toggle.set(brake)

    # Receive emergency brake from the Train Controller or Passenger
    def receive_emergencyBrake(self, train, emergencyBrake):
        self.trainList[train].emergencyBrake = emergencyBrake
        print(self.trainList[train].emergencyBrake)
        #self.ui.emergencyBrake_toggle.set(emergencyBrake)
        connect.train_model_send_emergencyBrake_passenger_UI.emit(emergencyBrake)
        
    # Receive temperature control from the Train Controller
    def receive_temperature(self, train, temperature):
        self.trainList[train].temperature = temperature
        self.ui.temp_text.setText(temperature)

    # Receive door open/closed from the Train Controller
    def receive_door(self, train, opened):
        self.trainList[train].doorOpened = opened

        if opened:
            self.ui.door_text.setText("OPEN")
        else:
            self.ui.door_text.setText("CLOSED")

# ---------------------------------------------------------------------------------------------
# ---------------------------- INPUTS FROM FAILURES (MURPHY) ----------------------------------
# ---------------------------------------------------------------------------------------------

    # Receive brake failure from Murphy
    def receive_brakeFailure(self, train, brakeFailure):
        self.trainList[train].brakeFailure = brakeFailure
        self.ui.brakeFailure_set(brakeFailure)

    # Receive signal pickup failure from Murphy
    def receive_signalPickupFailure(self, train, signalPickupFailure):
        self.trainList[train].signalPickupFailure = signalPickupFailure
        self.ui.signalPickupFailure_set(signalPickupFailure)
        
    # Receive engine failure from Murphy
    def receive_engineFailure(self, train, engineFailure):
        self.trainList[train].engineFailure = engineFailure
        self.ui.engineFailure_set(engineFailure)

# ---------------------------------------------------------------------------------------------
# ---------------------------------- INPUTS FROM PASSENGER ------------------------------------
# ---------------------------------------------------------------------------------------------

    # Receive passengers from station
    def receive_passengers(self, train, passengers):
        self.trainList[train].passengers = passengers
        self.ui.passengers_text.setText(str(passengers))

# ---------------------------------------------------------------------------------------------
# ----------------------- PASS THRU OUTPUTS TO TRAIN CONTROLLER -------------------------------
# ---------------------------------------------------------------------------------------------

    # Receive track circuit from the Track Model
    def send_trackCircuit(self, train, trackCircuit):
        # Send to Train Controller if signal pickup isn't failing
        if not(self.TrainList[train].signalPickupFailure):
            connect.train_model_send_trackCircuit(trackCircuit)

    # Receive brake failure from Murphy
    def send_brakeFailure(self, train, brakeFailure):
        self.trainList[train].brakeFailure = brakeFailure
        connect.train_model_send_failure.emit("brakeFailure", brakeFailure)

    # Receive signal pickup failure from Murphy
    def send_signalPickupFailure(self, train, signalPickupFailure):
        self.trainList[train].signalPickupFailure = signalPickupFailure
        connect.train_model_send_failure.emit("signalPickupFailure", signalPickupFailure)
        
    # Receive engine failure from Murphy
    def send_engineFailure(self, train, engineFailure):
        self.trainList[train].engineFailure = engineFailure
        connect.train_model_send_failure.emit("engineFailure", engineFailure)

if __name__ == '__main__':
    functions = Train_Functions(0)

# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     TrainModel = QtWidgets.QMainWindow()
#     ui = Ui_TrainModel()
#     ui.setupUi(TrainModel)
#     TrainModel.show()
#     sys.exit(app.exec_())

