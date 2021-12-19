import argparse
import numpy as np
import os
import re
import math

def readFile(fileName):
    fileObj = open(fileName, "r") #opens the file in read mode
    input = fileObj.read().splitlines() #puts the file into an array
    fileObj.close()
    return input


def parse(input):
    parsedinput = []
    for line in input:
        values = []
        depths = []
        depthmarker = 0
        x = 0
        while x < len(line):
            if(line[x] == '['):
                depthmarker += 1
                x += 1
            elif (line[x] == ']'):
                depthmarker -= 1
                x += 1
            elif (line[x] == ','):
                x += 1
            elif (line[x] in ['1','2','3','4','5','6','7','8','9','0']):
                y = 0
                number = ''
                while (line[x+y] in ['1','2','3','4','5','6','7','8','9','0']):
                    number = f'{number}{line[x+y]}'
                    y += 1
                values.append(int(number))
                depths.append(depthmarker)
                x += y
                

        parsedinput.append([values, depths])
    
    #print(parsedinput)
    return parsedinput

def checkexplodes(input):
    if 5 in input[1]:
        return True
    else:
        return False

def doexplodes(input):
    values = input[0]
    depths = input[1]

    location = depths.index(5)
    
    #case not leftmost item
    if(location != 0):
        values[location -1] += values[location]
    
     #case not rightmost item
    if(location+2 != len(values)):
        values[location +2] += values[location +1]

    values[location] = 0
    del(values[location+1])
    depths[location] -= 1
    del(depths[location+1])

    return [values, depths]

def checksplits(input):
    if any(y > 9 for y in input[0]):
        return True
    else:
        return False

def dosplits(input):
    values = input[0]
    depths = input[1]
    location = 0

    for number in values:
        if (number > 9):
            break
        location += 1
    
    newvalues = values[location]
    values[location] = math.floor(newvalues/2)
    depths[location] += 1
    values.insert(location+1, math.ceil(newvalues/2))
    depths.insert(location+1, depths[location])
    return [values, depths]


def doaddition(input, toadd):
    values = input[0]
    depths = input[1]

    for x in range(len(depths)):
        depths[x] += 1

    toaddvalues = toadd[0]
    toadddepths = toadd[1]

    for x in range(len(toadddepths)):
        toadddepths[x] += 1

    values = values + toaddvalues
    depths = depths + toadddepths

    return [values, depths]

def calculate(input):
    result = -1 
    for line in input:
        if(result == -1):
            result = input[0]
        else:
            result = doaddition(result, line)
        while True:
            if(checkexplodes(result)):
                result = doexplodes(result)
            elif(checksplits(result)):
                result = dosplits(result)
            else:
                #no explodes or splits to do
                break
            #print(result)
    return result


def checkmagnitude(input):

    values = input[0]
    depths = input[1]
    x = 0
    while True:
        if(len(values) == 1):
            break

        location = depths.index(max(depths))
        newmagnitude = 3*values[location] + 2*values[location+1]

        values[location] = newmagnitude
        del(values[location+1])
        depths[location] -= 1
        del(depths[location+1])


    return values[0]

def main(args):
    global shortestpath
    input = readFile(args.input)
    parsedinput = parse(input)
    result = calculate(parsedinput)
    magnitude = checkmagnitude(result)
    print(f'result {magnitude}')
    

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description='AdventOfCode2021Day18')
    parser.add_argument('--input', type=str, required=True,
                    help="File")
    args = parser.parse_args()

    main(args)