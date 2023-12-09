import os
import sys
from math import lcm



def part1(filename):
    file1 = open(os.path.join(sys.path[0], "data", filename), 'r')
    output = 0
    inpmap = []

    while True:
        line = file1.readline()
        if not line:
            break
        if line != '' and line != '\n':
            inpmap.append([int(d) for d in line.strip().split()])

    debug = 0
    for inpline in inpmap:
        debug += 1
        #print(inpline)
        maxidx = len(inpline)
        idx = maxidx-1
        resultmap = []
        resultmap.append(inpline[idx:maxidx])
        i = 0
        while True:
            if i == maxidx:
                break
            nextline = []   
            idx -= 1 
            for j in range(0, len(resultmap)):
                if j == 0:
                    resultmap[j].insert(0,inpline[idx])
                    
                if len(resultmap[j]) == 2:                    
                    nextline.append(resultmap[i][1]-resultmap[i][0])
                    resultmap.append(nextline)
                else:
                    resultmap[j+1].insert(0,resultmap[j][1]-resultmap[j][0])
            #print(resultmap)
            i += 1
        #print(resultmap) 
        
        #adding
        for j in range(len(resultmap)-1,-1,-1):
                if j == len(resultmap)-1:
                    resultmap[j].append(0)
                else:
                    resultmap[j].append(resultmap[j][-1]+resultmap[j+1][-1])
        print(resultmap)
        #print(f'{debug}: {resultmap[-2]}')
        
        print(resultmap[0][-1])
        output += resultmap[0][-1]
    print(output)
    
    file1.close()    
  


def part2(filename):
    file1 = open(os.path.join(sys.path[0], "data", filename), 'r')
    output = 0
    inpmap = []

    while True:
        line = file1.readline()
        if not line:
            break
        if line != '' and line != '\n':
            inpmap.append([int(d) for d in line.strip().split()])
            
    debug = 0
    for inpline in inpmap:
        inpline.reverse()
        debug += 1
        print(inpline)
        maxidx = len(inpline)
        idx = maxidx-1
        resultmap = []
        resultmap.append(inpline[idx:maxidx])
        i = 0
        while True:
            if i == maxidx-1:
                break
            nextline = []   
            idx -= 1 
            for j in range(0, len(resultmap)):
                if j == 0:
                    resultmap[j].insert(0,inpline[idx])
                    
                if len(resultmap[j]) == 2:                    
                    nextline.append(resultmap[i][0]-resultmap[i][1])
                    resultmap.append(nextline)
                else:
                    resultmap[j+1].insert(0,resultmap[j][0]-resultmap[j][1])
            #print(resultmap)
            i += 1
        #print(resultmap) 
        
        #adding
        for j in range(len(resultmap)-1,-1,-1):
            if j == len(resultmap)-1:
                resultmap[j].append(0)
            else:
                resultmap[j].append(resultmap[j][-1]-resultmap[j+1][-1])
        print(resultmap)
        print(f'{debug}: {resultmap[-2]}')
        
        print(resultmap[0][-1])
        output += resultmap[0][-1]
    print(output)
    
    file1.close()    
    
    
if __name__ == '__main__':
    part2('day9.prod.txt')