
class Train:

    # Static train attributes
    length = 0         # meters
    height = 0         # meters
    width = 0          # meters
    mass = 0           # tons
    crewCount = 0      # people
    passengerCount = 0 # people
 
    # Variable train attributes (calculated)
    position = 0       # m
    currentSpeed = 0   # m/s
    acceleration = 0   # m/s^2

    # from Train Controller
    power = 0          # watts
    brakeEngaged = False
    emergencyBrake = False      # also from Passenger
    doorOpened = False
    temperature = 70.0
    announcements = ""

    # from Track Model
    speedLimit = 0.0
    accelerationLimit = 0.0
    decelerationLimit = 0.0
    commandedSpeed = 0.0
    beacon = ""
    lights = False

    # Failure Cases (from Murphy)
    brakeFailure = False
    signalPickupFailure = False
    engineFailure = False

    # Mode
    automaticMode = True