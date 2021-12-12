import argparse
    

def readFile(fileName):
    fileObj = open(fileName, "r") #opens the file in read mode
    words = fileObj.read().splitlines() #puts the file into an array
    fileObj.close()
    return words


def buildgraphs(map):
    edges = {}
    reversemap = []
    for lines in map:
        edge = lines.split('-')
        reversemap.append(f'{edge[1]}-{edge[0]}')

    map += reversemap

    for lines in map:
        edge = lines.split('-')

        if edge[0] not in edges:
            edges[edge[0]] = []   

        if edge[1] != 'start':             
            edges[edge[0]].append(edge[1])

    for edge in edges.values():
        if 'end' in edge:
            edge.remove('end')
            edge.append('end')

    edges['end'] = []

    print(edges)
    return edges


validpaths = []
def addtovalidpaths(path):
    validpaths.append(path)

def checkfornextvalidpath(path, edges, node, counter): 
    for nextnode in edges[node]:
        print(f'checking path {path} {nextnode}')
        if(nextnode == 'end'):
            path.append(nextnode)
            addtovalidpaths(path)
            print(f'valid path {path}')
            counter += 1
            return counter

        elif(nextnode.islower()):
            if(nextnode not in path):
                print(f'going deeper for path {path + [nextnode]}')
                counter = checkfornextvalidpath(path + [nextnode], edges, nextnode, counter)
            else:
                visitedtwicealready = False
                smallnodescounter = {}
                for smallnode in path:
                    if(smallnode != 'start' and smallnode.lower() == smallnode):
                        if smallnode not in smallnodescounter:
                            smallnodescounter[smallnode] = 0
                        smallnodescounter[smallnode] += 1
                        if(smallnodescounter[smallnode] == 2):
                            visitedtwicealready = True
                            break
                if(visitedtwicealready == False):
                    print(f'going deeper for path {path + [nextnode]}')
                    counter = checkfornextvalidpath(path + [nextnode], edges, nextnode, counter)
                
        else:  
            print(f'going deeper for path {path + [nextnode]}')
            counter = checkfornextvalidpath(path + [nextnode], edges, nextnode, counter)

    return counter

def main(args):

    map = readFile(args.input)
    edges = buildgraphs(map)
    result = checkfornextvalidpath(['start'], edges, 'start', 0)
    print(validpaths)
    print(f'result {result}')
    

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description='AdventOfCode2021Day12')
    parser.add_argument('--input', type=str, required=True,
                    help="File")
    args = parser.parse_args()

    main(args)