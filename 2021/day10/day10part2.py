import argparse
from os import error
from math import floor


def readFile(fileName):
    fileObj = open(fileName, "r") #opens the file in read mode
    words = fileObj.read().splitlines() #puts the file into an array
    fileObj.close()
    return words


def checkforerrors(line):
    checkstring = ''
    completestring = ''
    for x in range(len(line)):
        if(line[x] in ['(', '[', '{', '<']):
            checkstring = f'{checkstring}{line[x]}'
        elif(line[x] == ')'):
            if(checkstring[-1:] == '('):
                checkstring = checkstring[:-1]
            else:
                #print(f'Expected {checkstring[-1:]}, but found {line[x]} instead')
                return -1
        elif(line[x] == ']'):
            if(checkstring[-1:] == '['):
                checkstring = checkstring[:-1]
            else:
                #print(f'Expected {checkstring[-1:]}, but found {line[x]} instead')
                return -1
        elif(line[x] == '}'):
            if(checkstring[-1:] == '{'):
                checkstring = checkstring[:-1]
            else:
                #print(f'Expected {checkstring[-1:]}, but found {line[x]} instead')
                return -1
        elif(line[x] == '>'):
            if(checkstring[-1:] == '<'):
                checkstring = checkstring[:-1]
            else:
                return -1

    #print(f'incomplete: {checkstring}')
    for x in range(len(checkstring) -1, -1, -1):
        if(checkstring[x] == '('):
            completestring = f'{completestring})'
        elif(checkstring[x] == '['):
            completestring = f'{completestring}]'
        elif(checkstring[x] == '{'):
            completestring = f'{completestring}}}'
        elif(checkstring[x] == '<'):
            completestring = f'{completestring}>'
    return completestring


def main(args):
    scores = []
    code = readFile(args.input)
    for line in code:
        completesting = checkforerrors(line)
        if(completesting != -1):
            #print(completesting)
            temp = 0
            for x in completesting:
                temp = temp * 5
                if(x == ')'):
                    temp += 1
                elif(x == ']'):
                    temp += 2
                elif(x == '}'):
                    temp += 3
                elif(x == '>'):
                    temp += 4
            scores.append(temp)

    scores.sort()
    answer = scores[floor(len(scores)/2)]
    print(f'result {answer}')
    

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description='AdventOfCode2021Day10')
    parser.add_argument('--input', type=str, required=True,
                    help="File")
    args = parser.parse_args()

    main(args)