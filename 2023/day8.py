import os
import sys
from math import lcm



def part1(filename):
    file1 = open(os.path.join(sys.path[0], "data", filename), 'r')
    output = 0
    map = {}
    linecount = 0
    rls = ''
    while True:
        line = file1.readline()
        if not line:
            break
        if line != '' and line != '\n':
            if linecount == 0:
                rls = line.strip().replace('L', '0').replace('R', '1')
            else:    
                node = line.strip().split('=')[0].strip()
                left, right = line.strip().split('=')[1].strip().split(',')
                left = left.replace('(','').strip()
                right = right.replace(')','').strip()
                if left == right and left == node:
                    print('ignored')
                else:
                    map[node] = [left,right]
                
            linecount += 1
    
    walker = 0   
    node = 'AAA'     
    while True:
        newnode = ''
        newnode = map[node][int(rls[walker%len(rls)])]
        print(newnode)
        if newnode == 'ZZZ':
            break;
        node = newnode
        walker += 1
               

        
    print(walker+1)
    
    file1.close()    
  
def part2(filename):
    file1 = open(os.path.join(sys.path[0], "data", filename), 'r')
    output = 0
    map = {}
    linecount = 0
    rls = ''
    while True:
        line = file1.readline()
        if not line:
            break
        if line != '' and line != '\n':
            if linecount == 0:
                rls = line.strip().replace('L', '0').replace('R', '1')
            else:    
                node = line.strip().split('=')[0].strip()
                left, right = line.strip().split('=')[1].strip().split(',')
                left = left.replace('(','').strip()
                right = right.replace(')','').strip()
                if left == right and left == node:
                    print('ignored')
                else:
                    map[node] = [left,right]
                
            linecount += 1
    
      
    nodes = []  
    ends = []
    
    for node in map:
        if node[2] == 'A':
            nodes.append(node)
    print(nodes) 
    
    nodecounter = 0
    for node in nodes:
        walker = 0         
        while True:
            newnode = ''           
            newnode = map[node][int(rls[walker%len(rls)])]
                
            print(newnode)
            if newnode[2] == 'Z':
                ends.append(walker+1)
                break    
            node = newnode
            walker += 1
        
        nodecounter += 1   

        
    print(lcm(*ends))
    
    file1.close()    
  

if __name__ == '__main__':
    part2('day8.prod.txt')