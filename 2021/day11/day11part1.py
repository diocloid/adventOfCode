import argparse
import numpy as np

# importing the sys module
import sys
 
# the setrecursionlimit function is
# used to modify the default recursion
# limit set by python. Using this,
# we can increase the recursion limit
# to satisfy our needs
 
sys.setrecursionlimit(10**7)


def readFile(fileName):
    matrix = np.genfromtxt(fileName, delimiter=1, dtype=int)
    matrix = np.pad(matrix, pad_width=1, mode='constant', constant_values=-1)
    return matrix

def increaseAllByOne(matrix):
    for x in range(matrix.shape[0] - 2, 0, -1):
            for y in range(matrix.shape[1] -2, 0, -1):
                matrix[x][y] += 1
    
    return matrix


def findMaximums(matrix):
    flashes = 0
    for x in range(matrix.shape[0] - 2, 0, -1):
        for y in range(matrix.shape[1] -2, 0, -1):
            if(matrix[x][y] > 9):
                flashes += testForFlashes(matrix, x, y)


    return flashes


def testForFlashes(matrix, x, y):
    flashes = 0
    #print(f'flash {x} {y}')
    matrix[x][y] = 0
    flashes += 1

    #increase all adjecent
    if(matrix[x+1][y] > 0):
        matrix[x+1][y] += 1

    if(matrix[x+1][y-1] > 0):
        matrix[x+1][y-1] += 1

    if(matrix[x+1][y+1] > 0):
        matrix[x+1][y+1] += 1

    if(matrix[x][y+1] > 0):
        matrix[x][y+1]  += 1

    if(matrix[x][y-1] > 0):
        matrix[x][y-1] += 1
        
    if(matrix[x-1][y] > 0):
        matrix[x-1][y] += 1

    if(matrix[x-1][y-1] > 0):
        matrix[x-1][y-1]  += 1

    if(matrix[x-1][y+1] > 0):
        matrix[x-1][y+1] += 1

    #check for flashes in adjecent  

    if(matrix[x+1][y] > 9):
        flashes += testForFlashes(matrix, x+1, y)

    if(matrix[x+1][y-1] > 9):
        flashes += testForFlashes(matrix, x+1, y-1)

    if(matrix[x+1][y+1] > 9):
        flashes += testForFlashes(matrix, x+1, y+1)

    if(matrix[x][y+1] > 9):
        flashes += testForFlashes(matrix, x, y+1)

    if(matrix[x][y-1] > 9):
        flashes += testForFlashes(matrix, x, y-1)

    if(matrix[x-1][y] > 9):
        flashes += testForFlashes(matrix, x-1, y)

    if(matrix[x-1][y-1] > 9):
        flashes += testForFlashes(matrix, x-1, y-1)

    if(matrix[x-1][y+1] > 9):
        flashes += testForFlashes(matrix, x-1, y+1)
                


    return flashes

def runsimulation(matrix):
    flashes = 0
    for day in range(0, 100):
        print(f'day {day+1}')
        matrix = increaseAllByOne(matrix)        
        flashes += findMaximums(matrix)
        print(f'flashes {flashes}')
        #print(matrix)
        

        



def main(args):
    numberoflines = 0
    matrix = readFile(args.input)
    results = runsimulation(matrix)
    print(f'result {results}')
    

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description='AdventOfCode2021Day11')
    parser.add_argument('--input', type=str, required=True,
                    help="File")
    args = parser.parse_args()

    main(args)