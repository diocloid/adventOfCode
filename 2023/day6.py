import os
import sys
from math import floor, ceil


    
def part1(filename):
    file1 = open(os.path.join(sys.path[0], "data", filename), 'r')
    output = 1
    times = []
    distances = []
    while True:
        line = file1.readline()
        if not line:
            break
        if line != '' and line != '\n':
            line = line.strip()
        
            if line[0:2] == 'Ti':
                input = line.split(':')[1].strip().split()
                for el in input:
                    times.append(int(el.strip())) 
            elif line[0:2] == 'Di':
                input = line.split(':')[1].strip().split()
                for el in input:
                    distances.append(int(el.strip()))                     
            
           
    for idx, time in enumerate(times):
        distance = distances[idx]
        print(f'distance {distance}')
        print(f'time {time}')
        minhold = (-time + (time ** 2 - ( 4 * distance)) ** 0.5 )/2
        maxhold = (-time - (time ** 2 - ( 4 * distance)) ** 0.5 )/2        
        print(f'minhold {minhold}')
        print(f'maxhold {maxhold}')
        if floor(minhold) == minhold and floor(maxhold) == maxhold:
            print(f'button presses {abs(ceil(maxhold)) - abs(floor(minhold)) + 1 -2}')
            output *= abs(ceil(maxhold)) - abs(floor(minhold)) + 1 -2
        else:
            print(f'button presses {abs(ceil(maxhold)) - abs(floor(minhold)) + 1}')
            output *= abs(ceil(maxhold)) - abs(floor(minhold)) + 1
        
    print(f'Output {output}')  
    
    
    file1.close()    
  
def part2(filename):
    file1 = open(os.path.join(sys.path[0], "data", filename), 'r')
    output = 1
    time = 0
    distance = 0
    while True:
        line = file1.readline()
        if not line:
            break
        if line != '' and line != '\n':
            line = line.strip()
        
            if line[0:2] == 'Ti':
                time = int(line.split(':')[1].strip().replace(' ', ''))
            elif line[0:2] == 'Di':
                distance = int(line.split(':')[1].strip().replace(' ', ''))        
            
           

    print(f'distance {distance}')
    print(f'time {time}')
    minhold = (-time + (time ** 2 - ( 4 * distance)) ** 0.5 )/2
    maxhold = (-time - (time ** 2 - ( 4 * distance)) ** 0.5 )/2        
    print(f'minhold {minhold}')
    print(f'maxhold {maxhold}')
    if floor(minhold) == minhold and floor(maxhold) == maxhold:
        print(f'button presses {abs(ceil(maxhold)) - abs(floor(minhold)) + 1 -2}')
        output *= abs(ceil(maxhold)) - abs(floor(minhold)) + 1 -2
    else:
        print(f'button presses {abs(ceil(maxhold)) - abs(floor(minhold)) + 1}')
        output *= abs(ceil(maxhold)) - abs(floor(minhold)) + 1
    
    print(f'Output {output}')  
    
    
    file1.close()  

if __name__ == '__main__':
    #part1('day6.prod.txt')
    part2('day6.prod.txt')