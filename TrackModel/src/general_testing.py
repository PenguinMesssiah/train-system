import os, sys
from services import trackBuilderService, connectionService

#Importing Connections Class
sys.path.append("..\Shared")
from connections import link

def main():
    #Defining connection
    #link.train_model_receive_lights.emit(1, True)
    trackBuilderService.readTrackFile()
    
    blockList = [ 1, 2, 3, 4, 5, 6]
    new_dict = connectionService.retrieveBlockOccupancy(blockList)
    print('\n\n', new_dict)
        
    #Call Test One
    #track_list = trackBuilderService.readTrackFile()

    #oList = connectionService.retrieveBlockOccupancy('A')
    #print(oList)

    #connectionService.setBlockOccupancyHigh(2)
    #oList = connectionService.retrieveBlockOccupancy('A')
    #print('\n', oList)

if __name__ == '__main__':
    main()