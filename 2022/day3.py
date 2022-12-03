import os
import sys
import math


def part1(filename):
    result = 0    
    file1 = open(os.path.join(sys.path[0], "data", filename), 'r')
        
    while True:
        line = file1.readline()
        if not line:
            break
        
        
        lengthofline = len(line)
        firstbackpackcompartment = line.strip()[:math.floor(lengthofline/2)]
        secondbackpackcompartment = line.strip()[math.floor(lengthofline/2):]
        
        #print(firstbackpackcompartment)
        #print(secondbackpackcompartment)
        
        for element in range(0, len(firstbackpackcompartment)):
            if firstbackpackcompartment[element] in secondbackpackcompartment:
                #print(firstbackpackcompartment[element])
                if firstbackpackcompartment[element].isupper():
                    #print(ord(firstbackpackcompartment[element])-38)
                    result += ord(firstbackpackcompartment[element])-38
                elif firstbackpackcompartment[element].islower():
                    #print(ord(firstbackpackcompartment[element])-96)
                    result += ord(firstbackpackcompartment[element])-96
                break
    file1.close()
    print(result)    
  
def part2(filename):
    result = 0    
    file1 = open(os.path.join(sys.path[0], "data", filename), 'r')
        
    while True:
        line1 = file1.readline().strip()        
        if not line1:
            break
        
        line2 = file1.readline().strip()
        line3 = file1.readline().strip()
                    
        in1and2 = []        
        for element in range(0, len(line1)):    
            if line1[element] in line2:  
                 in1and2.append(line1[element])  
                  
        
        for element in range(0, len(line3)):  
            if line3[element] in in1and2:                  
                if line3[element].isupper():
                    result += ord(line3[element])-38
                    break
                elif line3[element].islower():
                    result += ord(line3[element])-96
                    break
                
    file1.close()
    print(result)
    
    
if __name__ == '__main__':
    part1('day3.txt')
    part2('day3.txt')
