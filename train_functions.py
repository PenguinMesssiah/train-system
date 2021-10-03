# ECE 1140 Train Model Functions
# Daniel Uebelacker

import math

class Train_Functions:

    FRICTION = 0.4
    GRAVITY_ACC = 9.80665

    VELOCITY_LIMIT = 100 # m/s

    ACCELERATION_LIMIT = 50 # m/s^2

    DECELERATION_REGULAR_BRAKE = 0 # m/s^2
    DECELERATION_EMERGENCY_BRAKE = 0 # m/s^2

    def train_model_calculations(self, train, power):
        
        if self.engineFailure:
            power = 0

        # From train class
        commandedSpeed = self.trainList[train].commandedSpeed
        currentSpeed = self.trainList[train].currentSpeed
        prevPosition = self.trainList[train].position
        prevAcceleration = self.trainList[train].acceleration
        mass = self.trainList[train].mass
        brake = self.trainList[train].brake
        emergencyBrake = self.trainList[train].emergencyBrake

        # From track class
        currentBlockLength = blockList[block].blockLength
        speedLimit = blockList[block].speedLimit

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
            position -= currentBlockLength

        self.trainList[train].position = position
        self.trainList[train].block = newBlock