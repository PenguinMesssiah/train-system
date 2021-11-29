#class Wayside Implementation
#Elissa Wilton

#use to actually implement an instance of the wayside controller/the wayide controller object

class WaysideImplementation(object):

	def __init__(self, blocks, listen):
		self.blocks = blocks
		self.listen = listen
		self.relevant = [0] * 151;
		#for i in range(len(self.blocks)):
		#	self.relevant[self.blocks[i]] = 1
		#for i in range(len(self.listen)):
		#	self.relevant[self.listen[i]] = 1
		self.switches = dict()
		self.rules = dict()
		self.blockAuth = dict() #output from PLC
		self.blockOcc = dict()
		self.blockCTCAuth = dict()
		for block in self.blocks:
			self.blockOcc.update({block: self.getTrackOcc(block)})
			self.blockCTCAuth.update({block: self.getCTCAuth(block)}) #might have to rethink this since auth is an output of PLC
			self.blockAuth.update()
		print(self.blockOcc)
		print(self.blockCTCAuth)
		
		 
	def addSwitch(self, location):
		self.switches.update({location: 0})
		print(self.switches)

	def updateSwitch(self, location, position):
		self.switches.update({location: position})
		print(self.switches)

	def addRule(self, situation, resolution):
		self.rules.update({situation: resolution})
		print(self.rules)

	def getTrackOcc(self, block):
		#pull occ from track model
		return 1

	def getCTCAuth(self, block):
		#PULL AUTH FROM CTC SCHEDULE/ROUTE (s in plc lang)
		return 1

	def printOcc(self):
		print(self.blockOcc)

	def printAuth(self):
		print(self.blockAuth)

	def printCTCAuth(self):
		print(self.blockCTCAuth)
	#def getFullOcc(self):
		#pull full occ from track model




