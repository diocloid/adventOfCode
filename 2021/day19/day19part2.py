import argparse
import numpy as np
import os
import re
import math

def readFile(fileName):
    fileObj = open(fileName, "r") #opens the file in read mode
    input = fileObj.read().splitlines() #puts the file into an array
    fileObj.close()
    return input


def main(args):
    print(f'result {magnitude}')
    

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description='AdventOfCode2021Day19')
    parser.add_argument('--input', type=str, required=True,
                    help="File")
    args = parser.parse_args()

    main(args)