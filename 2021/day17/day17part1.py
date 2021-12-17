import argparse
import numpy as np
import os
import re

def readFile(fileName):
    fileObj = open(fileName, "r") #opens the file in read mode
    data = fileObj.read()
    target = re.findall(r'target area: x=(-?\d+)..(-?\d+), y=(-?\d+)..(-?\d+)', data)[0]
    target = [int(x) for x in target]
    fileObj.close()
    return target

def shoot(target):
    heighttoshoot = target[2]*(target[2]+1)/2
    return heighttoshoot

def main(args):
    global shortestpath
    target = readFile(args.input)
    result = shoot(target)

    print(f'result {result}')
    

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description='AdventOfCode2021Day17')
    parser.add_argument('--input', type=str, required=True,
                    help="File")
    args = parser.parse_args()

    main(args)