
class Train:

    # Static train attributes
    length = 25        # meters
    height = 3.5       # meters
    width = 2.5        # meters
    mass = 50          # tons
    crewCount = 2      # people
    passengerCount = 0 # people
 
    # Variable train attributes (calculated)
    position = 0       # m
    currentSpeed = 0   # m/s
    acceleration = 0   # m/s^2
    currentBlock = 0

    # from Train Controller
    power = 0          # watts
    brakeEngaged = False
    emergencyBrake = False      # also from Passenger
    doorOpened = False
    temperature = 70.0
    announcements = ""

    # from Track Model
    blockRoute = []
    destination = 0
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

    def __init__(self, destination, blockRoute):

        self.destination = destination
        self.blockRoute = blockRoute