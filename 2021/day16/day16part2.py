import argparse
import numpy as np
import os
import io

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


def calculate(packettype, input):
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

def readliteralvalue(transmission):
    value = []
    while True:
        endbit = transmission.read(1)
        value.append(int(transmission.read(4), 2))
        
        if (endbit == '0'):
            break
    return value
    
def readpacketsbylength(transmission, length):
    return 1

def readpacketsbynumbers(transmission, numberofpackes):
    return 1

    
def decodetransmission(transmission):

    
    packetversion = int(transmission.read(3), 2)
    print(f'versionnumber {packetversion}')
    packettype = int(transmission.read(3), 2)
    print(f'packettype {packettype}')

    if(packettype == 4):
        print('literal value')
        value = readliteralvalue(transmission)     
        return value       

    if(packettype == 6):
        print('operator')
        lengthtypebit = transmission.read(1)
        if(lengthtypebit == '0'):
            length = transmission.read(15)
            length = int(length, 2)
            readpacketsbylength(transmission, length)
        if(lengthtypebit == '1'):
            numberofpackes = transmission.read(11)
            numberofpackes = int(length, 2)
            readpacketsbynumbers(transmission, numberofpackes)



        # point = transmission.tell()
        # transmission.seek(0, os.SEEK_END)        
        # if(11 > transmission.seek()):
        #     break
        # transmission.seek(point)
        # transmission.tell()
    return transmission.tell()

def main(args):
    global shortestpath
    transmission = readFile(args.input)
    binatytransmission = hex2bin(transmission)
    buffer = io.StringIO(binatytransmission)
    answer = decodetransmission(buffer)
    print(f'answer {answer}')
    

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description='AdventOfCode2021Day16')
    parser.add_argument('--input', type=str, required=True,
                    help="File")
    args = parser.parse_args()

    main(args)