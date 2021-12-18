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
    values = ''
    while True:
        endbit = transmission.read(1)
        values += transmission.read(4)
        print(int(values, 2))
        if (endbit == '0'):
            break

    return int(values, 2)


def readpacketsbylength(transmission, length, outerpackettype):
    print(f'length in bytes {length}')
    values = []
    pointer = transmission.tell()
    while transmission.tell() - pointer < length:

        packetversion = int(transmission.read(3), 2)
        packettypebin = transmission.read(3)
        packettype = int(packettypebin, 2)
        print(f'packettype {packettype}')
        if(packettype == 4):
            values.append(readliteralvalue(transmission))                

        else:
            lengthtypebit = transmission.read(1)
            if(lengthtypebit == '0'):
                newlength = transmission.read(15)
                newlength = int(newlength, 2)
                values.append(readpacketsbylength(transmission, newlength, packettype))
            if(lengthtypebit == '1'):
                newnumberofpackes = transmission.read(11)
                newnumberofpackes = int(newnumberofpackes, 2)
                values.append(readpacketsbynumbers(transmission, newnumberofpackes, packettype))
             
        

    value = calculate(outerpackettype, values)
    return value

def readpacketsbynumbers(transmission, numberofpackes, outerpackettype):
    print(f'length in numbers {numberofpackes}')
    values = []
    counter = 0
    while counter < numberofpackes:
        packetversion = int(transmission.read(3), 2)
        packettypebin = transmission.read(3)
        packettype = int(packettypebin, 2)
        print(f'packettype {packettype}')
        if(packettype == 4):
            values.append(readliteralvalue(transmission))                

        else:
            lengthtypebit = transmission.read(1)
            if(lengthtypebit == '0'):
                newlength = transmission.read(15)
                newlength = int(newlength, 2)
                values.append(readpacketsbylength(transmission, newlength, packettype))
            if(lengthtypebit == '1'):
                newnumberofpackes = transmission.read(11)
                newnumberofpackes = int(newnumberofpackes, 2)
                values.append( readpacketsbynumbers(transmission, newnumberofpackes, packettype))
        counter += 1

    value = calculate(outerpackettype, values)
    return value

    
def decodetransmission(transmission):
    
    packetversion = int(transmission.read(3), 2)
    packettype = int(transmission.read(3), 2)
    print(f'packettype {packettype}')

    if(packettype == 4):
        value = readliteralvalue(transmission) 

    else:
        lengthtypebit = transmission.read(1)
        if(lengthtypebit == '0'):
            length = transmission.read(15)
            length = int(length, 2)
            value = readpacketsbylength(transmission, length, packettype)
        if(lengthtypebit == '1'):
            numberofpackes = transmission.read(11)
            numberofpackes = int(numberofpackes, 2)
            value = readpacketsbynumbers(transmission, numberofpackes, packettype)

        # point = transmission.tell()
        # transmission.seek(0, os.SEEK_END)        
        # if(11 > transmission.seek()):
        #     break
        # transmission.seek(point)
        # transmission.tell()
    return value  

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