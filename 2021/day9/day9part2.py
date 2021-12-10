import argparse
import numpy as np


def readFile(fileName):
    matrix = np.genfromtxt(fileName, delimiter=1, dtype=int)
    matrix = np.pad(matrix, pad_width=1, mode='constant', constant_values=10)
    return matrix


def checkforlowpoints(matrix):
    lowpoints = []
    for x in range(matrix.shape[0] - 2, 0, -1):
        for y in range(matrix.shape[1] -2, 0, -1):
            if(matrix[x][y] < matrix[x+1][y] and matrix[x][y] < matrix[x-1][y] and matrix[x][y] < matrix[x][y+1] and matrix[x][y] < matrix[x][y-1]):
                lowpoints.append((x,y))

    return lowpoints


def checkadjacent(matrix, lowpoint):
    x = lowpoint[0]
    y = lowpoint[1]
    ret = 1

    matrix[x][y] = 10

    if(matrix[x+1][y] < 9):
        ret += checkadjacent(matrix, (x+1,y))
    if(matrix[x-1][y] < 9):
        ret += checkadjacent(matrix, (x-1,y))
    if(matrix[x][y+1] < 9):
        ret += checkadjacent(matrix, (x,y+1))
    if(matrix[x][y-1] < 9):
        ret += checkadjacent(matrix, (x,y-1))

    return ret


def findbasinsize(matrix, lowpoints):
    basinsizes = []
    for lowpoint in lowpoints:
        basinsizes.append(checkadjacent(matrix, lowpoint))
    return basinsizes


def main(args):
    numberoflines = 0
    matrix = readFile(args.input)
    lowpoints = checkforlowpoints(matrix)
    basinsizes = findbasinsize(matrix, lowpoints)

    basinsizes.sort()
    answer = 1
    for size in basinsizes[-3:]:
        answer = answer * size

    print(f'result {answer}')
    

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description='AdventOfCode2021Day9')
    parser.add_argument('--input', type=str, required=True,
                    help="File")
    args = parser.parse_args()

    main(args)