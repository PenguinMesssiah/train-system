
class Track_Circuit_Data:

    def __init__(self, authority, commandedSpeed):
        self.authority = authority
        self.commandedSpeed = commandedSpeed

class Beacon_Data:

    def __init__(self, station, doorsSide):
        self.station = station
        self.doorsSide = doorsSide

class Conversion:

    def kmh_to_ms(kmh):
        return round(kmh*.277778, 2)

    def kmh_to_mph(kmh):
        return round(kmh*.621371, 2)

    def ms_to_mph(ms):
        return round(ms*2.23694, 2)

    def mph_to_ms(mph):
        return round(mph/2.23694, 2)

    def meters_to_feet(m):
        return round(m*3.28084, 2)

    def kg_to_tons(kg):
        return round(kg*0.00110231, 2)

class Constants:
    
    TIME_PERIOD = 0.1
