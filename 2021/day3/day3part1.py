import argparse
def flip(binary):
    flipped = '' 
    for i in binary:
        if i == '1':
            flipped = f'{flipped}0'
        else:
            flipped = f'{flipped}1'
    return flipped

def main(args):
    position = 0
    depth = 0
    aim = 0
    numberoflines = 0
    dioagnosticreport = readFile(args.input)
    lengthoflines = len(dioagnosticreport[0])
    numberoflines = len(dioagnosticreport)
    gammabinary = ''
    h = 0
    while h < lengthoflines:
        temparray = []
        for i in dioagnosticreport:
            temparray.append(int(i[h]))
        if(sum(temparray) < numberoflines/2):
            gammabinary = f'{gammabinary}0'
        else:
            gammabinary = f'{gammabinary}1'   
        h = h + 1

    print(int(gammabinary, 2))
    print(int(flip(gammabinary), 2))
    print(int(gammabinary, 2) * int(flip(gammabinary), 2))
   

def readFile(fileName):
        fileObj = open(fileName, "r") #opens the file in read mode
        words = fileObj.read().splitlines() #puts the file into an array
        fileObj.close()
        return words

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description='AdventOfCode2021Day3')
    parser.add_argument('--input', type=str, required=True,
                    help="File")
    args = parser.parse_args()

    main(args)