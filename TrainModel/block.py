class Block:

    def __init__(self, name, blockLength, speedLimit, elevation, slope, station, beacon):

        # Block properties
        self.name = name                 # Block name
        self.blockLength = blockLength   # Block length, meters
        self.speedLimit = speedLimit     # Speed limit, m/s
        self.elevation = elevation       # elevation, meters
        self.slope = slope               # slope, percent(float)
        self.station = station           # station, string
        self.beacon = beacon             # beacon, string