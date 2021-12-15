import argparse
import numpy as np
import os

def readFile(fileName):
    matrix = np.genfromtxt(fileName, delimiter=1, dtype=int)
    matrix = np.pad(matrix, pad_width=1, mode='constant', constant_values=-1)
    return matrix


def checkdirectpath(matrix): 
    pathlen = 0

    for i in range(1, len(matrix) - 2, +1):
        pathlen += matrix[i][i]
        pathlen += matrix[i][i+1]        

    pathlen -= matrix[1][1]

    return pathlen

shortestpath = 0
def testnextpoint(matrix, point, length, path):
    global shortestpath
    length += matrix[point[0]][point[1]] 
    path.append(point)


    if(point[0] == len(matrix[0])-2 and point[1] == len(matrix)-2):
        print(f'end: {path} {length}')
        shortestpath = length
    
    if(matrix[point[0]][point[1]-1] > 0):
        if(length + matrix[point[0]][point[1]-1] < shortestpath):
            #print('path shorter')
            newpoint = (point[0], point[1]-1)
            if(newpoint not in path):                
                newpath = path.copy()
                testnextpoint(matrix, newpoint, length, newpath)

    if(matrix[point[0]][point[1]+1] > 0):
        if(length + matrix[point[0]][point[1]+1] < shortestpath):
            #print('path shorter')
            newpoint = (point[0], point[1]+1)
            if(newpoint not in path):
                newpath = path.copy()
                testnextpoint(matrix, newpoint, length, newpath)
            
    if(matrix[point[0]-1][point[1]] > 0):
        if(length + matrix[point[0]-1][point[1]] < shortestpath):
            #print('path shorter')
            newpoint = (point[0]-1, point[1])
            if(newpoint not in path):                
                newpath = path.copy()
                testnextpoint(matrix, newpoint, length, newpath)

    if(matrix[point[0]+1][point[1]] > 0):
        if(length + matrix[point[0]+1][point[1]] < shortestpath):
            #print('path shorter')
            newpoint = (point[0]+1, point[1])
            if(newpoint not in path):                
                newpath = path.copy()
                testnextpoint(matrix, newpoint, length, newpath)

    os.system('cls' if os.name == 'nt' else 'clear')
    print(f'Path longer {length}')
    print(f'shortestpath: {shortestpath}')
    #print(path)

def checkforshortestpath(matrix):
    length = 0
    point = (1, 1)
    path = []
    testnextpoint(matrix, point, length, path)


def main(args):
    global shortestpath
    matrix = readFile(args.input)
    shortestpath = checkdirectpath(matrix)
    print(shortestpath)
    checkforshortestpath(matrix)
    shortestpath -= matrix[1][1] 
    print(f'result {shortestpath}')
    

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description='AdventOfCode2021Day15')
    parser.add_argument('--input', type=str, required=True,
                    help="File")
    args = parser.parse_args()

    main(args)