import argparse
import numpy as np
import os
import re
import math
from utils.all import *


def main(args):
    diestate = 1 
    answer = 0
    ticktock = 0
    player1score = 0
    player2score = 0
    player1space = args.player1
    player2space = args.player2
    while True:
        if(player1score > 999 or player2score > 999):
            break
        rolls = 0
        for i in range(3):
            rolls += diestate
            diestate += 1
        
        if (ticktock == 0):
            player1space += rolls%10
            if(player1space%10 == 0):
                player1finalspace = 10
            else:
                player1finalspace = player1space%10
            player1score += player1finalspace
            ticktock = 1
        elif (ticktock == 1):
            player2space += rolls%10
            if(player2space%10 == 0):
                player2finalspace = 10
            else:
                player2finalspace = player2space%10
            player2score += player2finalspace
            ticktock = 0
        

    print(min(player1score,player2score))
    print(min(player1score,player2score) * (diestate-1))
    

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description='AdventOfCode2021Day21')
    parser.add_argument('--player1', type=int, required=True,
                    )
    parser.add_argument('--player2', type=int, required=True,
                    )
    args = parser.parse_args()

    main(args)