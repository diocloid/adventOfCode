import os
import sys
import multiprocessing
from math import floor


def buildmap(currentmapping, line, fullmap):
    [deststart, sourcestart, rangelen] = line.strip().split(' ')
    deststart = int(deststart)
    sourcestart = int(sourcestart)
    rangelen = int(rangelen)
    idx = 0
    if currentmapping not in fullmap.keys():
        fullmap[currentmapping] = []
    fullmap[currentmapping].append([deststart, sourcestart, rangelen])
    
    return fullmap


def findlocation(seed, map):
    seed = int(seed)
    for line in map:
        if seed >= line[1] and seed <= line[1]+line[2]:
            nextseed = seed + line[0] - line[1]
            return nextseed
    
    return seed
    
    
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
           
                

        
    print(f'Seeds {seeds}')
    print(f'Fullmap {fullmap}')   
    locations = []
    for seed in seeds:
        for x in range(1,8):
            print(f'{seed} -> ', end="")            
            seed = findlocation(seed, fullmap[x])
        print(f'Location: {seed}')
        locations.append(seed)
    
    print(min(locations))
    
    file1.close()    


def calculate_locations(pair, fullmap, returnarray):
    locations = []
    splitter = floor(pair[1]%10)
    
    for i in range(splitter,pair[1],splitter):
        #print(i)
        seed = pair[0]+i
        for x in range(1,8):
            #print(f'{seed} -> ', end="")            
            seed = findlocation(seed, fullmap[x])
        #print(f'Location: {seed}')
        j=1
        while True:
            leftseed = pair[0]+i-j
            for x in range(1,8):
                #print(f'{leftseed} -> ', end="")            
                leftseed = findlocation(leftseed, fullmap[x])
            #print(f'Location: {leftseed}', end="")
            j += 1
            if leftseed < seed:
                #print(f' Leftseed is still smaller')
                seed = leftseed            
            else:                 
                #print(f' Rightseed was bigger')
                if min(returnarray) > seed:
                    returnarray.append(seed)
                break
            
            if j == splitter:
                #print(f' Checked {splitter} lefts, using smallest')                
                if min(returnarray) > seed:
                    returnarray.append(seed)
                break
            
        print(f'Part {i}/{pair[1]} done {i/pair[1]*100}% Current min {min(returnarray)}')    

        
                
    for seed in range(pair[0],pair[0]+pair[1],floor(len(range(pair[0],pair[0]+pair[1]))/5)):
            for x in range(1,8):
                print(f'{seed} -> ', end="")            
                seed = findlocation(seed, fullmap[x])
            print(f'Location: {seed}')
            locations.append(seed)
    returnarray.append(min(locations))  
    print(returnarray)  
   
            
def part2(filename):
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
           
                

        
    #print(f'Seeds {seeds}')
    #print(f'Fullmap {fullmap}')   
    
    seedpairs = []
    for i in range(0,len(seeds),2):
        seedpairs.append([int(seeds[i]), int(seeds[i+1])])
        
    print(seedpairs)    
    manager = multiprocessing.Manager()
    returnarray = manager.list()
    returnarray.append(100000000000000000000000001)
    processes = []
    
    # calculate_locations(seedpairs[0], fullmap, returnarray)
    
    for pair in seedpairs:   
        p = multiprocessing.Process(target=calculate_locations, args=(pair, fullmap, returnarray))
        processes.append(p)
        p.start()
    for p in processes:
        p.join()
        
    print(returnarray)
    print(min(returnarray))
    
    file1.close()    


if __name__ == '__main__':
    part1('day5.test.txt')
    #part2('day5.test.txt')