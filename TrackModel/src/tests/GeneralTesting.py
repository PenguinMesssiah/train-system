'''
Created on October 11, 2021

File for Testing Track Model Implementation
'''

from services import trackBuilderService

def main():
    
    trackList = trackBuilderService.readTrackFile()
    
    trackBuilderService.generatePositioningData(trackList)
    
    for curObj in trackList:
        if(curObj.objType == 'Switch'):
            continue; 
        
        print("\nCurrent Object Type: ", curObj.objType)
        print("\nCurrent Object Section: ", curObj.section)
        print("\nCurrent xPos: ", curObj.xPos)
        print("\nCurrent yPos: ", curObj.yPos)
        
##self.browseFileSelectButton.clicked.connect(lambda:trackBuilderService.readTrackFile())   
#self.browseFileSelectButton.clicked.connect(lambda:print("This shit is TRASH"))


if __name__ == '__main__':
    main()