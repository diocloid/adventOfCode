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

def checkliteral(transmission, stepper):
    result = []
    for i in range(0, len(transmission)-4, +5):
        print(transmission[i:i+5])
        result.append(transmission[i+1:i+5])
        if(transmission[i] == '0'):
            return (''.join(result), stepper+i)

def decodetransmission(transmission, versionsum, numberofpackages = -1):

    result = []
    packetversion = -1
    packettype = -1

    packetversion = int(transmission[0:3], 2)
    versionsum += packetversion
    print(f'versionnumber {packetversion}')
    packettype = int(transmission[3:6], 2)
    print(f'packettype {packettype}')

    rest = -1

    if(packettype == 4):
        print('literal value')
        for i in range(6, len(transmission)-4, +5):
            print(transmission[i:i+5])
            result.append(transmission[i+1:i+5])
            if(transmission[i] == '0'):
                if(numberofpackages > -1):
                    numberofpackages -= 1
                    if(numberofpackages > 0):
                        packagerest = i + 5
                        ret = decodetransmission(transmission[packagerest:], versionsum, numberofpackages)
                        result.append(ret[0])
                        versionsum = ret[1]
                        rest = ret[2]
                    else:
                        rest = transmission[i+5:]
                    
                    break

                else:
                    packagerest = i + 5
                    if(len(transmission) - packagerest < 10):
                        break
                    else:
                        ret = decodetransmission(transmission[packagerest:], versionsum)
                        result.append(ret[0])
                        versionsum = ret[1]
                        break

    else:
        print('operator package')
        if(transmission[6] == '0'):
            #number of bits in the sub-packets
            lengthofpackage = int(transmission[7:22], 2)   

            # run for packages in operator package         
            ret = decodetransmission(transmission[22:22+lengthofpackage], versionsum)
            result.append(ret[0])
            versionsum = ret[1]

            #run for rest
            if(len(transmission[22+lengthofpackage:]) > 9):
                ret = decodetransmission(transmission[22+lengthofpackage:], versionsum)
                result.append(ret[0])
                versionsum = ret[1]

        elif(transmission[6] == '1'):
            #number of sub-packets
            numberofpackages = int(transmission[7:18], 2) 

            #run for subpackages
            ret = decodetransmission(transmission[18:], versionsum, numberofpackages)
            result.append(ret[0])
            versionsum = ret[1]

            #run for rest
            if(ret[2] != -1):
                if(len(ret[2]) > 9):
                    ret = decodetransmission(ret[2], versionsum)
                    result.append(ret[0])
                    versionsum = ret[1]
    
    message = ''.join(result)
    return (message, versionsum, rest)

def main(args):
    global shortestpath
    transmission = readFile(args.input)
    binatytransmission = hex2bin(transmission)
    answer = decodetransmission(binatytransmission, 0)
    print(f'result {int(answer[0], 2)}')
    print(f'answer {answer[1]}')
    

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description='AdventOfCode2021Day16')
    parser.add_argument('--input', type=str, required=True,
                    help="File")
    args = parser.parse_args()

    main(args)