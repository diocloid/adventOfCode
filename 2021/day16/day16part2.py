import argparse
import numpy as np
import os

def readFile(fileName):
    fileObj = open(fileName, "r") #opens the file in read mode
    data = fileObj.read()
    fileObj.close()
    return data


def hex2bin(transmission):
    scale = 16     
    num_of_bits = 4
    result = []
    for bit in transmission:
        result.append(bin(int(bit, scale))[2:].zfill(num_of_bits))
    return ''.join(result)

def flattenList(nestedList):

    if(isinstance(nestedList, int)):
        return [nestedList]

    # check if list is empty
    if not(bool(nestedList)):
        return nestedList
 
     # to check instance of list is empty or not
    if isinstance(nestedList[0], list):
 
        # call function with sublist as argument
        return flattenList(*nestedList[:1]) + flattenList(nestedList[1:])
 
    # call function with sublist as argument
    return nestedList[:1] + flattenList(nestedList[1:])

def calculate(packettype, input):
    input = flattenList(input)
    if(packettype == 0):
        result = sum(input)
    elif(packettype == 1):
        result = int(np.prod(input))
    elif(packettype == 2):
        result = min(input)
    elif(packettype == 3):
        result = max(input)        
    elif(packettype == 5):
        if(input[0] > input[1]):
            result = 1
        else:
            result = 0      
    elif(packettype == 6):
        if(input[0] < input[1]):
            result = 1
        else:
            result = 0     
    elif(packettype == 7):
        if(input[0] == input[1]):
            result = 1
        else:
            result = 0 
    return result

    
def decodetransmission(transmission, result, numberofpackages = -1):

    packettype = -1
    packettype = int(transmission[3:6], 2)
    #print(f'packettype {packettype}')

    rest = -1

    if(packettype == 4):
        numbers = []
        #print('literal value')
        for i in range(6, len(transmission)-4, +5):
            #print(int(transmission[i+1:i+5],2))
            numbers.append(int(transmission[i+1:i+5], 2))
            if(transmission[i] == '0'):
                if(numberofpackages > -1):
                    numberofpackages -= 1
                    if(numberofpackages > 0):
                        packagerest = i + 5
                        ret = decodetransmission(transmission[packagerest:], result, numberofpackages)
                        numbers.append(ret[1])
                        rest = ret[2]
                    else:
                        rest = transmission[i+5:]
                    
                    break

                else:
                    packagerest = i + 5
                    if(len(transmission) - packagerest < 10):
                        break
                    else:
                        ret = decodetransmission(transmission[packagerest:], result)
                        numbers.append(ret[1])
                        break
        return (0, numbers, rest)


    else:
        operationoutput = []
        #print('operator package')
        #transmission[6] = length type ID
        if(transmission[6] == '0'):
            #number of bits in the sub-packets
            lengthofpackage = int(transmission[7:22], 2)   

            # run for packages in operator package         
            ret = decodetransmission(transmission[22:22+lengthofpackage], result)
            operationoutput.append(calculate(packettype, ret[1]))
            print(f'calculated {packettype, ret[1], operationoutput}')

            #run for rest
            if(len(transmission[22+lengthofpackage:]) > 9):
                ret = decodetransmission(transmission[22+lengthofpackage:], result)
                operationoutput.append(calculate(packettype, ret[1]))
                print(f'calculated {packettype, ret[1], operationoutput}')

        elif(transmission[6] == '1'):
            #number of sub-packets
            numberofpackages = int(transmission[7:18], 2) 

            #run for subpackages
            ret = decodetransmission(transmission[18:], result, numberofpackages)
            operationoutput.append(calculate(packettype, ret[1]))
            print(f'calculated {packettype, ret[1], operationoutput}')

            #run for rest
            if(ret[2] != -1):
                if(len(ret[2]) > 9):
                    ret = decodetransmission(ret[2], result)
                    operationoutput.append(calculate(packettype, ret[1]))
                    print(f'calculated {packettype, ret[1], operationoutput}')



            

        return (0, operationoutput, rest)

def main(args):
    global shortestpath
    transmission = readFile(args.input)
    binatytransmission = hex2bin(transmission)
    answer = decodetransmission(binatytransmission, [])
    print(f'answer {answer[1]}')
    

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description='AdventOfCode2021Day16')
    parser.add_argument('--input', type=str, required=True,
                    help="File")
    args = parser.parse_args()

    main(args)