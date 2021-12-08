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
    
    answer = 0

    

    for value in values:
        value = value.split('|')
        output = value[1].strip().split(' ')
        input = value[0].strip().split(' ')
    
        configuration = [[],[],[],[],[],[],[],[]]
        for test in input:
            if(len(test) == 2):
                configuration[2].append(test)
            elif(len(test) == 3):
                configuration[3].append(test)
            elif(len(test) == 4):
                configuration[4].append(test)
            elif(len(test) == 5):
                configuration[5].append(test)
            elif(len(test) == 6):
                configuration[6].append(test)
            elif(len(test) == 7):
                configuration[7].append(test)  


        pattern = ['','','','','','','']     

        # find the one with two digits this is a "1"
        theonewithtwodigits = configuration[2][0]

        # findtheonewith treee digits
        theonewiththreedigits = configuration[3][0]
        # p0 in the "7" but not in the "1"
        for point in theonewiththreedigits:
            if (point not in theonewithtwodigits):
                pattern[0] = point

        # find the one with four digits this is a "4"
        theonewithfourdigits = configuration[4][0]

        # find the three with five digits
        thetreewithfivedigits = configuration[5] 

        #findthecharacters present in all three five digit
        charcounter = {
            "a": 0,
            "b": 0,
            "c": 0,
            "d": 0,
            "e": 0,
            "f": 0,
            "g": 0,
        }
        for test in thetreewithfivedigits:
            for char in test:
                if(char == 'a'):
                    charcounter['a'] += 1
                elif(char == 'b'):
                    charcounter['b'] += 1
                elif(char == 'c'):
                    charcounter['c'] += 1
                elif(char == 'd'):
                    charcounter['d'] += 1
                elif(char == 'e'):
                    charcounter['e'] += 1
                elif(char == 'f'):
                    charcounter['f'] += 1
                elif(char == 'g'):
                    charcounter['g'] += 1
        charcounter = {key:val for key, val in charcounter.items() if val == 3}

        # discard p0
        del charcounter[pattern[0]]

        #find the remaining 2 characters against the "4"
        for char in charcounter:
            if(char in theonewithfourdigits):
                pattern[3] = char
            else:
                pattern[6] = char

        #find the tree with six digits
        thetreewithsixdigits = configuration[6]

        #find the char out of "1" in all three six digits
        charcounter = {
            "a": 0,
            "b": 0,
            "c": 0,
            "d": 0,
            "e": 0,
            "f": 0,
            "g": 0,
        }

        for char in theonewithtwodigits:
            for sixdigitentry in thetreewithsixdigits:
                if(char in sixdigitentry):
                    charcounter[char] += 1
        
        #the one in all three sixes is p5
        pattern[5] = list(charcounter.keys())[list(charcounter.values()).index(3)]

        #the one in only two sixes is p2
        pattern[2] = list(charcounter.keys())[list(charcounter.values()).index(2)]

        #find character not yet assigned in "4"
        for digit in theonewithfourdigits:
            if(digit not in pattern):
                pattern[1] = digit

        #find the last one
        for digit in ['a','b','c','d','e','f','g']:
            if(digit not in pattern):
                pattern[4] = digit

        #pattern done
        lookup = []
        # 0
        lookup.append(f'{pattern[0]}{pattern[1]}{pattern[2]}{pattern[4]}{pattern[5]}{pattern[6]}')
        # 1
        lookup.append(f'{pattern[2]}{pattern[5]}')
        # 2
        lookup.append(f'{pattern[0]}{pattern[2]}{pattern[3]}{pattern[4]}{pattern[6]}')
        # 3
        lookup.append(f'{pattern[0]}{pattern[2]}{pattern[3]}{pattern[5]}{pattern[6]}')
        # 4
        lookup.append(f'{pattern[1]}{pattern[2]}{pattern[3]}{pattern[5]}')
        # 5
        lookup.append(f'{pattern[0]}{pattern[1]}{pattern[3]}{pattern[5]}{pattern[6]}')
        # 6
        lookup.append(f'{pattern[0]}{pattern[1]}{pattern[3]}{pattern[4]}{pattern[5]}{pattern[6]}')
        # 7
        lookup.append(f'{pattern[0]}{pattern[2]}{pattern[5]}')
        # 8
        lookup.append(f'{pattern[0]}{pattern[1]}{pattern[2]}{pattern[3]}{pattern[4]}{pattern[5]}{pattern[6]}')
        # 9
        lookup.append(f'{pattern[0]}{pattern[1]}{pattern[2]}{pattern[3]}{pattern[5]}{pattern[6]}')

        newlookup = []
        for look in lookup:
            sorted_characters = sorted(look)
            newlookup.append("".join(sorted_characters))
        lookup = newlookup

        

        print(f'pattern: {pattern}')
        print(f'lookup: {lookup}')

        result = ''

        for digits in output:
            sorted_characters = sorted(digits)
            digits = "".join(sorted_characters)
            result = f'{result}{lookup.index(digits)}'
        print(result)
        answer += int(result)
    
    print(f'answer: {answer}')


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description='AdventOfCode2021Day8')
    parser.add_argument('--input', type=str, required=True,
                    help="File")
    args = parser.parse_args()

    main(args)