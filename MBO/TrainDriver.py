import time


class Driver(object):


# -- constructor class for Driver. Defaults new worker to being available every day
    def __init__(self, name):
        self.name = name
        self.hoursWorked = 0
        self.active = True
        self.DaysAvailable = [1, 1, 1, 1, 1, 1, 1]
        self.IDnumber = 0

    def __init__(self, name, sun, mon, tues, wed, thurs, fri, sat, idn):
        self.name = name
        self.hoursWorked = 0
        self.active = True
        self.DaysAvailable = [ sun, mon, tues, wed, thurs, fri, sat]
        self.IDnumber = idn

# -- return name of the driver
    def getName(self):
        return self.name

# -- return the number of hours worked by the driver
    def getHoursWorked(self):
        return self.hoursWorked

    def addShift(self):
        self.hoursWorked += 8
        
    def getStatus(self):
        return self.active

    def freeToWork(self,num):
        return self.DaysAvailable[num]

    def changeName(self, name2):
        self.name = name2

    def activateDriver(self):
        self.active = True

    def deactivateDriver(self):
        self.active = False

    def updateAvailability(self, num, num2):
        self.DaysAvailable[num] = num2

    def getIDNumber(self):
        return self.IDnumber

    
    



    
