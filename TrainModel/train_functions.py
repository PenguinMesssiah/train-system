# ECE 1140 Train Model Functions
# Daniel Uebelacker

from PyQt5 import QtCore, QtGui, QtWidgets
import math
from train import Train
from block import Block
from train_model_ui import Ui_TrainModel
from datetime import datetime
from common import Track_Circuit_Data
from connections import connect

class Train_Functions:

    def __init__(self):

        self.FRICTION = 0.4
        self.GRAVITY_ACC = 9.80665               # m/s^2
        self.VELOCITY_LIMIT = 100                # m/s
        self.ACCELERATION_LIMIT = 50             # m/s^2
        self.DECELERATION_REGULAR_BRAKE = 0      # m/s^2
        self.DECELERATION_EMERGENCY_BRAKE = 2.73 # m/s^2

        self.trainList = []
        self.blockList = []

        self.update_UI()

    def update_UI(self):
        #self.displayUI.doors_text.valueChanged.connect(self.trainList[trainNum].doors)
        #self.displayUI.currentTime_text.valueChanged.connect(datetime.now().strftime("%H:%M:%S"))
        #self.displayUI.accLimit_text.valueChanged.connect(self.trainList[trainNum].accelerationLimit)

        self.timer = QtCore.QTimer()
        tempBlock1 = Block("A0", 100, 50, 20, 0, "ABC", "beacon1")
        tempBlock2 = Block("A1", 120, 60, 20, 0, "ABC", "beacon2")
        tempList = []
        tempList.append(tempBlock1)
        tempList.append(tempBlock2)
        tempTC = Track_Circuit_Data(60, 70)

        self.blockList = tempList

        self.dispatch_train(5, tempList, tempTC)
        self.timer.timeout.connect(self.update_kinematics(0, 5))
        self.timer.start(1000)

    def dispatch_train(self, destination, blockRoute, trackCircuitInput):

        dispatchedTrain = Train(destination, blockRoute)

        self.trainList.append(dispatchedTrain)

        connect.train_ctrl_train_dispatched.emit(trackCircuitInput)


    def update_kinematics(self, trainNum, power):
        
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
        trackAngle = currentBlock.trackAngle

        # For calculations
        timePeriod = 0.2

        # --------------------- FORCE CALCULATIONS ---------------------
        # --------------------------------------------------------------
        if (currentSpeed == 0):
            if (brake or emergencyBrake):
                force = 0
            else:
                force = self.FRICTION * mass * self.ACC_GRAVITY * math.cos(trackAngle)
        else:
            force = power / currentSpeed - (self.FRICTION + mass * self.ACC_GRAVITY + math.cos(trackAngle))
    
        # --------------------- ACCELERATION CALCULATIONS ---------------------
        # ---------------------------------------------------------------------
        acceleration = force / mass

        if (acceleration > self.ACCELERATION_LIMIT and not brake and not emergencyBrake):
            acceleration = self.ACCELERATION_LIMIT
        if (brake and not emergencyBrake):
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
        print("hello!")
        connect.train_model_update_ui.emit("position", position)
        connect.train_model_update_ui.emit("power", power)
        connect.train_model_update_ui.emit("velocity", velocity)
        connect.train_model_update_ui.emit("acceleration", acceleration)
        connect.train_model_update_ui.emit("blockName", currentBlock.name)
        
# ---------------------------------------------------------------------------------------------
# -------------------------------- INPUTS FROM TRACK MODEL ------------------------------------
# ---------------------------------------------------------------------------------------------
    # Receives acceleration limit from the Track Model
    def receive_accelerationLimit(self, train, accelerationLimit):
        self.trainList[train].accelerationLimit = accelerationLimit
        self.trainUI.accLimit_text.setText(str(accelerationLimit))

    # Receives authority from the Track Model
    def receive_authority(self, train, authority):
        self.trainList[train].authority = authority
        self.trainUI.authority_text.setText(str(authority))

    # Receives beacon from the Track Model
    def receive_beacon(self, train, beacon):
        self.trainList[train].beacon = beacon

    # Receive commanded speed from the Track Model
    def receive_commandedSpeed(self, train, commandedSpeed):
        self.trainList[train].commandedSpeed = commandedSpeed
        self.trainUI.commandedSpeed_text.setText(str(commandedSpeed))

    # Receive deceleration limit from the Track Model
    def receive_decelerationLimit(self, train, decelerationLimit):
        self.trainList[train].decelerationLimit = decelerationLimit
        self.trainUI.decelerationLimit_text.setText(str(decelerationLimit))

    # Receives light toggle from the Track Model
    def receive_lights(self, train, lights):
        self.trainList[train].lights = lights
        self.trainUI.lightToggle.set(lights)

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
        self.trainUI.serviceBrake_toggle.set(brake)

    # Receive emergency brake from the Train Controller or Passenger
    def receive_emergencyBrake(self, train, emergencyBrake):
        self.trainList[train].emergencyBrake = emergencyBrake
        self.trainUI.serviceBrake_toggle.set(emergencyBrake)
        
    # Receive temperature control from the Train Controller
    def receive_temperature(self, train, temperature):
        self.trainList[train].temperature = temperature
        self.trainUI.temp_text.setText(temperature)

    # Receive door open/closed from the Train Controller
    def receive_door(self, train, opened):
        self.trainList[train].doorOpened = opened

        if opened:
            self.trainUI.door_text.setText("OPEN")
        else:
            self.trainUI.door_text.setText("CLOSED")

# ---------------------------------------------------------------------------------------------
# ---------------------------- INPUTS FROM FAILURES (MURPHY) ----------------------------------
# ---------------------------------------------------------------------------------------------

    # Receive brake failure from Murphy
    def receive_brakeFailure(self, train, brakeFailure):
        self.trainList[train].brakeFailure = brakeFailure

    # Receive signal pickup failure from Murphy
    def receive_signalPickupFailure(self, train, signalPickupFailure):
        self.trainList[train].signalPickupFailure = signalPickupFailure
        
    # Receive engine failure from Murphy
    def receive_engineFailure(self, train, engineFailure):
        self.trainList[train].engineFailure = engineFailure

# ---------------------------------------------------------------------------------------------
# ----------------------- PASS THRU OUTPUTS TO TRAIN CONTROLLER -------------------------------
# ---------------------------------------------------------------------------------------------

    # Receive track circuit from the Track Model
    def receive_trackCircuit(self, train, trackCircuit):
        if (self.TrainList[train].signalPickupFailure == False):
            # Send to Train Controller
            
            # Temporary for iteration 2:
            return trackCircuit
        else:
            # Send to Train Controller

            # Temporary for iteration 2:
            trackCircuit = False
            return trackCircuit

    # Receive signal pickup failure from Murphy
    def receive_signalPickupFailure(self, train, signalPickupFailure):
        self.trainList[train].signalPickupFailure = signalPickupFailure
        
    # Receive engine failure from Murphy
    def receive_engineFailure(self, train, engineFailure):
        self.trainList[train].engineFailure = engineFailure

#functions = Train_Functions()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    TrainModel = QtWidgets.QMainWindow()
    ui = Ui_TrainModel()
    ui.setupUi(TrainModel)
    TrainModel.show()
    sys.exit(app.exec_())

