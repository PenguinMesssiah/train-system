import time
from BlueLineSet import BlueLine
class Path(object):

    def __init__(self, leaveT, Ctime, arriveD, departD):

         self.departTime = leaveT

         self.arrivalTime = Ctime

         self.destB = arriveD

         self.departB = departD

         


    def getDestB(self):
        return self.destB

    def getDepartB(self):
        return self.departB

    def getDepartTime(self):
        return self.departTime

    def getArrivalTime(self):
        return self.arrivalTime


         

    
         
