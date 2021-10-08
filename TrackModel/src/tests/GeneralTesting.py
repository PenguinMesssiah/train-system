'''
Created on October 8, 2021

File for Testing Track Model Implementation
'''

from models.trackBlock import trackBlock

def main():
    c = trackBlock
    c.xPos = 4;
    print("x Position of C equals = ", c.xPos)

    
if __name__ == '__main__':
    main()