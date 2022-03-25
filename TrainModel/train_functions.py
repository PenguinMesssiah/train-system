# ECE 1140 Train Model Functions
# Daniel Uebelacker

from PyQt5 import QtCore, QtWidgets
import math, time
from datetime import datetime, timedelta
import sys
sys.path.append("..")

from Models.train                  import *
from Models.block                  import *
from UI.train_model_mainpage_ui    import Mainpage_UI
from UI.train_model_passenger_ui   import Passenger_UI
from UI.train_model_diagnostics_ui import Diagnostics_UI
from UI.train_model_testing_ui     import Testing_UI

from Shared.common import Track_Circuit_Data, Beacon_Data, Conversion, Constants
from Shared.connections import *

class Train_Functions:

    def __init__(self, trainNum, UI_mode):

        self.currentTrainNum = trainNum
        self.UI_mode = UI_mode

        self.FRICTION = 0.4
        self.GRAVITY_ACC = 9.80665               # m/s^2

        self.POWER_LIMIT = 120000                # W
        self.VELOCITY_LIMIT = 19.4444            # km/h = 70
        self.ACCELERATION_LIMIT = 0.5            # m/s^2
        self.DECELERATION_REGULAR_BRAKE = -1.2    # m/s^2
        self.DECELERATION_EMERGENCY_BRAKE = -2.73 # m/s^2

        self.PASSENGER_LIMIT = 148

        self.trainList = []
        self.blockList = []

        self.trainNum_const = 0

        # Connections
        link.train_model_receive_authority.connect(self.receive_authority)

        link.train_model_update_kinematics.connect(self.update_kinematics)
        link.train_model_dispatch_train.connect(self.dispatch_train)

        link.train_model_receive_blockList.connect(self.receive_blockList)

        link.train_model_stop_run.connect(self.stopRun)

        link.train_model_toggleDoors.connect(self.receive_door)
        

        if UI_mode == "Default" or UI_mode == "Test":
              
            link.train_model_ui_passenger_button_pressed.connect(self.open_passenger_dialog)
            link.train_model_ui_diagnostics_button_pressed.connect(self.open_diagnostics_dialog)
            link.train_model_ui_testing_button_pressed.connect(self.open_testing_dialog)

            link.train_model_testing_send_serviceBrake.connect(self.receive_serviceBrake)

            link.train_model_diagnostics_toggleEngineFailure.connect(self.receive_engineFailure)
            link.train_model_diagnostics_toggleBrakeFailure.connect(self.receive_brakeFailure)
            link.train_model_diagnostics_toggleSignalPickupFailure.connect(self.receive_signalPickupFailure)

            link.train_model_receive_passenger_emergencyBrake.connect(self.receive_emergencyBrake)

            link.train_model_send_testing_values.connect(self.receive_testing_values)

            import sys

            #for i in range(len(trainList)):
            self.app = QtWidgets.QApplication(sys.argv)
            TrainModel = QtWidgets.QMainWindow()
            self.ui = Mainpage_UI()
            self.ui.setupUi(TrainModel, trainNum)       # this trainNum should be temporary too
            TrainModel.show()

            self._translate = QtCore.QCoreApplication.translate

            self.already_run = False
            self.run_continously = True

            sys.exit(self.app.exec_())



    def open_passenger_dialog(self, trainNum):
        self.passenger_dialog = QtWidgets.QDialog()
        self.passenger_ui = Passenger_UI()
        self.passenger_ui.setupUi(self.passenger_dialog, trainNum)
        self.passenger_dialog.show()


    def open_diagnostics_dialog(self, trainNum):
        self.diagnostics_dialog = QtWidgets.QDialog()
        self.dialog_ui = Diagnostics_UI()
        self.dialog_ui.setupUi(self.diagnostics_dialog, trainNum)
        self.diagnostics_dialog.show()


    def open_testing_dialog(self, trainNum):
        self.testing_dialog = QtWidgets.QDialog()
        self.testing_ui = Testing_UI()
        self.testing_ui.setupUi(self.testing_dialog, trainNum)
        self.testing_dialog.show()


    def receive_testing_values(self, trainNum, passengers, temperature, suggestedSpeed, commandedSpeed, speedLimit, power):
        tempList = []
        tempList.append(Block("A1", 50, 0.25, 0.5, "Shadyside", ""))
        tempList.append(Block("A2", 50, 0.5, 1, "Shadyside", ""))
        tempList.append(Block("A3", 50, 0.75, 1.5, "Shadyside", ""))
        tempList.append(Block("B4", 50, 1, 2, "Shadyside", ""))
        tempList.append(Block("B5", 50, 0.75, 1.5, "Shadyside", ""))
        tempList.append(Block("B6", 50, 0.5, 1, "Shadyside", ""))
        tempList.append(Block("C7", 75, 0.38, 0.5, "Shadyside", "arrived_at_station"))
        tempList.append(Block("C8", 75, 0, 0 ,"", ""))

        tempTrackCircuit = Track_Circuit_Data(450, 40)

        # Give time for old run to end and new to start
        if self.already_run:
            self.run_continously = False
            time.sleep(Constants.TIME_PERIOD*2)
            self.run_continously = True

        self.ui.trainNum_text.setText(str(self.trainNum_const))
        self.trainNum_const = self.trainNum_const + 1

        self.dispatch_train("Shadyside", tempList, tempTrackCircuit)
        
        self.receive_passengers(trainNum, passengers)
        self.receive_temperature(trainNum, temperature)
        self.receive_suggestedSpeed(trainNum, Conversion.mph_to_ms(suggestedSpeed))
        self.receive_commandedSpeed(trainNum, Conversion.mph_to_ms(commandedSpeed))
        self.receive_speedLimit(trainNum, Conversion.mph_to_ms(speedLimit))

        self.ui.power_text.setText(str(round(power)))
        self.update_continuously(trainNum, power)
        self.run_continously = True


    def stopRun(self):
        self.run_continously = False


    def receive_blockList(self, blockList):
        self.blockList = blockList


    def dispatch_train(self, destination, blockRoute, trackCircuitInput):

        dispatchedTrain = Train(destination, blockRoute)
        self.blockList = blockRoute
        self.trainList.append(dispatchedTrain)

        # Update departure time
        self.ui.departureTime_text.setText(time.strftime("%H:%M:%S"))
        self.ui.arrivalTime_text.setText((datetime.now() + timedelta(hours=1)).strftime("%H:%M:%S"))

        link.train_model_train_dispatched_ctrl.emit(trackCircuitInput)


    def update_continuously(self, trainNum, power):  
        self.already_run = True 

        self.timer = QtCore.QTimer()
        self.update_continuously_trainNum = trainNum
        self.update_continuously_power = power
        self.timer.timeout.connect(self.update_continuously_kinematics)
        self.timer.start(int(Constants.TIME_PERIOD*100)) # in ms, so x 100
        
        self.timer2 = QtCore.QTimer()
        self.timer2.timeout.connect(self.update_time)
        self.timer2.start(int(Constants.TIME_PERIOD*100))

    def update_time(self):
        self.ui.currentTime_text.setText(time.strftime("%H:%M:%S"))

    # temp for iteration 2
    def update_continuously_kinematics(self):
        self.update_kinematics(self.update_continuously_trainNum, self.update_continuously_power)
        

    def update_kinematics(self, trainNum, power):
        if self.run_continously:

            # Convert from kW to W
            power = power*1000

            # Cap at power limit
            if power > self.POWER_LIMIT:
                power = self.POWER_LIMIT

            # Can't run if engine isn't working
            if self.trainList[trainNum].engineFailure:
                power = 0

            # From train class
            currentSpeed = self.trainList[trainNum].currentSpeed
            prevPosition = self.trainList[trainNum].position
            prevAcceleration = self.trainList[trainNum].acceleration
            mass = self.trainList[trainNum].mass
            brake = self.trainList[trainNum].serviceBrake
            emergencyBrake = self.trainList[trainNum].emergencyBrake
            currentBlockNum = self.trainList[trainNum].currentBlock

            run = True
            # If blocklist exists, set current block
            if len(self.blockList) > 0:
                if self.blockList[0].beacon == "":
                    currentBlock = self.blockList[0]
                    currentBlockLength = currentBlock.blockLength
                    slope = currentBlock.slope
                    self.ui.nextStation_text.setText(self.blockList[1].station)
                    run = True
                else:
                    self.run_continously = False
                    run = False
            else:
                # Stop running
                self.run_continously = False
                run = False

            # For calculations
            timePeriod = Constants.TIME_PERIOD 

            if run:
                # --------------------- FORCE CALCULATIONS ---------------------
                # --------------------------------------------------------------
                if (brake or emergencyBrake or power == 0):
                    force = 0
                else:
                    if (currentSpeed == 0):
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
                elif (self.trainList[trainNum].doors[0] or self.trainList[trainNum].doors[1]):
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

                #Move position to next block on track
                if (position > currentBlockLength):
                    
                    # This if statement is only for testing, not needed for functionality
                    if len(self.blockList) <= 1:
                        self.blockList.pop(0)
                        position = currentBlockLength

                        self.destination_reached = True
                        self.run_continously = False
                    else:
                        # Fix block length
                        position -= currentBlockLength

                        # Remove traveled block from list and update current block
                        self.blockList.pop(0)
                        self.trainList[trainNum].currentBlock = self.blockList[0]
                        currentBlock = self.blockList[0]
                        #self.currentBlockNum += 1

                        # Send block occupancy to track model
                        link.track_model_update_block_occupancy.emit(trainNum, currentBlock)
                
                # Update rest of values
                self.trainList[trainNum].position = position
                self.trainList[trainNum].power = power
                self.trainList[trainNum].currentSpeed = velocity
                self.trainList[trainNum].acceleration = acceleration

                # Send position and velocity to MBO
                link.train_model_send_gps_velocity_mbo.emit(trainNum, position, currentBlock, velocity)
                
            # Update UI
            # connect.train_model_update_ui.emit("position", position)
            # connect.train_model_update_ui.emit("power", power)
            # connect.train_model_update_ui.emit("velocity", velocity)
            # connect.train_model_update_ui.emit("acceleration", acceleration)
            # connect.train_model_update_ui.emit("blockName", currentBlock.name)

                if self.UI_mode:
                    self.ui.power_text.setText(str(power))
                    self.ui.currentSpeed_text.setText(str(Conversion.ms_to_mph(velocity)) + " mph")
                    #self.ui.currentSpeed_text.setText(str(acceleration))
                    self.ui.block_text.setText(str(currentBlock.name))
        
