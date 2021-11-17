import time
from BlueLineSet import BlueLine
class Path(object):

     def __init__(self, Ctime, leaveT, arriveD, departD):

         self.departTime = leaveT

         self.arrivalTime = Ctime

         self.destB = arriveD

         self.departB = departD


         

         
