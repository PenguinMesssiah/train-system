import time
import json
from PyQt5 import QtCore, QtGui, QtWidgets
from TestUI import MBODisplay

trainNumber = 0.0
authority = 0.0
suggestedSpeed = 0.0

def setMBOValues():
    trainNumber = MBO_UI.trainNumberInput.value()
    authority = MBO_UI.authorityInput.value()
    suggestedSpeed = MBO_UI.suggestedSpeedInput.value()

    #writing values to json
    MBO_data = {"trainNumber":trainNumber,
                "authority":authority,
                "suggestedSpeed":suggestedSpeed}
    file = open('TestValues.json', 'w')
    json.dump(MBO_data, file)
    

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    
    MBOWindow = QtWidgets.QMainWindow()
    MBO_UI = MBODisplay()
    MBO_UI.setupUI(MBOWindow)
    MBOWindow.show()

    MBO_UI.enterButton.clicked.connect(setMBOValues)
