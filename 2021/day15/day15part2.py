import argparse
import numpy as np
import os
import heapq

def readFile(fileName):
    matrix = np.genfromtxt(fileName, delimiter=1, dtype=int)
    return matrix


def checkpath(matrix):
    width = len(matrix[0])
    depth = len(matrix)
    visited = {}
    pointstocheck = [(0,0,0)]

    while pointstocheck:
        x, y, cost = heapq.heappop(pointstocheck)

        if(x == width - 1 and y == depth - 1):
            print('this is the end')
            return cost

        for testx, testy in ((x-1,y),(x+1,y),(x,y-1),(x,y+1)):
            #check if path to current path is faster somewhere else
            if (0 <= testx < width and 0 <= testy < depth):
                newcost = cost + matrix[testx][testy]
                if(visited.get((testx,testy),9999) > newcost):
                    visited[(testx,testy)] = newcost
                    heapq.heappush(pointstocheck, (testx, testy, newcost))


def expandmatrix(matrix):    
    width = len(matrix[0])
    depth = len(matrix)
    bigmatrix = []

    for x in range(0, depth * 5, +1):

        line = [0] * width * 5
        for y in range(0, width * 5, +1):
            distance = x // width + y // depth
            line[y] = (matrix[x%depth][y%width]+distance)%9
            if(line[y] == 0):
                line[y] = 9
            
        bigmatrix.append(line)

    return bigmatrix

def main(args):
    global shortestpath
    matrix = readFile(args.input)

    bigmatrix = expandmatrix(matrix)
    shortestpath = checkpath(bigmatrix)
    print(f'result {shortestpath}')
    

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description='AdventOfCode2021Day15')
    parser.add_argument('--input', type=str, required=True,
                    help="File")
    args = parser.parse_args()

    main(args)