## This is not working code

import os
import os
import sys
from math import floor

def testlowest(lowest, nextup, fullmap):
    
    for line in fullmap:
        if nextup >= line[1] and nextup <= line[1]+line[2]:
            testnext = nextup + line[0] - line[1]
            break
        
    if testnext == lowest:
        return True
    return False

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
    
    
    offset = 0
    while True:
        lowest = 1000000000000
        nextup = 0
        for x in range(7,0,-1):
            for i in range(0,len(fullmap[x])):
                if x == 7:
                    if offset > fullmap[x][i][2]:
                        break
                    idx = 0
                    for j in range(fullmap[x][i][0], fullmap[x][i][0]+fullmap[x][i][2]):    
                        newlowest = fullmap[x][i][0]+idx+offset
                        if lowest == 1000000000000:
                            lowest = newlowest
                            nextup = fullmap[x][i][1]+idx+offset
                            #print(f'{lowest} is lowest: {x} {nextup} ->', end="")
                            break              
                        if newlowest < lowest:
                            #if testlowest(newlowest, fullmap[x][i][1]+idx, fullmap[x]):
                            if True:
                                lowest = newlowest
                                nextup = fullmap[x][i][1]+idx+offset
                                #print(f'{lowest} is lowest: {x} {nextup} ->', end="")
                                break
                            else: 
                                lowest += 1
                        else:
                            #print(f'{lowest} is lowest: {x} {nextup} ->', end="")
                            break
                        idx += 1
                else:
                    #print(f'{lowest}, {nextup}')
                    if nextup > fullmap[x][i][0] and nextup < fullmap[x][i][0]+fullmap[x][i][2]:
                        nextup = nextup - fullmap[x][i][0] + fullmap[x][i][1]
                        #print(f'{x} {nextup} ->', end = "")
                        break
        
        #print(f'Lowest: {lowest}')
        if lowest >= 291529182:
            print('here')
        if str(nextup) in seeds:
            break
        else:
            #print(f'{nextup} not in Seeds')
            offset += 1                
                        
                        
                        
                
                

        
    print(f'Lowest {lowest}')
    print(f'Seed {nextup}')   
    
    
    file1.close()    


if __name__ == '__main__':
    part2('day5.prod.txt')