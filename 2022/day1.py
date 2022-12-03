import os
import sys

def testvalue(currentvalue, highestvalue):
    if currentvalue > highestvalue[0]:
        highestvalue.insert(0, currentvalue)
    elif currentvalue > highestvalue[1]:
        highestvalue.insert(1, currentvalue)
    elif currentvalue > highestvalue[2]:
        highestvalue.insert(2, currentvalue)
                
    if len(highestvalue) > 3:
    	highestvalue = highestvalue[ : -1]
    return highestvalue

def readfile(filename):
    file1 = open(os.path.join(sys.path[0], "data", filename), 'r')
    currentvalue = 0

    highestvalue = [0]

    while True:
        line = file1.readline()
        if not line:
            break

        if line.strip() == '':
            highestvalue = testvalue(currentvalue, highestvalue)
            print(highestvalue)
            currentvalue = 0

        else:
            currentvalue = currentvalue + int(line)
 
    highestvalue = testvalue(currentvalue, highestvalue)
   
    print(highestvalue)
    print(sum(highestvalue))

    file1.close()

if __name__ == '__main__':
    readfile('day1.txt')
