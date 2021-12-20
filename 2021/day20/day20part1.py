import argparse
import numpy as np
import os
import re
import math

def readFile(fileName):
    fileObj = open(fileName, "r") #opens the file in read mode
    lines = fileObj.read()
    lines = lines.replace('.', '0')
    lines = lines.replace('#', '1')
    lines = lines.rsplit('\n')
    fileObj.close()
    return lines

def parseinput(input):
    algorithmstring = input[0]
    algorithm = []
    for char in algorithmstring:
        algorithm.append(int(char))

    matrixstring = input[2:]
    matrix = []
    for line in matrixstring:
        matrixline = []
        for char in line:
            matrixline.append(int(char))
        matrix.append(matrixline)
    matrix = np.array(matrix)
    return algorithm, matrix

def checkenhancementpixel(matrix, algorithm, tupel):
    number = ''
    x = tupel[0]
    y = tupel[1]
    number += str(matrix[x][y])
    number += str(matrix[x][y+1])
    number += str(matrix[x][y+2])
    number += str(matrix[x+1][y])
    number += str(matrix[x+1][y+1])
    number += str(matrix[x+1][y+2])
    number += str(matrix[x+2][y])
    number += str(matrix[x+2][y+1])
    number += str(matrix[x+2][y+2])
    bit = int(number, 2)
    #print(bit)
    pixel = algorithm[bit]
    return pixel

def enhance(matrix, algorithm, sillypaddingnotinthetest):
    newmatrix = np.pad(matrix, pad_width=1, mode='constant', constant_values=sillypaddingnotinthetest)
    scanmatrix =  np.pad(newmatrix, pad_width=1, mode='constant', constant_values=sillypaddingnotinthetest)
    for y in range(0, len(newmatrix), +1):
        for x in range(0, len(newmatrix[0]), +1):

            pixel = checkenhancementpixel(scanmatrix, algorithm, (y,x))
            newmatrix[y][x] = pixel
    sillypaddingnotinthetest = algorithm[int(str(sillypaddingnotinthetest)*9, 2)]
    return newmatrix, sillypaddingnotinthetest

def main(args):
    input = readFile(args.input)
    algorithm, matrix = parseinput(input)
    sillypaddingnotinthetest = 0
    for i in range(2):
        #print(matrix)
        matrix, sillypaddingnotinthetest = enhance(matrix, algorithm, sillypaddingnotinthetest)
    #print(matrix)
    answer = np.count_nonzero(matrix)
    print(answer)
    

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description='AdventOfCode2021Day20')
    parser.add_argument('--input', type=str, required=True,
                    help="File")
    args = parser.parse_args()

    main(args)