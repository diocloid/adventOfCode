import argparse
    

def readFile(fileName):
    fileObj = open(fileName, "r") #opens the file in read mode
    words = fileObj.read().splitlines() #puts the file into an array
    fileObj.close()
    return words


def datafrompaper(paper): 
    datafrompaper = [[], [], []]
    firstpart = True
    papersize = [0,0]
    for line in paper:
        #print(line)
        if line == '':
            firstpart = False            
        elif(firstpart):   
            tupel = line.split(',')
            if(papersize[0] < int(tupel[0])):
                papersize[0] = int(tupel[0])
            if(papersize[1] < int(tupel[1])):
                papersize[1] = int(tupel[1])  
            datafrompaper[0].append((int(tupel[0]),int(tupel[1])))
        else:
            datafrompaper[1].append(line.replace('fold along ', ''))
    
    datafrompaper[2] = papersize
    return datafrompaper


def buildpaper(points, size):
    paper = [['.' for col in range(size[0]+1)] for row in range(size[1]+1)]
    for tupel in points:
        paper[tupel[1]][tupel[0]] = '#'
    return paper


def fold(paper, size, passedfolddata):
    foldinfo = passedfolddata.split('=')
    if(foldinfo[0] == 'y'):
        #fold up for now
        foldedpaper = [['.' for col in range(size[0]+1)] for row in range(int(foldinfo[1]))]
        foldedpapertemp = [['.' for col in range(size[0]+1)] for row in range(int(foldinfo[1]))]
        count = 1
        for i in range(int(foldinfo[1])-1, -1, -1):
            foldedpaper[i] = paper[i]
            foldedpapertemp[i] = paper[int(foldinfo[1])+count]

            for y in range(0, size[0]+1, +1):
                if(foldedpapertemp[i][y] == '#'):
                    foldedpaper[i][y] = '#'
            count += 1

    elif(foldinfo[0] == 'x'):
        paperlength = len(paper)
        paperwidth = int(foldinfo[1])

        #fold up for now
        foldedpaper = [['.' for col in range(paperwidth)] for row in range(paperlength)]
        foldedpapertemp = [['.' for col in range(paperwidth)] for row in range(paperlength)]

        
        for i in range(paperwidth-1, -1, -1):

            for y in range(paperlength-1, -1, -1):
                foldedpaper[y][i] = paper[y][i]
                if(paper[y][len(paper[0])-i-1] == '#'):
                    foldedpaper[y][i] = paper[y][len(paper[0])-i-1]
        
    paper = foldedpaper
    return paper


def countdots(paper):
    count = 0
    for i in range(len(paper)-1, -1, -1):
        for y in range(len(paper[0])-1, -1, -1):
            if(paper[i][y] == '#'):
                count += 1
    return count 


def main(args):
    input = readFile(args.input)
    data = datafrompaper(input)
    paper = buildpaper(data[0], data[2])
    paper = fold(paper, data[2], data[1][0])
    print(paper)
    result = countdots(paper)

    print(f'result {result}')
    

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description='AdventOfCode2021Day13')
    parser.add_argument('--input', type=str, required=True,
                    help="File")
    args = parser.parse_args()

    main(args)