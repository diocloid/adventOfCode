import argparse
import math

def readFile(fileName):
        fileObj = open(fileName, "r") #opens the file in read mode
        words = fileObj.read().splitlines() #puts the file into an array
        fileObj.close()
        return words

# The smart solution would be something with n(n+1)/2 but this works aswell

def main(args):
    crabs = readFile(args.input)
    crabs = crabs[0].split(',')
    crabs = list(map(int, crabs))
    crabs.sort()
    avg_value = math.floor(sum(crabs) / len(crabs))
    results = []

    for target in range(avg_value-2, avg_value+2):
        print(f'target {target} from {crabs[-1]+1}')
        allfuel = 0
        for crab in crabs:
            fuel = 0
            increase = 0
            for move in range(crab, target):
                increase = increase + 1
                fuel = fuel + increase
            for move in range(target, crab):
                increase = increase + 1
                fuel = fuel + increase
            allfuel = allfuel + fuel
        results.append(allfuel)


    min_value = min(results)
    min_index = results.index(min_value)
    print(f'spent fuel {min_value}')
    print(f'index {min_index+avg_value-2}')
 
if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description='AdventOfCode2021Day7')
    parser.add_argument('--input', type=str, required=True,
                    help="File")
    args = parser.parse_args()

    main(args)