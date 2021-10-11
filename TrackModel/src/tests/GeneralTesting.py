'''
Created on October 8, 2021

File for Testing Track Model Implementation
'''

from services import trackBuilderService

def main():
    
    trackList = trackBuilderService.readTrackFile()
    
    for curObj in trackList:
        print("\nCurrent Block Type: ", curObj.objType)
        

if __name__ == '__main__':
    main()