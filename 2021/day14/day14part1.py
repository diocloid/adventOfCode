import argparse
from collections import Counter

def readFile(fileName):
    fileObj = open(fileName, "r") #opens the file in read mode
    words = fileObj.read().splitlines() #puts the file into an array
    fileObj.close()
    return words


def datafrominput(input): 
    replacementrules = {}
    polymer = input[0]
    del(input[0])
    del(input[0])
    for line in input:
        rule = line.split(' -> ')
        replacementrules[rule[0]] = rule[1]
    
    return([polymer, replacementrules])

def buildpolymer(polymer, replacementrules, replacements): 
    pairs = []
    for i in range(len(polymer)-1):
        pairs.append(f'{polymer[i]}{polymer[i+1]}')

    for x in range(1, replacements+1, +1):
        newpairs = []

        for i in range(len(pairs)):
            newpairs.append(f'{pairs[i][0]}{replacementrules[pairs[i]]}')
            newpairs.append(f'{replacementrules[pairs[i]]}{pairs[i][1]}')
        pairs = newpairs

        printpairs = []
        for i in range(0, len(pairs), +1):
            printpairs.append(pairs[i][0])
        printpairs.append(pairs[len(pairs)-1][1])
        printstring = ' '.join([str(elem) for elem in printpairs])
        print(f'After step {x}: {printstring}')


    return pairs

def answerfrompairs(pairs):
    last = pairs[len(pairs)-1][1]
    for i in range(len(pairs)-1, -1, -1):
        pairs[i] = pairs[i][0]
    pairs.append(last)

    maxoccurence = max(set(pairs), key = pairs.count)
    minoccurence = min(set(pairs), key = pairs.count)
    counter = Counter(pairs)
    return counter[maxoccurence] - counter[minoccurence]

def main(args):
    input = readFile(args.input)
    data = datafrominput(input)
    pairs = buildpolymer(data[0], data[1], 10)
    answer = answerfrompairs(pairs)
    print(f'result {answer}')
    

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description='AdventOfCode2021Day14')
    parser.add_argument('--input', type=str, required=True,
                    help="File")
    args = parser.parse_args()

    main(args)