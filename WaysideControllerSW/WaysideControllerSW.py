#class WaysideControllerSW
#author: Elissa Wilton

import time
from waysideUi import WaysideUi
from PyQt5 import QtCore, QtGui, QtWidgets

#will have specific Wayside controller for each section of track
class WaysideControllerSW(object): #for PyQt
	
	def __init__(self, ui, numBlocks, numSwitches, numCrossings, numLights):
		self.numBlocks = numBlocks
		self.numSwitches = numSwitches
		self.numCrossings = numCrossings
		self.numLights = numLights
		self.blockOccupancy = [0]* numBlocks
		self.blockAuthority = [1]* numBlocks
		self.blockAuthorityData = [0]* numBlocks #eventually from external
		self.blockSpeed = [1]* numBlocks
		self.blockSpeedData = [0]* numBlocks #eventually from external
		self.switchPosition = [0] * numSwitches
		self.crossingPosition = [0] * numCrossings
		self.lightColor = [[0 for i in range(4)] for j in range(numLights)] #red, yellow, green, super green for each light
		
		self.ui = ui
		self.waysideWindow()
	

	#--------------Wayside UI------------------------
	def waysideWindow(self):
		
		#Controls
		self.ui.autoButton.pressed.connect(self.display)
	
		self.ui.checkBox1.stateChanged.connect(lambda: self.checkBox(self.ui.checkBox1, 1))
		self.ui.checkBox2.stateChanged.connect(lambda: self.checkBox(self.ui.checkBox2, 2))
		self.ui.checkBox3.stateChanged.connect(lambda: self.checkBox(self.ui.checkBox3, 3))
		self.ui.checkBox4.stateChanged.connect(lambda: self.checkBox(self.ui.checkBox4, 4))
		self.ui.checkBox5.stateChanged.connect(lambda: self.checkBox(self.ui.checkBox5, 5))
		self.ui.checkBox6.stateChanged.connect(lambda: self.checkBox(self.ui.checkBox6, 6))
		self.ui.checkBox7.stateChanged.connect(lambda: self.checkBox(self.ui.checkBox7, 7))
		self.ui.checkBox8.stateChanged.connect(lambda: self.checkBox(self.ui.checkBox8, 8))
		self.ui.checkBox9.stateChanged.connect(lambda: self.checkBox(self.ui.checkBox9, 9))
		self.ui.checkBox10.stateChanged.connect(lambda: self.checkBox(self.ui.checkBox10, 10))
		self.ui.checkBox11.stateChanged.connect(lambda: self.checkBox(self.ui.checkBox11, 11))
		self.ui.checkBox12.stateChanged.connect(lambda: self.checkBox(self.ui.checkBox12, 12))
		self.ui.checkBox13.stateChanged.connect(lambda: self.checkBox(self.ui.checkBox13, 13))
		self.ui.checkBox14.stateChanged.connect(lambda: self.checkBox(self.ui.checkBox14, 14))
		self.ui.checkBox15.stateChanged.connect(lambda: self.checkBox(self.ui.checkBox15, 15))
		
		self.ui.radioButton.pressed.connect(lambda: self.switch(0))
		self.ui.radioButton_2.pressed.connect(lambda: self.switch(1))
	
	#---------------Functions------------------------
	#Getters
		
	def getNumBlocks(self):
		return self.numBlocks
	
	def getNumSwitches(self):
		return self.numSwitches
	
	def getNumCrossings(self):
		return self.numCrossings
	
	def getNumLights(self):
		return self.numLights()	
	
	def getBlockOccupancy(self, block): #shouldn't have option to ask for nonexistant actually
		if i >= len(blockOccupancy):
			return 1 #for now, if ask for a nonexistant block assume you can't go there (return occupied)
		return self.blockOccupancy[block]
		
	def getBlockAuthority(self, block):
		return self.blockAuthority[block]
	
	def getBlockSpeed(self, block):
		return self.blockSpeed[block]	
	
	def getSwitchPositions(self, switch): 
		return self.switchPosition[switch]	
	
	def getCrossingPosition(self, crossing):
		return self.crossingPosition[crossing]
	
	def getLightColor(self, light): #light should only ever be one color
		return self.lightColor[light] #returns the 4 element vector
		
	#Setters
	def setBlockOccupancy(self, block, value):
		self.blockOccupancy[block] = value
		
		
	def setBlockAuthority(self, block, value):
		self.blockAuthority[block] = value
		
	def setBlockSpeed(self, block, value):
		self.blockSpeed[block] = value		
	
	def setSwitchPositions(self, switch, value): 
		self.switchPositions[switch] = value
	
	def setCrossingPosition(self, crossing, value):
		self.crossingPosition[crossing] = value
	
	def setLightColor(self, light, value): #light should only ever be one color, pass in 4 element vector
		self.lightColor[light] = value
		
	def display(self):	
		blockOccStr = ""
		blockAuthStr = ""
		blockSpeedStr = ""
		for i in range(len(self.blockOccupancy)):
			newStr = 'Block '+ str(i+1) + ': ' + str(self.blockOccupancy[i]) + '\n'
			blockOccStr +=  newStr
			if(self.blockOccupancy[i] == 1):
				if(self.blockAuthority[i] ==1):
					auth = self.blockAuthorityData[i]
				else:
					auth = 0
				if(self.blockSpeed[i] ==1):
					speed = self.blockSpeedData[i]
				else: 
					speed = 0
			else:
				auth = 0
				speed = 0
			newStr2 = 'Block '+ str(i+1) + ': ' + str(auth) + '\n'
			blockAuthStr +=  newStr2
			newStr3 = 'Block '+ str(i+1) + ': ' + str(speed) + '\n'
			blockSpeedStr +=  newStr3
			
			#needs to be put in loop
			switchState = ""
			if (self.switchPosition[0]==0):
				state = "5/6"
			else:
				state = "5/11"
			switchState += 'Switch 1: ' + state + '\n'
			
		self.ui.trackOccTxt.setText(blockOccStr)
		self.ui.speedTxt.setText(blockSpeedStr)
		self.ui.authorityTxt.setText(blockAuthStr)
		self.ui.switchTxt.setText(switchState)
		
	def checkBox(self, box, blockNum):
		if box.isChecked():
			self.setOcc(blockNum)
		else:
			self.clearOcc(blockNum)
		
	def setOcc(self, blockNum): #need to add edge cases
		blockNum = blockNum-1
		self.blockOccupancy[blockNum] = 1
		if(self.blockOccupancy[blockNum-1]==1):
			self.blockAuthority[blockNum-1] = 0
			self.blockAuthority[blockNum] = 0
			self.blockSpeed[blockNum-1] = 0
			self.blockSpeed[blockNum] = 0
			
		if(self.blockOccupancy[blockNum+1]==1):
			self.blockAuthority[blockNum+1] = 0
			self.blockAuthority[blockNum] = 0
			self.blockSpeed[blockNum+1] = 0
			self.blockSpeed[blockNum] = 0
		
		#hardcoded for blue line for the moment because no plc
		if(self.blockOccupancy[4]==1 and self.blockOccupancy[10]==1):
			self.blockAuthority[4] = 0
			self.blockAuthority[10] = 0
			self.blockSpeed[4] = 0
			self.blockSpeed[10] = 0
		self.display()
		
	def clearOcc(self, blockNum):
		blockNum = blockNum-1
		self.blockOccupancy[blockNum] =0
		self.blockAuthority[blockNum] =1
		self.blockSpeed[blockNum]=1
		self.display()
		
	def switch(self, state):
		curr = self.switchPosition[0]
		
		#hardcoded because no PLC
		if state != curr:
			if (self.blockOccupancy[4]==1 or self.blockOccupancy[5]==1 or self.blockOccupancy[10]==1):
				self.switchPosition[0] = curr
			else:
				self.switchPosition[0] =state
			
		self.display()
			
		
if __name__ == "__main__":
	import sys
	app = QtWidgets.QApplication(sys.argv)
	display = QtWidgets.QMainWindow()
	
	waysideBlue_ui = WaysideUi()
	waysideBlue_ui.setupUi(display)
	display.show()
	
	blue = WaysideControllerSW(waysideBlue_ui, 15, 1, 0, 0)
	
	#Data for auto mode
	blue.blockOccupancy[2] = 1
	blue.blockOccupancy[10] = 1
	blue.blockSpeedData= [50,49,50,48,46,50,50,45,50,50,50,47,46,50,50]
	blue.blockAuthorityData = [50,50,50,50,50,50,50,50,50,50,50,50,50,50,50]
	blue.switchPosition[0] = 0
	
	sys.exit(app.exec_())
		
		
		
	
	
