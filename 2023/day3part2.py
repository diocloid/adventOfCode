import os
import sys

def isGear(char):
    if char == '*':
        return True
    else:
        return False


def findfullnumber(fullline,gearindex, index):
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
    return [int(fullnumber), gearindex, ''.join(linelist)]
    
def testline(fullline, linelen):
    for index in range(0, len(fullline)):
        currentchar = fullline[index]
        #print(currentchar)
        if isGear(currentchar):
            print(f'isGear on index {index}: {fullline[index]}')
            if fullline[index-1].isnumeric():
                print(f'foundnumber {fullline[index-1]}')                
                return findfullnumber(fullline, index, index-1)
            if fullline[index-linelen-1].isnumeric():
                print(f'foundnumber {fullline[index-linelen-1]}')
                return findfullnumber(fullline, index, index-linelen-1)
            if fullline[index-linelen].isnumeric():
                print(f'foundnumber {fullline[index-linelen]}')
                return findfullnumber(fullline, index, index-linelen)
            if fullline[index-linelen+1].isnumeric():
                print(f'foundnumber {fullline[index-linelen+1]}')
                return findfullnumber(fullline, index, index-linelen+1)
            if fullline[index+1].isnumeric():
                print(f'foundnumber {fullline[index+1]}')
                return findfullnumber(fullline, index, index+1)
            if fullline[index+linelen+1].isnumeric():
                print(f'foundnumber {fullline[index+linelen+1]}')
                return findfullnumber(fullline, index, index+linelen+1)
            if fullline[index+linelen].isnumeric():
                print(f'foundnumber {fullline[index+linelen]}')
                return findfullnumber(fullline, index, index+linelen)
            if fullline[index+linelen-1].isnumeric():
                print(f'foundnumber {fullline[index+linelen-1]}') 
                return findfullnumber(fullline, index, index+linelen-1)
            else: 
                print('No Numbers around Gear, deleting')
                linelist = list(fullline)
                linelist[index] = '.'
                return [-1, -1, ''.join(linelist)]
            
    return False, -1, fullline
    
    
def part2(filename):
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
    gearindex = -1
    firstnumber = -1
    secondnumber = -1
    while True:
        foundNumber, newgearindex, fullline = testline(fullline, linelen)
        print(f'fullnumber {foundNumber}')
        if foundNumber == False:
            break
        elif foundNumber == -1:
            print(f'Found Gear without numbers')
            if firstnumber != -1 and secondnumber != -1:
                print('first and second numbers are set on deleted gear index adding')
                output += firstnumber * secondnumber
            gearindex = -1
            firstnumber = -1
            secondnumber = -1
        else:
            if newgearindex == gearindex:
                if secondnumber == -1:
                    print('found second number')
                    secondnumber = foundNumber                    
                else:  
                    print("second number already set discarding and deleting gear")
                    linelist = list(fullline)
                    linelist[newgearindex] = '.'
                    fullline = ''.join(linelist)
                    gearindex = -1
                    firstnumber = -1
                    secondnumber = -1
            else: 
                if firstnumber == -1:
                    print('found first number')
                    firstnumber = foundNumber
                    gearindex = newgearindex
                else:
                    print('first number is set but a different gear index')
                    if secondnumber != -1:
                        print('first and second numbers are set on old gear index adding the old gear')
                        output += firstnumber * secondnumber
                    print("resetting")
                    firstnumber = foundNumber
                    gearindex = newgearindex
                    
                
            #output += foundNumber
            #print(f'New Output {output}')

        
        
    
            


    file1.close()
    
    print(output)


if __name__ == '__main__':
    part2('day3.prod.txt')