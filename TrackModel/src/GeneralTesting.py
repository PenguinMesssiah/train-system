'''
Created on October 11, 2021

File for Testing Track Model Implementation
'''
from services import trackBuilderService

def main():
    
    trackList = trackBuilderService.readTrackFile()

    trackLayout = trackBuilderService.readDatabase();

    print("\n\n--------Track Layout Testing---------")
    for curObject in trackLayout:
        print('Current Object Type = ', curObject.objType);

if __name__ == '__main__':
    main()