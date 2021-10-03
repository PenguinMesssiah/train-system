class Train:
    
    # Static train attributes
    length = 0 # meters
    height = 0 # meters
    width = 0 # meters
    mass = 0 # tons
    crewCount = 0 # people
    passengerCount = 0 # people
 
    # Variable train attributes (calculated)
    position = 0 # m
    currentSpeed = 0 # m/s
    acceleration = 0 # m/s^2

    # from Train Controller
    power = 0 # watts
    brakeEngaged = False
    doorOpened = False
    tempControl = False

    # from Track Model
    speedLimit = 0
    accelerationLimit = 0
    decelerationLimit = 0
    commandedSpeed = 0
    beaconInput = ""

    emergencyBrake_passenger = False
    
    # Failure Cases (from Murphy)
    brakeFailure = False
    signalPickupFailure = False
    engineFailure = False

    # Mode
    automaticMode = True