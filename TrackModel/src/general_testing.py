import os
from services import trackBuilderService, connectionService

def main():
    #Call Test One
    track_list = trackBuilderService.readTrackFile()

    oList = connectionService.retrieveBlockOccupancy('A')
    print(oList)

    connectionService.setBlockOccupancyHigh(2)
    oList = connectionService.retrieveBlockOccupancy('A')
    print('\n', oList)

if __name__ == '__main__':
    main()