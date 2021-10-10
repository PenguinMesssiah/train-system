'''
Last Updated: October 8, 2021
@author: Will Scott
'''

# Imports
import pylightxl as xl

from models.trackBlock      import trackBlock
from models.railwayCrossing import railwayCrossing
from models.station         import station
from models.trackLight      import trackLight
from models.trackSwitch     import trackSwitch



# Main Method
def main():
    # Defined Variables
    trackLayout      = []
    count, rowlength = 0, 17;
    
    # Opening & Reading Excel File
    database = xl.readxl(fn='C:/Users/willi/Documents/School/SystemsProjectEngineering/TrackLayoutVehicleDatavF2.xlsx')
    
    for row in database.ws(ws='Blue Line').rows:
        # Skipping first row to avoid the section headers
        count += 1
        if(count == 1):
            continue
        elif(count == rowlength):
            break;
        
        # Saving Block Information
        curTrackBlock = trackBlock(row[0],row[1], row[2], row[3], row[4], row[5], row [8], row[9]);
        
        #Check & Adding Any Infrastructure
        if(row[6] != ''):
            if(row[6][0:3] == 'Sw'):
                str = row[6].replaceAll(' ','')
                str = str.replace('Switch','')
                str = str[1 : str.len()-1]
                
                
                curSwitch = trackSwitch('', str[0], str[str.len])
            elif(row[6][0:3] == 'St')
        
        trackLayout.append(curTrackBlock)
        
    
    print("\nLine = ", trackLayout[0].line)
    print("\nSection = ", trackLayout[0].section)    
    print("\nBlockNumber = ", trackLayout[0].elementId)
    print("\nBlockLength = ", trackLayout[0].size)    
    print("\nBlockGrade = ", trackLayout[0].gradLevel)
    print("\nSpeedLimit = ", trackLayout[0].speedLimit)      
        
     
    print("\nFinished Building Track Layout")


if __name__ == '__main__':
    main()