# ---------------------------------------------------------------------------------------------
# -------------------------------- INPUTS FROM TRACK MODEL ------------------------------------
# ---------------------------------------------------------------------------------------------
    # Receives acceleration limit from the Track Model
    def receive_accelerationLimit(self, train, accelerationLimit):
        self.trainList[train].accelerationLimit = accelerationLimit
        self.ui.accLimit_text.setText(str(Conversion.ms_to_mph(accelerationLimit)))

    # Receives authority from the Track Model
    def receive_authority(self, train, authority):
        self.trainList[train].authority = authority
        self.ui.authority_text.setText(str(Conversion.meters_to_feet(authority)))

    # Receives beacon from the Track Model
    def receive_beacon(self, train, beacon):
        self.trainList[train].beacon = beacon

    # Receive suggested speed from the Track Model
    def receive_suggestedSpeed(self, train, suggestedSpeed):
        link.train_model_send_suggestedSpeed_ctrl.emit(train, suggestedSpeed)
        self.ui.suggestedSpeed_text.setText(str(Conversion.ms_to_mph(suggestedSpeed)))

    # Receive deceleration limit from the Track Model
    def receive_decelerationLimit(self, train, decelerationLimit):
        self.trainList[train].decelerationLimit = decelerationLimit
        self.ui.decelerationLimit_text.setText(str(Conversion.ms_to_mph(decelerationLimit)))

    # Receives light toggle from the Track Model
    def receive_lights(self, train, lights):
        self.trainList[train].lights = lights
        #self.ui.lightToggle.set(lights)

    # Receive speed limit from the Track Model
    def receive_speedLimit(self, train, speedLimit):
        self.trainList[train].speedLimit = speedLimit
        self.ui.speedLimit_text.setText(str(Conversion.ms_to_mph(speedLimit)))

    def receive_blockList(self, blockList):
        self.blockList = blockList

