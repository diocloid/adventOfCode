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

def builddiagram(linelist):

    w, h = 1000, 1000
    diagram = [[0 for x in range(w)] for y in range(h)] 

    for line in linelist:
        coordinates = line.split(' -> ')
        coordinate0 = coordinates[0].split(',')
        coordinate1 = coordinates[1].split(',')


        if(coordinate0[0] == coordinate1[0]):
            #print('vertical line')
            #print(f'{coordinates}')
            if(int(coordinate0[1]) > int(coordinate1[1])):
                temp = coordinate0[1]
                coordinate0[1] = coordinate1[1]
                coordinate1[1] = temp

            for x in range(int(coordinate0[1]), int(coordinate1[1])+1):
                y = int(coordinate0[0])
                #print(f'{x}, {y}')

                diagram[x][y] = diagram[x][y] + 1



        if(coordinate0[1] == coordinate1[1]):
            #print('horizontal line')
            #print(f'{coordinates}')

            if(int(coordinate0[0]) > int(coordinate1[0])):
                temp = coordinate0[0]
                coordinate0[0] = coordinate1[0]
                coordinate1[0] = temp

            for y in range(int(coordinate0[0]), int(coordinate1[0])+1):
                x = int(coordinate0[1])
                #print(f'{x}, {y}')

                diagram[x][y] = diagram[x][y] + 1

    #print('\n'.join([''.join(['{:4}'.format(item) for item in row]) for row in diagram]))

    return diagram

def checkdiagram(diagram):
    result = 0
    for m in range(len(diagram) - 1, -1, -1):
        for n in range(len(diagram[m]) - 1, -1, -1):
            if(diagram[m][n] > 1):
                result = result + 1

    return result

def main(args):
    numberoflines = 0
    linelist = readFile(args.input)
    diagram = builddiagram(linelist)
    result = checkdiagram(diagram)


    print(f'result {result}')
    

    
    


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description='AdventOfCode2021Day5')
    parser.add_argument('--input', type=str, required=True,
                    help="File")
    args = parser.parse_args()

    main(args)