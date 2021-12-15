
class Track_Circuit_Data:

    def __init__(self, authority, commandedSpeed):
        self.authority = authority
        self.commandedSpeed = commandedSpeed

class Beacon_Data:

    def __init__(self, station, doorsSide):
        self.station = station
        self.doorsSide = doorsSide

class Conversion:

    def kmh_to_ms(self, kmh):
        return kmh*.277778

    def kmh_to_mph(self, kmh):
        return kmh*.621371

    def ms_to_mph(self, ms):
        return ms*2.23694

    def meters_to_feet(self, m):
        return m*3.28084

    def kg_to_tons(self, kg):
        return kg*0.00110231

class Constants:
    
    TIME_PERIOD = 0.1