# ---------------------------------------------------------------------------------------------
# ----------------------------- INPUTS FROM TRAIN CONTROLLER ----------------------------------
# ---------------------------------------------------------------------------------------------

    # Receive brake command from the Train Controller
    # def receive_serviceBrake(self, train, brake):
    #     self.trainList[train].brake = brake
    #     #self.ui.serviceBrake_toggle.set(brake)
    #     connect.train_model_send_serviceBrake_UI.emit(brake)
    #     if brake:
    #         self.ui.serviceBrakes_indicator.setText(self._translate("TrainModel", "<html><head/><body><p><span style=\" color:#ff0004;\">Engaged</span></p></body></html>"))
    #     else:
    #         self.ui.serviceBrakes_indicator.setText("Disengaged")

    #temp for iteration 2:

    def receive_serviceBrake(self, train):

        if not self.trainList[train].brakeFailure:
            self.trainList[train].serviceBrake = not(self.trainList[train].serviceBrake)
        else:
            self.trainList[train].serviceBrake = False
        
        #self.ui.serviceBrake_toggle.set(brake)

        if self.UI_mode:
            link.train_model_update_UI_serviceBrake.emit(self.trainList[train].serviceBrake)
            if self.trainList[train].serviceBrake:
                self.ui.serviceBrakes_indicator.setText(self._translate("TrainModel", "<html><head/><body><p><span style=\" color:#ff0004;\">Engaged</span></p></body></html>"))
            else:
                self.ui.serviceBrakes_indicator.setText("Disengaged")


    # Receive emergency brake from the Train Controller or Passenger
    def receive_emergencyBrake(self, train, emergencyBrake):
        self.trainList[train].emergencyBrake = emergencyBrake
        #self.ui.emergencyBrake_toggle.set(emergencyBrake)
        #connect.train_model_send_emergencyBrake_passenger_UI.emit(emergencyBrake),
        if self.UI_mode:
            if emergencyBrake:
                self.ui.emergencyBrakes_indicator.setText(self._translate("TrainModel", "<html><head/><body><p><span style=\" color:#ff0004;\">Engaged</span></p></body></html>"))
            else:
                self.ui.emergencyBrakes_indicator.setText("Disengaged")
        
    # Receive temperature control from the Train Controller
    def receive_temperature(self, train, temperature):
        self.trainList[train].temperature = temperature
        if self.UI_mode:
            self.ui.temp_text.setText(str(temperature))

    # Receive commanded speed from the Train Controller
    def receive_commandedSpeed(self, train, commandedSpeed):
        self.trainList[train].commandedSpeed = commandedSpeed
        if self.UI_mode:
            self.ui.commandedSpeed_text.setText(str(Conversion.ms_to_mph(commandedSpeed)))

    # Receive door open/closed from the Train Controller
    def receive_door(self, train, side):
        
        doors = self.trainList[train].doors

        if side == "left":
            self.trainList[train].doors = [not(doors[0]), doors[1]]
        elif side == "right":
            self.trainList[train].doors = [doors[0], not(doors[1])]

        doors = self.trainList[train].doors

        # Change this to an indicator later maybe?
        if self.UI_mode:
            if doors[0] and doors[1]:
                self.ui.doors_text.setText("LEFT OPEN; RIGHT OPEN")
            elif not(doors[0]) and doors[1]:
                self.ui.doors_text.setText("LEFT CLOSED; RIGHT OPEN")
            if doors[0] and not(doors[1]):
                self.ui.doors_text.setText("LEFT OPEN; RIGHT CLOSED")
            elif not(doors[0]) and not(doors[1]):
                self.ui.doors_text.setText("LEFT CLOSED; RIGHT CLOSED")

