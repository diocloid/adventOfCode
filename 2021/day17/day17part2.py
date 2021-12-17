import argparse
import numpy as np
import os
import re

def readFile(fileName):
    fileObj = open(fileName, "r") #opens the file in read mode
    data = fileObj.read()
    target = re.findall(r'target area: x=(-?\d+)..(-?\d+), y=(-?\d+)..(-?\d+)', data)[0]
    target = [int(x) for x in target]
    fileObj.close()
    return target

def testshot(target):
    testoffset = -200
    velocityvalues = []

    for x in range(0, target[1] * 5):
        for y in range(-(target[3] - target[2]) * 5, (target[3] - target[2]) * 5) :   
    # 
    # x=6
    # y=0        
            pointX = 0
            pointY = -testoffset
            velX = x
            velY = y
            originalVelX = x
            originalVelY = y
            #print ((pointX,pointY))

            #test some fly time iterations
            for run in range(target[1] * 3):                
                #change position by velocity
                pointX += velX
                pointY += velY
                #decrease X velocity
                velX -= 1
                if(velX < 0):
                    velX = 0
                #increase Y velocity
                velY -= 1
                #print ((pointX,pointY))
                if(target[0] <= pointX <= target[1] and target[2]-testoffset <= pointY <= target[3]-testoffset):
                    #print(f'{originalVelX},{originalVelY}')
                    velocityvalues.append((originalVelX, originalVelY))
                    break
                if(pointX > target[1]):
                    #print('miss x')
                    break
                if(pointY < target[2]-testoffset):    
                    #print('miss y')
                    break


    return velocityvalues

def main(args):
    global shortestpath
    target = readFile(args.input)
    result = testshot(target)

    print(f'result {len(result)}')
    

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description='AdventOfCode2021Day17')
    parser.add_argument('--input', type=str, required=True,
                    help="File")
    args = parser.parse_args()

    main(args)