import time
import RPi.GPIO as GPIO
import wiringpi
import essential

#Unit Test 1: Emergency Brake Works
def unit_test_one():
    emergencyBrake=essential.emergencyBrake
    self.assertTrue(emergencyBrake)
  

#Unit Test 2: Change in Speed Works
def unit_test_two():
  suggestedSpeed = getSuggestedSpeed()
  currentSpeed = suggestedSpeed
  if(incSpeed==1)
    assert currentSpeed>suggestedSpeed
  if(decSpeed==1)
    assert currentSpeed<suggestedSpeed

#Unit Test 3: Service Brake Works
def unit_test_three()::
    serviceBrake=essential.serviceBrake
    self.assertTrue(serviceBrake)

def main():
    #call unit tests
    unit_test_one()
    unit_test_two()
    unit_test_three()

if __name__ == '__main__':
    main()