# ---------------------------------------------------------------------------------------------
# ---------------------------- INPUTS FROM FAILURES (MURPHY) ----------------------------------
# ---------------------------------------------------------------------------------------------

    # Receive brake failure from Murphy
    def receive_brakeFailure(self, train):
        self.trainList[train].brakeFailure = not(self.trainList[train].brakeFailure)
        #self.ui.engineStatus_indicator.setText(brakeFailure)

        if self.UI_mode:
            if self.trainList[train].brakeFailure:
                self.ui.brakeStatus_indicator.setText(self._translate("TrainModel", "<html><head/><body><p><span style=\" color:#ff0004;\">FAILURE</span></p></body></html>"))
            else:
                self.ui.brakeStatus_indicator.setText(self._translate("TrainModel", "<html><head/><body><p><span style=\" color:#00ff00;\">Working</span></p></body></html>"))

    # Receive signal pickup failure from Murphy
    def receive_signalPickupFailure(self, train):
        self.trainList[train].signalPickupFailure = not(self.trainList[train].signalPickupFailure)
        #self.ui.signalPickupFailure_set(signalPickupFailure)

        if self.UI_mode:
            if self.trainList[train].signalPickupFailure:
                self.ui.signalpickupStatus_indicator.setText(self._translate("TrainModel", "<html><head/><body><p><span style=\" color:#ff0004;\">FAILURE</span></p></body></html>"))
            else:
                self.ui.signalpickupStatus_indicator.setText(self._translate("TrainModel", "<html><head/><body><p><span style=\" color:#00ff00;\">Working</span></p></body></html>"))
        
    # Receive engine failure from Murphy
    def receive_engineFailure(self, train):
        self.trainList[train].engineFailure = not(self.trainList[train].engineFailure)
        #self.ui.engineFailure_set(engineFailure)

        if self.UI_mode:
            if self.trainList[train].engineFailure:
                self.ui.engineStatus_indicator.setText(self._translate("TrainModel", "<html><head/><body><p><span style=\" color:#ff0004;\">FAILURE</span></p></body></html>"))
            else:
                self.ui.engineStatus_indicator.setText(self._translate("TrainModel", "<html><head/><body><p><span style=\" color:#00ff00;\">Working</span></p></body></html>"))

