import os
import sys


def part1(filename):
    file1 = open(os.path.join(sys.path[0], "data", filename), 'r')
    output = 0
    true = 0
    false = 0
    while True:
        line = file1.readline()
        if not line:
            break
        line = line[5:len(line)]
        lineobjects = line.split(':')
        gamenumber = lineobjects[0]
        pulledcubes = lineobjects[1]
        pulledcubes = pulledcubes.replace(';',',')
        nicerpulledcubes = pulledcubes.split(',')
        #print(f'Gamenumber {gamenumber}')
        ispossible = True
        
        for onepull in nicerpulledcubes:
            onepull = onepull[1:len(onepull)]
            onepullobject = onepull.split(' ')
            pullnumber = int(onepullobject[0])
            pullcolor = onepullobject[1].strip()
            #print(f'Pullnumber {pullnumber}, {pullcolor}')
            
            if pullcolor == 'red' and pullnumber > 12:
                ispossible = False
                break;
            elif pullcolor == 'green' and pullnumber > 13:
                ispossible = False
                break;
            elif pullcolor == 'blue' and pullnumber > 14:
                ispossible = False
                break;
            
       
        if ispossible == True:
            output += int(gamenumber)
            print(f'Gamenumber {gamenumber} is True')
            true += 1
        else: 
            #print(f'Gamenumber {gamenumber} is False')
            false += 1
        #print(f'Current Output: {output}\n\n')
        #print(lineobjects)
        
        


    file1.close()
    
    print(output)


def part2(filename):
    file1 = open(os.path.join(sys.path[0], "data", filename), 'r')
    output = 0
    true = 0
    false = 0
    while True:
        line = file1.readline()
        if not line:
            break
        line = line[5:len(line)]
        lineobjects = line.split(':')
        gamenumber = lineobjects[0]
        pulledcubes = lineobjects[1]
        pulledcubes = pulledcubes.replace(';',',')
        nicerpulledcubes = pulledcubes.split(',')
        #print(f'Gamenumber {gamenumber}')
        biggestred = 0
        biggestgreen = 0
        biggestblue = 0
        
        for onepull in nicerpulledcubes:
            onepull = onepull[1:len(onepull)]
            onepullobject = onepull.split(' ')
            pullnumber = int(onepullobject[0])
            pullcolor = onepullobject[1].strip()
            #print(f'Pullnumber {pullnumber}, {pullcolor}')
            
            if pullcolor == 'red' and pullnumber > biggestred:
                biggestred = pullnumber
            elif pullcolor == 'green' and pullnumber > biggestgreen:
                biggestgreen = pullnumber
            elif pullcolor == 'blue' and pullnumber > biggestblue:
                biggestblue = pullnumber
            
       
        
        output += biggestred * biggestgreen * biggestblue
        print(f'Gamenumber {gamenumber} is {biggestred * biggestgreen * biggestblue}')

    file1.close()
    
    print(output)


if __name__ == '__main__':
    part2('day2.prod.txt')