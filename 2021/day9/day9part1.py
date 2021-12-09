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
                lowpoints.append(matrix[x][y])

    return lowpoints



def main(args):
    numberoflines = 0
    matrix = readFile(args.input)
    lowpoints = checkforlowpoints(matrix)
    answer = sum(lowpoints) + len(lowpoints)


    print(f'result {answer}')
    

    
    


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description='AdventOfCode2021Day5')
    parser.add_argument('--input', type=str, required=True,
                    help="File")
    args = parser.parse_args()

    main(args)