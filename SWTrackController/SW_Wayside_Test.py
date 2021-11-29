import unittest
from WaysideImplementation import WaysideImplementation

class SW_Wayside_Test(unittest.TestCase):

#	def init_test_case(self):


#	def cleanup_test_case(self):


#Unit Test 1: Adding Switch to a Wayside Controller Representation
	def test_addSwitch(self):
		wayside = WaysideImplementation([61, 62, 63, 64, 65, 66], [0, 58, 59, 60])
		wayside.addSwitch(62)
		assertTrue(wayside[62]==0)

#Unit Test 2: Updating Switch Position
	def test_updateSwitch(self):
		wayside = WaysideImplementation([61, 62, 63, 64, 65, 66], [0, 58, 59, 60])
		wayside.addSwitch(62)
		assertTrue(wayside[62]==0)
		wayside.updateSwitch(62, 1)
		assertTrue(wayside[62]==1)

#Unit Test 3: Setting a light to green
	def test_setGreenLight(self):
		wayside = WaysideImplementation([61, 62, 63, 64, 65, 66], [0, 58, 59, 60])
		wayside.addLight(62)
		assertTrue(wayside[62]==[0, 0, 0, 0])
		wayside.setGreenLight(62)
		assertTrue(wayside[62]==[0, 0, 1, 0])



if __name__ == '__main__':
    unittest.main()