import argparse

def flip(binary):
    flipped = '' 
    for i in binary:
        if i == '1':
            flipped = f'{flipped}0'
        else:
            flipped = f'{flipped}1'
    return flipped

def readFile(fileName):
        fileObj = open(fileName, "r") #opens the file in read mode
        words = fileObj.read().splitlines() #puts the file into an array
        fileObj.close()
        return words


def main(args):
    numberoflines = 0
    school = readFile(args.input)
    school = school[0].split(',')
    school = list(map(int, school))
    days = 256
    result = 0
    
    print(f'Initial state: {school}')
    for i in range(0, days):
        
        for index, item in enumerate(school):
            if(school[index] == 0):
                school[index] = 6
                school.append(9)
            else:
                school[index] = school[index] - 1
        print(f'After {i} days: {len(school)}')


    print(f'result {len(school)}')
    

    
    


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description='AdventOfCode2021Day6')
    parser.add_argument('--input', type=str, required=True,
                    help="File")
    args = parser.parse_args()

    main(args)