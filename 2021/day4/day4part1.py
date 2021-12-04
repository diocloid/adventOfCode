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

def buildboards(boardsinput):
    boards = []
    board = []
    for i in boardsinput:
        if(i == ''):
            boards.append(board)
            board = []
        else:
            i = i.replace('  ', ' ').strip()
            board.append(i.split(' '))
    boards.append(board)
    boards.pop(0)
    return boards

def findbingo(boards, drawnnumbers):
    for i in drawnnumbers:
        print(i)
        for k in range(len(boards)):
            for l in range(len(boards[k])): 
                for m in range(len(boards[k][l])):    
                    if(int(i) == int(boards[k][l][m])):
                        boards[k][l][m] = -1  
        for k in range(len(boards)):
            for l in range(len(boards[k])): 
                testsum = 0
                for m in range(len(boards[k][l])):    
                    testsum = testsum + int(boards[k][l][m])
                if(testsum == -5):
                    print(f'bingo in board {k} row {l}')
                    ret = ['row', k, l, i]
                    return ret

        for k in range(len(boards)):
            for l in range(len(boards[k])): 
                testsum = 0
                for m in range(len(boards[k][l])):    
                    testsum = testsum + int(boards[k][m][l])
                if(testsum == -5):
                    print(f'bingo in board {k} column {l}')
                    ret = ['col', k, l, i]
                    return ret
                 
        print(boards)

def main(args):
    position = 0
    depth = 0
    aim = 0
    numberoflines = 0
    bingosheet = readFile(args.input)
    drawnnumbers = bingosheet.pop(0).split(',')
    boards = buildboards(bingosheet)
    print(boards)
    bingo = findbingo(boards, drawnnumbers)
    
    
    winningboard = boards[bingo[1]]
    print(winningboard)

    winningsum = 0
    for k in range(len(winningboard)):
            for l in range(len(winningboard[k])):
                if(int(winningboard[k][l]) != -1):
                    winningsum = winningsum + int(winningboard[k][l])

    print(f'winningsum {winningsum}')
    print(f'winningboard {bingo[3]}')
    print(f'result {winningsum*int(bingo[3])}')
    

    
    


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description='AdventOfCode2021Day4')
    parser.add_argument('--input', type=str, required=True,
                    help="File")
    args = parser.parse_args()

    main(args)