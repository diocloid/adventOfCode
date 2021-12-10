import argparse
from os import error
import numpy as np


def readFile(fileName):
    fileObj = open(fileName, "r") #opens the file in read mode
    words = fileObj.read().splitlines() #puts the file into an array
    fileObj.close()
    return words


def checkforerrors(line):
    checkstring = ''
    for x in range(len(line)):
        if(line[x] in ['(', '[', '{', '<']):
            checkstring = f'{checkstring}{line[x]}'
        elif(line[x] == ')'):
            if(checkstring[-1:] == '('):
                checkstring = checkstring[:-1]
            else:
                print(f'Expected {checkstring[-1:]}, but found {line[x]} instead')
                return line[x]
        elif(line[x] == ']'):
            if(checkstring[-1:] == '['):
                checkstring = checkstring[:-1]
            else:
                print(f'Expected {checkstring[-1:]}, but found {line[x]} instead')
                return line[x]
        elif(line[x] == '}'):
            if(checkstring[-1:] == '{'):
                checkstring = checkstring[:-1]
            else:
                print(f'Expected {checkstring[-1:]}, but found {line[x]} instead')
                return line[x]
        elif(line[x] == '>'):
            if(checkstring[-1:] == '<'):
                checkstring = checkstring[:-1]
            else:
                print(f'Expected {checkstring[-1:]}, but found {line[x]} instead')
                return line[x]

    return -1


def main(args):
    answer = 0
    errors = [0,0,0,0]
    code = readFile(args.input)
    for line in code:
        error = checkforerrors(line)
        print(error)
        if(error == ')'):
            errors[0] += 1
        elif(error == ']'):
            errors[1] += 1
        elif(error == '}'):
            errors[2] += 1
        elif(error == '>'):
            errors[3] += 1

    answer = errors[0] * 3 + errors[1] * 57 + errors[2] * 1197 + errors[3] * 25137
    print(f'result {answer}')
    

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description='AdventOfCode2021Day10')
    parser.add_argument('--input', type=str, required=True,
                    help="File")
    args = parser.parse_args()

    main(args)