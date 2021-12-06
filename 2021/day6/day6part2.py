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

        #vertical lines
        if(coordinate0[0] == coordinate1[0]):
            #print(f'vertical {line}:')
            if(int(coordinate0[1]) > int(coordinate1[1])):
                temp = coordinate0[1]
                coordinate0[1] = coordinate1[1]
                coordinate1[1] = temp

            for x in range(int(coordinate0[1]), int(coordinate1[1])+1):
                y = int(coordinate0[0])
                #print(f'{x}, {y}')
                diagram[x][y] = diagram[x][y] + 1


        #horizontal lines
        elif(coordinate0[1] == coordinate1[1]):
            #print(f'horizontal {line}:')
            if(int(coordinate0[0]) > int(coordinate1[0])):
                temp = coordinate0[0]
                coordinate0[0] = coordinate1[0]
                coordinate1[0] = temp
            for y in range(int(coordinate0[0]), int(coordinate1[0])+1):
                x = int(coordinate0[1])
                #print(f'{x}, {y}')
                diagram[x][y] = diagram[x][y] + 1

        

        #diagonal top-left to bottom-right
        elif(int(coordinate0[0]) < int(coordinate1[0]) and int(coordinate0[1]) < int(coordinate1[1])):
            #print(f'diagonal top-left to bottom-right {line}:')
            i = 0
            for x in range(int(coordinate0[0]), int(coordinate1[0])+1):
                y = int(coordinate0[1]) + i
                i = i + 1
                #print(f'{x}, {y}')
                diagram[y][x] = diagram[y][x] + 1

        #diagonal bottom-right to top-left
        elif(int(coordinate0[0]) > int(coordinate1[0]) and int(coordinate0[1]) > int(coordinate1[1])):
            #print(f'diagonal bottom-right to top-left {line}:')
            i = 0
            for x in range(int(coordinate1[0]), int(coordinate0[0])+1):
                y = int(coordinate1[1]) + i
                i = i + 1
                #print(f'{x}, {y}')
                diagram[y][x] = diagram[y][x] + 1

        #diagonal top-right to bottom-left
        elif(int(coordinate0[0]) > int(coordinate1[0]) and int(coordinate0[1]) < int(coordinate1[1])):
            #print(f'diagonal top-right to bottom-left {line}:')
            i = 0
            for x in range(int(coordinate1[0]), int(coordinate0[0])+1):
                y = int(coordinate1[1]) - i
                i = i + 1
                #print(f'{x}, {y}')
                diagram[y][x] = diagram[y][x] + 1

        #diagonal bottom-left to top-right
        elif(int(coordinate0[0]) < int(coordinate1[0]) and int(coordinate0[1]) > int(coordinate1[1])):
            #print(f'diagonal bottom-left to top-right {line}:')
            i = 0
            for x in range(int(coordinate0[0]), int(coordinate1[0])+1):
                y = int(coordinate0[1]) - i
                i = i + 1
                #print(f'{x}, {y}')
                diagram[y][x] = diagram[y][x] + 1


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
        description='AdventOfCode2021Day6')
    parser.add_argument('--input', type=str, required=True,
                    help="File")
    args = parser.parse_args()

    main(args)