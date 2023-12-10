import os
import sys


def printmap(printablemap):
    for line in printablemap:
        print('')
        for char in line:
            print(f' {char} ', end='')
                
    print('')

def fillmap(inpmap, start):
    #printmap(inpmap)
    if inpmap[start[0]][start[1]] != 'X':
        inpmap[start[0]][start[1]] = '0'


    try:
        if  inpmap[start[0]][start[1]+1] not in ['X','0']:
            inpmap = fillmap(inpmap, [start[0], start[1]+1])
    except IndexError:
        pass
    try:
        if start[1]-1 > 0:
            if  inpmap[start[0]][start[1]-1] not in ['X','0']:
                inpmap = fillmap(inpmap, [start[0], start[1]-1])
    except IndexError:
        pass
    try:
        if  inpmap[start[0]+1][start[1]] not in ['X','0']:
            inpmap = fillmap(inpmap, [start[0]+1, start[1]])
    except IndexError:
        pass
    try:
        if start[0]-1 > 0:
            if  inpmap[start[0]-1][start[1]] not in ['X','0']:
                inpmap = fillmap(inpmap, [start[0]-1, start[1]])
    except IndexError:
        pass
        
    return inpmap        
        

def part1(filename):
    file1 = open(os.path.join(sys.path[0], "data", filename), 'r')
    output = 0
    inpmap = []
    start = []
    x = 0
    y = 0
    
    while True:        
        line = file1.readline()
        if not line:
            break
        if line != '' and line != '\n':
            linearr = []
            line = line.strip()
            x = 0
            for char in line:                
                linearr.append(char)
                if char == 'S':
                    start = [y,x]
                x += 1
            inpmap.append(linearr)
        y += 1
   
    #print(inpmap)
    #print(start)
    
    found = False
    pathlen = 0
    lastmove = ''
    w, h = len(inpmap[0])*2, len(inpmap)*2
    doublemap = [['.' for x in range(w)] for y in range(h)] 
    
    for x in range(0, len(inpmap)):
        for y in range(0, len(inpmap[x])):
            doublemap[x*2][y*2] = inpmap[x][y]    
    
    for line in doublemap:
        line.insert(0,'.')
        line.append('.')
    
    temp = []
    for i in doublemap[0]:
        temp.append('.')
    doublemap.insert(0,temp)
    
    for y in range(0, len(doublemap)-1):
        for x in range(0, len(doublemap[y])-1):
            if doublemap[y][x] == '.':
                pass
            elif doublemap[y][x] == '-':
                if doublemap[y][x+1] == '.':
                    doublemap[y][x+1] = '-'
            elif doublemap[y][x] == '|':
                if doublemap[y+1][x] == '.':
                    doublemap[y+1][x] = '|'
            elif doublemap[y][x] == 'F':
                doublemap[y+1][x] = '|'
                doublemap[y][x+1] = '-'
            elif doublemap[y][x] == '7':
                doublemap[y+1][x] = '|'
                doublemap[y][x-1] = '-'
            elif doublemap[y][x] == 'J':
                doublemap[y-1][x] = '|'
                doublemap[y][x-1] = '-'
            elif doublemap[y][x] == 'L':
                doublemap[y-1][x] = '|'
                doublemap[y][x+1] = '-'
            elif doublemap[y][x] == 'S':
                if doublemap[y-2][x] == '|':
                    doublemap[y-1][x] = '|'
                if doublemap[y+2][x] == '|':
                    doublemap[y+1][x] = '|'
                if doublemap[y][x+2] == '-':
                    doublemap[y][x+1] = '-'
                if doublemap[y][x-2] == '-':
                    doublemap[y][x-1] = '-'
                
                
    finalmap = inpmap        
    inpmap = doublemap
    start = [(start[0]*2)+1,(start[1]*2)+1]
            
    while True:
        if found:
            print(pathlen/2)
            break
        
        #findfirst
        if pathlen == 0:
            if inpmap[start[0]][start[1]+1] in ['-','J','7']:
                #print('right')
                lastmove = 'right'
                pathlen += 1
                start = [start[0], start[1]+1] 
            elif inpmap[start[0]+1][start[1]] in ['|','J','L']:
                #print('down')
                lastmove = 'down'
                pathlen += 1
                start = [start[0]+1, start[1]]
            elif inpmap[start[0]][start[1]-1] in ['-','F','L']:
                #print('left')
                lastmove = 'left'
                pathlen += 1
                start = [start[0], start[1]-1]
            elif inpmap[start[0]-1][start[1]] in ['|','F','7']:
                #print('up')
                lastmove = 'up'
                pathlen += 1
                start = [start[0]-1, start[1]]
                
        else:
            if inpmap[start[0]][start[1]] == '-':
                inpmap[start[0]][start[1]] = 'X'
                pathlen += 1
                if lastmove == 'right':                
                    start = [start[0], start[1]+1]
                    lastmove = 'right' 
                if lastmove == 'left':                
                    start = [start[0], start[1]-1]
                    lastmove = 'left' 
            if inpmap[start[0]][start[1]] == '|':
                inpmap[start[0]][start[1]] = 'X'
                pathlen += 1
                if lastmove == 'up':                
                    start = [start[0]-1, start[1]]
                    lastmove = 'up' 
                if lastmove == 'down':                
                    start = [start[0]+1, start[1]]
                    lastmove = 'down' 
            if inpmap[start[0]][start[1]] == 'J':
                inpmap[start[0]][start[1]] = 'X'
                pathlen += 1
                if lastmove == 'right':                
                    start = [start[0]-1, start[1]]
                    lastmove = 'up' 
                if lastmove == 'down':                
                    start = [start[0], start[1]-1]
                    lastmove = 'left' 
            if inpmap[start[0]][start[1]] == '7':
                inpmap[start[0]][start[1]] = 'X'
                pathlen += 1
                if lastmove == 'right':                
                    start = [start[0]+1, start[1]]
                    lastmove = 'down' 
                if lastmove == 'up':                
                    start = [start[0], start[1]-1]
                    lastmove = 'left' 
            if inpmap[start[0]][start[1]] == 'F':
                inpmap[start[0]][start[1]] = 'X'
                pathlen += 1
                if lastmove == 'left':                
                    start = [start[0]+1, start[1]]
                    lastmove = 'down' 
                if lastmove == 'up':                
                    start = [start[0], start[1]+1]
                    lastmove = 'right'
            if inpmap[start[0]][start[1]] == 'L':
                inpmap[start[0]][start[1]] = 'X'
                pathlen += 1
                if lastmove == 'left':                
                    start = [start[0]-1, start[1]]
                    lastmove = 'up' 
                if lastmove == 'down':                
                    start = [start[0], start[1]+1]
                    lastmove = 'right'
            if inpmap[start[0]][start[1]] == 'S':
                inpmap[start[0]][start[1]] = 'X'
                found = True     
    
    inpmap = fillmap(inpmap, [0,0])
    # for x in range(0,len(inpmap[0])-1):
    #     inpmap = fillmap(inpmap, [0,x])
    #     inpmap = fillmap(inpmap, [len(inpmap)-1,x])
        
    # for y in range(0,len(inpmap)-1):
    #     inpmap = fillmap(inpmap, [y,0])
    #     inpmap = fillmap(inpmap, [y,len(inpmap[0])-1])
    
    printmap(inpmap)

    for x in range(0, len(finalmap)):
        for y in range(0, len(finalmap[x])):
            finalmap[x][y] = inpmap[(x*2)-1][(y*2)-1]
    
    printmap(finalmap)
    
    for line in finalmap:
        print('')
        for char in line:
            print(f' {char} ', end='')
            if char not in ['X','0']:
                output += 1
    print('') 
    print(output)            
    file1.close()    
    
    
if __name__ == '__main__':
    sys.setrecursionlimit(100000)
    part1('day10.prod.txt')