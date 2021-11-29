from pyfirmata import ArduinoMega
from time import sleep
import numpy as np
import pandas as pd
import re
import iteration3
import io


class TestCases(unittest.TestCase):
    def test_PLC_upload(self):
        """
        Test that a PLC Program can be uploaded
        """
        file = 'wayside2_PLC.txt'     # upload program
        self.assertTrue(exists(file)) # make sure program uploaded correctly

    def test_manual_control(self):
        """
        Test that Manual Control can be enabled
        """
        capturedOutput = io.StringIO()      # capture console output
        sys.stdout = capturedOutput
        testinterface()         # start manual mode
        # Check output to make sure manual mode has started
        self.assertEqual(capturedOutput.getvalue(), "Enter 1 to change all Inputs, Enter 2 to choose which Input to change: ")

    def test_change_switch(self):
        """
        Test that a switch can be changed
        """
        pos = 0
        set_switch(pos)
        current_pos = get_switch(self)
        self.assertEqual(current_pos, 0)
        pos = 1
        set_switch(pos)
        current_pos = get_switch(self)
        self.assertEqual(current_pos, 1)

if __name__ == '__main__':
    unittest.main()
