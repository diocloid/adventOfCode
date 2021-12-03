import argparse

def main(args):
    position = 0
    depth = 0
    aim = 0
    numberoflines = 0
    positionarray = readFile(args.input)
    for i in positionarray:
        movement = i.split(' ')
        numberoflines = numberoflines + 1
        if(movement[0] == 'forward'):
            position = position + int(movement[1])
        elif(movement[0] == 'down'):
            depth = depth + int(movement[1])
        elif(movement[0] == 'up'):
            depth = depth - int(movement[1])
    answer = position * depth
    print(f'------------------------------------')     
    print(f'numberoflines: {numberoflines}')    
    print(f'position: {position}')
    print(f'depth: {depth}')
    print(f'answer: {answer}')

def readFile(fileName):
        fileObj = open(fileName, "r") #opens the file in read mode
        words = fileObj.read().splitlines() #puts the file into an array
        fileObj.close()
        return words

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description='AdventOfCode2021Day2')
    parser.add_argument('--input', type=str, required=True,
                    help="File")
    args = parser.parse_args()

    main(args)