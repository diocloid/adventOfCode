import argparse

def readFile(fileName):
        fileObj = open(fileName, "r") #opens the file in read mode
        words = fileObj.read().splitlines() #puts the file into an array
        fileObj.close()
        return words

def main(args):
    school = readFile(args.input)
    school = school[0].split(',')
    school = list(map(int, school))
    days = 256

    timetobreed = [0,0,0,0,0,0,0,0,0]
    for index, item in enumerate(school):
        timetobreed[item] = timetobreed[item] + 1

    for day in range(0, days):
        newfish = timetobreed[0]
        timetobreed[0] = timetobreed[1]
        timetobreed[1] = timetobreed[2]
        timetobreed[2] = timetobreed[3]
        timetobreed[3] = timetobreed[4]
        timetobreed[4] = timetobreed[5]
        timetobreed[5] = timetobreed[6]
        timetobreed[5] = timetobreed[6]
        timetobreed[6] = timetobreed[7]

        timetobreed[6] += newfish

        timetobreed[7] = timetobreed[8]
        timetobreed[8] = newfish

        print(f'After {day+1} days: {timetobreed}')


    print(f'result {sum(timetobreed)}')
    

    
    


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description='AdventOfCode2021Day6')
    parser.add_argument('--input', type=str, required=True,
                    help="File")
    args = parser.parse_args()

    main(args)