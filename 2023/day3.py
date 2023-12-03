import os
import sys

def isSpecial(char):
    if char == '.':
        return False
    elif char.isnumeric():
        return False
    else:
        return True


def findfullnumber(fullline, index):
    fullnumber = fullline[index]
    linelist = list(fullline)
    i=1
    while True:        
        if linelist[index-i].isnumeric():
            fullnumber = f'{linelist[index-i]}{fullnumber}' 
            linelist[index-i] = '.'
            i += 1
        else:
            break; 
    i=1
    while True:        
        if linelist[index+i].isnumeric():
            fullnumber = f'{fullnumber}{linelist[index+i]}' 
            linelist[index+i] = '.'
            i += 1
        else:
            break;
    linelist[index] = '.'
    return [int(fullnumber), ''.join(linelist)]
    
def testline(fullline, linelen):
    foundSpecial = False
    for index in range(0, len(fullline)):
        currentchar = fullline[index]
        #print(currentchar)
        if isSpecial(currentchar):
            print(f'special char on index {index}: {fullline[index]}')
            foundSpecial = True
            if fullline[index-1].isnumeric():
                print(f'foundnumber {fullline[index-1]}')                
                return findfullnumber(fullline, index-1)
            if fullline[index-linelen-1].isnumeric():
                print(f'foundnumber {fullline[index-linelen-1]}')
                return findfullnumber(fullline, index-linelen-1)
            if fullline[index-linelen].isnumeric():
                print(f'foundnumber {fullline[index-linelen]}')
                return findfullnumber(fullline, index-linelen)
            if fullline[index-linelen+1].isnumeric():
                print(f'foundnumber {fullline[index-linelen+1]}')
                return findfullnumber(fullline, index-linelen+1)
            if fullline[index+1].isnumeric():
                print(f'foundnumber {fullline[index+1]}')
                return findfullnumber(fullline, index+1)
            if fullline[index+linelen+1].isnumeric():
                print(f'foundnumber {fullline[index+linelen+1]}')
                return findfullnumber(fullline, index+linelen+1)
            if fullline[index+linelen].isnumeric():
                print(f'foundnumber {fullline[index+linelen]}')
                return findfullnumber(fullline, index+linelen)
            if fullline[index+linelen-1].isnumeric():
                print(f'foundnumber {fullline[index+linelen-1]}') 
                return findfullnumber(fullline, index+linelen-1)
            else: 
                print('No Numbers around Special Char, deleting')
                linelist = list(fullline)
                linelist[index] = '.'
                return [-1, ''.join(linelist)]
            
    return foundSpecial, fullline
    
    
def part1(filename):
    file1 = open(os.path.join(sys.path[0], "data", filename), 'r')
    fullline = ''
    output = 0
    linelen = 0
    while True:
        line = file1.readline()
        if not line:
            break
        linelen = len(line.strip())
        fullline = f'{fullline}{line.strip()}'        
    
    #print(fullline)
    while True:
        foundNumber, fullline = testline(fullline, linelen)
        print(f'fullnumber {foundNumber}')
        if foundNumber == False:
            break
        elif foundNumber == -1:
            print(f'Found Special without numbers, continuing')
        else:
            output += foundNumber
            print(f'New Output {output}')

        
        
    
            


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
    part1('day3.prod.txt')