# ---------------------------------------------------------------------------------------------
# ---------------------------------- INPUTS FROM PASSENGER ------------------------------------
# ---------------------------------------------------------------------------------------------

    # Receive passengers from station
    def receive_passengers(self, train, passengers):
        self.trainList[train].passengers = passengers
        self.trainList[train].mass = self.trainList[train].mass + (Conversion.kg_to_tons(62)) # Average mass of a human is 62 kg
        if self.UI_mode:
            self.ui.passengers_text.setText(str(passengers))

# ---------------------------------------------------------------------------------------------
# ----------------------- PASS THRU OUTPUTS TO TRAIN CONTROLLER -------------------------------
# ---------------------------------------------------------------------------------------------

    # Receive track circuit from the Track Model
    def send_trackCircuit(self, train, trackCircuit):
        # Send to Train Controller if signal pickup isn't failing
        if not(self.TrainList[train].signalPickupFailure):
            link.train_model_send_trackCircuit(trackCircuit)

    # Receive brake failure from Murphy
    def send_brakeFailure(self, train, brakeFailure):
        self.trainList[train].brakeFailure = brakeFailure
        link.train_model_send_failure_ctrl.emit("brakeFailure", brakeFailure)

    # Receive signal pickup failure from Murphy
    def send_signalPickupFailure(self, train, signalPickupFailure):
        self.trainList[train].signalPickupFailure = signalPickupFailure
        link.train_model_send_failure_ctrl.emit("signalPickupFailure", signalPickupFailure)
        
    # Receive engine failure from Murphy
    def send_engineFailure(self, train, engineFailure):
        self.trainList[train].engineFailure = engineFailure
        link.train_model_send_failure_ctrl.emit("engineFailure", engineFailure)

if __name__ == '__main__':

    TrainModel = Train_Functions(0, "Test")
