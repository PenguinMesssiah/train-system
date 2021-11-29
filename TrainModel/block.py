class Block:

    def __init__(self, name, blockLength, elevation, slope, station, beacon):

        # Block properties
        self.name = name                 # Block name
        self.blockLength = blockLength   # Block length, meters
        self.elevation = elevation       # elevation, meters
        self.slope = slope               # slope, percent(float)
        self.station = station           # station, string
        self.beacon = beacon             # beacon, string