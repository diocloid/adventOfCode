import argparse

def readFile(fileName):
        fileObj = open(fileName, "r") #opens the file in read mode
        words = fileObj.read().splitlines() #puts the file into an array
        fileObj.close()
        return words


def main(args):
    values = readFile(args.input)
    input = []
    output = []
    onefourseveneight = 0
    for value in values:
        value = value.split('|')
        output.append(value[1].strip().split(' '))
        input.append(value[0].strip().split(' '))
        
    for testarray in output:
        for test in testarray:
            if(len(test) in [2, 3, 4, 7]):
                onefourseveneight += 1




    
    print(f'Initial state: {output}')
    print(f'answer: {onefourseveneight}')

    
    

    
    


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description='AdventOfCode2021Day8')
    parser.add_argument('--input', type=str, required=True,
                    help="File")
    args = parser.parse_args()

    main(args)