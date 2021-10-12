class Block:

    def __init__(self, name, blockLength, speedLimit, elevation, slope, station, beacon):

        # Block properties
        self.name = name
        self.blockLength = blockLength
        self.speedLimit = speedLimit
        self.elevation = elevation
        self.slope = slope
        self.station = station
        self.beacon = beacon