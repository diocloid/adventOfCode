import os
import sys
from math import floor

    
    
def part1(filename):
    file1 = open(os.path.join(sys.path[0], "data", filename), 'r')

    output = 0
    while True:
        line = file1.readline()
        if not line:
            break
        if line == '':
            break
        line = line.strip()
        [winners, mynumbers] = line.split(':')[1].split('|')
        winners = winners.strip().replace('  ', ' ').split(' ')
        mynumbers = mynumbers.strip().replace('  ', ' ').split(' ')
        i = 0
        for x in mynumbers:
            if x in winners:
                i += 1
        linnr = line.split(':')[0]
        print(f'Line {linnr}')
        print(f'Winners {i}')
        output += floor(2**(i-1))
        print(f'Output {output}')
                   
    file1.close()    
    print(output)


def part2(filename):
    file1 = open(os.path.join(sys.path[0], "data", filename), 'r')

    output = 0
    winstat = {}
    cardstat = {}
    while True:
        line = file1.readline()
        if not line:
            break
        if line == '':
            break
        
        line = line.strip()
        [winners, mynumbers] = line.split(':')[1].split('|')
        winners = winners.strip().replace('  ', ' ').split(' ')
        mynumbers = mynumbers.strip().replace('  ', ' ').split(' ')
        i = 0
        for x in mynumbers:
            if x in winners:
                i += 1
        linenr = int(line.split(':')[0][5:len(line.split(':')[0])].strip())
        winstat[linenr] = i
        cardstat[linenr] = 1
        
    print(cardstat)
    for j in range(1, len(cardstat)+1): 
        print(f'{j} has {winstat[j]} winners')
        for k in range(j+1, winstat[j]+j+1):    
            cardstat[k] += cardstat[j]
        print(cardstat)
          
    for l in cardstat:
        output += cardstat[l]  
    file1.close()    
    print(cardstat)
    print(output)

if __name__ == '__main__':
    part2('day4.prod.txt')