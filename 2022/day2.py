import os
import sys



def readfile(filename):
    result = 0    
    file1 = open(os.path.join(sys.path[0], "data", filename), 'r')
        
    while True:
        line = file1.readline()
        if not line:
            break
        
        values = line.strip().split(" ")
        #Part 1 
        # if values[0] == "A" and values[1] == "X":
        #     result = result + 1 + 3
        # elif values[0] == "A" and values[1] == "Y":
        #     result = result + 2 + 6
        # elif values[0] == "A" and values[1] == "Z":
        #     result = result + 3 + 0
        # elif values[0] == "B" and values[1] == "X":
        #     result = result + 1 + 0
        # elif values[0] == "B" and values[1] == "Y":
        #     result = result + 2 + 3
        # elif values[0] == "B" and values[1] == "Z":
        #     result = result + 3 + 6
        # elif values[0] == "C" and values[1] == "X":
        #     result = result + 1 + 6
        # elif values[0] == "C" and values[1] == "Y":
        #     result = result + 2 + 0
        # elif values[0] == "C" and values[1] == "Z":
        #     result = result + 3 + 3
        #Part2
        if values[1] == "X" and values[0] == "A":
            result = result + 3 + 0
        elif values[1] == "X" and values[0] == "B":
            result = result + 1 + 0
        elif values[1] == "X" and values[0] == "C":
            result = result + 2 + 0
        elif values[1] == "Y" and values[0] == "A":
            result = result + 1 + 3
        elif values[1] == "Y" and values[0] == "B":
            result = result + 2 + 3
        elif values[1] == "Y" and values[0] == "C":
            result = result + 3 + 3
        elif values[1] == "Z" and values[0] == "A":
            result = result + 2 + 6
        elif values[1] == "Z" and values[0] == "B":
            result = result + 3 + 6
        elif values[1] == "Z" and values[0] == "C":
            result = result + 1 + 6
            
        print(result)
    
    file1.close()

if __name__ == '__main__':
    readfile('day2.txt')
