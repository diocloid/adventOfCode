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
    pairs = {}
    counter = {}
    for i in range(len(polymer)-1):
        if(f'{polymer[i]}{polymer[i+1]}' not in pairs):
            pairs[(f'{polymer[i]}{polymer[i+1]}')] = 1
        else:
            pairs[(f'{polymer[i]}{polymer[i+1]}')] += 1

    for i in range(len(polymer)):
        if(polymer[i] not in counter):
            counter[polymer[i]] = 1
        else:
            counter[polymer[i]] += 1

    for x in range(1, replacements+1, +1):

        localpairs = pairs.copy()
        for pair, value in localpairs.items():
            pairs[pair] -= value
            if(pair[0] + replacementrules[pair] not in pairs):
               pairs[pair[0] + replacementrules[pair]] = value
            else:
                pairs[pair[0] + replacementrules[pair]] += value

            if(replacementrules[pair] + pair[1] not in pairs):
               pairs[replacementrules[pair] + pair[1]] = value
            else:
                pairs[replacementrules[pair] + pair[1]] += value
            
            if(replacementrules[pair] not in counter):
               counter[replacementrules[pair]] = 0            
            counter[replacementrules[pair]] += value


        #print(f'After step {x}: {counter}')


    return max(counter.values()) - min(counter.values())




def main(args):
    input = readFile(args.input)
    data = datafrominput(input)
    result = buildpolymer(data[0], data[1], 40)
    print(f'result {result}')
    

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description='AdventOfCode2021Day14')
    parser.add_argument('--input', type=str, required=True,
                    help="File")
    args = parser.parse_args()

    main(args)