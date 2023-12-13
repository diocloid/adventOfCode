import os
import sys
import functools

@functools.cache
def findoptions(line, count):
    
    return count
        

def part1(filename):
    file1 = open(os.path.join(sys.path[0], "data", filename), 'r')
    output = 0
    inpmap = []
    
    while True:        
        line = file1.readline()
        if not line:
            break
        if line != '' and line != '\n':
            springs,check = line.strip().split()
            check = [int(d) for d in check.split(',')]
            inpmap.append([springs,check])
    
    for line in inpmap:
        output += findoptions(line, 0)
        
    print(f'Output: {output}') 
    print(inpmap)           
    file1.close()    
    
    
if __name__ == '__main__':
    part1('day12.test.txt')     