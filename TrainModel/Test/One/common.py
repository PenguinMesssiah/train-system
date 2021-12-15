
class Track_Circuit_Data:

    def __init__(self, authority, commandedSpeed, speedLimit):
        self.authority = authority
        self.commandedSpeed = commandedSpeed
        self.speedLimit = speedLimit

class Beacon_Data:

    def __init__(self, station, doorsSide):
        self.station = station
        self.doorsSide = doorsSide

class Conversion:

    def kmh_to_ms(kmh):
        return kmh*.277778

    def kmh_to_mph(kmh):
        return kmh*.621371

    def ms_to_mph(ms):
        return ms*2.23694

    def meters_to_feet(m):
        return m*3.28084

    def kg_to_tons(kg):
        return kg*0.00110231

class Constants:
    
    TIME_PERIOD = 0.1