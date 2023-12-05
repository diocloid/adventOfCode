import os
import sys
from math import floor


def buildmap(currentmapping, line, fullmap):
    [deststart, sourcestart, rangelen] = line.strip().split(' ')
    deststart = int(deststart)
    sourcestart = int(sourcestart)
    rangelen = int(rangelen)
    idx = 0
    print(f'mapping {currentmapping}')
    if currentmapping not in fullmap.keys():
        fullmap[currentmapping] = {}
        
    for x in range(sourcestart, sourcestart+rangelen):
        fullmap[currentmapping][x] = deststart+idx
        idx += 1
        
    fullmap[currentmapping] = dict(sorted(fullmap[currentmapping].items()))
    return fullmap


def fillrest(minseed, maxseed, fullmap, step):
    idx = 0
    for x in range(minseed, maxseed+1):
        if x not in fullmap[step].keys():
            fullmap[step][x] = x
            idx += 1
            
    fullmap[step] = dict(sorted(fullmap[step].items()))    
        
    if(step < 7):
        lowest = min(fullmap[step].items(), key=lambda x: x[1])
        highest = max(fullmap[step].items(), key=lambda x: x[1])
        fullmap = fillrest(int(lowest[1]), int(highest[1]), fullmap, step+1)
        
    fullmap[step] = dict(sorted(fullmap[step].items()))
    return fullmap
    
def part1(filename):
    file1 = open(os.path.join(sys.path[0], "data", filename), 'r')
    seeds = []
    output = 0
    fullmap = {}
    currentmapping = 0
    while True:
        line = file1.readline()
        if not line:
            break
        if line != '' and line != '\n':
            line = line.strip()
        
        
            if line[0:5] == 'seeds':
                seeds = line.split(':')[1].strip().split(' ')
                for seed in seeds:
                    seed = seed.strip()                
            elif line[0:12] == 'seed-to-soil':
                currentmapping = 1
            elif line[0:4] == 'soil':
                currentmapping = 2
            elif line[0:4] == 'fert':
                currentmapping = 3
            elif line[0:4] == 'wate':
                currentmapping = 4
            elif line[0:4] == 'ligh':
                currentmapping = 5
            elif line[0:4] == 'temp':
                currentmapping = 6
            elif line[0:4] == 'humi':
                currentmapping = 7   
            else:  
                fullmap = buildmap(currentmapping, line, fullmap)  
           
                    
    fullmap = fillrest(int(min(seeds)), int(max(seeds)), fullmap, 1)
        
    print(f'Seeds {seeds}')
    print(f'Fullmap {fullmap}')   
    locations = []
    for seed in seeds:
        location = fullmap[7][fullmap[6][fullmap[5][fullmap[4][fullmap[3][fullmap[2][fullmap[1][int(seed)]]]]]]]
        print(f'Seed {seed}: location {location}')
        locations.append(location)      
    file1.close()    
    print(min(locations))


if __name__ == '__main__':
    part1('day5.prod.txt')