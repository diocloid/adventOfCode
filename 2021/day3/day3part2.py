import argparse
def flip(binary):
    flipped = '' 
    for i in binary:
        if i == '1':
            flipped = f'{flipped}0'
        else:
            flipped = f'{flipped}1'
    return flipped

def scrub(array, bit, lengthoflines):
    scrubbing = array
    h = 0
    while h < lengthoflines:
        numberoflines = len(scrubbing)
        temparray = []
        bittotest = 0
        for i in scrubbing:
            temparray.append(int(i[h]))

        if(sum(temparray) < numberoflines/2):
            bittotest = 0
        else:
            bittotest = 1      
        if(bit == 1):
            scrubbing = [num for num in scrubbing if int(num[h]) == int(bittotest) ]       
        elif(bit == 0):
            scrubbing = [num for num in scrubbing if int(num[h]) != int(bittotest) ]  
        print(scrubbing)
        if(len(scrubbing) == 1):
            return scrubbing[0]
            
        h = h + 1


def main(args):
    dioagnosticreport = readFile(args.input)
    lengthoflines = len(dioagnosticreport[0])

    o2 = scrub(dioagnosticreport, 1, lengthoflines)
    co2 = scrub(dioagnosticreport, 0, lengthoflines)    

    print(int(o2, 2))
    print(int(co2, 2))
    print(int(o2, 2) * int(co2, 2))

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