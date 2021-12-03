import argparse

def main(args):
    increases = 0
    decreases = 0
    numberoflines = 0
    prev = -1
    deptharray = readFile(args.input)
    for i in deptharray:
        numberoflines = numberoflines + 1
        if(prev == -1):
            print(f'{i} (N/A - no previous measurement)')
        elif(prev < int(i)):
            print(f'{i} (increased)')
            increases = increases + 1
        elif(prev > int(i)):
            print(f'{i} (decreased)')
            decreases = decreases + 1
        prev = int(i)
    print(f'------------------------------------')     
    print(f'{numberoflines} numberoflines')    
    print(f'{increases} increases')
    print(f'{decreases} decreases')

def readFile(fileName):
        fileObj = open(fileName, "r") #opens the file in read mode
        words = fileObj.read().splitlines() #puts the file into an array
        fileObj.close()
        return words

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description='AdventOfCode2021Day1')
    parser.add_argument('--input', type=str, required=True,
                    help="File")
    args = parser.parse_args()

    main(args)